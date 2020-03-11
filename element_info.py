# -*- coding: utf-8 -*-
"""
Documentation string.
"""

__author__ = "Denis Trputec"
__copyright__ = "HOPS 2020, Element information for 'Dinamička stabilnost'"
__credits__ = ["Denis Trputec"]
__license__ = "HOPS d.o.o."
__version__ = "1.0.1"
__maintainer__ = "Denis Trputec"
__email__ = "denis.trputec@hops.hr"
__status__ = "Production"


import os
import sys
import psspy


def start_psse():
    psse_path = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
    sys.path.append(psse_path)
    os.environ['PATH'] += ';' + psse_path

    # File names
    case_file = r"""HR02_BAZNI_DYN.sav"""
    snapshot_file = r"""HR02_BAZNI_INIT.snp"""

    # Start PSSE and import files
    psspy.psseinit(10000)
    psspy.case(case_file)
    psspy.rstr(snapshot_file)


def options():
    option = -1
    while option == -1:
        option = input("\nChoose option:\n\t1 - Bus Info\n\t2 - Branch Info\n\t3 - Machine Info\n\nOption: ")
        if option == 1:
            bus_info()
        elif option == 2:
            branch_info()
        elif option == 3:
            machine_info()
        else:
            print "Invalid option!"
            option = -1


def return_parameter_lengths(int_len, real_len, char_len):
    return [int_len, int_len + real_len, int_len + real_len + char_len]


def user_input(flags, option_list):
    print option_list
    option_string = raw_input("Options you want to print (use space (' ') to separate them): ")
    user_option_list = option_string.split(' ')
    for i in range(0, len(option_list)):
        if option_list[i] in user_option_list:
            flags[i] = True
    return flags


def create_array(all_arrays):
    array = []
    for i in range(0, len(all_arrays[0][0])):
        element = []
        for j in range(0, len(all_arrays)):
            for k in range(0, len(all_arrays[j])):
                element.append(all_arrays[j][k][i])
        array.append(element)
    return array


def filter_array(parameter_list, parameter_lengths, array):
    # Parameter_lengths because of different input types
    new_array = []
    user_filter = []
    print "\nFilter by:"
    for i in range(0, len(parameter_list)):
        user_filter.append(raw_input(parameter_list[i] + ": "))
    for element in array:
        flags = [False] * len(element)
        for i in range(0, len(element)):
            if i < parameter_lengths[0]:
                if user_filter[i] != "":
                    try:
                        if int(user_filter[i]) == element[i]:
                            flags[i] = True
                    except ValueError:
                        pass
                else:
                    flags[i] = True
            elif i < parameter_lengths[1]:
                if user_filter[i] != "":
                    try:
                        if float(user_filter[i]) == element[i]:
                            flags[i] = True
                    except ValueError:
                        pass
                else:
                    flags[i] = True
            else:
                if user_filter[i] != "":
                    if user_filter[i] in element[i]:
                        flags[i] = True
                else:
                    flags[i] = True
        if all(flag is True for flag in flags):
            new_array.append(element)
    return new_array


def create_header(user_options, parameter_list):
    header = []
    for i in range(0, len(user_options)):
        if user_options[i]:
            header.append(parameter_list[i])
    print "\nOptions selected:"
    print header


def print_info(user_options, array):
    for i in range(0, len(array)):
        temp_array = []
        for j in range(0, len(user_options)):
            if user_options[j]:
                temp_array.append(array[i][j])
        print temp_array


def bus_info():
    # Lists of parameters
    int_list = ['NUMBER', 'TYPE', 'AREA', 'ZONE']
    real_list = ['BASE', 'KV', 'ANGLED']
    char_list = ['NAME', 'EXNAME']
    parameter_list = int_list + real_list + char_list
    parameter_lengths = return_parameter_lengths(len(int_list), len(real_list), len(char_list))

    # Create array of bus data
    iierr, iarray = psspy.abusint(sid=-1, flag=2, string=int_list)
    rierr, rarray = psspy.abusreal(sid=-1, flag=2, string=real_list)
    cierr, carray = psspy.abuschar(sid=-1, flag=2, string=char_list)
    all_arrays = [iarray, rarray, carray]
    array = create_array(all_arrays)

    # Filters
    user_options = [False] * 9
    user_options = user_input(user_options, parameter_list)
    array = filter_array(parameter_list, parameter_lengths, array)

    # Print information
    create_header(user_options, parameter_list)
    print_info(user_options, array)


def branch_info():
    # Lists of parameters
    int_list = ['FROMNUMBER', 'TONUMBER', 'STATUS']
    real_list = ['AMPS', 'RATEA', 'P', 'Q', 'MVA']
    char_list = ['ID', 'FROMNAME', 'FROMEXNAME', 'TONAME', 'TOEXNAME']
    parameter_list = int_list + real_list + char_list
    parameter_lengths = return_parameter_lengths(len(int_list), len(real_list), len(char_list))

    # Create array of branch data
    iierr, iarray = psspy.aflowint(sid=-1, owner=1, ties=1, flag=2, string=int_list)
    rierr, rarray = psspy.aflowreal(sid=-1, owner=1, ties=1, flag=2, string=real_list)
    cierr, carray = psspy.aflowchar(sid=-1, owner=1, ties=1, flag=2, string=char_list)
    all_arrays = [iarray, rarray, carray]
    array = create_array(all_arrays)

    # Filters
    user_options = [False] * 13
    user_options = user_input(user_options, parameter_list)
    array = filter_array(parameter_list, parameter_lengths, array)

    # Print information
    create_header(user_options, parameter_list)
    print_info(user_options, array)


def machine_info():
    # Lists of parameters
    int_list = ['NUMBER', 'STATUS']
    real_list = ['MBASE', 'GENTAP', 'PGEN', 'QGEN', 'MVA', 'PMAX', 'PMIN', 'QMAX', 'QMIN']
    char_list = ['ID', 'NAME', 'EXNAME']
    parameter_list = int_list + real_list + char_list
    parameter_lengths = return_parameter_lengths(len(int_list), len(real_list), len(char_list))

    # Create array of machine data
    iierr, iarray = psspy.amachint(sid=-1, flag=4, string=int_list)
    rierr, rarray = psspy.amachreal(sid=-1, flag=4, string=real_list)
    cierr, carray = psspy.amachchar(sid=-1, flag=4, string=char_list)
    all_arrays = [iarray, rarray, carray]
    array = create_array(all_arrays)

    # Filters
    user_options = [False] * 14
    user_options = user_input(user_options, parameter_list)
    array = filter_array(parameter_list, parameter_lengths, array)

    # Print information
    create_header(user_options, parameter_list)
    print_info(user_options, array)


if __name__ == '__main__':
    start_psse()
    options()

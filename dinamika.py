# -*- coding: utf-8 -*-
"""
Documentation string.
"""

__author__ = "Denis Trputec"
__copyright__ = "HOPS 2020, Dinamička stabilnost"
__credits__ = ["Elvis Mikac", "Denis Trputec"]
__license__ = "HOPS d.o.o."
__version__ = "1.0.1"
__maintainer__ = "Denis Trputec"
__email__ = "denis.trputec@hops.hr"
__status__ = "Production"


import os
import sys
import pandas
import numpy
from matplotlib import pyplot
import psspy
import dyntools


# Global variables
xls_file = r"""xls_file.xlsx"""


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
        option = input("\nChoose option:\n\t1 - Bus\n\t2 - Branch\n\t3 - Machine\n\t4 - Disturbance\n\nOption: ")
        if option == 1:
            # Choose output file name
            out_file = get_out_file()
            # Add bus channels
            plot_counter = add_bus_channels()
            # Initialize a PSSE dynamic simulation for state-space simulations and specify the Channel Output File
            psspy.strt(0, out_file)
            # Run option
            time = float(input("Time of pause: "))
            psspy.run(tpause=time)
            # Plotting graph
            plot_graph(out_file, plot_counter)
        elif option == 2:
            # Choose output file name
            out_file = get_out_file()
            # Add bus channels
            plot_counter = add_branch_channels()
            # Initialize a PSSE dynamic simulation for state-space simulations and specify the Channel Output File
            psspy.strt(0, out_file)
            # Run option
            time = float(input("Time of pause: "))
            psspy.run(tpause=time)
            # Plotting graph
            plot_graph(out_file, plot_counter)
        elif option == 3:
            # Choose output file name
            out_file = get_out_file()
            # Add bus channels
            plot_counter = add_machine_channels()
            # Initialize a PSSE dynamic simulation for state-space simulations and specify the Channel Output File
            psspy.strt(0, out_file)
            # Run option
            time = float(input("Time of pause: "))
            psspy.run(tpause=time)
            # Plotting graph
            plot_graph(out_file, plot_counter)
        elif option == 4:
            disturbance()
        else:
            option = -1


# <editor-fold desc="###  Check if element exist  ###">
def check_if_bus_exist(bus_number):
    iierr, iarray = psspy.abusint(sid=-1, flag=2, string=['NUMBER'])
    for i in range(0, len(iarray[0])):
        if iarray[0][i] == bus_number:
            return True
    return False


def check_if_branch_exist(bus1_number, bus2_number, circuit_id):
    iierr, iarray = psspy.aflowint(sid=-1, owner=1, ties=1, flag=2, string=['FROMNUMBER', 'TONUMBER'])
    cierr, carray = psspy.aflowchar(sid=-1, owner=1, ties=1, flag=2, string=['ID'])
    for i in range(0, len(iarray[0])):
        if (iarray[0][i] == bus1_number) and (iarray[1][i] == bus2_number) \
                and ((carray[0][i] == circuit_id) or (int(carray[0][i]) == int(circuit_id))):
            return True
    return False


def check_if_machine_exist(bus_number, machine_id):
    iierr, iarray = psspy.amachint(sid=-1, flag=4, string=['NUMBER'])
    cierr, carray = psspy.amachchar(sid=-1, flag=4, string=['ID'])
    for i in range(0, len(iarray[0])):
        if (iarray[0][i] == bus_number) and ((carray[0][i] == machine_id) or (int(carray[0][i]) == int(machine_id))):
            return True
    return False
# </editor-fold>


# <editor-fold desc="###  Add Channels  ###">

def add_bus_channels():
    # Initialization
    bus_number = None
    plot_counter = 0
    # Enter bus number until exists
    bus_exist = False
    while not bus_exist:
        bus_number = input("\nEnter bus number: ")
        bus_exist = check_if_bus_exist(bus_number)
    # Choose Channels
    print "\nChoose options ('T' or 'F'):"
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nFrequency: ")
        if option == 'T':
            psspy.bus_frequency_channel([-1, bus_number], r"""Hz""")
            plot_counter += 1
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nVoltage: ")
        if option == 'T':
            psspy.voltage_channel([-1, -1, -1, bus_number], r"""kV""")
            plot_counter += 1
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nVoltage and Angle: ")
        if option == 'T':
            psspy.voltage_and_angle_channel([-1, -1, -1, bus_number], [r"""kV""", r"""DEG"""])
            plot_counter += 2
    # Return plot counter
    return plot_counter


def add_branch_channels():
    # Initialization
    bus1_number = bus2_number = circuit_id = None
    plot_counter = 0
    # Enter bus numbers and circuit id until exists
    branch_exist = False
    while not branch_exist:
        bus1_number = input("\nEnter number of the from bus of the branch: ")
        bus2_number = input("Enter number of the to bus of the branch: ")
        circuit_id = raw_input("Enter circuit id: ")
        branch_exist = check_if_branch_exist(bus1_number, bus2_number, circuit_id)
    # Choose Channels
    print "\nChoose options ('T' or 'F'):"
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nMVA: ")
        if option == 'T':
            psspy.branch_mva_channel([-1, -1, -1, bus1_number, bus2_number], circuit_id, r"""MVA""")
            plot_counter += 1
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nP and Q: ")
        if option == 'T':
            psspy.branch_p_and_q_channel([-1, -1, -1, bus1_number, bus2_number], circuit_id, [r"""P""", r"""Q"""])
            plot_counter += 2
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nP: ")
        if option == 'T':
            psspy.branch_p_channel([-1, -1, -1, bus1_number, bus2_number], circuit_id, r"""P""")
            plot_counter += 1
    # Return plot counter
    return plot_counter


def add_machine_channels():
    # Initialization
    bus_number = machine_id = None
    plot_counter = 0
    # Enter bus number and machine id until exists
    machine_exist = False
    while not machine_exist:
        bus_number = input("\nEnter bus number: ")
        machine_id = raw_input("Enter machine id: ")
        machine_exist = check_if_machine_exist(bus_number, machine_id)
    # Choose Channels
    print "\nChoose options ('T' or 'F'):"
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nAngle: ")
        if option == 'T':
            psspy.machine_array_channel([-1, 1, bus_number], machine_id, r"""DEG""")
            plot_counter += 1
    option = 'Default'
    while option != 'T' and option != 'F':
        option = raw_input("\nPelec: ")
        if option == 'T':
            psspy.machine_array_channel([-1, 2, bus_number], machine_id, r"""P""")
            plot_counter += 1
    # Return plot counter
    return plot_counter

# </editor-fold>


def disturbance():
    pass


def get_out_file():
    file_name = raw_input("\nEnter output file name: ")
    if file_name.endswith('.out') or file_name.endswith('.outx'):
        return "out_files\\" + file_name
    else:
        return "out_files\\" + file_name + '.outx'


# <editor-fold desc="###  Plot Graph  ###">
def save_xls_file(out_file):
    xls_result = dyntools.CHNF([out_file])
    xls_header, chan_id = xls_result.get_id(out_file)
    need_delete = os.path.exists(xls_file)
    if need_delete:
        os.remove(xls_file)
    dyntools.CHNF.xlsout(xls_result, channels=[], show=False, xlsfile=xls_file, outfile=out_file)
    return chan_id


def read_xls_file():
    data = pandas.read_excel(xls_file, header=None, skiprows=5, dtype=numpy.float64)
    return data


def plot_graph(out_file, plot_counter):
    chan_id = save_xls_file(out_file)
    data = read_xls_file()
    for i in range(1, plot_counter + 1):
        plot_options(data, chan_id, i)
    pyplot.show()


def plot_options(data, chan_id, i):
    pyplot.figure(i)
    max_y = max(data[i])
    min_y = min(data[i])
    max_y += max_y * 0.025
    min_y -= min_y * 0.025
    last_index = data.index[-1]
    max_x = data[0][last_index]

    pyplot.plot(data[0], data[i], label=chan_id[i])
    pyplot.legend(loc='best')
    pyplot.xlim(xmin=0, xmax=max_x)
    pyplot.ylim(ymin=min_y, ymax=max_y)
# </editor-fold>


if __name__ == '__main__':
    start_psse()
    options()

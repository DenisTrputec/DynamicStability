# -*- coding: utf-8 -*-
"""
This Help/API Manual describes the API routines corresponding to the operational functions of the PSSE.
Every API routine that is called in 'dinamika.py' is in this manual.
To see information about routine just run the script and write name of python syntax for routine e.g. 'psseinit'
"""

__author__ = "Denis Trputec"
__copyright__ = "HOPS 2020, API Manual for 'Dinamička stabilnost'"
__credits__ = ["Denis Trputec"]
__license__ = "HOPS"
__version__ = "1.0.1"
__maintainer__ = "Denis Trputec"
__email__ = "denis.trputec@hops.hr"
__status__ = "Production"


def psseinit():
    print r"""
########################################################################################################################

Initialize PSSE

Python syntax:
ierr = psseinit(buses)

int BUSES - Is the requested bus size; zero for default size level (input).
int IERR - Is the error code (output). This is future use. No errors are currently defined

########################################################################################################################
"""


def case():
    print r"""
########################################################################################################################

Use this API to open PSSE Saved Case file and transfers its data ito the PSSE working case

Python syntax:
ierr = case(sfile)

char[260] SFILE- Is the name of the PSSE Saved Case File (input; no default allowed).
                    If SFILE is '*', CASE attempts to reopen the most recently accessed Saved Case File. If no Saved
                    Case File was accessed in the current execution of PSSE, CASE returns an error code.
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 SFILE is blank
            IERR = 2 error reading from SFILE
            IERR = 3 error opening SFILE
            IERR = 4 prerequisite requirements for API are not met

########################################################################################################################
"""


def read():
    print r"""
########################################################################################################################

Use this API to read a Power Flow Raw Data File and add all the data specified in it to the working case (activity READ)

Python syntax:
ierr = read(numnam, ifile)

int NUMNAM -  Is the flag for bus number or name specification on input records (input; 0 by default).
                NUMNAM = 0 bus numbers.
                NUMNAM = 1 bus names.
char[260] IFILE- Is the filename of the Power Flow Raw Data file (input; no default allowed).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid NUMNAM value.
            IERR = 2 invalid revision number.
            IERR = 3 unable to convert file.
            IERR = 4 error opening temporary file.
            IERR = 10 error opening IFILE.
            IERR = 11 prerequisite requirements for API are not met.

########################################################################################################################
"""


def dyre_new():
    print r"""
########################################################################################################################

Use this API to clear dynamics working memory, read a Dynamics Data File, and place the model references specified on
its data records into dynamics working memory (activity DYRE). It optionally creates a command file for compiling the
CONEC and CONET subroutines.

Python syntax:
ierr = dyre_new(startindx, dyrefile, conecfile, conetfile, compilfil, ierr)

int[4] STARTINDX - Is an array of four elements specifying starting locations in the dynamics data storage arrays(input)
                    STARTINDX[0] starting CON index (1 by default).
                    STARTINDX[1] starting STATE index (1 by default).
                    STARTINDX[2] starting VAR index (1 by default).
                    STARTINDX[3] starting ICON index (1 by default).
char[260] DYREFILE - Is the name of the Dynamics Model Raw Data File (input; no default allowed).
char[260] CONECFILE - Is the name of CONEC output file; blank for output to the progress area (input; blank by default).
char[260] CONETFILE - Is the name of CONET output file; blank for output to the progress area (input; blank by default).
char[260] COMPILFIL - Is the name of file containing commands to compile the CONEC and CONET output files;
                        blank for none (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred
            IERR = 1 invalid STARTINDX value
            IERR = 2 machine model connection tables full--use pack plant model tables function
            IERR = 3 error opening output file DYREFILE
            IERR = 4 prerequisite requirements for API are not met.

########################################################################################################################
"""


def rstr():
    print r"""
########################################################################################################################

Use this API to read a dynamics Snapshot File into PSSE working memory.

Python syntax:
ierr = rstr(sfile)

char[260] SFILE- Is the Snapshot File; '*' to restore the most recently accessed Snapshot FIle in the current execution 
                    of PSSE(input; no default allowed).
int IERR - Is the error code (output).
            IERR = 0 no error
            IERR = 1 error opening SFILE
            IERR = 2 error reading from SFILE
            IERR = 3 prerequisite requirements for API are not met

########################################################################################################################
"""


def snap():
    print r"""
########################################################################################################################

Use this API to save PSSE dynamics working memory into a Snapshot File. 

Python syntax:
ierr = snap(option, sfile)

int[5] STATUS - Is a five-element array (input). For each entry, -1 may be specified to indicate that the number of 
                elements of the corresponding array(s) to save in the Snapshot File is 1 through the next available - 1.
                    STATUS[0] number of CONs to save (next available-1 by default).
                    STATUS[1] number of STATEs to save (next available-1 by default).
                    STATUS[2] number of VARs to save (next available-1 by default).
                    STATUS[3] number of ICONs to save (next available-1 by default).
                    STATUS[4] number of output channels to save (next available-1 by default).
char[260] SFILE - Is the Snapshot File; '*' to use the most recently accessed Snapshot File in the current execution of 
                    PSSE (input; no default allowed).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid STATUS value.
            IERR = 2 error opening SFILE.
            IERR = 3 error writing SFILE
            IERR = 4 prerequisite requirements for API are not met.

########################################################################################################################
"""


def strt():
    print r"""
########################################################################################################################

Use this API to initialize a PSSE dynamic simulation for state-space simulations (i.e., in preparation for activity RUN)
and to specify the Channel Output File into which the output channel values are to be recorded during the dynamic 
simulation.

Python syntax:
ierr = strt(option, outfile)

int OPTION - Is the network solution convergence monitor option (input; 0 by default).
            OPTION = 1 automatically print the convergence monitor.
            OPTION = 0 print the convergence monitor only if it is enabled via the CM interrupt control code.
char[260] OUTFILE - Is the name of the Channel Output File (blank to bypass recording of the output channel values in a 
                    Channel Output File) (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 generators are not converted.
            IERR = 2 invalid OPTION value.
            IERR = 3 prior initialization modified the loads - pick up original converted case.
            IERR = 4 error opening OUTFILE.
            IERR = 5 prerequisite requirements for API are not met.

########################################################################################################################
"""


def run():
    print r"""
########################################################################################################################

Use this API to calculate PSSE state-space dynamic simulations.

Python syntax:
ierr = run(option, tpause, nprt, nplt, crtplt)

int OPTION - Is the network solution convergence monitor option (input; 0 by default).
            OPTION = 1 automatically print the convergence monitor.
            OPTION = 0 print the convergence monitor only if it is enabled via the CM interrupt control code.
float TPAUSE - Is the value of simulated time at which the simulation should next pause (input; no default allowed).
int NPRT - Is the number of time steps between the printing of the output channel values (input; unchanged by default).
int NPLT - Is the number of time steps between the writing of the output channel values to the current Channel Output
            File (input; unchanged by default).
int CRTPLT - Is the number of time steps between the plotting of those output channel values that have been designated
             as CRT output channels (input; unchanged by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 activity STRT needs to be executed.
            IERR = 2 invalid OPTION value.
            IERR = 3 generators are not converted.
            IERR = 4 error opening the current Channel Output File.
            IERR = 5 prerequisite requirements for API are not met.

########################################################################################################################
"""


def tree():
    print r"""
########################################################################################################################

Use this API to check for the existence of in-service ac islands that do not contain a Type 3 (swing) bus (activity 
TREE). Following each successful call, it returns BUSES as the number of buses in a swingless island (0 for no more 
swingless islands). When a BUSES value of 0 is returned, no further calls are needed.
The API must be called once with APIOPT set to 1. If BUSES is returned as 0 (i.e., there are no swingless islands), no 
further calls are needed. Otherwise, if BUSES is greater than zero, it must be called one or more times with APIOPT set 
to 2 and OPTION set to indicate the disposition of the current swingless island. APIOPT 2 calls are required until 
either BUSES is returned as zero or an APIOPT 2 call is made with OPTION set to a negative value.

Python syntax:
ierr,buses = tree(apiopt, option)

int APIOPT - Is the mode of operation (input; no default allowed).
                APIOPT = 1 initialize and check for the presence of a swingless island.
                APIOPT = 2 process previously detected island as dictated by OPTION; then check for the presence of
                            another swingless island.
int OPTION - Is the option for the handling of previously detected swingless island (input; used only when APIOPT is 2; 
                -1 by default).
                OPTION = <0 leave this island alone and terminate activity TREE.
                OPTION = 0 leave this island alone and check for another swingless island.
                OPTION = >0 disconnect this island, then check for another swingless island.
int BUSES - Is returned as the number of buses in this swingless island; 0 if no more swingless islands (output).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid APIOPT value.
            IERR = 2 unexpected APIOPT value.
            IERR = 3 prerequisite requirements for API are not met.

########################################################################################################################
"""


def fnsl():
    print r"""
########################################################################################################################

Use this API to apply the Newton-Raphson power flow calculation (activity FNSL).

Python syntax:
ierr = fnsl(options)

int APIOPT - Is the mode of operation (input; no default allowed).
                APIOPT = 1 initialize and check for the presence of a swingless island.
                APIOPT = 2 process previously detected island as dictated by OPTION; then check for the presence of
                            another swingless island.
int[8] OPTION - Is an array of eight elements specifying solution options (input). The values are as follows:
                    OPTIONS[0] tap adjustment flag (use tap adjustment option setting by default).
                    OPTIONS[0] = 0 disable.
                    OPTIONS[0] = 1 enable stepping adjustment.
                    OPTIONS[0] = 2 enable direct adjustment.
                    OPTIONS[1] area interchange adjustment flag (use area interchange adjustment option setting by
                                default).
                    OPTIONS[1] = 0 disable.
                    OPTIONS[1] = 1 enable using tie line flows only in calculating area interchange.
                    OPTIONS[1] = 2 enable using tie line flows and loads in calculating area interchange.
                    OPTIONS[2] phase shift adjustment flag (use phase shift adjustment option setting by default).
                    OPTIONS[2] = 0 disable.
                    OPTIONS[2] = 1 enable.
                    OPTIONS[3] dc tap adjustment flag (use dc tap adjustment option setting by default).
                    OPTIONS[3] = 0 disable.
                    OPTIONS[3] = 1 enable.
                    OPTIONS[4] switched shunt adjustment flag (use switched shunt adjustment option setting by default).
                    OPTIONS[4] = 0 disable.
                    OPTIONS[4] = 1 enable.
                    OPTIONS[4] = 2 enable continuous mode, disable discrete mode.
                    OPTIONS[5] flat start flag (0 by default).
                    OPTIONS[5] = 0 do not flat start.
                    OPTIONS[5] = 1 flat start.
                    OPTIONS[6] var limit flag (99 by default).
                    OPTIONS[6] = 0 apply var limits immediately.
                    OPTIONS[6] = >0 apply var limits on iteration n (or sooner if mismatch gets small).
                    OPTIONS[6] = -1 ignore var limits.
                    OPTIONS[7] non-divergent solution flag (use non-divergent solution option setting by default).
                    OPTIONS[7] = 0 disable.
                    OPTIONS[7] = 1 enable.
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid OPTIONS value.
            IERR = 2 generators are converted.
            IERR = 3 buses in island(s) without a swing bus; use activity TREE.
            IERR = 4 bus type code and series element status inconsistencies.
            IERR = 5 prerequisite requirements for API are not met.

########################################################################################################################
"""


# <editor-fold desc="###  Add Channels  ###">
def machine_array_channel():
    print r"""
########################################################################################################################

Use this API to add an output channel containing a plant related model variable of a designated type for a specified 
machine.

Python syntax:
ierr = machine_array_channel(status, id, ident)

int[3] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] used to indicate the quantity to be placed in an output channel (1 by default).
                    STATUS[1] = 1 ANGLE, machine relative rotor angle (degrees).
                    STATUS[1] = 2 PELEC, machine electrical power (pu on SBASE)
                    STATUS[1] = 3 QELEC, machine reactive power.
                    STATUS[1] = 4 ETERM, machine terminal voltage (pu).
                    STATUS[1] = 5 EFD, generator main field voltage (pu).
                    STATUS[1] = 6 PMECH, turbine mechanical power (pu on MBASE).
                    STATUS[1] = 7 SPEED, machine speed deviation from nominal (pu).
                    STATUS[1] = 8 XADIFD, machine field current (pu).
                    STATUS[1] = 9 ECOMP, voltage regulator compensated voltage (pu).
                    STATUS[1] = 10 VOTHSG, stabilizer output signal (pu).
                    STATUS[1] = 11 VREF, voltage regulator voltage setpoint (pu).
                    STATUS[1] = 12 VUEL, minimum excitation limiter output signal (pu).
                    STATUS[1] = 13 VOEL, maximum excitation limiter output signal (pu).
                    STATUS[1] = 14 GREF, turbine governor reference.
                    STATUS[1] = 15 LCREF, turbine load control reference.
                    STATUS[1] = 16 WVLCTY, wind velocity (m/s).
                    STATUS[1] = 17 WTRBSP, wind turbine rotor speed deviation (pu).
                    STATUS[1] = 18 WPITCH, pitch angle (degrees).
                    STATUS[1] = 19 WAEROT, aerodynamic torque (pu on MBASE).
                    STATUS[1] = 20 WROTRV, rotor voltage (pu on MBASE).
                    STATUS[1] = 21 WROTRI, rotor current (pu on MBASE).
                    STATUS[1] = 22 WPCMND, active power command from wind control (pu on MBASE).
                    STATUS[1] = 23 WQCMND, reactive power command from wind control (pu on MBASE).
                    STATUS[1] = 24 WAUXSG, output of wind auxiliary control (pu on MBASE).
                    STATUS[2] is the number of the bus to which the machine for which the quantity is to be placed in an
                                output channel is connected (on default allowed).
char[2] ID - Is the machine identifier (input; '1' by default)
char[32] IDENT - Is identifier to be assigned to the output channel. If a blank channel identifier is specified, the API 
                    generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 selected plot quantity can only be associated with renewable machine.
            IERR = 4 bus not found.
            IERR = 5 machine not found.
            IERR = 6 prerequisite requirements for API are not met.

########################################################################################################################
"""


def branch_app_r_x_channel():
    print r"""
########################################################################################################################

Use this API to add a pair of output channels containing the apparent impedance, as seen at the from bus of a specified 
branch, along with a corresponding call to the RELAY2 monitoring model.

Python syntax:
ierr = branch_app_r_x_channel(status, id, ident)

int[5] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the from bus of the branch for which apparent impedance is to be placed 
                                in output channels (no default allowed).
                    STATUS[4] is the number of the to bus of the branch for which apparent impedance is to be placed in 
                                output channels (no default allowed).
char[2] ID - Is the machine identifier (input; '1' by default)
char[32] IDENT - Is an array of two identifiers to be assigned to the two output channels. If a blank channel identifier
                    is specified, the API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 model RELAY2 needs 3 ICONs but the last one exceeds the largest ICON index allowed.
            IERR = 6 the maximum number of channel monitoring models has already been specified.
            IERR = 7 model RELAY2 needs 2 VARs but the last one exceeds the largest VAR index allowed.
            IERR = 8 model RELAY2 needs 2 channels but the last one exceeds the largest channel number allowed.
            IERR = 9 bus not found.
            IERR = 10 branch not found.
            IERR = 11 prerequisite requirements for API are not met.

########################################################################################################################
"""


def branch_mva_channel():
    print r"""
########################################################################################################################

Use this API to add an output channel containing the MVA flow at the from bus of a specified branch, along with a 
corresponding call to the FLOW1 monitoring model.

Python syntax:
ierr = branch_mva_channel(status, id, ident)

int[5] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the from bus of the branch for which MVA flow is to be placed in an 
                                output channel (no default allowed).
                    STATUS[4] is the number of the to bus of the branch for which MVA flow is to be placed in an output
                                channel (no default allowed).
char[2] ID - Is the machine identifier (input; '1' by default)
char[32] IDENT - Is an array of two identifiers to be assigned to the two output channels. If a blank channel identifier
                    is specified, the API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 model FLOW1 needs 3 ICONs but the last one exceeds the largest ICON index allowed.
            IERR = 6 the maximum number of channel monitoring models has already been specified.
            IERR = 7 bus not found.
            IERR = 8 branch not found.
            IERR = 9 prerequisite requirements for API are not met.

########################################################################################################################
"""


def branch_p_and_q_channel():
    print r"""
########################################################################################################################

Use this API to add a pair of output channels containing the active and reactive power flow at the from bus of a 
specified branch, along with a corresponding call to the FLOW1 monitoring model.

Python syntax:
ierr = branch_p_and_q_channel(status, id, ident)

int[5] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the from bus of the branch for which active and reactive flows are to be 
                                placed in an output channels (no default allowed).
                    STATUS[4] is the number of the to bus of the branch for which active and reactive flows are to be 
                                placed in an output channels (no default allowed).
char[2] ID - Is the machine identifier (input; '1' by default)
char[32] IDENT - Is an array of two identifiers to be assigned to the two output channels. If a blank channel identifier
                    is specified, the API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 model FLOW1 needs 3 ICONs but the last one exceeds the largest ICON index allowed.
            IERR = 6 the maximum number of channel monitoring models has already been specified.
            IERR = 7 model FLOW1 needs 2 VARs but the last one exceeds the largest VAR index allowed.
            IERR = 8 model FLOW1 needs 2 channels but the last one exceeds the largest channel number allowed.
            IERR = 9 bus not found.
            IERR = 10 branch not found.
            IERR = 11 prerequisite requirements for API are not met.

########################################################################################################################
"""


def branch_p_channel():
    print r"""
########################################################################################################################

Use this API to add an output channel containing the active power flow at the from bus of a specified branch, along with 
a corresponding call to the FLOW1 monitoring model.

Python syntax:
ierr = branch_p_channel(status, id, ident)

int[5] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the from bus of the branch for which active power flow is to be 
                                placed in an output channel (no default allowed).
                    STATUS[4] is the number of the to bus of the branch for which active power flow is to be 
                                placed in an output channel (no default allowed).
char[2] ID - Is the machine identifier (input; '1' by default)
char[32] IDENT - Is an array of two identifiers to be assigned to the two output channels. If a blank channel identifier
                    is specified, the API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 model FLOW1 needs 3 ICONs but the last one exceeds the largest ICON index allowed.
            IERR = 6 the maximum number of channel monitoring models has already been specified.
            IERR = 7 bus not found.
            IERR = 8 branch not found.
            IERR = 9 prerequisite requirements for API are not met.

########################################################################################################################
"""


def bus_frequency_channel():
    print r"""
########################################################################################################################

Use this API to add an output channel containing the per unit frequency deviation at a specified bus.

Python syntax:
ierr = bus_frequency_channel(status, ident)

int[2] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the number of the bus for which frequency deviation is to be placed in an output 
                                channel is connected (no default allowed).
char[32] IDENT - Is the identifier to be assigned to the output channel. If a blank channel identifier is specified, the 
                    API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 bus not found.
            IERR = 4 prerequisite requirements for API are not met.

########################################################################################################################
"""


def bus_voltage_channel():
    print r"""
########################################################################################################################

Use this API to add an output channel containing the voltage magnitude in per unit of a specified bus, along with a 
corresponding call to the VOLMAG monitoring model.

Python syntax:
ierr = bus_voltage_channel(status, ident)

int[4] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the bus for which voltage magnitude is to be placed in an output channel 
                                (no default allowed).
char[32] IDENT - Is the identifier to be assigned to the output channel. If a blank channel identifier is specified, the 
                    API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 the maximum number of channel monitoring models has already been specified.
            IERR = 6 bus not found.
            IERR = 7 prerequisite requirements for API are not met.

########################################################################################################################
"""


def bus_voltage_and_angle_channel():
    print r"""
########################################################################################################################

Use this API to add a pair of output channels containing the voltage magnitude in per unit and phase angle in degrees of 
a specified bus, along with a corresponding call to the VOLMAG monitoring model.

Python syntax:
ierr = bus_voltage_and_angle_channel(status, ident)

int[4] STATUS - Is an array of three elements (input).
                    STATUS[0] is the starting channel index, or -1 for the next available (next available by default).
                    STATUS[1] is the starting VAR index, or -1 for the next available (next available by default).
                    STATUS[2] is the starting ICON index, or -1 for the next available (next available by default).
                    STATUS[3] is the number of the bus for which voltage magnitude and phase are to be placed in an 
                                output channels (no default allowed).
char[32] IDENT - Is an array of two identifiers to be assigned to the two output channels. If a blank channel identifier 
                    is specified, the API generates an appropriate channel identifier (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error.
            IERR = 1 invalid STATUS value.
            IERR = 2 starting channel number is greater than the largest channel number allowed.
            IERR = 3 starting VAR index is greater than the largest VAR index allowed.
            IERR = 4 starting ICON index is greater than the largest ICON index allowed.
            IERR = 5 the maximum number of channel monitoring models has already been specified.
            IERR = 6 bus not found.
            IERR = 7 model VOLMAG needs 2 VARs but the last one exceeds the largest VAR index allowed.
            IERR = 8 model VOLMAG needs 2 channels but the last one exceeds the largest channel number allowed.
            IERR = 9 prerequisite requirements for API are not met.

########################################################################################################################
"""
# </editor-fold desc>


# <editor-fold desc="###  Disturbance  ###">
def dist_branch_fault():
    print r"""
########################################################################################################################

Use this API to apply a fault at the IBUS end of a non-transformer branch or a two-winding transformer during dynamic 
simulations.

Python syntax:
ierr = dist_branch_fault(ibus, jbus, id, units, basekv, values)

int IBUS - Is the bus number of the bus at which the fault is to be placed (input; no default allowed).
int JBUS - Is the bus number of the other bus (input; no default allowed).
char[2] ID - Is the circuit identifier (input; '1' by default).
int UNITS - Is the units in which fault admittance or impedance is specified in VALUES (input; 1 by default).
                UNITS = 1 admittance in MVA.
                UNITS = 2 admittance in mhos.
                UNITS = 3 impedance in ohms.
float BASEKV - Is the base voltage in kV used to calculate the per unit fault admittance if UNITS is 2 or 3; ignored if 
                UNITS is 1. If BASEKV is specified as 0.0, the base voltage of bus IBUS is used (input; 0.0 by default).
float[2] VALUES - Is an array of two elements (input).
                VALUES[0] is the real component of the complex fault admittance or impedance according to the value 
                            specified for UNITS (0.0 by default).
                VALUES[1] is the reactive component of the complex fault admittance or impedance according to the value 
                            specified for UNITS (-2.0E11 by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 STRT or MSTR has not been successfully executed.
            IERR = 2 bus not found.
            IERR = 3 branch not found.
            IERR = 4 branch is out-of-service.
            IERR = 5 invalid UNITS value.
            IERR = 6 invalid BASEKV value (<0.0).
            IERR = 7 both BASEKV and the base voltage of bus IBUS are 0.0.
            IERR = 8 prerequisite requirements for API are not met.

########################################################################################################################
"""


def dist_branch_trip():
    print r"""
########################################################################################################################

Use this API to set a non-transformer branch or a two-winding transformer to out-of-service during dynamic simulations.

Python syntax:
ierr = dist_branch_trip(ibus, jbus, id)

int IBUS - Is the bus number of the bus at which the fault is to be placed (input; no default allowed).
int JBUS - Is the bus number of the other bus (input; no default allowed).
char[2] ID - Is the circuit identifier (input; '1' by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 STRT or MSTR has not been successfully executed.
            IERR = 2 bus not found.
            IERR = 3 branch not found.
            IERR = 4 branch is out-of-service.
            IERR = 5 prerequisite requirements for API are not met.

########################################################################################################################
"""


def dist_clear_fault():
    print r"""
########################################################################################################################

Use this API to clear a fault during dynamic simulations. The fault must have previously been applied using one of the 
following APIs:
        • DIST_3WIND_FAULT
        • DIST_BRANCH_FAULT
        • DIST_BUS_FAULT
        • DIST_SCMU_FAULT
        • DIST_SPCB_FAULT    

Python syntax:
ierr = dist_clear_fault(ifault)

int IFAULT - Is the index in the fault memory tables of the fault to be cleared (input; 1 by default). Faults are stored 
                in the fault memory tables in the order in which they are applied; the index assigned to a fault is the 
                next available location in the tables. Each time a fault is cleared using this API, the fault memory
                tables are compressed. Thus, if there are three faults active, the most recently applied fault will have 
                index number 3.
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 STRT or MSTR not successfully executed.
            IERR = 2 bus not found.
            IERR = 3 branch not found.
            IERR = 4 three-winding transformer not found
            IERR = 5 fixed bus shunt not found
            IERR = 6 no faults in the fault memory tables
            IERR = 7 invalid IFAULT value
            IERR = 8 prerequisite requirements for API are not met.

########################################################################################################################
"""
# </editor-fold>


# <editor-fold desc="###  Contingency calculations and reports ###">

def accc():
    print r"""
########################################################################################################################

This API routine is obsolete. It has been replaced by the API routine ACCC_WITH_DSP_3, and is implemented by a call to 
ACCC_WITH_DSP_3. Use this API routine to run the AC contingency calculation function (activity ACCC).

Python syntax:
ierr = accc(tol, options, dfxfile, accfile, thrfile)

float TOL - Is the mismatch tolerance (input; Newton solution convergence tolerance, TOLN, by default).
int[7] OPTIONS - Is an array of seven elements specifying solution options (input). The values are as follows:
                    OPTIONS[0] tap adjustment flag (tap adjustment option setting by default).
                    OPTIONS[0] = 0 disable.
                    OPTIONS[0] = 1 enable stepping adjustment.
                    OPTIONS[0] = 2 enable direct adjustment.
                    OPTIONS[1] area interchange adjustment flag (area interchange adjustment option setting by default).
                    OPTIONS[1] = 0 disable.
                    OPTIONS[1] = 1 enable using tie line flows only in calculating area interchange.
                    OPTIONS[1] = 2 enable using tie line flows and loads in calculating area interchange.
                    OPTIONS[2] phase shift adjustment flag (phase shift adjustment option setting by default).
                    OPTIONS[2] = 0 disable.
                    OPTIONS[2] = 1 enable.
                    OPTIONS[3] dc tap adjustment flag (dc tap adjustment option setting by default).
                    OPTIONS[3] = 0 disable.
                    OPTIONS[3] = 1 enable.
                    OPTIONS[4] switched shunt adjustment flag (switched shunt adjustment option setting by default).
                    OPTIONS[4] = 0 disable.
                    OPTIONS[4] = 1 enable.
                    OPTIONS[4] = 2 enable continuous mode, disable discrete mode.
                    OPTIONS[5] solution method flag (0 by default).
                    OPTIONS[5] = 0 FDNS.
                    OPTIONS[5] = 1 FNSL.
                    OPTIONS[5] = 2 optimized FDNS.
                    OPTIONS[6] non-divergent solution flag (non-divergent solution option setting by default).
                    OPTIONS[6] = 0 disable.
                    OPTIONS[6] = 1 enable.
char[260] DFXFILE - Is the name of the Distribution Factor Data File (input; no default allowed).
char[260] ACCFILE - Is the name of the Contingency Solution Output file (input; no default allowed).
char[260] THRFILE - Is the name of the Load Throwover Data file; blank for none (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR > 0 as for ACCC_WITH_DSP_3.

########################################################################################################################
"""


def accc_with_dsp_3():
    print r"""
########################################################################################################################

Use this API routine to run the third release the AC contingency calculation function. A generation dispatch function 
to handle imbalances in power resources and demand due to contingencies may be enabled.

Python syntax:
ierr = accc_with_dsp_3(tol, options, label, dfxfile, accfile, thrfile, inlfile, zipfile)

float TOL - Is the mismatch tolerance (input; Newton solution convergence tolerance, TOLN, by default).
int[7] OPTIONS - Is an array of seven elements specifying solution options (input). The values are as follows:
                    OPTIONS[0] tap adjustment flag (tap adjustment option setting by default).
                    OPTIONS[0] = 0 disable.
                    OPTIONS[0] = 1 enable stepping adjustment.
                    OPTIONS[0] = 2 enable direct adjustment.
                    OPTIONS[1] area interchange adjustment flag (area interchange adjustment option setting by default).
                    OPTIONS[1] = 0 disable.
                    OPTIONS[1] = 1 enable using tie line flows only in calculating area interchange.
                    OPTIONS[1] = 2 enable using tie line flows and loads in calculating area interchange.
                    OPTIONS[2] phase shift adjustment flag (phase shift adjustment option setting by default).
                    OPTIONS[2] = 0 disable.
                    OPTIONS[2] = 1 enable.
                    OPTIONS[3] dc tap adjustment flag (dc tap adjustment option setting by default).
                    OPTIONS[3] = 0 disable.
                    OPTIONS[3] = 1 enable.
                    OPTIONS[4] switched shunt adjustment flag (switched shunt adjustment option setting by default).
                    OPTIONS[4] = 0 disable.
                    OPTIONS[4] = 1 enable.
                    OPTIONS[4] = 2 enable continuous mode, disable discrete mode.
                    OPTIONS[5] solution method flag (0 by default).
                    OPTIONS[5] = 0 FDNS.
                    OPTIONS[5] = 1 FNSL.
                    OPTIONS[5] = 2 optimized FDNS.
                    OPTIONS[6] non-divergent solution flag (non-divergent solution option setting by default).
                    OPTIONS[6] = 0 disable.
                    OPTIONS[6] = 1 enable.
                    OPTIONS[7] induction motor treatment flag (applied when an induction motor fails to solve due to 
                                low terminal bus voltage, 0 by default).
                    OPTIONS[7] = 0 stall.
                    OPTIONS[7] = 1 trip.
                    OPTIONS[8] induction machine failure flag (0 by default)
                    OPTIONS[8] = 0 treat contingency as non-converged if any induction machines are placed in the 
                                "stalled" or "tripped" state.
                    OPTIONS[8] = 1 treat contingency as solved if it converges, even if any induction machines are 
                                    placed in the  "stalled" or "tripped" state.
                    OPTIONS[9] dispatch mode (0 by default)
                    OPTIONS[9] = 0 disable.
                    OPTIONS[9] = 1 subsystem machines (reserve).
                    OPTIONS[9] = 2 subsystem machines (pmax).
                    OPTIONS[9] = 3 subsystem machines (inertia).
                    OPTIONS[9] = 4 subsystem machines (governor droop).
                    OPTIONS[10] ZIP archive flag (0 by default)
                    OPTIONS[10] = 0 do not write a ZIP archive file.
                    OPTIONS[10] = 1 write a ZIP archive using the file specified as ZIPFILE.        
char[12] LABEL - Is the name of the generation dispatch subsystem (blank by default, no default allowed if OPTIONS[9] 
                    is not 0). 
char[260] DFXFILE - Is the name of the Distribution Factor Data File (input; no default allowed).
char[260] ACCFILE - Is the name of the Contingency Solution Output file (input; no default allowed).
char[260] THRFILE - Is the name of the Load Throwover Data file; blank for none (input; blank by default).
char[260] INLFILE - Is the name of the Unit Inertia and Governor Data File (input; blank by default).
char[260] ZIPFILE - Is the name of the ZIP Archive Output File (input; blank by default).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid TOL value.
            IERR = 2 invalid OPTIONS value.
            IERR = 3 generators are converted.
            IERR = 4 buses in island(s) without a swing bus; use activity TREE.
            IERR = 5 largest mismatch exceeds mismatch tolerance.
            IERR = 6 generation dispatch subsystem is not defined.
            IERR = 7 too many islands in base case.
            IERR = 8 no Distribution Factor Data File specified.
            IERR = 9 no AC Contingency Solution Output File specified.
            IERR = 10 in-service induction machines are in the "stalled" or "tripped" state.
            IERR = 11 buses with bus type code and series element status inconsistencies.
            IERR = 12 no ZIP Archive Output File specified.
            IERR = 21 file DFXFILE is not in the form of a PSS®E-25 or later DFAX file; run DFAX.
            IERR = 22 monitored elements exceed limit when adding multisection line members.
            IERR = 51 error opening Contingency Solution Output File.
            IERR = 52 error opening Distribution Factor Data File.
            IERR = 53 error opening Load Throwover Data File.
            IERR = 54 error opening Unit Inertia and Governor Data File.
            IERR = 55 error opening ZIP Archive Output File.
            IERR = 56 prerequisite requirements for API are not met.
            
########################################################################################################################
"""


def accc_single_run_report():
    print r"""
########################################################################################################################

Use this API, the AC Contingency Report function, to report the results of the AC Contingency Calculation function.

Python syntax:
ierr = accc_single_run_report(status, intval, realval, rfile)

int[8] STATUS - Is an array of eight elements (input). The values are as follows.
                STATUS[0] report format (3 by default).
                STATUS[0] = 0 spreadsheet overload report.
                STATUS[0] = 1 spreadsheet loading table.
                STATUS[0] = 2 available capacity table.
                STATUS[0] = 3 non-spreadsheet overload report.
                STATUS[0] = 4 non-spreadsheet loading table.
                STATUS[0] = 5 non-converged networks report.
                STATUS[1] - base case rating set; used only when STATUS[0] is 0, 1, 3 or 4 (rating set program option 
                            setting by default).
                STATUS[1] = 1 rate A.
                STATUS[1] = 2 rate B.
                STATUS[1] = 3 rate C.
                STATUS[2] contingency case rating set when STATUS(1) is 0, 1, 3 or 4; base case and contingency case 
                            rating set when STATUS(1) is 2 (rating set program option setting by default).
                STATUS[2] = 1 rate A.
                STATUS[2] = 2 rate B.
                STATUS[2] = 3 rate C.
                STATUS[3] exclude interfaces from report; used only when STATUS[0] is 0, 1, 2, 3 or 4 (0 by default).
                STATUS[3] = 0 no.
                STATUS[3] = 1 yes.
                STATUS[4] run voltage limit check; used only when STATUS[0] is 0, 1, 3 or 4 (0 by default).
                STATUS[4] = 0 no.
                STATUS[4] = 1 yes.
                STATUS[5] in overload reports, exclude monitored branches and interfaces that show loading violations 
                            in the base case from being checked and reported in contingency cases; used only when 
                            STATUS[0] is 0 or 3 (0 by default).
                STATUS[5] = 0 no.
                STATUS[5] = 1 yes.
                STATUS[6] in voltage range violation reports, exclude monitored buses that show voltage range violations
                            in the base case from the corresponding check in contingency case reports; used only when
                            STATUS[6] is 0 or 3 (0 by default).
                STATUS[6] = 0 no.
                STATUS[6] = 1 yes.
                STATUS[7] exclude cases with no overloads from non spreadsheet overload report; used only when
                            STATUS[0] is 3 (0 by default).
                STATUS[7] = 0 no.
                STATUS[7] = 1 yes.
int[5] INTVAL - Is an array of five elements (input). The values are as follows.
                INTVAL[0] number of low voltage range violations filtering criterion (0 by default).
                INTVAL[1] number of high voltage range violations filtering criterion (0 by default).
                INTVAL[2] number of voltage deviation violations filtering criterion; not applied to base case (0 by 
                            default).
                INTVAL[3] number of buses in the largest disconnected island filtering criterion; not applied to base 
                            case (0 by default).
                INTVAL[4] maximum number of elements in the available capacity table (no limit by default).
float[7] REALVAL - Is an array of seven elements (input). The values are as follows.
                    REALVAL[0] bus mismatch converged tolerance (MW or Mvar) (0.5 by default).
                    REALVAL[1] system mismatch converged tolerance (MVA) (5.0 by default).
                    REALVAL[2] percent of flow rating; used only when STATUS[0] is 0, 3 or 4 (100.0 by default).
                    REALVAL[3] in overload reports, minimum contingency case flow change from base case value; used 
                                only when STATUS[0] is 0 or 3 (0.0 by default).
                    REALVAL[4] in overload reports, minimum contingency case percent loading increase from base case 
                                value; used only when STATUS[0] is 0 or 3 (0.0 by default).
                    REALVAL[5] in voltage range violation reports, minimum contingency case voltage change from base 
                                case value; used only when STATUS[0] is 0, 1, 3 or 4 (0.0 by default).
                    REALVAL[6] cutoff threshold for available capacity table; used only when STATUS[3] is 2 (99999.0 by 
                                default).
char[260] RFILE - Is the Contingency Solution Output File (input; no default allowed).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid STATUS value.
            IERR = 2 invalid INTVAL value.
            IERR = 3 invalid REALVAL value.
            IERR = 4 error opening RFILE.
            IERR = 5 error reading RFILE.
            IERR = 6 prerequisite requirements for API are not met.

########################################################################################################################
"""


def dfax():
    print r"""
########################################################################################################################

Use this API to construct a Distribution Factor Data File (activity DFAX).

Python syntax:
ierr = dfax(options, subfile, monfile, confile, dfxfile)

int[2] OPTIONS - Is an array of two elements specifying calculation options (input). The value of each element is as 
                    follows.
                OPTIONS[0] distribution factor option flag (1 by default).
                OPTIONS[0] = 0 do not calculate distribution factors (i.e., DFAX,AC).
                OPTIONS[0] = 1 calculate distribution factors.
                OPTIONS[1] monitored element sorting flag (0 by default).
                OPTIONS[1] = 0 do not sort (i.e., leave in Monitored Element Description File order).
                OPTIONS[1] = 1 sort.
char[260] SUBFILE - Is the name of the Subsystem Description File; blank for none (input; blank by default).
char[260] MONFILE - Is the name of Monitored Element Description File (input; no default allowed).
char[260] CONFILE - Is the name of Contingency Description Data File (input; no default allowed).
char[260] DFXFILE - Is the name of Distribution Factor Data File (input; no default allowed).
int IERR - Is the error code (output).
            IERR = 0 no error occurred.
            IERR = 1 invalid OPTIONS value.
            IERR = 2 generators are converted.
            IERR = 3 buses in island(s) without a swing bus; use activity TREE.
            IERR = 4 no Distribution Factor Data File specified.
            IERR = 5 no Monitored Element Data input file specified.
            IERR = 6 no Contingency Description Data file specified.
            IERR = 7 fatal error reading input file.
            IERR = 8 error opening output file DFXFILE.
            IERR = 9 error opening input file SUBFILE.
            IERR = 10 error opening input file MONFILE.
            IERR = 11 error opening input file CONFILE.
            IERR = 12 prerequisite requirements for API are not met.

########################################################################################################################
"""

# </editor-fold>


# <editor-fold desc="###  Element Information  ###">
def abusint():
    print r"""
########################################################################################################################

Use this API to return an array of integer values for subsystem buses.

Python syntax:
ierr, iarray = abusint(sid, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int FLAG - Is a flag indicating which subsystem buses to include (input; 1 by default).
            FLAG = 1, for only in-service buses.
            FLAG = 2, for all buses.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus quantities 
                    desired (input; no default allowed):
                        ’NUMBER’ Bus number.
                        ’TYPE’ Bus type code.
                        ’AREA’ Bus area number.
                        ’ZONE’ Bus zone number.
                        ’OWNER’ Bus owner number.
                        ’DUMMY’ Returns 1 if the bus is a dummy bus of a multisection line, or 0 if it is not.
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid FLAG value.
            IERR = 4 Invalid NSTR value.
            IERR = 5 DIM, and hence the size of IARRAY, is not large enough.
            IERR = 6 Invalid STRING value.

########################################################################################################################
"""


def abuschar():
    print r"""
########################################################################################################################

Use this API to return an array of character values for subsystem buses.

Python syntax:
ierr, carray = abuschar(sid, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int FLAG - Is a flag indicating which subsystem buses to include (input; 1 by default).
            FLAG = 1, for only in-service buses.
            FLAG = 2, for all buses.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus quantities 
                    desired (input; no default allowed):
                        ’NAME’ Bus name (12 characters).
                        ’EXNAME’ Extended bus name (18 characters).
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid FLAG value.
            IERR = 4 Invalid NSTR value.
            IERR = 5 DIM, and hence the size of CARRAY, is not large enough.
            IERR = 6 Invalid STRING value.

########################################################################################################################
"""


def aflowint():
    print r"""
########################################################################################################################

Use this API to return an array of integer values for subsystem branches.

Python syntax:
ierr, iarray = aflowint(sid, owner, ties, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int OWNER - Is a flag indicating owner usage if ownership is a subsystem selection criterion (ignored if SID is 
            negative) (input; 1 by default).
                OWNER = 1 to use bus ownership.
                OWNER = 2 to use branch ownership.
int TIES -  Is a flag indicating which subsystem branches to include (ignored if SID is negative) (input; 1 by default).
                TIES = 1 for each end of interior subsystem branches only.
                TIES = 2 for the subsystem bus end of tie branches only.
                TIES = 3 for the non-subsystem bus end of tie branches only.
                TIES = 4 for each end of tie branches only.
                TIES = 5 for each end of interior subsystem branches and the subsystem bus end of tie branches.
                TIES = 6 for each end of interior subsystem branches and tie branches.
int FLAG - Is a flag indicating which subsystem branches to include (input; 1 by default).
                FLAG = 1 for only in-service branches.
                FLAG = 2 for all branches.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus and/or 
                    machine quantities desired (input; no default allowed):
                        ’FROMNUMBER’ From bus number.
                        ’TONUMBER’ To bus number (>10000000 for a three-winding transformer winding).
                        ’STATUS’ Branch status.
                        ’NMETERNUMBER' Non-metered end bus number.
                        ’OWNERS’ Number of owners.
                        ’OWN1’ First owner.
                        ’OWN2’ Second owner.
                        ’OWN3’ Third owner.
                        ’OWN4’ Fourth owner.
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid OWNER value.
            IERR = 4 Invalid TIES value.
            IERR = 5 Invalid FLAG value.
            IERR = 6 Invalid NSTR value.
            IERR = 7 DIM, and hence the size of IARRAY, is not large enough.
            IERR = 8 Invalid STRING value.

########################################################################################################################
"""


def aflowchar():
    print r"""
########################################################################################################################

Use this API to return an array of character values for subsystem branches.

Python syntax:
ierr, iarray = aflowchar(sid, owner, ties, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int OWNER - Is a flag indicating owner usage if ownership is a subsystem selection criterion (ignored if SID is 
            negative) (input; 1 by default).
                OWNER = 1 to use bus ownership.
                OWNER = 2 to use branch ownership.
int TIES -  Is a flag indicating which subsystem branches to include (ignored if SID is negative) (input; 1 by default).
                TIES = 1 for each end of interior subsystem branches only.
                TIES = 2 for the subsystem bus end of tie branches only.
                TIES = 3 for the non-subsystem bus end of tie branches only.
                TIES = 4 for each end of tie branches only.
                TIES = 5 for each end of interior subsystem branches and the subsystem bus end of tie branches.
                TIES = 6 for each end of interior subsystem branches and tie branches.
int FLAG - Is a flag indicating which subsystem branches to include (input; 1 by default).
                FLAG = 1 for only in-service branches.
                FLAG = 2 for all branches.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus and/or 
                    machine quantities desired (input; no default allowed):
                        ’ID’ Circuit identifier (2 characters).
                        ’FROMNAME’ From bus name (12 characters).
                        ’FROMEXNAME’ From bus extended bus name (18 characters).
                        ’TONAME’ To bus name (three-winding transformer name for a three-winding transformer winding) 
                                    (12 characters).
                        ’TOEXNAME’ To bus extended bus name (three-winding transformer name and winding number for a 
                                    threewinding transformer winding) (18 characters).
                        ’NMETERNAME’ Non-metered bus name (12 characters).
                        ’NMETEREXNAME’ Non-metered bus extended bus name (18 characters).
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid OWNER value.
            IERR = 4 Invalid TIES value.
            IERR = 5 Invalid FLAG value.
            IERR = 6 Invalid NSTR value.
            IERR = 7 DIM, and hence the size of CARRAY, is not large enough.
            IERR = 8 Invalid STRING value.

########################################################################################################################
"""


def amachint():
    print r"""
########################################################################################################################

Use this API to return an array of integer values for subsystem machines.

Python syntax:
ierr, iarray = amachint(sid, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int FLAG - Is a flag indicating which subsystem machines to include (input; 1 by default).
            FLAG = 1 for only in-service machines at in-service plants (type code 2 or 3).
            FLAG = 2 for all machines at in-service plants (type code 2 or 3).
            FLAG = 3 for only in-service machines, including those at Type 1 and 4 buses.
            FLAG = 4 for all machines.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus and/or 
                    machine quantities desired (input; no default allowed):
                        ’NUMBER’ Bus number.
                        ’STATUS’ Machine status.
                        ’WMOD’ Wind machine reactive power limits mode; 0 if the machine is not a wind machine.
                        ’OWNERS’ Number of owners.
                        ’OWN1’ First owner.
                        ’OWN2’ Second owner.
                        ’OWN3’ Third owner.
                        ’OWN4’ Fourth owner.
                        ’CZG’ Grounding impedance data input/output (I/O) code (1 for per unit, 2 for ohms).
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid FLAG value.
            IERR = 4 Invalid NSTR value.
            IERR = 5 DIM, and hence the size of IARRAY, is not large enough.
            IERR = 6 Invalid STRING value.
            IERR = 7 Sequence data not in case (when STRING = ’CZG’).

########################################################################################################################
"""


def amachchar():
    print r"""
########################################################################################################################

Use this API to return an array of character values for subsystem machines.

Python syntax:
ierr, carray = amachchar(sid, flag, string)

int SID - Defines the bus subsystem to be used (input; -1 by default).
            SID = a negative value, to instruct the API to assume a subsystem containing all buses in the working case.
            SID = a valid bus subsystem identifier. Valid subsystem identifiers range from 0 to 11. Subsystem SID must
                    have been previously defined.
int FLAG - Is a flag indicating which subsystem machines to include (input; 1 by default).
            FLAG = 1 for only in-service machines at in-service plants (type code 2 or 3).
            FLAG = 2 for all machines at in-service plants (type code 2 or 3).
            FLAG = 3 for only in-service machines, including those at Type 1 and 4 buses.
            FLAG = 4 for all machines.
char[[]] STRING - Is an array of NSTR elements specifying NSTR of the following strings indicating the bus and/or 
                    machine quantities desired (input; no default allowed):
                        ’ID’ Machine identifier (2 characters).
                        ’NAME’ Bus name (12 characters).
                        ’EXNAME’ Extended bus name (18 characters).
int IERR - Is the error code (output).
            IERR = 0 No error.
            IERR = 1 Working case is empty.
            IERR = 2 Invalid SID value.
            IERR = 3 Invalid FLAG value.
            IERR = 4 Invalid NSTR value.
            IERR = 5 DIM, and hence the size of CARRAY, is not large enough.
            IERR = 6 Invalid STRING value.

########################################################################################################################
"""
# </editor-fold>


if __name__ == '__main__':
    function_name = raw_input("API: ")
    globals()[function_name]()

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


if __name__ == '__main__':
    function_name = raw_input("API: ")
    globals()[function_name]()

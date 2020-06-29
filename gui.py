# -*- coding: utf-8 -*-
"""
Documentation string.
"""

__author__ = "Denis Trputec"
__copyright__ = "HOPS 2020, Dinamička stabilnost"
__credits__ = ["Elvis Mikac", "Denis Trputec"]
__license__ = "HOPS d.o.o."
__app_name__ = "Dinamička stabilnost"
__version__ = "1.0.1"
__maintainer__ = "Denis Trputec"
__email__ = "denis.trputec@hops.hr"
__status__ = "Development"

import psse
import element_info
import Tkinter as Tk
import ttk
import tkFont
from PIL import ImageTk, Image


# <editor-fold desc="###  Class Definition  ###">
class Bus:
    def __init__(self):
        self.out_file = None
        self.bus_number = None
        self.freq_ch = None
        self.vol_ch = None
        self.vol_ang_ch = None
        self.time = None
        self.channel_count = None


class Branch:
    def __init__(self):
        self.out_file = None
        self.from_bus_number = None
        self.to_bus_number = None
        self.circuit_id = None
        self.mva_ch = None
        self.pq_ch = None
        self.p_ch = None
        self.time = None
        self.channel_count = None


class Machine:
    def __init__(self):
        self.out_file = None
        self.bus_number = None
        self.machine_id = None
        self.angle_ch = None
        self.pelec_ch = None
        self.time = None
        self.channel_count = None


class LineFault:
    def __init__(self):
        self.from_bus_number = None
        self.to_bus_number = None
        self.circuit_id = None
        self.time = None


class BusFault:
    def __init__(self):
        self.bus_number = None
        self.time = None
# </editor-fold>


def set_window_size(window, app_width, app_height):
    # Set application window dimensions and put it on center of a user screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = screen_width / 2 - app_width / 2
    position_down = screen_height / 2 - app_height / 2
    window.geometry("%dx%d+%d+%d" % (app_width, app_height, position_right, position_down))


def set_button_size(buttons, btn_width, btn_height, font_size):
    text_font = tkFont.Font(size=font_size)
    for button in buttons:
        button.config(width=btn_width, height=btn_height)
        button["font"] = text_font


def set_root_window():
    root.title(__app_name__)
    set_window_size(root, 1280, 720)
    button_dynamics = Tk.Button(root, text="Dynamic Analysis", command=set_dynamic_analysis_window)
    button_dynamics.grid(row=0, column=0)
    button_semaphore = Tk.Button(root, text="Traffic Light", command=set_traffic_light_window)
    button_semaphore.grid(row=1, column=0)
    set_button_size([button_dynamics, button_semaphore], 15, 2, 14)


def set_dynamic_analysis_window():
    def return_to_root():
        root.deiconify()
        dynamics_window.destroy()
    root.withdraw()
    dynamics_window = Tk.Toplevel(root)
    dynamics_window.title("Dynamic analysis")
    set_window_size(dynamics_window, 1280, 720)
    button_bus = Tk.Button(dynamics_window, text="Bus", command=set_bus_window)
    button_bus.grid(row=0, column=0)
    button_branch = Tk.Button(dynamics_window, text="Branch", command=set_branch_window)
    button_branch.grid(row=1, column=0)
    button_machine = Tk.Button(dynamics_window, text="Machine", command=set_machine_window)
    button_machine.grid(row=2, column=0)
    button_back = Tk.Button(dynamics_window, text="Back", command=return_to_root)
    button_back.grid(row=3, column=0)
    set_button_size([button_bus, button_branch, button_machine, button_back], 15, 2, 14)
    dynamics_window.protocol("WM_DELETE_WINDOW", on_closing)


def set_traffic_light_window():
    pass


def set_bus_window():
    def initialize():
        # Start PSSe
        psse.start_psse()

        # Copy user entries into class object
        bus.out_file = out_file_entry.get()
        temp = (bus_name_combo.get()).split(' ')
        bus.bus_number = temp[0]
        bus.freq_ch = freq_var.get()
        bus.vol_ch = vol_var.get()
        bus.vol_ang_ch = vol_ang_var.get()

        # Check user entries
        bus.out_file = psse.check_out_file(bus.out_file)
        bus.bus_number = check_bus_entry(bus.bus_number)
        if bus.bus_number == -1:
            show_popup_window(bus_window, "Error", "Bus number or name doesn't exist!")
            return
        if (bus.freq_ch + bus.vol_ch + bus.vol_ang_ch) == 0:
            show_popup_window(bus_window, "Error", "Check at least one output channel!")
            return

        # Add output channels
        bus.channel_count = psse.add_bus_channels(bus.out_file, bus.bus_number,
                                                  bus.freq_ch, bus.vol_ch, bus.vol_ang_ch)

        # Enable run button and disable disturbance and plot buttons
        run_button["state"] = "normal"
        line_fault_button["state"] = "disabled"
        bus_fault_button["state"] = "disabled"
        plot_button["state"] = "disabled"
        return

    def run():
        # Run dynamics
        bus.time = run_entry.get()
        try:
            bus.time = float(bus.time)
        except ValueError:
            show_popup_window(bus_window, "Error", "Time of pause must be float value!")
        else:
            # Enable disturbance buttons and plot button
            line_fault_button["state"] = "normal"
            bus_fault_button["state"] = "normal"
            plot_button["state"] = "normal"
            psse.run(bus.time)

    def line_fault():
        # Copy user entries into class object
        temp = (lf_from_bus_name_combo.get()).split(' ')
        lf.from_bus_number = temp[0]
        temp = (lf_to_bus_name_combo.get()).split(' ')
        lf.to_bus_number = temp[0]
        lf.circuit_id = lf_circuit_id_entry.get()
        lf.time = lf_time_entry.get()

        # Check user entries
        lf.from_bus_number = check_bus_entry(lf.from_bus_number)
        if lf.from_bus_number == -1:
            show_popup_window(bus_window, "Error", "From bus number or name doesn't exist!")
            return
        lf.to_bus_number = check_bus_entry(lf.to_bus_number)
        if lf.to_bus_number == -1:
            show_popup_window(bus_window, "Error", "To bus number or name doesn't exist!")
            return
        if not psse.check_if_branch_exist(lf.from_bus_number, lf.to_bus_number, lf.circuit_id):
            show_popup_window(bus_window, "Error", "Branch doesn't exist!")
            return
        try:
            lf.time = float(lf.time)
        except ValueError:
            show_popup_window(bus_window, "Error", "Time must be float value!")
            return
        if lf.time <= bus.time or lf.time > bus.time + 0.3:
            show_popup_window(bus_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (bus.time, bus.time + 0.3))
            return

        # Call method line_fault from psse.py
        psse.line_fault(lf.from_bus_number, lf.to_bus_number, lf.circuit_id, lf.time)

    def bus_fault():
        temp = (bf_bus_name_combo.get()).split(' ')
        bf.bus_number = temp[0]
        bf.time = bf_time_entry.get()

        # Check user entries
        bf.bus_number = check_bus_entry(bf.bus_number)
        if bf.bus_number == -1:
            show_popup_window(bus_window, "Error", "Bus number or name doesn't exist!")
            return
        try:
            bf.time = float(bf.time)
        except ValueError:
            show_popup_window(bus_window, "Error", "Time must be float value!")
            return
        if bf.time <= bus.time or bf.time > bus.time + 0.3:
            show_popup_window(bus_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (bus.time, bus.time + 0.3))
            return

        # Call method bus_fault from psse.py
        psse.bus_fault(bf.bus_number, bf.time)

    def update_if_combobox(_):
        # Underscore is event object that is not used
        bus_names_new = [elem for elem in bus_names if if_value.get() in elem]
        bus_name_combo["value"] = bus_names_new

    def update_lf_from_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_from_value.get() in elem]
        lf_from_bus_name_combo["value"] = bus_names_new

    def update_lf_to_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_to_value.get() in elem]
        lf_to_bus_name_combo["value"] = bus_names_new

    def update_bf_combobox(_):
        bus_names_new = [elem for elem in bus_names if bf_value.get() in elem]
        bf_bus_name_combo["value"] = bus_names_new

    # Start PSSe
    psse.start_psse()

    # Create Bus window
    bus_window = Tk.Toplevel(root)
    bus_window.grab_set()
    bus_window.title("Bus")
    set_window_size(bus_window, 960, 540)

    # Create class objects
    bus = Bus()
    lf = LineFault()
    bf = BusFault()

    # Create list of elements for combobox
    user_options = [True, False, False, False, False, False, False, True, False]
    user_filter = [""] * 9
    _, bus_names_list = element_info.bus_info(user_options, user_filter)
    bus_names = [(str(element[0]) + " " + element[1]).decode('latin1') for element in bus_names_list]

    # Create frame Initialize
    initialize_frame = Tk.LabelFrame(bus_window, text="Initialize")
    initialize_frame.grid(row=0, column=0, sticky=Tk.N)
    Tk.Label(initialize_frame, text="Output file name: ").grid(row=0, column=0)
    Tk.Label(initialize_frame, text="Bus number: ").grid(row=1, column=0)
    Tk.Label(initialize_frame, text="Add channels: ").grid(row=2, column=0)
    out_file_entry = Tk.Entry(initialize_frame)
    out_file_entry.grid(row=0, column=1, sticky=Tk.W)
    if_value = Tk.StringVar()
    bus_name_combo = ttk.Combobox(initialize_frame, values=bus_names, textvariable=if_value)
    bus_name_combo.set("")
    bus_name_combo.bind("<KeyRelease>", update_if_combobox)
    bus_name_combo.grid(row=1, column=1)
    freq_var = Tk.IntVar()
    vol_var = Tk.IntVar()
    vol_ang_var = Tk.IntVar()
    Tk.Checkbutton(initialize_frame, text="Frequency", variable=freq_var).grid(row=2, column=1, sticky=Tk.W)
    Tk.Checkbutton(initialize_frame, text="Voltage", variable=vol_var).grid(row=3, column=1, sticky=Tk.W)
    Tk.Checkbutton(initialize_frame, text="Voltage and angle", variable=vol_ang_var).grid(row=4, column=1, sticky=Tk.W)
    Tk.Button(initialize_frame, text="Initialize", command=initialize).grid(row=5, column=0, columnspan=2)

    # Create frame Run
    run_frame = Tk.LabelFrame(bus_window, text="Run dynamics")
    run_frame.grid(row=1, column=0, sticky=Tk.N, pady=(20, 0))
    Tk.Label(run_frame, text="Time of pause: ").grid(row=0, column=0)
    run_entry = Tk.Entry(run_frame)
    run_entry.grid(row=0, column=1)
    run_button = Tk.Button(run_frame, text="Run", state="disabled", command=run)
    run_button.grid(row=1, column=0, columnspan=2)

    # Create frame Add Disturbance
    disturbance_frame = Tk.LabelFrame(bus_window, text="Add disturbance")
    disturbance_frame.grid(row=0, column=1, rowspan=2, padx=(50, 0), sticky=Tk.N)
    # Create frame Line Fault
    line_fault_frame = Tk.LabelFrame(disturbance_frame, text="Line fault")
    line_fault_frame.grid(row=0, column=0, pady=(10, 0))
    Tk.Label(line_fault_frame, text="From bus number: ").grid(row=0, column=0)
    Tk.Label(line_fault_frame, text="To bus number: ").grid(row=1, column=0)
    Tk.Label(line_fault_frame, text="Circuit ID: ").grid(row=2, column=0)
    Tk.Label(line_fault_frame, text="End time of fault: ").grid(row=3, column=0)
    lf_from_value = Tk.StringVar()
    lf_from_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_from_value)
    lf_from_bus_name_combo.set("")
    lf_from_bus_name_combo.bind("<KeyRelease>", update_lf_from_combobox)
    lf_from_bus_name_combo.grid(row=0, column=1)
    lf_to_value = Tk.StringVar()
    lf_to_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_to_value)
    lf_to_bus_name_combo.set("")
    lf_to_bus_name_combo.bind("<KeyRelease>", update_lf_to_combobox)
    lf_to_bus_name_combo.grid(row=1, column=1)
    lf_circuit_id_entry = Tk.Entry(line_fault_frame)
    lf_circuit_id_entry.grid(row=2, column=1, sticky=Tk.W)
    lf_time_entry = Tk.Entry(line_fault_frame)
    lf_time_entry.grid(row=3, column=1, sticky=Tk.W)
    line_fault_button = Tk.Button(line_fault_frame, text="Add disturbance", state="disabled", command=line_fault)
    line_fault_button.grid(row=4, column=0, columnspan=2)
    # Create frame Bus Fault
    bus_fault_frame = Tk.LabelFrame(disturbance_frame, text="Bus fault")
    bus_fault_frame.grid(row=1, column=0, pady=(30, 0))
    Tk.Label(bus_fault_frame, text="Bus number: ").grid(row=0, column=0)
    Tk.Label(bus_fault_frame, text="End time of fault: ").grid(row=1, column=0)
    bf_value = Tk.StringVar()
    bf_bus_name_combo = ttk.Combobox(bus_fault_frame, values=bus_names, textvariable=bf_value)
    bf_bus_name_combo.set("")
    bf_bus_name_combo.bind("<KeyRelease>", update_bf_combobox)
    bf_bus_name_combo.grid(row=0, column=1)
    bf_time_entry = Tk.Entry(bus_fault_frame)
    bf_time_entry.grid(row=1, column=1, sticky=Tk.W)
    bus_fault_button = Tk.Button(bus_fault_frame, text="Add disturbance", state="disabled", command=bus_fault)
    bus_fault_button.grid(row=2, column=0, columnspan=2)

    # Plot Graph
    plot_button = Tk.Button(bus_window, text="Plot graph", state="disabled")
    plot_button["command"] = lambda: psse.plot_graph(bus.out_file, bus.channel_count)
    plot_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    # Element Information
    info_button = Tk.Button(bus_window, text="Element Info", command=element_info_bus)
    info_button.grid(row=3, column=1, pady=(50, 0), sticky=Tk.SE)

    # Show Grid
    info_button = Tk.Button(bus_window, text="Show Grid", command=show_grid_image)
    info_button.grid(row=4, column=1, sticky=Tk.SE)


def set_branch_window():
    def initialize():
        # Start PSSe
        psse.start_psse()

        # Copy user entries into class object
        br.out_file = out_file_entry.get()
        temp = (from_bus_name_combo.get()).split(' ')
        br.from_bus_number = temp[0]
        temp = (to_bus_name_combo.get()).split(' ')
        br.to_bus_number = temp[0]
        br.circuit_id = circuit_id_entry.get()
        br.mva_ch = mva_var.get()
        br.pq_ch = pq_var.get()
        br.p_ch = p_var.get()

        # Check user entries
        br.out_file = psse.check_out_file(br.out_file)
        br.from_bus_number = check_bus_entry(br.from_bus_number)
        if br.from_bus_number == -1:
            show_popup_window(branch_window, "Error", "From bus number or name doesn't exist!")
            return
        br.to_bus_number = check_bus_entry(br.to_bus_number)
        if br.to_bus_number == -1:
            show_popup_window(branch_window, "Error", "To bus number or name doesn't exist!")
            return
        if not psse.check_if_branch_exist(br.from_bus_number, br.to_bus_number, br.circuit_id):
            show_popup_window(branch_window, "Error", "Branch doesn't exist!")
            return
        if (br.mva_ch + br.pq_ch + br.p_ch) == 0:
            show_popup_window(branch_window, "Error", "Check at least one output channel!")
            return

        # Add output channels
        br.channel_count = psse.add_branch_channels(br.out_file, br.from_bus_number, br.to_bus_number, br.circuit_id,
                                                    br.mva_ch, br.pq_ch, br.p_ch)

        # Enable run button and disable disturbance and plot buttons
        run_button["state"] = "normal"
        line_fault_button["state"] = "disabled"
        bus_fault_button["state"] = "disabled"
        plot_button["state"] = "disabled"
        return

    def run():
        # Run dynamics
        br.time = run_entry.get()
        try:
            br.time = float(br.time)
        except ValueError:
            show_popup_window(branch_window, "Error", "Time of pause must be float value!")
        else:
            # Enable disturbance buttons and plot button
            line_fault_button["state"] = "normal"
            bus_fault_button["state"] = "normal"
            plot_button["state"] = "normal"
            psse.run(br.time)

    def line_fault():
        # Copy user entries into class object
        temp = (lf_from_bus_name_combo.get()).split(' ')
        lf.from_bus_number = temp[0]
        temp = (lf_to_bus_name_combo.get()).split(' ')
        lf.to_bus_number = temp[0]
        lf.circuit_id = lf_circuit_id_entry.get()
        lf.time = lf_time_entry.get()

        # Check user entries
        lf.from_bus_number = check_bus_entry(lf.from_bus_number)
        if lf.from_bus_number == -1:
            show_popup_window(branch_window, "Error", "From bus number or name doesn't exist!")
            return
        lf.to_bus_number = check_bus_entry(lf.to_bus_number)
        if lf.to_bus_number == -1:
            show_popup_window(branch_window, "Error", "To bus number or name doesn't exist!")
            return
        if not psse.check_if_branch_exist(lf.from_bus_number, lf.to_bus_number, lf.circuit_id):
            show_popup_window(branch_window, "Error", "Branch doesn't exist!")
            return
        try:
            lf.time = float(lf.time)
        except ValueError:
            show_popup_window(branch_window, "Error", "Time must be float value!")
            return
        if lf.time <= br.time or lf.time > br.time + 0.3:
            show_popup_window(branch_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (br.time, br.time + 0.3))
            return

        # Call method line_fault from psse.py
        psse.line_fault(lf.from_bus_number, lf.to_bus_number, lf.circuit_id, lf.time)

    def bus_fault():
        # Copy user entries into class object
        temp = (bf_bus_name_combo.get()).split(' ')
        bf.bus_number = temp[0]
        bf.time = bf_time_entry.get()

        # Check user entries
        bf.bus_number = check_bus_entry(bf.bus_number)
        if bf.bus_number == -1:
            show_popup_window(branch_window, "Error", "Bus number or name doesn't exist!")
            return
        try:
            bf.time = float(bf.time)
        except ValueError:
            show_popup_window(branch_window, "Error", "Time must be float value!")
            return
        if bf.time <= br.time or bf.time > br.time + 0.3:
            show_popup_window(branch_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (br.time, br.time + 0.3))
            return

        # Call method bus_fault from psse.py
        psse.bus_fault(bf.bus_number, bf.time)

    def update_if_from_combobox(_):
        bus_names_new = [elem for elem in bus_names if from_value.get() in elem]
        from_bus_name_combo["value"] = bus_names_new

    def update_if_to_combobox(_):
        bus_names_new = [elem for elem in bus_names if to_value.get() in elem]
        to_bus_name_combo["value"] = bus_names_new

    def update_lf_from_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_from_value.get() in elem]
        lf_from_bus_name_combo["value"] = bus_names_new

    def update_lf_to_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_to_value.get() in elem]
        lf_to_bus_name_combo["value"] = bus_names_new

    def update_bf_combobox(_):
        bus_names_new = [elem for elem in bus_names if bf_value.get() in elem]
        bf_bus_name_combo["value"] = bus_names_new

    # Start PSSe
    psse.start_psse()

    # Create branch window
    branch_window = Tk.Toplevel(root)
    branch_window.grab_set()
    branch_window.title("Branch")
    set_window_size(branch_window, 960, 540)

    # Create class objects
    br = Branch()
    lf = LineFault()
    bf = BusFault()

    # Create list of elements for combobox
    user_options = [True, False, False, False, False, False, False, True, False]
    user_filter = [""] * 9
    _, bus_names_list = element_info.bus_info(user_options, user_filter)
    bus_names = [(str(element[0]) + " " + element[1]).decode('latin1') for element in bus_names_list]

    # Create frame Initialize
    initialize_frame = Tk.LabelFrame(branch_window, text="Initialize")
    initialize_frame.grid(row=0, column=0, sticky=Tk.N)
    Tk.Label(initialize_frame, text="Output file name: ").grid(row=0, column=0)
    Tk.Label(initialize_frame, text="From bus number: ").grid(row=1, column=0)
    Tk.Label(initialize_frame, text="To bus number: ").grid(row=2, column=0)
    Tk.Label(initialize_frame, text="Circuit ID: ").grid(row=3, column=0)
    Tk.Label(initialize_frame, text="Add channels: ").grid(row=4, column=0)
    out_file_entry = Tk.Entry(initialize_frame)
    out_file_entry.grid(row=0, column=1, sticky=Tk.W)
    from_value = Tk.StringVar()
    from_bus_name_combo = ttk.Combobox(initialize_frame, values=bus_names, textvariable=from_value)
    from_bus_name_combo.set("")
    from_bus_name_combo.bind("<KeyRelease>", update_if_from_combobox)
    from_bus_name_combo.grid(row=1, column=1)
    to_value = Tk.StringVar()
    to_bus_name_combo = ttk.Combobox(initialize_frame, values=bus_names, textvariable=to_value)
    to_bus_name_combo.set("")
    to_bus_name_combo.bind("<KeyRelease>", update_if_to_combobox)
    to_bus_name_combo.grid(row=2, column=1)
    circuit_id_entry = Tk.Entry(initialize_frame)
    circuit_id_entry.grid(row=3, column=1, sticky=Tk.W)
    mva_var = Tk.IntVar()
    pq_var = Tk.IntVar()
    p_var = Tk.IntVar()
    Tk.Checkbutton(initialize_frame, text="MVA", variable=mva_var).grid(row=4, column=1, sticky=Tk.W)
    Tk.Checkbutton(initialize_frame, text="P and Q", variable=pq_var).grid(row=5, column=1, sticky=Tk.W)
    Tk.Checkbutton(initialize_frame, text="P", variable=p_var).grid(row=6, column=1, sticky=Tk.W)
    Tk.Button(initialize_frame, text="Initialize", command=initialize).grid(row=7, column=0, columnspan=2)

    # Create frame Run
    run_frame = Tk.LabelFrame(branch_window, text="Run dynamics")
    run_frame.grid(row=1, column=0, sticky=Tk.N, pady=(20, 0))
    Tk.Label(run_frame, text="Time of pause: ").grid(row=0, column=0)
    run_entry = Tk.Entry(run_frame)
    run_entry.grid(row=0, column=1)
    run_button = Tk.Button(run_frame, text="Run", state="disabled", command=run)
    run_button.grid(row=1, column=0, columnspan=2)

    # Create frame add Disturbance
    disturbance_frame = Tk.LabelFrame(branch_window, text="Add disturbance")
    disturbance_frame.grid(row=0, column=1, rowspan=2, padx=(50, 0), sticky=Tk.N)
    # Create frame Line Fault
    line_fault_frame = Tk.LabelFrame(disturbance_frame, text="Line fault")
    line_fault_frame.grid(row=0, column=0, pady=(10, 0))
    Tk.Label(line_fault_frame, text="From bus number: ").grid(row=0, column=0)
    Tk.Label(line_fault_frame, text="To bus number: ").grid(row=1, column=0)
    Tk.Label(line_fault_frame, text="Circuit ID: ").grid(row=2, column=0)
    Tk.Label(line_fault_frame, text="End time of fault: ").grid(row=3, column=0)
    lf_from_value = Tk.StringVar()
    lf_from_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_from_value)
    lf_from_bus_name_combo.set("")
    lf_from_bus_name_combo.bind("<KeyRelease>", update_lf_from_combobox)
    lf_from_bus_name_combo.grid(row=0, column=1)
    lf_to_value = Tk.StringVar()
    lf_to_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_to_value)
    lf_to_bus_name_combo.set("")
    lf_to_bus_name_combo.bind("<KeyRelease>", update_lf_to_combobox)
    lf_to_bus_name_combo.grid(row=1, column=1)
    lf_circuit_id_entry = Tk.Entry(line_fault_frame)
    lf_circuit_id_entry.grid(row=2, column=1, sticky=Tk.W)
    lf_time_entry = Tk.Entry(line_fault_frame)
    lf_time_entry.grid(row=3, column=1, sticky=Tk.W)
    line_fault_button = Tk.Button(line_fault_frame, text="Add disturbance", state="disabled", command=line_fault)
    line_fault_button.grid(row=4, column=0, columnspan=2)
    # Create frame Bus Fault
    bus_fault_frame = Tk.LabelFrame(disturbance_frame, text="Bus fault")
    bus_fault_frame.grid(row=1, column=0, pady=(30, 0))
    Tk.Label(bus_fault_frame, text="Bus number: ").grid(row=0, column=0)
    Tk.Label(bus_fault_frame, text="End time of fault: ").grid(row=1, column=0)
    bf_value = Tk.StringVar()
    bf_bus_name_combo = ttk.Combobox(bus_fault_frame, values=bus_names, textvariable=bf_value)
    bf_bus_name_combo.set("")
    bf_bus_name_combo.bind("<KeyRelease>", update_bf_combobox)
    bf_bus_name_combo.grid(row=0, column=1)
    bf_time_entry = Tk.Entry(bus_fault_frame)
    bf_time_entry.grid(row=1, column=1, sticky=Tk.W)
    bus_fault_button = Tk.Button(bus_fault_frame, text="Add disturbance", state="disabled", command=bus_fault)
    bus_fault_button.grid(row=2, column=0, columnspan=2)

    # Plot Graph
    plot_button = Tk.Button(branch_window, text="Plot graph", state="disabled")
    plot_button["command"] = lambda: psse.plot_graph(br.out_file, br.channel_count)
    plot_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    # Element Information
    info_button = Tk.Button(branch_window, text="Element Info", command=element_info_branch)
    info_button.grid(row=3, column=1, pady=(50, 0), sticky=Tk.SE)

    # Show Grid
    info_button = Tk.Button(branch_window, text="Show Grid", command=show_grid_image)
    info_button.grid(row=4, column=1, sticky=Tk.SE)


def set_machine_window():
    def initialize():
        # Start PSSe
        psse.start_psse()

        # Copy user entries into class object
        mch.out_file = out_file_entry.get()
        temp = (bus_name_combo.get()).split(' ')
        mch.bus_number = temp[0]
        mch.machine_id = machine_id_entry.get()
        mch.angle_ch = angle_var.get()
        mch.pelec_ch = pelec_var.get()

        # Check user entries
        mch.out_file = psse.check_out_file(mch.out_file)
        mch.bus_number = check_bus_entry(mch.bus_number)
        if mch.bus_number == -1:
            show_popup_window(machine_window, "Error", "Bus number or name doesn't exist!")
            return
        if not psse.check_if_machine_exist(mch.bus_number, mch.machine_id):
            show_popup_window(machine_window, "Error", "Machine doesn't exist!")
            return
        if (mch.angle_ch + mch.pelec_ch) == 0:
            show_popup_window(machine_window, "Error", "Check at least one output channel!")
            return

        # Add output channels
        mch.channel_count = psse.add_machine_channels(mch.out_file, mch.bus_number, mch.machine_id,
                                                      mch.angle_ch, mch.pelec_ch)

        # Enable run button and disable disturbance and plot buttons
        run_button["state"] = "normal"
        line_fault_button["state"] = "disabled"
        bus_fault_button["state"] = "disabled"
        plot_button["state"] = "disabled"
        return

    def run():
        # Run dynamics
        mch.time = run_entry.get()
        try:
            mch.time = float(mch.time)
        except ValueError:
            show_popup_window(machine_window, "Error", "Time of pause must be float value!")
        else:
            # Enable disturbance buttons and plot button
            line_fault_button["state"] = "normal"
            bus_fault_button["state"] = "normal"
            plot_button["state"] = "normal"
            psse.run(mch.time)

    def line_fault():
        # Copy user entries into class object
        temp = (lf_from_bus_name_combo.get()).split(' ')
        lf.from_bus_number = temp[0]
        temp = (lf_to_bus_name_combo.get()).split(' ')
        lf.to_bus_number = temp[0]
        lf.circuit_id = lf_circuit_id_entry.get()
        lf.time = lf_time_entry.get()

        # Check user entries
        lf.from_bus_number = check_bus_entry(lf.from_bus_number)
        if lf.from_bus_number == -1:
            show_popup_window(machine_window, "Error", "From bus number or name doesn't exist!")
            return
        lf.to_bus_number = check_bus_entry(lf.to_bus_number)
        if lf.to_bus_number == -1:
            show_popup_window(machine_window, "Error", "To bus number or name doesn't exist!")
            return
        if not psse.check_if_branch_exist(lf.from_bus_number, lf.to_bus_number, lf.circuit_id):
            show_popup_window(machine_window, "Error", "Branch doesn't exist!")
            return
        try:
            lf.time = float(lf.time)
        except ValueError:
            show_popup_window(machine_window, "Error", "Time must be float value!")
            return
        if lf.time <= mch.time or lf.time > mch.time + 0.3:
            show_popup_window(machine_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (mch.time, mch.time + 0.3))
            return

        # Call method line_fault from psse.py
        psse.line_fault(lf.from_bus_number, lf.to_bus_number, lf.circuit_id, lf.time)

    def bus_fault():
        # Copy user entries into class object
        temp = (bf_bus_name_combo.get()).split(' ')
        bf.bus_number = temp[0]
        bf.time = bf_time_entry.get()

        # Check user entries
        bf.bus_number = check_bus_entry(bf.bus_number)
        if bf.bus_number == -1:
            show_popup_window(machine_window, "Error", "Bus number or name doesn't exist!")
            return
        try:
            bf.time = float(bf.time)
        except ValueError:
            show_popup_window(machine_window, "Error", "Time must be float value!")
            return
        if bf.time <= mch.time or bf.time > mch.time + 0.3:
            show_popup_window(machine_window, "Error", "End time of fault must be between <%.2f, %.2f]"
                              % (mch.time, mch.time + 0.3))
            return

        # Call method bus_fault from psse.py
        psse.bus_fault(bf.bus_number, bf.time)

    def update_if_combobox(_):
        # Underscore is event object that is not used
        bus_names_new = [elem for elem in bus_names if if_value.get() in elem]
        bus_name_combo["value"] = bus_names_new

    def update_lf_from_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_from_value.get() in elem]
        lf_from_bus_name_combo["value"] = bus_names_new

    def update_lf_to_combobox(_):
        bus_names_new = [elem for elem in bus_names if lf_to_value.get() in elem]
        lf_to_bus_name_combo["value"] = bus_names_new

    def update_bf_combobox(_):
        bus_names_new = [elem for elem in bus_names if bf_value.get() in elem]
        bf_bus_name_combo["value"] = bus_names_new

    # Start PSSe
    psse.start_psse()

    # Create branch window
    machine_window = Tk.Toplevel(root)
    machine_window.grab_set()
    machine_window.title("Machine")
    set_window_size(machine_window, 960, 540)

    # Create class objects
    mch = Machine()
    lf = LineFault()
    bf = BusFault()

    # Create list of elements for combobox
    user_options = [True, False, False, False, False, False, False, True, False]
    user_filter = [""] * 9
    _, bus_names_list = element_info.bus_info(user_options, user_filter)
    bus_names = [(str(element[0]) + " " + element[1]).decode('latin1') for element in bus_names_list]

    # Create frame Initialize
    initialize_frame = Tk.LabelFrame(machine_window, text="Initialize")
    initialize_frame.grid(row=0, column=0, sticky=Tk.N)
    Tk.Label(initialize_frame, text="Output file name: ").grid(row=0, column=0)
    Tk.Label(initialize_frame, text="Bus: ").grid(row=1, column=0)
    Tk.Label(initialize_frame, text="Machine ID: ").grid(row=2, column=0)
    Tk.Label(initialize_frame, text="Add channels: ").grid(row=3, column=0)
    out_file_entry = Tk.Entry(initialize_frame)
    out_file_entry.grid(row=0, column=1, sticky=Tk.W)
    if_value = Tk.StringVar()
    bus_name_combo = ttk.Combobox(initialize_frame, values=bus_names, textvariable=if_value)
    bus_name_combo.set("")
    bus_name_combo.bind("<KeyRelease>", update_if_combobox)
    bus_name_combo.grid(row=1, column=1, sticky=Tk.W)
    machine_id_entry = Tk.Entry(initialize_frame)
    machine_id_entry.grid(row=2, column=1, sticky=Tk.W)
    angle_var = Tk.IntVar()
    pelec_var = Tk.IntVar()
    Tk.Checkbutton(initialize_frame, text="Angle", variable=angle_var).grid(row=3, column=1, sticky=Tk.W)
    Tk.Checkbutton(initialize_frame, text="Pelec", variable=pelec_var).grid(row=4, column=1, sticky=Tk.W)
    Tk.Button(initialize_frame, text="Initialize", command=initialize).grid(row=5, column=0, columnspan=2)

    # Create frame Run
    run_frame = Tk.LabelFrame(machine_window, text="Run dynamics")
    run_frame.grid(row=1, column=0, sticky=Tk.N, pady=(20, 0))
    Tk.Label(run_frame, text="Time of pause: ").grid(row=0, column=0)
    run_entry = Tk.Entry(run_frame)
    run_entry.grid(row=0, column=1)
    run_button = Tk.Button(run_frame, text="Run", state="disabled", command=run)
    run_button.grid(row=1, column=0, columnspan=2)

    # Create frame add Disturbance
    disturbance_frame = Tk.LabelFrame(machine_window, text="Add disturbance")
    disturbance_frame.grid(row=0, column=1, rowspan=2, padx=(50, 0), sticky=Tk.N)
    # Create frame Line Fault
    line_fault_frame = Tk.LabelFrame(disturbance_frame, text="Line fault")
    line_fault_frame.grid(row=0, column=0, pady=(10, 0))
    Tk.Label(line_fault_frame, text="From bus: ").grid(row=0, column=0)
    Tk.Label(line_fault_frame, text="To bus: ").grid(row=1, column=0)
    Tk.Label(line_fault_frame, text="Circuit ID: ").grid(row=2, column=0)
    Tk.Label(line_fault_frame, text="End time of fault: ").grid(row=3, column=0)
    lf_from_value = Tk.StringVar()
    lf_from_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_from_value)
    lf_from_bus_name_combo.set("")
    lf_from_bus_name_combo.bind("<KeyRelease>", update_lf_from_combobox)
    lf_from_bus_name_combo.grid(row=0, column=1)
    lf_to_value = Tk.StringVar()
    lf_to_bus_name_combo = ttk.Combobox(line_fault_frame, values=bus_names, textvariable=lf_to_value)
    lf_to_bus_name_combo.set("")
    lf_to_bus_name_combo.bind("<KeyRelease>", update_lf_to_combobox)
    lf_to_bus_name_combo.grid(row=1, column=1)
    lf_circuit_id_entry = Tk.Entry(line_fault_frame)
    lf_circuit_id_entry.grid(row=2, column=1, sticky=Tk.W)
    lf_time_entry = Tk.Entry(line_fault_frame)
    lf_time_entry.grid(row=3, column=1, sticky=Tk.W)
    line_fault_button = Tk.Button(line_fault_frame, text="Add disturbance", state="disabled", command=line_fault)
    line_fault_button.grid(row=4, column=0, columnspan=2)
    # Create frame Bus Fault
    bus_fault_frame = Tk.LabelFrame(disturbance_frame, text="Bus fault")
    bus_fault_frame.grid(row=1, column=0, pady=(30, 0))
    Tk.Label(bus_fault_frame, text="Bus: ").grid(row=0, column=0)
    Tk.Label(bus_fault_frame, text="End time of fault: ").grid(row=1, column=0)
    bf_value = Tk.StringVar()
    bf_bus_name_combo = ttk.Combobox(bus_fault_frame, values=bus_names, textvariable=bf_value)
    bf_bus_name_combo.set("")
    bf_bus_name_combo.bind("<KeyRelease>", update_bf_combobox)
    bf_bus_name_combo.grid(row=0, column=1)
    bf_time_entry = Tk.Entry(bus_fault_frame)
    bf_time_entry.grid(row=1, column=1, sticky=Tk.W)
    bus_fault_button = Tk.Button(bus_fault_frame, text="Add disturbance", state="disabled", command=bus_fault)
    bus_fault_button.grid(row=2, column=0, columnspan=2)

    # Plot Graph
    plot_button = Tk.Button(machine_window, text="Plot graph", state="disabled")
    plot_button["command"] = lambda: psse.plot_graph(mch.out_file, mch.channel_count)
    plot_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    # Element Information
    info_button = Tk.Button(machine_window, text="Element Info", command=element_info_machine)
    info_button.grid(row=3, column=1, pady=(50, 0), sticky=Tk.SE)

    # Show Grid
    info_button = Tk.Button(machine_window, text="Show Grid", command=show_grid_image)
    info_button.grid(row=4, column=1, sticky=Tk.SE)


def element_info_bus():
    def bus_filter():
        # Save user 'Show' input to array but cast it from integer to boolean
        user_options = [False] * 9
        user_options[0] = True if number_var.get() == 1 else False
        user_options[1] = True if type_var.get() == 1 else False
        user_options[2] = True if area_var.get() == 1 else False
        user_options[3] = True if zone_var.get() == 1 else False
        user_options[4] = True if base_var.get() == 1 else False
        user_options[5] = True if kv_var.get() == 1 else False
        user_options[6] = True if angled_var.get() == 1 else False
        user_options[7] = True if name_var.get() == 1 else False
        user_options[8] = True if exname_var.get() == 1 else False

        # At least one attribute must be checked
        if not any(user_options):
            show_popup_window(ei_bus_window, "Error", "Check at least one attribute!")
            return

        # Save user 'Filter' input to array
        user_filter = [number_entry.get(), type_entry.get(), area_entry.get(), zone_entry.get(), base_entry.get(),
                       kv_entry.get(), angled_entry.get(), name_entry.get(), exname_entry.get()]

        # Call element_info.py methods to find and write information
        header, info = element_info.bus_info(user_options, user_filter)
        show_elements(ei_bus_window, header, info)

    # Create Element Info Bus window
    ei_bus_window = Tk.Toplevel(root)
    ei_bus_window.grab_set()
    ei_bus_window.title("Element info - Bus")
    set_window_size(ei_bus_window, 1280, 720)

    # Create frame Input
    input_frame = Tk.Frame(ei_bus_window)
    input_frame.grid(row=0, column=0, sticky=Tk.N)

    # Create header
    Tk.Label(input_frame, text="Show:").grid(row=0, column=0)
    Tk.Label(input_frame, text="Filter by:").grid(row=0, column=1)
    # Bus Attributes
    # Create Tkinter variables
    number_var = Tk.IntVar()
    type_var = Tk.IntVar()
    area_var = Tk.IntVar()
    zone_var = Tk.IntVar()
    base_var = Tk.IntVar()
    kv_var = Tk.IntVar()
    angled_var = Tk.IntVar()
    name_var = Tk.IntVar()
    exname_var = Tk.IntVar()
    # Create check buttons
    Tk.Checkbutton(input_frame, text="Number", variable=number_var).grid(row=1, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Type", variable=type_var).grid(row=2, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Area", variable=area_var).grid(row=3, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Zone", variable=zone_var).grid(row=4, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Base", variable=base_var).grid(row=5, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="kV", variable=kv_var).grid(row=6, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Angle", variable=angled_var).grid(row=7, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Name", variable=name_var).grid(row=8, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Ex Name", variable=exname_var).grid(row=9, column=0, sticky=Tk.W)
    # Create Tkinter entries
    number_entry = Tk.Entry(input_frame)
    type_entry = Tk.Entry(input_frame)
    area_entry = Tk.Entry(input_frame)
    zone_entry = Tk.Entry(input_frame)
    base_entry = Tk.Entry(input_frame)
    kv_entry = Tk.Entry(input_frame)
    angled_entry = Tk.Entry(input_frame)
    name_entry = Tk.Entry(input_frame)
    exname_entry = Tk.Entry(input_frame)
    # Set grid coordinates for entries
    number_entry.grid(row=1, column=1)
    type_entry.grid(row=2, column=1)
    area_entry.grid(row=3, column=1)
    zone_entry.grid(row=4, column=1)
    base_entry.grid(row=5, column=1)
    kv_entry.grid(row=6, column=1)
    angled_entry.grid(row=7, column=1)
    name_entry.grid(row=8, column=1)
    exname_entry.grid(row=9, column=1)
    # Create filter button
    Tk.Button(input_frame, text="Filter", command=bus_filter).grid(row=10, column=0, pady=(10, 0), columnspan=2)


def element_info_branch():
    def branch_filter():
        # Save user 'Show' input to array but cast it from integer to boolean
        user_options = [False] * 13
        user_options[0] = True if fromnumber_var.get() == 1 else False
        user_options[1] = True if tonumber_var.get() == 1 else False
        user_options[2] = True if status_var.get() == 1 else False
        user_options[3] = True if amps_var.get() == 1 else False
        user_options[4] = True if ratea_var.get() == 1 else False
        user_options[5] = True if p_var.get() == 1 else False
        user_options[6] = True if q_var.get() == 1 else False
        user_options[7] = True if mva_var.get() == 1 else False
        user_options[8] = True if id_var.get() == 1 else False
        user_options[9] = True if fromname_var.get() == 1 else False
        user_options[10] = True if fromexname_var.get() == 1 else False
        user_options[11] = True if toname_var.get() == 1 else False
        user_options[12] = True if toexname_var.get() == 1 else False

        # At least one attribute must be checked
        if not any(user_options):
            show_popup_window(ei_branch_window, "Error", "Check at least one attribute!")
            return

        # Save user 'Filter' input to array
        user_filter = [fromnumber_entry.get(), tonumber_entry.get(), status_entry.get(), amps_entry.get(),
                       ratea_entry.get(), p_entry.get(), q_entry.get(), mva_entry.get(), id_entry.get(),
                       fromname_entry.get(), fromexname_entry.get(), toname_entry.get(), toexname_entry.get()]

        # Call element_info.py methods to find and write information
        header, info = element_info.branch_info(user_options, user_filter)
        show_elements(ei_branch_window, header, info)

    # Create Element Info Branch window
    ei_branch_window = Tk.Toplevel(root)
    ei_branch_window.grab_set()
    ei_branch_window.title("Element info - Branch")
    set_window_size(ei_branch_window, 1280, 720)

    # Create frame Input
    input_frame = Tk.Frame(ei_branch_window)
    input_frame.grid(row=0, column=0, sticky=Tk.N)

    # Create header
    Tk.Label(input_frame, text="Show:").grid(row=0, column=0)
    Tk.Label(input_frame, text="Filter by:").grid(row=0, column=1)
    # Branch attributes
    # Create Tkinter variables
    fromnumber_var = Tk.IntVar()
    tonumber_var = Tk.IntVar()
    status_var = Tk.IntVar()
    amps_var = Tk.IntVar()
    ratea_var = Tk.IntVar()
    p_var = Tk.IntVar()
    q_var = Tk.IntVar()
    mva_var = Tk.IntVar()
    id_var = Tk.IntVar()
    fromname_var = Tk.IntVar()
    fromexname_var = Tk.IntVar()
    toname_var = Tk.IntVar()
    toexname_var = Tk.IntVar()
    # Create check buttons
    Tk.Checkbutton(input_frame, text="From number", variable=fromnumber_var).grid(row=1, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="To number", variable=tonumber_var).grid(row=2, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Status", variable=status_var).grid(row=3, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Amps", variable=amps_var).grid(row=4, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Rate A", variable=ratea_var).grid(row=5, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="P", variable=p_var).grid(row=6, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Q", variable=q_var).grid(row=7, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="MVA", variable=mva_var).grid(row=8, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="ID", variable=id_var).grid(row=9, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="From name", variable=fromname_var).grid(row=10, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="From exname", variable=fromexname_var).grid(row=11, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="To name", variable=toname_var).grid(row=12, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="To exname", variable=toexname_var).grid(row=13, column=0, sticky=Tk.W)
    # Create Tkinter entries
    fromnumber_entry = Tk.Entry(input_frame)
    tonumber_entry = Tk.Entry(input_frame)
    status_entry = Tk.Entry(input_frame)
    amps_entry = Tk.Entry(input_frame)
    ratea_entry = Tk.Entry(input_frame)
    p_entry = Tk.Entry(input_frame)
    q_entry = Tk.Entry(input_frame)
    mva_entry = Tk.Entry(input_frame)
    id_entry = Tk.Entry(input_frame)
    fromname_entry = Tk.Entry(input_frame)
    fromexname_entry = Tk.Entry(input_frame)
    toname_entry = Tk.Entry(input_frame)
    toexname_entry = Tk.Entry(input_frame)
    # Set grid coordinates for entries
    fromnumber_entry.grid(row=1, column=1)
    tonumber_entry.grid(row=2, column=1)
    status_entry.grid(row=3, column=1)
    amps_entry.grid(row=4, column=1)
    ratea_entry.grid(row=5, column=1)
    p_entry.grid(row=6, column=1)
    q_entry.grid(row=7, column=1)
    mva_entry.grid(row=8, column=1)
    id_entry.grid(row=9, column=1)
    fromname_entry.grid(row=10, column=1)
    fromexname_entry.grid(row=11, column=1)
    toname_entry.grid(row=12, column=1)
    toexname_entry.grid(row=13, column=1)
    # Create filter button
    Tk.Button(input_frame, text="Filter", command=branch_filter).grid(row=14, column=0, pady=(10, 0), columnspan=2)


def element_info_machine():
    def machine_filter():
        # Save user 'Show' input to array but cast it from integer to boolean
        user_options = [False] * 14
        user_options[0] = True if number_var.get() == 1 else False
        user_options[1] = True if status_var.get() == 1 else False
        user_options[2] = True if mbase_var.get() == 1 else False
        user_options[3] = True if gentap_var.get() == 1 else False
        user_options[4] = True if pgen_var.get() == 1 else False
        user_options[5] = True if qgen_var.get() == 1 else False
        user_options[6] = True if mva_var.get() == 1 else False
        user_options[7] = True if pmax_var.get() == 1 else False
        user_options[8] = True if pmin_var.get() == 1 else False
        user_options[9] = True if qmax_var.get() == 1 else False
        user_options[10] = True if qmin_var.get() == 1 else False
        user_options[11] = True if id_var.get() == 1 else False
        user_options[12] = True if name_var.get() == 1 else False
        user_options[13] = True if exname_var.get() == 1 else False

        # At least one attribute must be checked
        if not any(user_options):
            show_popup_window(ei_machine_window, "Error", "Check at least one attribute!")
            return

        # Save user 'Filter' input to array
        user_filter = [number_entry.get(), status_entry.get(), mbase_entry.get(), gentap_entry.get(), pgen_entry.get(),
                       qgen_entry.get(), mva_entry.get(), pmax_entry.get(), pmin_entry.get(), qmax_entry.get(),
                       qmin_entry.get(), id_entry.get(), name_entry.get(), exname_entry.get()]

        # Call element_info.py methods to find and write information
        header, info = element_info.machine_info(user_options, user_filter)
        show_elements(ei_machine_window, header, info)

    # Create Element Info Branch window
    ei_machine_window = Tk.Toplevel(root)
    ei_machine_window.grab_set()
    ei_machine_window.title("Element info - Machine")
    set_window_size(ei_machine_window, 1280, 720)

    # Create frame Input
    input_frame = Tk.Frame(ei_machine_window)
    input_frame.grid(row=0, column=0, sticky=Tk.N)

    # Create header
    Tk.Label(input_frame, text="Show:").grid(row=0, column=0)
    Tk.Label(input_frame, text="Filter by:").grid(row=0, column=1)
    # Machine attributes
    # Create Tkinter variables
    number_var = Tk.IntVar()
    status_var = Tk.IntVar()
    mbase_var = Tk.IntVar()
    gentap_var = Tk.IntVar()
    pgen_var = Tk.IntVar()
    qgen_var = Tk.IntVar()
    mva_var = Tk.IntVar()
    pmax_var = Tk.IntVar()
    pmin_var = Tk.IntVar()
    qmax_var = Tk.IntVar()
    qmin_var = Tk.IntVar()
    id_var = Tk.IntVar()
    name_var = Tk.IntVar()
    exname_var = Tk.IntVar()
    # Create check buttons
    Tk.Checkbutton(input_frame, text="Number", variable=number_var).grid(row=1, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Status", variable=status_var).grid(row=2, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="M base", variable=mbase_var).grid(row=3, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Gen tap", variable=gentap_var).grid(row=4, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="P gen", variable=pgen_var).grid(row=5, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Q gen", variable=qgen_var).grid(row=6, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="MVA", variable=mva_var).grid(row=7, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="P max", variable=pmax_var).grid(row=8, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="P min", variable=pmin_var).grid(row=9, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Q max", variable=qmax_var).grid(row=10, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Q min", variable=qmin_var).grid(row=11, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="ID", variable=id_var).grid(row=12, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Name", variable=name_var).grid(row=13, column=0, sticky=Tk.W)
    Tk.Checkbutton(input_frame, text="Ex name", variable=exname_var).grid(row=14, column=0, sticky=Tk.W)
    # Create Tkinter entries
    number_entry = Tk.Entry(input_frame)
    status_entry = Tk.Entry(input_frame)
    mbase_entry = Tk.Entry(input_frame)
    gentap_entry = Tk.Entry(input_frame)
    pgen_entry = Tk.Entry(input_frame)
    qgen_entry = Tk.Entry(input_frame)
    mva_entry = Tk.Entry(input_frame)
    pmax_entry = Tk.Entry(input_frame)
    pmin_entry = Tk.Entry(input_frame)
    qmax_entry = Tk.Entry(input_frame)
    qmin_entry = Tk.Entry(input_frame)
    id_entry = Tk.Entry(input_frame)
    name_entry = Tk.Entry(input_frame)
    exname_entry = Tk.Entry(input_frame)
    # Set grid coordinates for entries
    number_entry.grid(row=1, column=1)
    status_entry.grid(row=2, column=1)
    mbase_entry.grid(row=3, column=1)
    gentap_entry.grid(row=4, column=1)
    pgen_entry.grid(row=5, column=1)
    qgen_entry.grid(row=6, column=1)
    mva_entry.grid(row=7, column=1)
    pmax_entry.grid(row=8, column=1)
    pmin_entry.grid(row=9, column=1)
    qmax_entry.grid(row=10, column=1)
    qmin_entry.grid(row=11, column=1)
    id_entry.grid(row=12, column=1)
    name_entry.grid(row=13, column=1)
    exname_entry.grid(row=14, column=1)
    # Create filter button
    Tk.Button(input_frame, text="Filter", command=machine_filter).grid(row=15, column=0, pady=(10, 0), columnspan=2)


def check_bus_number(bus_number):
    if not bus_number.isdigit():
        return False
    return psse.check_if_bus_exist(int(bus_number))


def check_bus_entry(user_input):
    # Return bus number or -1 if bus doesn't exist
    if user_input.isdigit():
        return int(user_input)
    else:
        return psse.check_bus_name(user_input)


def show_popup_window(window, title, message):
    popup_window = Tk.Toplevel(window)
    popup_window.grab_set()
    popup_window.title(title)
    set_window_size(popup_window, 300, 60)
    Tk.Label(popup_window, text=message).pack()
    ok_button = Tk.Button(popup_window, text="OK", command=popup_window.destroy)
    set_button_size([ok_button], 4, 1, 10)
    ok_button.pack()


def show_elements(ei_window, header, info):
    # Initialize Text and Scrollbar instances
    text = Tk.Text(ei_window)
    scroll = Tk.Scrollbar(ei_window, command=text.yview, orient=Tk.VERTICAL)

    # Write header
    header_string = ""
    for attribute in header:
        # Name uses more space
        if "NAME" in attribute:
            header_string += attribute + "\t     "
        else:
            header_string += attribute + "\t"
    text.insert(Tk.INSERT, header_string)

    # Max width od some element and max_height
    max_width = len(header_string)
    max_height = 1

    # Write element info
    for element in info:
        element_string = "\n"
        for attribute in element:
            attribute = round(attribute, 2) if isinstance(attribute, float) else attribute
            element_string += str(attribute) + "\t"
        text.insert(Tk.INSERT, element_string)
        if len(element_string) > max_width:
            max_width = len(element_string)
        if max_height < 43:
            max_height += 1

    # Configure text and set grid positions for text and scrollbar
    text.configure(width=max_width+20, height=max_height, yscrollcommand=scroll.set)
    text.grid(row=0, column=1, sticky=Tk.NSEW)
    scroll.grid(row=0, column=2, sticky=Tk.NS+Tk.W)


def show_grid_image():
    grid_image = Image.open('images/croatian_ees_grid.jpg')
    grid_image.show()


def on_closing():
    root.destroy()


if __name__ == '__main__':
    root = Tk.Tk()
    set_root_window()
    root.mainloop()

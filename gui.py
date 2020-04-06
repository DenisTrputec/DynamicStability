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
import Tkinter as Tk
import tkFont
# from PIL import ImageTk, Image


class Bus:
    def __init__(self):
        self.out_file = None
        self.bus_number = None
        self.freq_ch = None
        self.vol_ch = None
        self.vol_ang_ch = None
        self.time = None
        self.channel_count = None


class LineFault:
    def __init__(self):
        self.bus1_number = None
        self.bus2_number = None
        self.circuit_id = None
        self.time = None


class BusFault:
    def __init__(self):
        self.bus_number = None
        self.time = None


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
    button_dynamics = Tk.Button(root, text="Dynamic analysis", command=set_dynamic_analysis_window)
    button_dynamics.grid(row=0, column=0)
    button_semaphore = Tk.Button(root, text="Semaphore", command=set_semaphore_window)
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
    button_branch = Tk.Button(dynamics_window, text="Branch", command=set_bus_window)
    button_branch.grid(row=1, column=0)
    button_machine = Tk.Button(dynamics_window, text="Machine", command=set_bus_window)
    button_machine.grid(row=2, column=0)
    button_back = Tk.Button(dynamics_window, text="Back", command=return_to_root)
    button_back.grid(row=3, column=0)
    set_button_size([button_bus, button_branch, button_machine, button_back], 15, 2, 14)
    dynamics_window.protocol("WM_DELETE_WINDOW", on_closing)


def set_semaphore_window():
    pass


def set_bus_window():
    def initialize():
        # Start PSSe
        psse.start_psse()

        # Copy user entries into class object
        bus.out_file = out_file_entry.get()
        bus.bus_number = bus_number_entry.get()
        bus.freq_ch = freq_var.get()
        bus.vol_ch = vol_var.get()
        bus.vol_ang_ch = vol_ang_var.get()

        # Check user entries
        bus.out_file = psse.check_out_file(bus.out_file)
        if not check_bus_number(bus.bus_number):
            show_popup_window(bus_window, "Error", "Bus number doesn't exist!")
            return
        bus.bus_number = int(bus.bus_number)
        if (freq_var.get() + vol_var.get() + vol_ang_var.get()) == 0:
            show_popup_window(bus_window, "Error", "Check at least one output channel!")
            return

        # Add output channels
        bus.channel_count = psse.add_bus_channels(bus.out_file, int(bus_number_entry.get()),
                                                  freq_var.get(), vol_var.get(), vol_ang_var.get())

        # Enable run button
        run_button["state"] = "normal"
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
        lf.bus1_number = lf_bus1_number_entry.get()
        lf.bus2_number = lf_bus2_number_entry.get()
        lf.circuit_id = lf_circuit_id_entry.get()
        lf.time = lf_time_entry.get()

        # Check user entries
        if lf.bus1_number.isdigit() and lf.bus2_number.isdigit():
            lf.bus1_number = int(lf.bus1_number)
            lf.bus2_number = int(lf.bus2_number)
        else:
            show_popup_window(bus_window, "Error", "Bus number entry should be integer!")
            return
        if not psse.check_if_branch_exist(lf.bus1_number, lf.bus2_number, lf.circuit_id):
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
        psse.disturbance(lf.bus1_number, lf.bus2_number, lf.circuit_id, lf.time)

    def bus_fault():
        pass

    # Create Bus window
    bus_window = Tk.Toplevel(root)
    bus_window.grab_set()
    bus_window.title("Bus")
    set_window_size(bus_window, 960, 540)

    # Create class objects
    bus = Bus()
    lf = LineFault()

    # Create frame Initialize
    initialize_frame = Tk.LabelFrame(bus_window, text="Initialize")
    initialize_frame.grid(row=0, column=0, sticky=Tk.N)
    Tk.Label(initialize_frame, text="Output file name: ").grid(row=0, column=0)
    Tk.Label(initialize_frame, text="Bus number: ").grid(row=1, column=0)
    Tk.Label(initialize_frame, text="Add channels: ").grid(row=2, column=0)
    out_file_entry = Tk.Entry(initialize_frame)
    out_file_entry.grid(row=0, column=1)
    bus_number_entry = Tk.Entry(initialize_frame)
    bus_number_entry.grid(row=1, column=1)
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

    # Create frame add Disturbance
    disturbance_frame = Tk.LabelFrame(bus_window, text="Add disturbance")
    disturbance_frame.grid(row=0, column=1, rowspan=2, padx=(50, 0), sticky=Tk.N)
    # Create frame Line Fault
    line_fault_frame = Tk.LabelFrame(disturbance_frame, text="Line fault")
    line_fault_frame.grid(row=0, column=0, pady=(10, 0))
    Tk.Label(line_fault_frame, text="Bus number 1: ").grid(row=0, column=0)
    Tk.Label(line_fault_frame, text="Bus number 2: ").grid(row=1, column=0)
    Tk.Label(line_fault_frame, text="Circuit ID: ").grid(row=2, column=0)
    Tk.Label(line_fault_frame, text="End time of fault: ").grid(row=3, column=0)
    lf_bus1_number_entry = Tk.Entry(line_fault_frame)
    lf_bus1_number_entry.grid(row=0, column=1)
    lf_bus2_number_entry = Tk.Entry(line_fault_frame)
    lf_bus2_number_entry.grid(row=1, column=1)
    lf_circuit_id_entry = Tk.Entry(line_fault_frame)
    lf_circuit_id_entry.grid(row=2, column=1)
    lf_time_entry = Tk.Entry(line_fault_frame)
    lf_time_entry.grid(row=3, column=1)
    line_fault_button = Tk.Button(line_fault_frame, text="Add disturbance", state="disabled", command=line_fault)
    line_fault_button.grid(row=4, column=0, columnspan=2)
    # Create frame Bus Fault
    bus_fault_frame = Tk.LabelFrame(disturbance_frame, text="Bus fault")
    bus_fault_frame.grid(row=1, column=0, pady=(30, 0))
    Tk.Label(bus_fault_frame, text="Bus number: ").grid(row=0, column=0)
    Tk.Label(bus_fault_frame, text="End time of fault: ").grid(row=1, column=0)
    bf_bus_number_entry = Tk.Entry(bus_fault_frame)
    bf_bus_number_entry.grid(row=0, column=1)
    bf_time_entry = Tk.Entry(bus_fault_frame)
    bf_time_entry.grid(row=1, column=1)
    bus_fault_button = Tk.Button(bus_fault_frame, text="Add disturbance", state="disabled", command=bus_fault)
    bus_fault_button.grid(row=2, column=0, columnspan=2)

    # Plot Graph
    plot_button = Tk.Button(bus_window, text="Plot graph", state="disabled")
    plot_button["command"] = lambda: psse.plot_graph(bus.out_file, bus.channel_count)
    plot_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))


def check_bus_number(bus_number):
    if not bus_number.isdigit():
        return False
    return psse.check_if_bus_exist(int(bus_number))


def show_popup_window(window, title, message):
    popup_window = Tk.Toplevel(window)
    popup_window.grab_set()
    popup_window.title(title)
    set_window_size(popup_window, 300, 60)
    Tk.Label(popup_window, text=message).pack()
    ok_button = Tk.Button(popup_window, text="OK", command=popup_window.destroy)
    set_button_size([ok_button], 4, 1, 10)
    ok_button.pack()


def on_closing():
    root.destroy()


if __name__ == '__main__':
    root = Tk.Tk()
    set_root_window()
    root.mainloop()

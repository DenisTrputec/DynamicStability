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
    button_bus = Tk.Button(root, text="Bus", command=set_bus_window)
    button_bus.grid(row=0, column=0)
    set_button_size([button_bus], 15, 2, 14)


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
            psse.run(bus.out_file, bus.channel_count, bus.time)

    # Create Bus window
    bus_window = Tk.Toplevel(root)
    bus_window.grab_set()
    bus_window.title("Bus")
    set_window_size(bus_window, 960, 540)

    # Create class object
    bus = Bus()

    # Create frame Initialize
    initialize_frame = Tk.Frame(bus_window)
    initialize_frame.grid(row=0, column=0)
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
    run_frame = Tk.Frame(bus_window)
    run_frame.grid(row=1, column=0, pady=(30, 0))
    Tk.Label(run_frame, text="Time of pause: ").grid(row=0, column=0)
    run_entry = Tk.Entry(run_frame)
    run_entry.grid(row=0, column=1)
    run_button = Tk.Button(run_frame, text="Run", state="disabled", command=run)
    run_button.grid(row=8, column=0, columnspan=2)


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


if __name__ == '__main__':
    root = Tk.Tk()
    set_root_window()
    root.mainloop()

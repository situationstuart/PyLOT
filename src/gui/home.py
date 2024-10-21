# This is the page for the logbook elements of the app.
# Contained within here should be any functionality of viewing, creating, and editing logbook entries.


import customtkinter as ctk
from CTkTable import CTkTable # Source: https://github.com/Akascape/CTkTable
from utils.screen_utils import generate_frame_header

tableDataPlaceholder = [
    ["Date", "Reg.", "Dep.", "Arr.", "Duration"],
    ["20-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["19-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["18-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["17-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["16-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["15-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"],
    ["14-Oct-2024", "G-CLFY", "EGKB", "EGKB", "1:23"]
]

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)
        self.app = app

        generate_frame_header(self, "PyLOT")

        self.frm_body = ctk.CTkFrame(self, fg_color="transparent")
        self.frm_body.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        # Configure columns for proportional resizing
        self.frm_body.columnconfigure(0, weight=1)  # Left third
        self.frm_body.columnconfigure(1, weight=2)  # Right two-thirds
        self.frm_body.columnconfigure(2, weight=1)

        # Frame instantiations
        self.frm_recent = ctk.CTkFrame(self.frm_body)
        self.frm_dashboard = ctk.CTkFrame(self.frm_body)
        self.frm_notifs = ctk.CTkFrame(self.frm_body)
        self.frm_upcoming = ctk.CTkFrame(self.frm_body)
        self.frm_map = ctk.CTkFrame(self.frm_body)

        # Frame placements
        self.frm_recent.grid(row=0, column=0, sticky="nsew", padx=10)
        self.frm_dashboard.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=10)
        self.frm_notifs.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.frm_upcoming.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.frm_map.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # frm_recent configuration & elements
        self.lbl_recent_title = ctk.CTkLabel(self.frm_recent, 
                                             text="Recent Logbook Entries", 
                                             font=("", 20),
                                             anchor="center")
        self.lbl_recent_title.grid(row=0, column=0, sticky="new", pady=10)

        self.tbl_recent = CTkTable(self.frm_recent, row=6, column=5,
                                   values=tableDataPlaceholder,
                                   width=0)
        self.tbl_recent.grid(row=1, column=0, sticky="nsew")

        self.frm_recent.rowconfigure(0, weight=1) # Configure row for tbl_recent to expand
        self.frm_recent.columnconfigure(0, weight=1) # Configure column for tbl_recent to expand

        # frm_dashboard configuration & elements
        self.lbl_dashboard_title = ctk.CTkLabel(self.frm_dashboard, 
                                             text="Dashboard", 
                                             font=("", 20),
                                             anchor="center")
        self.lbl_dashboard_title.grid(row=0, column=0, sticky="new")

        self.frm_dashboard.rowconfigure(0, weight=1)
        self.frm_dashboard.columnconfigure(0, weight=1)


        # frm_notifs configuration & elements
        self.lbl_notifs_title = ctk.CTkLabel(self.frm_notifs, 
                                             text="Notifications", 
                                             font=("", 20),
                                             anchor="center")
        self.lbl_notifs_title.grid(row=0, column=0, sticky="new")

        self.frm_notifs.rowconfigure(0, weight=1)
        self.frm_notifs.columnconfigure(0, weight=1)

        # frm_upcoming configuration & elements
        self.lbl_upcoming_title = ctk.CTkLabel(self.frm_upcoming, 
                                             text="Upcoming Flights", 
                                             font=("", 20),
                                             anchor="center")
        self.lbl_upcoming_title.grid(row=0, column=0, sticky="new")

        self.frm_upcoming.rowconfigure(0, weight=1)
        self.frm_upcoming.columnconfigure(0, weight=1)

        # frm_map configuration & elements
        self.lbl_map_title = ctk.CTkLabel(self.frm_map, 
                                             text="Map", 
                                             font=("", 20),
                                             anchor="center")
        self.lbl_map_title.grid(row=0, column=0, sticky="new")

        self.frm_map.rowconfigure(0, weight=1)
        self.frm_map.columnconfigure(0, weight=1)
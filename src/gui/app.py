import customtkinter as ctk
from gui.home import HomePage
from gui.logbook import LogbookPage
from utils import screen_utils

class App(ctk.CTk):

    # APP SETTINGS
    APP_NAME = "PyLOT: Python Logbook for Organised Tracking"
    SCR_WIDTH, SCR_HEIGHT = screen_utils.get_screen_dimensions()
    PAGES = [
        LogbookPage,
        HomePage
    ]
    INIT_PAGE = 1

    def __init__(self):
        super().__init__()

        self.geometry(f"{self.SCR_WIDTH}x{self.SCR_HEIGHT}")
        self.title(self.APP_NAME)
        self.wm_attributes("-fullscreen", True)
        self.state("normal")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        i = 1
        for F in self.PAGES:
            frame = F(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            i += 1
        
        self.show_page(self.INIT_PAGE)

    # Show a certain page, from 1 to upwards
    def show_page(self, page_number : int):
        self.frames.get(page_number).tkraise()
    
    # Get a certain page, from 1 to upwards
    def get_page(self, page_number : int):
        return self.frames.get(page_number)
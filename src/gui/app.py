import customtkinter as ctk
from gui.home import HomePage
from gui.logbook import LogbookPage

class App(ctk.CTk):

    # APP SETTINGS
    APP_NAME = "PyLOT: Python Logbook for Organised Tracking"
    # SCR_WIDTH, SCR_HEIGHT = map(lambda x: x/1.5, screen_utils.get_screen_dimensions())
    TEST_WIDTH, TEST_HEIGHT = 600, 400
    PAGES = [
        HomePage,
        LogbookPage
    ]
    INIT_PAGE = 1

    def __init__(self):
        super().__init__()

        SCR_WIDTH = int(round(self.winfo_screenwidth() / 1.5, 0))
        SCR_HEIGHT = int(round(self.winfo_screenheight() / 1.5, 0))
        self.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")
        print(SCR_WIDTH, SCR_HEIGHT)
        self.after(50, lambda: self.state("zoomed"))

        self.title(self.APP_NAME)
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
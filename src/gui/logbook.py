# This is the page for the logbook elements of the app.
# Contained within here should be any functionality of viewing, creating, and editing logbook entries.


import customtkinter
from utils import screen_utils

class LogbookPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        scrwidth, scrheight = screen_utils.get_screen_dimensions()
        self.geometry(f"{scrwidth}x{scrheight}")
        self.title("CTk example")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        print("button click")

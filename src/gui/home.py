# This is the page for the logbook elements of the app.
# Contained within here should be any functionality of viewing, creating, and editing logbook entries.


import customtkinter as ctk
from utils.screen_utils import generate_frame_header

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)
        self.app = app

        generate_frame_header(self)

        print(self.btn_menu.cget("image"))
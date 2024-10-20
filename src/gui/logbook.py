# This is the page for the logbook elements of the app.
# Contained within here should be any functionality of viewing, creating, and editing logbook entries.


import customtkinter as ctk

class LogbookPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)
        self.app = app

        # Label for title
        # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
        self.labelTitle1 = ctk.CTkLabel(master=self, text="Example Page 1")
        self.labelTitle1.place(relx=0.5, rely=0.07, anchor=ctk.CENTER)

        # Label for description
        # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
        self.labelTitleDescription = ctk.CTkLabel(master=self, text="What's up?")
        self.labelTitleDescription.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)
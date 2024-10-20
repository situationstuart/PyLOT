import customtkinter as ctk
from PIL import Image
import os

def load_icon(image_name: str): # -> Image
    """Loads a given image from the assets/icons directory

    Args:
        image_name (str): filename of the image to load

    Returns:
        Image: returns the loaded image
    """
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                              "assets", "icons", image_name)
    try:
        image = Image.open(image_path)
        return image
    except IOError:
        print(f"Error: Unable to load image {image_name}")
        return None
    
def generate_frame_header(self: ctk.CTkFrame, titleString: str): # -> None
    """Generates a header for a frame with a title and buttons for menu, help, and settings

    Args:
        self (ctk.CTkFrame): Frame to generate the header for
        titleString (str): Title to display in the header
    """
    self.menu_image = ctk.CTkImage(light_image=load_icon("ico_menu_light.png"),
                                       dark_image=load_icon("ico_menu_dark.png"),
                                       size=(50, 50))
    self.help_image = ctk.CTkImage(light_image=load_icon("ico_help_light.png"),
                                    dark_image=load_icon("ico_help_dark.png"),
                                    size=(50, 50))
    self.settings_image = ctk.CTkImage(light_image=load_icon("ico_settings_light.png"),
                                    dark_image=load_icon("ico_settings_dark.png"),
                                    size=(50, 50))

    self.frm_header = ctk.CTkFrame(self)
    self.frm_header.grid(row=0, column=0, sticky="ew")
    self.grid_columnconfigure(0, weight=1)
    # self.frm_header.grid_rowconfigure(0, weight=0)
    self.frm_header.grid_columnconfigure(0, weight=0)  # Column for btn_menu
    self.frm_header.grid_columnconfigure(1, weight=1)  # Column for lbl_title
    self.frm_header.grid_columnconfigure(2, weight=0)  # Column for btn_help

    self.btn_menu = ctk.CTkButton(self.frm_header, text="", image=self.menu_image,
                                    fg_color="transparent", width=60)
    self.btn_menu.grid(row=0, column=0, sticky="w")

    self.lbl_title = ctk.CTkLabel(self.frm_header, text=titleString, font=("", 35),
                                    padx=10, anchor="center")
    self.lbl_title.grid(row=0, column=1, sticky="w")

    self.btn_settings = ctk.CTkButton(self.frm_header, text="", image=self.settings_image,
                                    fg_color="transparent", width=60)
    self.btn_settings.grid(row=0, column=2, sticky="e")

    self.btn_help = ctk.CTkButton(self.frm_header, text="", image=self.help_image,
                                    fg_color="transparent", width=60)
    self.btn_help.grid(row=0, column=3, sticky="e")
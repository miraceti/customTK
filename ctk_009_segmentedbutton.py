from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x300')

def clicker(value):
    my_label.configure(text=f'Hello {value}')
    # my_label.configure(text=f'Hello {my_seg_button.get()}')


my_values = ["John", "April", "Wes"]
my_seg_button = customtkinter.CTkSegmentedButton(root, values=my_values, command=clicker,
                                                 width=300,
                                                 height=100,
                                                 font=("helvetica",60),
                                                 corner_radius=5,
                                                 border_width=5,
                                                 fg_color="red",
                                                 selected_color="green",
                                                 selected_hover_color="purple",
                                                 unselected_color="pink",
                                                 unselected_hover_color="orange",
                                                 text_color="yellow",
                                                 dynamic_resizing=True,


                                                 )
my_seg_button.pack(pady=40)

#set default selection
# my_seg_button.set("John")

my_label = customtkinter.CTkLabel(root, text="", font=("helvetica",18))
my_label.pack(pady=10)

root.mainloop()
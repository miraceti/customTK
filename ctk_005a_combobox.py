from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x450')

def color_picker(choice):
    output_label.configure(text=choice, text_color=choice)

def color_picker2():
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())

def color_picker_yellow():
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())

my_label = customtkinter.CTkLabel(root, text="Pick a color", font=("helvetica",18))
my_label.pack(pady=40)

colors =["Red","Green","Blue","Purple","Pink"]
my_combo = customtkinter.CTkComboBox(root, values=colors,
                                     height=50,
                                     width=200,
                                     font=("helvetica",24),
                                     dropdown_font=("helvetica",24),
                                     corner_radius=50,
                                     border_width=2,
                                     border_color="red",
                                     button_color="red",
                                     button_hover_color="green",
                                     dropdown_hover_color="green",
                                     dropdown_fg_color="purple",
                                     dropdown_text_color="yellow",
                                     text_color="red",
                                     justify="right",

                                     )
my_combo.pack(pady=0)

my_button = customtkinter.CTkButton(master=root, text="pick a color", command=color_picker2)
my_button.pack(pady=20)

yellow_button = customtkinter.CTkButton(master=root, text="pick Yellow", command=color_picker_yellow)
yellow_button.pack(pady=20)

output_label = customtkinter.CTkLabel(root, text=" ", font=("helvetica",18))
output_label.pack(pady=20)

root.mainloop()
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



my_label = customtkinter.CTkLabel(root, text="Pick a color", font=("helvetica",18))
my_label.pack(pady=40)

colors =["Red","Green","Blue","Yellow"]
my_combo = customtkinter.CTkComboBox(root, values=colors, command=color_picker)
my_combo.pack(pady=0)

output_label = customtkinter.CTkLabel(root, text=" ", font=("helvetica",18))
output_label.pack(pady=20)

root.mainloop()
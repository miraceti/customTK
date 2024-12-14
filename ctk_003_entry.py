from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('600x350')

def submit():
    my_label.configure(text=f'Hello {my_entry.get()}')
    my_entry.configure(state="disabled")

def clear():
    my_entry.configure(state="normal")
    my_entry.delete(0, END)
    


my_label = customtkinter.CTkLabel(root, text="lol", font=("Helvetica",24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root, 
                                  placeholder_text="Enter your name",
                                  height=50,
                                  width=200,
                                  font=("Helvetica",18),
                                  corner_radius=100,
                                  text_color="red",
                                  placeholder_text_color="yellow",
                                  fg_color=("red","purple"),#outer, inner
                                #   state="disabled",
                                  )
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)

root.mainloop()
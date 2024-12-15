from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x300')

def sliding(value):
    my_label.configure(text=int(value))


# my_sliderv = customtkinter.CTkSlider(root, from_=0, to=100, command=sliding, orientation="vertical")
# my_sliderv.pack(pady=40)

# # define starting point
# my_sliderv.set(0)

my_sliderh = customtkinter.CTkSlider(root, from_=0, to=100, command=sliding, orientation="horizontal",
                                     number_of_steps=10,
                                     width=400,
                                     height=50,
                                     border_width=20,
                                     fg_color="red",
                                     progress_color="green",
                                     button_color="yellow",
                                     button_hover_color="orange",
                                     )
my_sliderh.pack(pady=40)

# define starting point
my_sliderh.set(0)

my_label = customtkinter.CTkLabel(root, text=my_sliderh.get(), font=("helvetica",20))
my_label.pack(pady=20)

root.mainloop()
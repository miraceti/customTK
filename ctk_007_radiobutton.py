from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x350')

def get_rad():
    if radio_var.get() == "other":
        my_label2.configure(text="choisis une case")
    elif radio_var.get() == "Yes":
        my_label2.configure(text="Bien sur tu aime les pizzas !")
    else:
        my_label2.configure(text="pourquoi tu n'aimes pas les pizzas!!")

my_label = customtkinter.CTkLabel(root, text="Do you like Pizza ?!!", font=("helvetica",18))
my_label.pack(pady=40)

radio_var = customtkinter.StringVar(value="other")
my_rad1 = customtkinter.CTkRadioButton(root, text="Yes I do", value="Yes", variable=radio_var,
                                    #    width=50,
                                    #    height=50,
                                    radiobutton_width=50,
                                    radiobutton_height=50,
                                    corner_radius=1,
                                    border_width_checked=10,
                                    border_width_unchecked=3,
                                    border_color="red",
                                    hover_color="yellow",
                                    fg_color="green",
                                    text_color="red",
                                    font=("helvetica",20),

                                       
                                       )#state="disabled",over=False, command=get_rad)
my_rad1.pack(pady=10)
my_rad2 = customtkinter.CTkRadioButton(root, text="No at all", value="No" , variable=radio_var,
                                    #    width=50,
                                    #    height=50,
                                    radiobutton_width=50,
                                       
                                       )#, command=get_rad)
my_rad2.pack(pady=10)

my_button = customtkinter.CTkButton(master=root, text="select", command=get_rad)
my_button.pack(pady=10, padx=80)

my_label2 = customtkinter.CTkLabel(root, text="", font=("helvetica",18))
my_label2.pack(pady=40)

root.mainloop()
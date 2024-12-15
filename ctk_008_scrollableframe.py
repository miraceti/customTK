from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x300')

my_framev = customtkinter.CTkScrollableFrame(root,
                                             orientation="vertical",
                                             width=300,
                                             height=200,
                                             label_text="Hellow world!",
                                             label_fg_color="blue",
                                             label_text_color="yellow",
                                             label_font=("helvetica", 20, "bold"),
                                             #label_anchor="w",#w,n,e,s,ne,se,sw,nw,center
                                             border_width=5,
                                             border_color="green",
                                             fg_color="red",
                                             scrollbar_fg_color="yellow",
                                             scrollbar_button_color="pink",
                                             scrollbar_button_hover_color="blue",
                                             corner_radius=20,
                                             )
my_framev.pack(pady=40)

for x in range(20):
    customtkinter.CTkButton(my_framev, text="this is button "+ str(x)).pack(pady=10)


root.mainloop()
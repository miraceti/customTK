from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x450')

def game():
    if check_var.get() == "on":
        my_label.configure(text="you clicked !!")
    else:
        my_label.configure(text="you didn't clicked !!")

    text_var.set("okioki !!")
    print(text_var.get())

def clear_me():
    my_check.deselect()
    # my_check.toggle()
    # my_check.select()
    text_var.set("Tu veux jouer ?")

# checkbox state
check_var = customtkinter.StringVar(value="off")
# checkbox text
text_var = customtkinter.StringVar(value="Tu veux jouer ?")
my_check = customtkinter.CTkCheckBox(root, 
                                     text="Tu veux jouer ?",
                                     variable=check_var,
                                     onvalue="on",
                                     offvalue="off",
                                    #  command=game,
                                    checkbox_width=50,
                                    checkbox_height=50,
                                    font=("Helvetica",24),
                                    corner_radius=50,
                                    fg_color="red",
                                    hover_color="yellow",
                                    text_color="green",
                                    # hover=False,#not active if false
                                    textvariable=text_var,

                                     )
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(master=root, text="Submit", command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(master=root, text="Clear", command=clear_me)
clear_button.pack(pady=10)

toggle_button = customtkinter.CTkButton(master=root, text="Toggle", command=my_check.toggle)
toggle_button.pack(pady=10)

select_button = customtkinter.CTkButton(master=root, text="Select", command=my_check.select)
select_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)


root.mainloop()
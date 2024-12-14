import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('600x350')

def hello1():
    my_label.configure(text="Tout")

def hello2():
    my_label.configure(text=button_2.cget("text"))

button_1 = customtkinter.CTkButton(master=root, text="Hello world!1", command=hello1)
button_1.pack(pady=10, padx=40)

button_2 = customtkinter.CTkButton(master=root, text="Hello world!2", command=hello2)
button_2.pack(pady=10, padx=80)

button_3 = customtkinter.CTkButton(master=root, 
                                   text="Hello world!3", 
                                   command=hello2,
                                   height=100,
                                   width=200,
                                   font=("Helvetica",24),
                                   text_color="black",
                                   fg_color="red",
                                   hover_color="green",
                                   corner_radius=50,
                                   bg_color="white",
                                   border_width=10,
                                   border_color="yellow",
                                #    state="disabled",#"normal"
                                   )
button_3.pack(pady=10, padx=80)

my_label = customtkinter.CTkLabel(root, text="lol")
my_label.pack(pady=10)

root.mainloop()
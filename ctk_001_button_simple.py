import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('600x350')

button_1 = customtkinter.CTkButton(master=root, text="Hello world!")
button_1.pack(pady=50, padx=50)

root.mainloop()
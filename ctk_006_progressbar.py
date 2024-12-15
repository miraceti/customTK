from tkinter import *
import customtkinter

#theme et couleur
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title('CustomTK')
root.geometry('700x350')

def clicker():
    my_progressbar.step()
    my_label.configure(text=int((my_progressbar.get()*100)))

def start():
    my_progressbar.start()

def stop():
    my_progressbar.stop()

my_progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal",
                                              width=300,
                                              height=30,
                                              corner_radius=10,
                                              border_width=5,
                                              border_color="red",
                                              fg_color="yellow",
                                              progress_color="purple",
                                              mode="determinate",
                                              determinate_speed=1,
                                              indeterminate_speed=1,
                                              
                                              
                                              )
my_progressbar.pack(pady=40)

my_progressbar.set(0)

my_button = customtkinter.CTkButton(master=root, text="click me!", command=clicker)
my_button.pack(pady=10)

start_button = customtkinter.CTkButton(master=root, text="start", command=start)
start_button.pack(pady=10)

stop_button = customtkinter.CTkButton(master=root, text="stop", command=stop)
stop_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="", font=("helvetica",18))
my_label.pack(pady=10)


root.mainloop()
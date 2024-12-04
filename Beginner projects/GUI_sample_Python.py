"""GUI SAMPLES TKinter"""

import customtkinter


#defining basic parameteres
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("pink")

root = customtkinter.CTk()
root.geometry("800x450")


def login():
    print("Test")

frame_windows = customtkinter.CTkFrame(master=root)
frame_windows.pack(pady=20,padx=65, fill=both,expand=True)

label = customtkinter.CTkLabel(master=frame_windows, text="Login System", text_font=("Italic", 22))
label.pack(pady=14,padx=12)

entry1 = customtkinter,CTkEntry(master=frame_windows,placeholder_text = "Username")
entry1.pack(pady=14,padx=12)

entry2 = customtkinter,CTkEntry(master=frame_windows,placeholder_text = "Password", show = "#")
entry2.pack(pady=14,padx=12)


button = customtkinter.CTkButton(master=frame_windows,text ="Login", command = login)
button.pack(pady=14,padx=12)

checkbox = customtkinter.CTkCheckBox(master=frame_windows, text = "Remember me")
checkbox.pack(pady=14,padx=12)

root.mainloop()

#modern UI that we got rn



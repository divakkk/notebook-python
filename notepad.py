import customtkinter
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("700x600")
app.title('Notepad by Zakhar')

file_path = ''

def dark():
    customtkinter.set_appearance_mode("dark")

def light():
    customtkinter.set_appearance_mode("light")

def open_txt():
    global file_path
    file_path = customtkinter.filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            textbox.delete(1.0, "end")
            textbox.insert(1.0, file_contents)
    else:
        print("No file path specified.")

def save_as():
    global file_path
    file_path = os.path.join(os.path.expanduser("~/Desktop"), "new_file.txt")
    with open(file_path, 'w') as file:
        file_contents = textbox.get(1.0, "end-1c")
        file.write(file_contents)

def edit_txt():
    global file_path
    if file_path:
        with open(file_path, 'w') as file:
            file_contents = textbox.get(1.0, "end-1c")
            file.write(file_contents)
    else:
        print("No file path specified.")

def light_dark(choice):
    if choice == "Light":
        light()
    elif choice == "Dark":
        dark()

def create_file_window():
    global file_path
    create_file_window = customtkinter.CTkToplevel(app)
    create_file_window.title("Create File")
    create_file_window.geometry("300x150")

    file_name_label = customtkinter.CTkLabel(master=create_file_window, text="Enter file name:")
    file_name_label.pack(pady=10)

    file_name_entry = customtkinter.CTkEntry(master=create_file_window, width=200, height=25, placeholder_text="Enter file name(.txt)", corner_radius=10)
    file_name_entry.pack(pady=10)

    def create_file():
        global file_path
        file_name = file_name_entry.get()
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop_path, file_name)
        with open(file_path, 'tw', encoding='utf-8') as f:
            pass
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
        textbox.delete(1.0, "end")
        textbox.insert(1.0, file_contents)
        create_file_window.destroy()

    submit_button = customtkinter.CTkButton(master=create_file_window, text="Submit", command=create_file)
    submit_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


create_file_window_button = customtkinter.CTkButton(master=app, text="Create file", command=create_file_window)
create_file_window_button.place(relx=0.2, rely=0.25, anchor=customtkinter.E)

button_path = customtkinter.CTkButton(master=app, text="Enter path", command=open_txt)
button_path.place(relx=0.2, rely=0.1, anchor=customtkinter.E)

button_open = customtkinter.CTkButton(master=app, text="OpenTXT", command=open_txt)
button_open.place(relx=0.2, rely=0.15, anchor=customtkinter.E)

button_path = customtkinter.CTkButton(master=app, text="Save as", command=save_as)
button_path.place(relx=0.2, rely=0.3, anchor=customtkinter.E)

button_edit = customtkinter.CTkButton(master=app, text="Save Changes", command=edit_txt)
button_edit.place(relx=0.2, rely=0.2, anchor=customtkinter.E)

textbox = customtkinter.CTkTextbox(master=app, width=550, height=600)
textbox.place(relx=0.60, rely=0.5, anchor=customtkinter.CENTER)

light_dark_var = customtkinter.Variable(value="Theme")
light_dark = customtkinter.CTkOptionMenu(master=app, values=["Light", "Dark"], command=light_dark, variable=light_dark_var)
light_dark.place(relx=0.2, rely=0.97, anchor=customtkinter.E)

app.mainloop()
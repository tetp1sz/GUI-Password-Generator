import tkinter
import customtkinter
from class_file import Password

def generate():
    count = entry.get()
    passw = Password(int(count))
    entry_result.configure(text=f'{passw.logic()}')

if __name__ == '__main__':
    root_tk = customtkinter.CTk()
    root_tk.geometry("400x240")
    root_tk.title("Password Generate")
    customtkinter.set_appearance_mode("Dark")
    root_tk.resizable(False, False)
    root_tk.config(bg='black')

    label = customtkinter.CTkLabel(master=root_tk, text="Length of password", width=150, height=30, corner_radius=8, font=('Consolas bold', 16), bg_color='black', text_color='#f0eff4')
    entry = customtkinter.CTkEntry(master=root_tk, width=150, height=25, corner_radius=8, font=('Consolas', 16), bg_color='black', fg_color='#3a3b3e', text_color='#f0eff4', border_color='#3a3b3e')
    btn = customtkinter.CTkButton(master=root_tk, text="Generate", command=generate, width=120, height=32, border_width=0, corner_radius=8, font=('Consolas', 16), bg_color='black', fg_color='#291528', hover_color='#9e829c')
    label_second = customtkinter.CTkLabel(master=root_tk, text="Your password", width=150, height=30, corner_radius=8, font=('Consolas bold', 16), bg_color='black', text_color='#f0eff4')
    entry_result = customtkinter.CTkLabel(master=root_tk, text='', width=150, height=30, corner_radius=8, font=('Consolas', 16), bg_color='black', text_color='#f0eff4')

    text = entry.get()

    entry_result.place(relx=0.475, rely=0.425, anchor=tkinter.W)
    label_second.place(relx=0.4, rely=0.425, anchor=tkinter.E)
    btn.place(relx=0.5, rely=0.7, anchor=tkinter.N)
    entry.place(relx=0.525, rely=0.25, anchor=tkinter.W)
    label.place(relx=0.425, rely=0.25, anchor=tkinter.E)
    root_tk.mainloop()
import pyautogui as pg
import tkinter as tk
from tkinter import messagebox
import time

window = tk.Tk()
window.title("Whatsapp Message Sender")
window.geometry('550x300')
window.configure(bg='green')

welcome = tk.Label(window, text="Welcome To Whatsapp Message Sender..!", font=("Arial Bold", 15))
welcome.place(relx=0.5, rely=0.5, anchor='center')
welcome2 = tk.Label(window, text="This sends multiple messages to any person.", font=("Arial Bold", 11))
welcome2.place(relx=0.5, rely=0.6, anchor='center')

def remove_welcome_message():
    welcome.place_forget()
    welcome2.place_forget()
    show_main_content()

window.after(5000, remove_welcome_message)

def show_main_content():
    label1 = tk.Label(window, text="Enter the message you want to send:", font=("Arial Bold", 12))
    label1.grid(row=1, column=0, padx=7, pady=7)

    entry1 = tk.Entry(window, width=30)
    entry1.grid(row=1, column=1, padx=10, pady=10)

    label2 = tk.Label(window, text="Enter the number of times to send:", font=("Arial Bold", 12))
    label2.grid(row=2, column=0, padx=7, pady=7)

    spinbox1 = tk.Spinbox(window, from_=1, to=25, width=5)
    spinbox1.grid(row=2, column=1, padx=7, pady=7)

    label = tk.Label(window, font=("Arial Bold", 17))
    label.grid(row=3, column=0, columnspan=2, padx=7, pady=7)

    def send_messages():
        mess = entry1.get()
        times = spinbox1.get()
        if mess == "":
            messagebox.showinfo("ERROR!", "Enter a Message")
        else:
            for x in range(11):
                label.configure(text="Place the Cursor on Whatsapp Message Box\nStarting in "+str(10-x)+" seconds.....!\n ")
                time.sleep(1)
                window.update()
            label.configure(text="Started...")
            window.update()
            for _ in range(int(times)):
                pg.write(mess)
                pg.press("Enter")
            label.configure(text="Completed!")
            window.update()
    def clicked():
        send_messages()
        
    button = tk.Button(window, text="START", command=clicked, width=15, height=1, font=("Serif Bold", 12), bg="grey", fg="white")
    button.grid(row=4, column=0, columnspan=2, padx=7, pady=7)

window.mainloop()

sender_email = "user@mail.com"  # email address used to generate password
target_users = ["user1@mail.com", "user2@mail.com"] # a list of recipients 
password = "" # the 16 code generated
mail_subject = "The Subject of the Mail"

def get_csv():
    import tkinter as tk
    from tkinter import filedialog
    import os

    current_dir = os.getcwd()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir=current_dir, title ="Select your CSV file" , filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    return file_path


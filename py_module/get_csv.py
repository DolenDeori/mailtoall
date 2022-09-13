def get_csv():
    import tkinter as tk
    from tkinter import filedialog
    import os

    current_dir = os.getcwd()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir=current_dir, title ="Select your CSV file" , filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    return file_path
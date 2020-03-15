import tkinter as tk
import sqlite3
import os
dbName = "user.db"

def submit_data():
    if not all((ent_nama.get(), ent_email.get())):
        lbl_info['text'] = "Form can't be empty"
        return
    if os.path.isfile(dbName) == True:
        try:
            sqliteConnection = sqlite3.connect(dbName)
            cursor = sqliteConnection.cursor()
            lbl_info['text'] = ("Successfully reConnected to SQLite")
            sqlite_insert_query = """INSERT INTO user
                                (name, email) 
                                VALUES 
                                ('{}','{}')""".format(ent_nama.get(), ent_email.get())

            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            lbl_info['text'] = "Data Sent!"
            cursor.close()
        except sqlite3.Error as error:
            lbl_info['text'] = ("Failed to insert data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
                ent_nama.delete(0, len(ent_nama.get()))
                ent_email.delete(0, len(ent_email.get()))
                return
    else:
        print("Database Belum dibuat!")
        return

# Mempersiapkan Window
window = tk.Tk()
window.title("Register")
window.geometry("500x500")
window.resizable(width=False, height=False)

# Membuat Label dan Entry Untuk Nama dan Email
frm_entry = tk.Frame(master=window)
lbl_nama = tk.Label(master=frm_entry, text="Nama: ")
ent_nama = tk.Entry(master=frm_entry, width=10)
lbl_email = tk.Label(master=frm_entry, text="Email: ")
ent_email = tk.Entry(master=frm_entry, width=10)


# Menyusun label dan entry dengan Grid Tkinter
ent_nama.grid(row=0, column=1)
lbl_nama.grid(row=0, column=0)
ent_email.grid(row=1, column=1)
lbl_email.grid(row=1, column=0)


# Membuat tombol submit
btn_submit = tk.Button(
    master=window,
    text="Submit",
    command=submit_data
)

lbl_info = tk.Label(master=window, text="")

# Menyusun Grid Window
frm_entry.grid(row=0, column=0, padx=10)
btn_submit.grid(row=1, column=0, pady=10)
lbl_info.grid(row=2, column=0)
# Run the application
window.mainloop()
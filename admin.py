import tkinter as tk
import sqlite3
import os.path
dbName = "user.db"

#Membuat file DB
def initDB():
    if os.path.isfile(dbName) == False:
        try:
            sqliteConnection = sqlite3.connect(dbName)
            sqlite_create_table_query = '''CREATE TABLE user (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE);'''

            cursor = sqliteConnection.cursor()
            lbl_sqlout['text'] = ("Successfully Connected to SQLite")
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            lbl_sqlout['text'] = ("SQLite table created")
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
    else:
        print("Database sudah ada!")

# Mempersiapkan Window
window = tk.Tk()
window.title("Admin")
window.geometry("500x500")
window.resizable(width=False, height=False)

# Membuat Label dan Entry Untuk Nama dan Email
lbl_sqlout = tk.Label(master=window, text="aaaaa")




# Membuat tombol submit
btn_submit = tk.Button(
    master=window,
    text="Initialize Database",
    command=initDB
)

# Menyusun Grid Window

btn_submit.grid(row=0, column=0, pady=10)
lbl_sqlout.grid(row=1, column=0)
# Run the application
window.mainloop()

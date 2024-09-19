import tkinter as tk
import ttkbootstrap as ttk 
import mysql.connector
import os
from tkinter import messagebox

try:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'mazen01120908137b',
        database = 'student_management_system'
    )

    cursor = db.cursor()

except mysql.connector.errors.ProgrammingError:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Error in Database', 'Failed in Database Connection')
    quit()
 

# Window

class App(ttk.Window):

    def __init__(self):

        # Window Settings
        super().__init__(themename = 'cosmo')
        self.geometry('600x400')
        self.title('Student Managment System')
        dir = os.path.realpath(os.path.join("\\".join(__file__.split("\\")[:-1]),'icon.ico'))
        self.iconbitmap(dir)
        MainWindow(self)

        # Run
        self.mainloop()


class MainWindow():
    def __init__(self, parent):

        self.parent = parent
        self.grade_var = tk.StringVar()
        self.ls = [
            '1st Prim',
            '2nd Prim',
            '3rd Prim',
            '4th Prim',
            '5th Prim',
            '6th Prim',
            '1st Prip',
            '2nd Prip',
            '3rd Prip',
            '1st Sec',
            '2nd Sec',
            '3rd Sec',
        ]

        self.create_widgets()
        self.create_layout()


    def create_widgets(self):

        # Welcome Lable
        self.lable_frame = ttk.Frame(self.parent)
        self.lable = ttk.Label(self.lable_frame, text = 'Welcome to Student Managment System', font = ('Calibri', '20', 'bold'), foreground = '#000')

        # Grade Section
        self.main_frame = ttk.Frame(self.parent)
        self.grade_entry_frame = ttk.Frame(self.main_frame)
        self.grade_label = ttk.Label(self.grade_entry_frame, text = 'Grade ', font = ('Calibri', 14))
        self.grade_entry = ttk.Combobox(self.grade_entry_frame, values = self.ls, textvariable = self.grade_var, bootstyle = 'success')

        # Date Section
        self.date_entry_frame = ttk.Frame(self.main_frame)
        self.date_entry = ttk.DateEntry(self.date_entry_frame, bootstyle = 'success')

        # Buttons Section
        self.buttons_frame = ttk.Frame(self.parent)
        self.add_button = ttk.Button(self.buttons_frame, text = 'Add', command = self.add_button_func, bootstyle = 'success outline')
        self.search_button = ttk.Button(self.buttons_frame, text = 'Search', command = self.search_button_func, bootstyle = 'success outline')
        self.exit_button = ttk.Button(self.buttons_frame, text = 'Exit', command = self.parent.quit, bootstyle = 'success outline')


    def create_layout(self):

        # Grid Settings
        self.parent.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.parent.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')

        # Layout
        self.lable_frame.grid(row = 0, column = 0, columnspan = 3, sticky = 'nsew')
        self.main_frame.grid(row = 1, column = 0, columnspan = 3, rowspan = 2, sticky = 'nsew')
        self.buttons_frame.grid(row = 3, column = 0, columnspan = 3, sticky = 'nsew')

        self.lable.pack(fill = 'both', expand = 1, side = 'top', padx = 20)

        self.grade_entry_frame.pack(expand = 1, side = 'left')
        self.grade_label.pack(expand = 1, side = 'left')
        self.grade_entry.pack(expand = 1, side = 'right')

        self.date_entry_frame.pack(expand = 1, side = 'left')
        self.date_entry.pack(expand = 1, side = 'right', padx = 0)

        self.add_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)
        self.search_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)
        self.exit_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)

        self.grade_entry.focus()


    def add_button_func(self):
        if self.grade_var.get():

            # Initiate The Window
            window = AddWindow(f"a{self.date_entry.entry.get().replace('/', '_')}x{self.grade_var.get().replace(' ', '_')}")
            window.focus()

            # Execute Query
            query = f"CREATE TABLE IF NOT EXISTS {window.get_db_name()} ( name NVARCHAR(100), homeword BOOLEAN, mark INT, phone VARCHAR(20) )"
            cursor.execute(query)
            db.commit()

        else:
            messagebox.showerror('Enter the Grade', 'No Grade Inserted')
        

    def search_button_func(self):

        if self.grade_var.get():

            db_name = f"a{self.date_entry.entry.get().replace('/', '_')}x{self.grade_var.get().replace(' ', '_')}"
            try:
                query = f"SELECT * FROM {db_name}"
                cursor.execute(query)
                window = SearchWindow()
                window.focus()
                for row in cursor.fetchall():
                    window.table.insert(parent = '', index = tk.END, values = row)
            except mysql.connector.errors.ProgrammingError :
                messagebox.showerror("Not Found", "There is No Such Session")
        else:
            messagebox.showerror('Enter The Grade', 'No Grade Inserted')


class AddWindow(ttk.Toplevel):

    def __init__(self, db_name = ''):
        super().__init__()
        self.__db_name = db_name
        self.homework_var = tk.StringVar(value = 'Yes')

        self.name_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.name_frame, text = 'Name :')
        self.name_entry = ttk.Entry(self.name_frame, width = 30)

        self.mark_frame = ttk.Frame(self)
        self.mark_entry = ttk.Entry(self.mark_frame, width = 30)
        self.mark_label = ttk.Label(self.mark_frame, text = 'Mark :')

        self.homework_frame = ttk.Frame(self)
        self.homework_entry = ttk.Combobox(self.homework_frame, values = ['Yes', 'No'], width = 27, textvariable = self.homework_var)
        self.homework_label = ttk.Label(self.homework_frame, text = 'Homework :')

        self.phone_frame = ttk.Frame(self)
        self.phone_entry = ttk.Entry(self.phone_frame, width = 29)
        self.phone_label = ttk.Label(self.phone_frame, text = 'Phone :')

        self.buttons_frame = ttk.Frame(self)
        self.save_button = ttk.Button(self.buttons_frame, text = 'Save', command = self.save_button_func)
        self.cancel_button = ttk.Button(self.buttons_frame, text = 'Cancel', command = self.destroy)

        self.create_layout(self)

    def create_layout(self, parent : ttk.Toplevel):
        
        # Grid
        parent.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')
        parent.columnconfigure((0, 1), weight = 1, uniform = 'a')

        # Layout
        self.name_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'right')
        
        self.mark_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.mark_label.pack(side = 'left')
        self.mark_entry.pack(side = 'right')
        
        self.phone_frame.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.phone_label.pack(side = 'left')
        self.phone_entry.pack(side = 'right')
        
        self.homework_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.homework_label.pack(side = 'left')
        self.homework_entry.pack(side = 'right')

        self.buttons_frame.grid(row = 2, column = 0, columnspan = 2, pady = 10, sticky = 'nsew')
        self.save_button.pack(side = 'left', expand = 1, ipadx = 40)
        self.cancel_button.pack(side = 'left', expand = 1, ipadx = 40)

    def save_button_func(self):
        
        if self.get_db_name():
            try:
                query = f"INSERT INTO {self.get_db_name()} VALUES ('{self.name_entry.get()}', {'true' if self.homework_var.get().lower() == 'yes' else 'false'}, {self.mark_entry.get()}, '{self.phone_entry.get()}')"
                cursor.execute(query)
                db.commit()
                messagebox.showinfo('Success', 'Date Inserted Successfully')
                self.focus()
            except mysql.connector.errors.ProgrammingError :
                messagebox.showerror('Invalid Info', 'Invalid Input')
                self.focus()
        else:
            messagebox.showerror('Wrong in Add Button', 'Falied to Format Database Name')
        
    def set_db_name(self, value):
        self.__db_name = value

    def get_db_name(self):
        return self.__db_name


class SearchWindow(ttk.Toplevel):
    def __init__(self):
        super().__init__()

        # Table
        self.table = ttk.Treeview(self, columns = ('name', 'homework', 'mark', 'phone'), show = 'headings', style = 'success')
        self.table.pack(expand = 1, fill = 'both', side = 'left')

        self.table.heading(column = 'name', text = 'Name')
        self.table.heading(column = 'homework', text = 'Homework')
        self.table.heading(column = 'mark', text = 'Mark')
        self.table.heading(column = 'phone', text = 'Phone')

        # Scroll Bar
        scroll_bar = ttk.Scrollbar(self, orient = 'vertical', command = self.table.yview_scroll)
        self.table.config(yscrollcommand = scroll_bar.set)
        scroll_bar.pack(side = 'left', fill = 'y')
    
if __name__ == '__main__':
    App()
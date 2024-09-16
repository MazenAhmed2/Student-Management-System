import tkinter as tk
import ttkbootstrap as ttk 
import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mazen01120908137b',
    database = 'student_management_system'
)
cursor = db.cursor()

# Window

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Student Managment System')
        MainWindow(self, AddWindow)

        # Run
        self.mainloop()

class MainWindow():
    def __init__(self, parent, add_window):

        self.add_window = add_window
        self.parent = parent

        ls = [
            '1st Prim',
            '2st Prim',
            '3st Prim',
            '4st Prim',
            '5st Prim',
            '6st Prim',
            '1st Prip',
            '2st Prip',
            '3st Prip',
            '1st Sec',
            '2st Sec',
            '3st Sec',
        ]
        self.grade_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Main page

        self.lable_frame = ttk.Frame(parent)
        self.lable = ttk.Label(self.lable_frame, text = 'Welcome to Student Managment System', font = ('Calibri', '20', 'bold'), foreground = '#000')

        self.main_frame = ttk.Frame(parent)
        self.grade_entry_frame = ttk.Frame(self.main_frame)
        self.grade_label = ttk.Label(self.grade_entry_frame, text = 'Grade :', font = ('Calibri', 14))
        self.grade_entry = ttk.Combobox(self.grade_entry_frame, values = ls, textvariable = self.grade_var)

        self.date_entry_frame = ttk.Frame(self.main_frame)
        # self.date_label = ttk.Label(self.date_entry_frame, text = 'Date :', font = ('Calibri', 14))
        self.date_entry = ttk.DateEntry(self.date_entry_frame)

        self.buttons_frame = ttk.Frame(parent)
        self.add_button = ttk.Button(self.buttons_frame, text = 'Add', command = self.add_button_func)
        self.search_button = ttk.Button(self.buttons_frame, text = 'Search', command = self.search_button_func)
        self.exit_button = ttk.Button(self.buttons_frame, text = 'Exit', command = parent.quit)

        self.create_layout()


    def create_layout(self):

        # Layout
        self.parent.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.parent.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')

        self.lable_frame.grid(row = 0, column = 0, columnspan = 3, sticky = 'nsew')
        self.main_frame.grid(row = 1, column = 0, columnspan = 3, rowspan = 2, sticky = 'nsew')
        self.buttons_frame.grid(row = 3, column = 0, columnspan = 3, sticky = 'nsew')

        self.lable.pack(fill = 'both', expand = 1, side = 'top', padx = 20)

        self.grade_entry_frame.pack(expand = 1, side = 'left')
        self.grade_label.pack(expand = 1, side = 'left')
        self.grade_entry.pack(expand = 1, side = 'right')

        self.date_entry_frame.pack(expand = 1, side = 'left')
        # self.date_label.pack(expand = 1, side = 'left')
        self.date_entry.pack(expand = 1, side = 'right', padx = 0)


        self.add_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)
        self.search_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)
        self.exit_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)


    def add_button_func(self):
        window = AddWindow()
        window.focus()
        if self.grade_var.get():

            window.db_name = f"a{self.date_entry.entry.get().replace('/', '_')}x{self.grade_var.get().replace(' ', '_')}"
            query = f"CREATE TABLE IF NOT EXISTS {window.db_name} ( name NVARCHAR(100), homeword BOOLEAN, mark INT, phone VARCHAR(20) )"
            cursor.execute(query)
            db.commit()
            print('Done')

        else:
            pass
        

    def search_button_func(self):
        window = SearchWindow()
        window.focus()
        if self.grade_var.get():
            window.db_name = f"a{self.date_entry.entry.get().replace('/', '_')}x{self.grade_var.get().replace(' ', '_')}"
            query = f"SELECT * FROM {window.db_name}"
            cursor.execute(query)
            for row in cursor.fetchall():
                window.table.insert(parent = '', index = tk.END, values = row)
        else:
            pass

class AddWindow(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.db_name = ''

        self.name_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.name_frame, text = 'Name :')
        self.name_entry = ttk.Entry(self.name_frame, width = 30)

        self.mark_frame = ttk.Frame(self)
        self.mark_entry = ttk.Spinbox(self.mark_frame, width = 27)
        self.mark_label = ttk.Label(self.mark_frame, text = 'Mark :')

        self.homework_frame = ttk.Frame(self)
        self.homework_entry = ttk.Combobox(self.homework_frame, values = ['Yes', 'No'], width = 27)
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
        if self.db_name:
            query = f"INSERT INTO {self.db_name} VALUES ('{self.name_entry.get()}', {'true' if self.homework_entry.get() == 'Yes' else 'false'}, {self.mark_entry.get()}, '{self.phone_entry.get()}')"
            print(query)
            cursor.execute(query)
            db.commit()
            print('Data Inserted')
        

class SearchWindow(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        # self.geometry('600x400')

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
    
App()
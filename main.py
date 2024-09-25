import tkinter as tk
import ttkbootstrap as ttk 
import mysql.connector
import os
from tkinter import messagebox
from mysql.connector.errors import Error
from tkinter import filedialog

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
 

ls = [
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



# Window

class App(ttk.Window):

    def __init__(self):

        # Window Settings
        super().__init__(themename = 'cosmo')
        self.geometry('600x400')
        self.title('Student Managment System')
        self.focus()
        MainWindow(self)

        # Run
        self.mainloop()

    def create_session_table(grade, date):

        query = f"CREATE TABLE IF NOT EXISTS a{date.replace('-', '_')}x{grade.replace(' ', '_')} ( name NVARCHAR(100), attend NVARCHAR(4), homeword NVARCHAR(5), interaction NVARCHAR(15), mark VARCHAR(10), phone VARCHAR(15), notes NVARCHAR(500) )"
        cursor.execute(query)
        db.commit()

    def create_session_table(table_name):

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ( name NVARCHAR(100), attend NVARCHAR(4), homeword NVARCHAR(5), interaction NVARCHAR(15), mark VARCHAR(10), phone VARCHAR(15), notes NVARCHAR(500) )"
        cursor.execute(query)
        db.commit()

# def insert_into_session_table(values):

#     query = f"CREATE TABLE IF NOT EXISTS {table_name} ( name NVARCHAR(100), attend NVARCHAR(4), homeword NVARCHAR(5), interaction NVARCHAR(15), mark VARCHAR(10), phone VARCHAR(15), notes NVARCHAR(500) )"
#     cursor.execute(query)
#     db.commit()

    def create_grade_table(table_name):

        query = f"CREATE TABLE IF NOT EXISTS {table_name} (name NVARCHAR(50), phone VARCHAR(20))"
        cursor.execute(query)
        db.commit()


class MainWindow():

    def __init__(self, parent):

        self.parent = parent
        

        self.create_widgets()
        self.create_layout()


    def create_widgets(self):

        # Welcome Lable
        self.lable_frame = ttk.Frame(self.parent)
        self.lable = ttk.Label(self.lable_frame, text = 'Welcome to Student Managment System', font = ('Calibri', '20', 'bold'), foreground = '#000')

        # # Grade Section
        self.main_frame = ttk.Frame(self.parent)
        # self.grade_entry_frame = ttk.Frame(self.main_frame)
        # self.grade_label = ttk.Label(self.grade_entry_frame, text = 'Grade ', font = ('Calibri', 14))
        # self.grade_entry = ttk.Combobox(self.grade_entry_frame, values = self.ls, textvariable = self.grade_var, bootstyle = 'success')

        # # Date Section
        # self.date_entry_frame = ttk.Frame(self.main_frame)
        # self.date_entry = ttk.DateEntry(self.date_entry_frame, bootstyle = 'success')

        # Buttons Section
        self.buttons_frame = ttk.Frame(self.parent)
        self.add_button = ttk.Button(self.buttons_frame, text = 'Add', command = AddWindow, bootstyle = 'success outline')
        self.search_session_button = ttk.Button(self.buttons_frame, text = 'Search Session', command = SearchSessionWindow, bootstyle = 'success outline')
        self.search_student_button = ttk.Button(self.buttons_frame, text = 'Search Student', command = SearchStudentWindow, bootstyle = 'success outline')
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

        # self.grade_entry_frame.pack(expand = 1, side = 'left')
        # self.grade_label.pack(expand = 1, side = 'left')
        # self.grade_entry.pack(expand = 1, side = 'right')

        # self.date_entry_frame.pack(expand = 1, side = 'left')
        # self.date_entry.pack(expand = 1, side = 'right', padx = 0)

        self.add_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)
        self.search_session_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 15)
        self.search_student_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 15)
        self.exit_button.pack(side = 'left', expand = 1, anchor = 's', pady = 15, ipadx = 40)

        # self.grade_entry.focus()



class AddWindow(ttk.Toplevel):

    def __init__(self):
        super().__init__()
        self.__table_name = None
        self.geometry('600x500')

        # Variables
        self.grade = tk.StringVar()
        self.date = tk.StringVar()
        self.name = tk.StringVar()
        self.attend = tk.StringVar()
        self.interaction = tk.StringVar()
        self.homework = tk.StringVar()
        self.mark = tk.StringVar()
        self.phone = tk.StringVar()
        
        self.create_widgets()
        self.grade_entry.focus()
        self.grade_entry.bind('<<ComboboxSelected>>', self.fetch_data_to_name_entry)
        self.create_layout()

    def create_widgets(self):

        # Grade Section
        self.grade_frame = ttk.Frame(self)
        self.grade_label = ttk.Label(self.grade_frame, text = 'Grade ')
        self.grade_entry = ttk.Combobox(self.grade_frame, values = ls, bootstyle = 'success', width = 28, textvariable = self.grade)

        # Date Section
        self.date_frame = ttk.Frame(self)
        self.date_label = ttk.Label(self.date_frame, text = 'Date :')
        self.date_box = ttk.DateEntry(self.date_frame, bootstyle = 'success', width = 24)
        self.date_box.entry.config(textvariable = self.date)

        self.name_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.name_frame, text = 'Name :')
        self.name_entry = ttk.Combobox(self.name_frame, width = 28, textvariable = self.name)

        self.attend_frame = ttk.Frame(self)
        self.attend_entry = ttk.Combobox(self.attend_frame, width = 27, values = ['حاضر', 'غائب'], textvariable = self.attend)
        self.attend_label = ttk.Label(self.attend_frame, text = 'Attend :')

        self.homework_frame = ttk.Frame(self)
        self.homework_entry = ttk.Combobox(self.homework_frame, values = ['نعم', 'لا', 'ناقص'], width = 28, textvariable = self.homework)
        self.homework_label = ttk.Label(self.homework_frame, text = 'Homework :')

        self.interaction_frame = ttk.Frame(self)
        self.interaction_entry = ttk.Combobox(self.interaction_frame, width = 27, values = ['متفاعل', 'غير متفاعل'], textvariable = self.interaction)
        self.interaction_label = ttk.Label(self.interaction_frame, text = 'Interaction :')

        self.mark_frame = ttk.Frame(self)
        self.mark_entry = ttk.Entry(self.mark_frame, width = 30, textvariable = self.mark)
        self.mark_label = ttk.Label(self.mark_frame, text = 'Mark :')

        self.phone_frame = ttk.Frame(self)
        self.phone_entry = ttk.Entry(self.phone_frame, width = 29, textvariable = self.phone)
        self.phone_label = ttk.Label(self.phone_frame, text = 'Phone :')

        self.notes_frame = ttk.Frame(self)
        self.notes_entry = ttk.ScrolledText(self.notes_frame, width = 29)
        self.notes_label = ttk.Label(self.notes_frame, text = 'Notes :')


        
        self.buttons_frame = ttk.Frame(self)
        self.save_button = ttk.Button(self.buttons_frame, text = 'Save', command = self.save_button_func, bootstyle = 'success outline')
        self.import_button = ttk.Button(self.buttons_frame, text = 'Import', command = self.import_file, bootstyle = 'success outline')
        self.cancel_button = ttk.Button(self.buttons_frame, text = 'Cancel', command = self.destroy, bootstyle = 'success outline')


    def create_layout(self):
        
        # Grid
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        # Layout
        self.grade_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.grade_entry.pack(side = 'right')
        self.grade_label.pack(side = 'left')

        self.date_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.date_label.pack(side = 'left')
        self.date_box.pack(side = 'right')

        self.name_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'right')
        
        self.attend_frame.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.attend_entry.pack(side = 'right')
        self.attend_label.pack(side = 'left')

        self.homework_frame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.homework_label.pack(side = 'left')
        self.homework_entry.pack(side = 'right')

        self.interaction_frame.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.interaction_entry.pack(side = 'right')
        self.interaction_label.pack(side = 'left')

        self.mark_frame.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.mark_label.pack(side = 'left')
        self.mark_entry.pack(side = 'right')
        
        self.phone_frame.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.phone_label.pack(side = 'left')
        self.phone_entry.pack(side = 'right')

        self.notes_frame.grid(row = 4, column = 0, columnspan = 2, sticky = 'nsew', padx = 10)
        self.notes_label.pack(side = 'left')
        self.notes_entry.pack(side = 'left', expand = 1, fill = 'both')


        self.buttons_frame.grid(row = 5, column = 0, columnspan = 2, pady = 15, sticky = 'nsew')
        self.save_button.pack(side = 'left', expand = 1, ipadx = 50)
        self.import_button.pack(side = 'left', expand = 1, ipadx = 50)
        self.cancel_button.pack(side = 'left', expand = 1, ipadx = 50)

    def check_valid_inputs(self):

        if not self.name.get() or not self.attend.get() or not self.date.get():
            messagebox.showerror('Enter date, attend and name', 'Enter date, attend and name')
            self.focus()
            return
            
        if self.grade.get() not in ls:
            messagebox.showerror('Invalid Grade', 'Invalid Grade')
            self.focus()
            return

    def save_button_func(self):

        try:
            
            self.check_valid_inputs()


            self.set_table_name(f"a{self.date.get().replace('/', '_')}x{self.grade.get().replace(' ', '_')}")

            query = f"CREATE TABLE IF NOT EXISTS {self.get_table_name()} ( name NVARCHAR(100), attend NVARCHAR(4), homeword NVARCHAR(5), interaction NVARCHAR(15), mark VARCHAR(10), phone VARCHAR(15), notes NVARCHAR(500) )"
            cursor.execute(query)
            db.commit()

            query = f"INSERT INTO {self.get_table_name()} VALUES ('{self.name.get()}', '{self.attend.get()}', '{self.homework_entry.get()}', '{self.interaction.get()}', '{self.mark.get()}', '{self.phone.get()}', '{self.notes_entry.get('0.0', tk.END)}')"
            cursor.execute(query)
            db.commit()


            messagebox.showinfo('Success', 'Date Inserted Successfully')
            self.save_student()
            self.clear()
            self.focus()

        except mysql.connector.errors.DataError as err:
            messagebox.showerror('Data Error', str(err))
            self.focus()
        
    def clear(self):

        self.name.set('')
        self.attend.set('')
        self.homework.set('')
        self.interaction.set('')
        self.mark.set('')
        self.phone.set('')


    def create_grade_table(self):

        table_name = f"g{self.grade.get().replace(' ', '_')}"
        query = f"CREATE TABLE IF NOT EXISTS {table_name} (name NVARCHAR(50), phone VARCHAR(20))"
        cursor.execute(query)
        db.commit()
        return table_name

    def save_student(self):

        table_name = self.create_grade_table()

        query = f"INSERT INTO {table_name} SELECT '{self.name.get()}', '{self.phone.get()}' WHERE NOT EXISTS (SELECT * FROM {table_name} WHERE name = '{self.name.get()}')"
        cursor.execute(query)
        db.commit()

    def set_table_name(self, value):
        self.__table_name = value

    def get_table_name(self):
        return self.__table_name

    def import_file(self):

        try:

            if self.grade.get() not in ls or not self.date.get():
                messagebox.showerror('Enter Grade and Date', 'Enter Grade and Date')
                self.focus()
                return

            # Get Table Name
            session_table_name = f"a{self.date.get().replace('/', '_')}x{self.grade.get().replace(' ', '_')}"
            grade_table_name = f"g{self.grade.get().replace(' ', '_')}"

            # Create Table
            App.create_session_table(session_table_name)
            App.create_grade_table(grade_table_name)

            # Get File Path
            path = filedialog.askopenfile(filetypes = {'TXT .txt' : '*.txt'}, title = 'Enter txt File').name

            # Open File
            file = open(path, 'r')

            # Insert Data
            student_infos = file.read().split('\n')
            for info in student_infos:
                if not info:
                    continue
                name, attend, homework, interaction, mark, phone, note = info.split('،')
                
                query = f"INSERT INTO {session_table_name}  \
                VALUES ('{name}', '{attend}', '{homework}', '{interaction}', '{mark}', '{phone}', '{note}')"
                cursor.execute(query)
                db.commit()

                query = f"INSERT INTO {grade_table_name} SELECT '{name}', '{phone}' WHERE NOT EXISTS (SELECT * FROM {grade_table_name} WHERE name = '{name}')"
                cursor.execute(query)            
                db.commit()    

            file.close()

            messagebox.showinfo('Data Inserted Successfully', 'Data Inserted Successfully')
            self.focus()

        except ValueError:
            messagebox.showerror('Error in inputs number', 'Check the number of inputs in the file')
            self.focus()

        except AttributeError as err:
            messagebox.showerror(err, err)

        except mysql.connector.Error as err:
            messagebox.showerror(err, err)


    def fetch_data_to_name_entry(self, _):

        try:

            table_name = f"g{self.grade.get().replace(' ', '_')}"
            query = f"SELECT name FROM {table_name} WHERE EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}')"
            cursor.execute(query)
            names = cursor.fetchall()
            names = [x[0] for x in names]
            self.name_entry.config(values = names)

        except mysql.connector.Error as err:
            print(err)

class SearchSessionWindow(ttk.Toplevel):

    def __init__(self):

        super().__init__()

        self.create_widgets()

        self.create_layout()

        self.fetch_sessions()
        self.all_sessions.bind('<<TreeviewSelect>>', self.fetch_data)


    def create_widgets(self):

        # Grade Section
        self.grade_frame = ttk.Frame(self)
        self.grade_label = ttk.Label(self.grade_frame, text = 'Grade :')
        self.grade_entry = ttk.Combobox(self.grade_frame, values = ls, bootstyle = 'success', width = 28)

        # Date Section
        self.date_frame = ttk.Frame(self)
        self.date_label = ttk.Label(self.date_frame, text = 'Date :')
        self.date_entry = ttk.DateEntry(self.date_frame, bootstyle = 'success', width = 24)

        # All Sessions Show
        self.table_frame = ttk.Frame(self)
        self.all_sessions = ttk.Treeview(self.table_frame, columns = ('grade', 'date'), show = 'headings')
        self.all_sessions.heading(column = 'grade', text = 'Grade')
        self.all_sessions.heading(column = 'date', text = 'Date')
        self.scroll_bar = ttk.Scrollbar(self.table_frame, orient = 'vertical', command = self.all_sessions.yview_scroll)
        self.all_sessions.config(yscrollcommand = self.scroll_bar.set)

        # Buttons
        self.buttons_frame = ttk.Frame(self)
        self.search_button = ttk.Button(self.buttons_frame, text = 'Search', command = lambda : self.data_show(f"a{self.date_entry.entry.get().replace('/', '_')}x{self.grade_entry.get().replace(' ', '_')}"))
        self.cancel_button = ttk.Button(self.buttons_frame, text = 'Cancel', command = self.destroy)

    def create_layout(self):
        
        # Grid settings
        self.rowconfigure((0, 2), weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 2, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        self.grade_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.grade_entry.pack(side = 'right')
        self.grade_label.pack(side = 'left')
        
        self.date_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')
        self.date_label.pack(side = 'left')
        self.date_entry.pack(side = 'right')


        self.table_frame.grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew', padx = 10)
        self.all_sessions.pack(side = 'left', fill = 'both', expand = 1)
        self.scroll_bar.pack(side = 'left', fill = 'y')

        self.buttons_frame.grid(row = 2, column = 0, columnspan = 2, sticky = 'nsew', padx = 10)
        self.search_button.pack(side = 'left', expand = 1, ipadx = 40)
        self.cancel_button.pack(side = 'left', expand = 1, ipadx = 40)

    def fetch_sessions(self):

        try:

            query = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'a%x%'"
            cursor.execute(query)
            for table in cursor.fetchall():
                date, grade = table[0][1:].split('x')
                grade = grade.replace('_', ' ')
                date = date.replace('_', '-')
                self.all_sessions.insert('', tk.END, values = (grade, date))

        except mysql.connector.Error as err:
            messagebox.showerror(err, err)

    def fetch_data(self, _):

        for id in self.all_sessions.selection():
            grade, date = self.all_sessions.item(id)['values']
            table_name  = f"a{date.replace('-', '_')}x{grade.replace(' ', '_')}"
            self.data_show(table_name)
            

    def data_show(self, table_name):

        try:
            
            window = DataShow()
            window.focus()
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            for row in cursor.fetchall():
                window.table.insert(parent = '', index = tk.END, values = row)
            
        except mysql.connector.Error as err:
            window.destroy()
            messagebox.showerror(err, err)
            self.focus()

class SearchStudentWindow(ttk.Toplevel):

    def __init__(self):
        super().__init__()

        self.input_frame = ttk.Frame(self)

        self.name_frame = ttk.Frame(self.input_frame)
        self.name_label = ttk.Label(self.name_frame, text = 'Student Name : ')
        self.name_entry = ttk.Combobox(self.name_frame)

        self.grade_frame = ttk.Frame(self.input_frame)
        self.grade_label = ttk.Label(self.grade_frame, text = 'Grade : ')
        self.grade_entry = ttk.Combobox(self.grade_frame, values = ls)

        self.textbox = ttk.ScrolledText(self)
        self.textbox.tag_configure('right', justify = 'right')
        
        self.button = ttk.Button(self, text = 'Search', command = self.search_student)

        self.grade_entry.bind('<<ComboboxSelected>>', self.fetch_data)

        self.create_layout()

    def create_layout(self):

        # Input Frame
        self.input_frame.pack(fill = 'x', padx = 10, pady = 10)
        self.input_frame.rowconfigure(0, weight = 1)
        self.input_frame.columnconfigure((0, 1), weight = 1, uniform = 'a')

        self.name_frame.grid(row = 0, column = 0, sticky = 'nsew', padx = 5)
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'right')

        self.grade_frame.grid(row = 0, column = 1, sticky = 'nsew', padx = 5)
        self.grade_label.pack(side = 'left')
        self.grade_entry.pack(side = 'right', ipadx = 25)

        # Text Box
        self.textbox.pack(expand = 1, fill = 'both', padx = 10, pady = 10)

        # Button
        self.button.pack(expand = 1, ipadx = 40, pady = 10)

    def search_student(self):

        if not self.name_entry.get() and not self.grade_entry.get():
            messagebox.showerror('Enter Name and Grade', 'Enter Name and Grade')

        data = []


        query = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%x{self.grade_entry.get().replace(' ', '_').lower()}'" 
        cursor.execute(query)
        for table in cursor.fetchall():
            try:
                query = f"SELECT * FROM {table[0]} WHERE name = '{self.name_entry.get()}'"
                cursor.execute(query)
                lis = list(cursor.fetchall()[0])
                lis.append(table[0][1:].split('x')[0].replace('_', '-'))
                data.append(lis)
            except IndexError:
                continue

        self.insert_data_into_text_box(data)

        

    def insert_data_into_text_box(self, data):

        for row in data:
            name, attend, homework, interaction, mark, phone, note, date = row
            self.textbox.insert(tk.END, \
            f'{date} \n \
              الاسم : {name} \n \
              الحضور : {attend} \n \
              الواجب : {homework} \n \
              التفاعل : {interaction} \n \
              الدرجة : {mark} \n \
              الهاتف : {phone} \n \
              ملاحظات : {note} \n \n \
            ')
            self.textbox.tag_add('right', '0.0', tk.END)

        self.clipboard_clear()
        self.clipboard_append(self.textbox.get('1.0', tk.END))
        messagebox.showinfo('Data Copied Successfully', 'Data Copied Successfully')
        self.focus()


    def fetch_data(self, _):

        query = f"SELECT name FROM g{self.grade_entry.get().replace(' ', '_')}"
        cursor.execute(query)
        names = cursor.fetchall()
        names = [x[0] for x in names]
        self.name_entry.config(values = names)



class DataShow(ttk.Toplevel):
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
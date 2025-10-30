def delete_row_rollno():
    roll_no=int(entry_rollno.get())

    mydb=bot.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='g09ds2'
    )

    if mydb==None:
        print('could not connect')

    else:
        print('connected successfully')
        sql_query = "DELETE FROM student WHERE rollno = %s"
        values = [roll_no]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)
        if (mycursor.rowcount>0):
            status_msg='ROW DELETED'
        else:
            status_msg='STUDENT NOT FOUND'

        label_status_msg.configure(text=status_msg)
        mydb.commit()


    

def display():

    mydb = bot.connect(
        host='localhost', 
        user='root', 
        password='Tiger@123', 
        database='g09ds2'
    )

    if mydb == None:
        print("Could not connect")
    else:
        print("Connected successfully")

        sql_query = "SELECT * FROM student"

        mycursor = mydb.cursor()
        mycursor.execute(sql_query)

        students = mycursor.fetchall()

        if students==None:
            print("Student not found")
        else:
            print("Student Found : ", students)
            
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

            for student in students:
                treeview_display_students.insert(parent='', index='end', values=student)


def search_section():
    section=entry_section.get()

    mydb = bot.connect(
        host='localhost', 
        user='root', 
        password='Tiger@123', 
        database='g09ds2'
    )

    if mydb == None:
        print("Could not connect")
    else:
        print("Connected successfully")

        sql_query = "SELECT * FROM student WHERE section LIKE %s"
        values = [section + "%"]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)

        students = mycursor.fetchall()
        print(students)

        if len(students) == 0:
            print("Student not found")
            label_status_msg.configure(text='STUDENT NOT FOUND')
        else:
            print("Student Found : ", students)
            
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

            for student in students:
                treeview_display_students.insert(parent='', index='end', values=student)


def search_grade():
    grade=entry_grade.get()

    mydb = bot.connect(
        host='localhost', 
        user='root', 
        password='Tiger@123', 
        database='g09ds2'
    )

    if mydb == None:
        print("Could not connect")
    else:
        print("Connected successfully")

        sql_query = "SELECT * FROM student WHERE grade LIKE %s"
        values = [grade + "%"]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)

        students = mycursor.fetchall()
        print(students)

        if len(students) == 0:
            print("Student not found")
            label_status_msg.configure(text='STUDENT NOT FOUND')
        else:
            print("Student Found : ", students)
            
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

            for student in students:
                treeview_display_students.insert(parent='', index='end', values=student)



def search_marks():
    marks=float(entry_marks.get())

    mydb = bot.connect(
        host='localhost', 
        user='root', 
        password='Tiger@123', 
        database='g09ds2'
    )

    if mydb == None:
        print("Could not connect")
    else:
        print("Connected successfully")

        sql_query = "SELECT * FROM student WHERE marks = %s"
        values = [marks]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)

        students = mycursor.fetchall()
        print(students)

        if len(students) == 0:
            print("Student not found")
            label_status_msg.configure(text='STUDENT NOT FOUND')

        else:
            print("Student Found : ", students)
            
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

            for student in students:
                treeview_display_students.insert(parent='', index='end', values=student)


def search_name():
    name = entry_name.get()

    mydb = bot.connect(
        host='localhost', 
        user='root', 
        password='Tiger@123', 
        database='g09ds2'
    )

    if mydb == None:
        print("Could not connect")
        
    else:
        print("Connected successfully")

        sql_query = "SELECT * FROM student WHERE name LIKE %s"
        values = [name + "%"]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)

        students = mycursor.fetchall()
        print(students)

        if len(students) == 0:
            print("Student not found")
            label_status_msg.configure(text='STUDENT NOT FOUND')
        else:
            print("Student Found : ", students)
            
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

            for student in students:
                treeview_display_students.insert(parent='', index='end', values=student)

def search_rollno():
    roll_no=int(entry_rollno.get())

    mydb=bot.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='g09ds2'
    )

    if mydb==None:
        print('could not connect')

    else:
        print('connected successfully')
        sql_query = "SELECT * FROM student WHERE rollno = %s"
        values = [roll_no]

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)
       
        Student=mycursor.fetchone()
        if Student==None:
            print("Student not found")
            label_status_msg.configure(text='STUDENT NOT FOUND')
        else:
            print("Student found: ", Student)
            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row)

        treeview_display_students.insert(parent='',index='end',values=Student)

def add_student():
    roll_no=int(entry_rollno.get())
    name=entry_name.get()
    marks=float(entry_marks.get())
    grade=entry_grade.get()
    section=entry_section.get()

    outputmsg=f"Student - {roll_no}, {name}, {marks}, {grade},{section} added successfully"



    mydb=bot.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='g09ds4'
    )

    if mydb==None:
        print('could not connect')

    else:
        print('connected successfully')
        sql_query = 'INSERT INTO student(rollno, name, marks, grade, section) VALUES(%s, %s, %s, %s, %s)'
        values = (roll_no, name, marks, grade, section)

        mycursor = mydb.cursor()
        mycursor.execute(sql_query, values)
        mydb.commit()
        mydb.close()
        output_msg = f"Student - {roll_no}, {name}, {marks}, {grade}, {section} added successfully"
        label_status_msg.configure(text=output_msg)

import mysql.connector as bot
import tkinter as tk
from tkinter import ttk

root_window=tk.Tk()
root_window.geometry('800x600')
root_window.configure(background='light pink')

frame1= tk.Frame(
    master=root_window,
    padx=10,
    pady=10,
    background='light pink'
)

label_heading=tk.Label(
    master=frame1,
    text='STUDENT MANAGEMENT SYSTEM',
    font=('Ariel',30,'bold'),
    background='light pink'
)

label_frame_input=tk.LabelFrame(
    master=root_window,
    text='enter student details',
    background='light pink'
)

frame_status=tk.Frame(
    master=root_window,
    padx=10,
    pady=10,
    background='light pink'
)

label_rollno=tk.Label(
    master=label_frame_input,
    text='enter roll number: ',
    background='light pink'
)

label_name=tk.Label(
    master=label_frame_input,
    text='enter name: ',
    background='light pink'
)

label_marks=tk.Label(
    master=label_frame_input,
    text='enter marks: ',
    background='light pink'
)

label_grade=tk.Label(
    master=label_frame_input,
    text='enter grade: ',
    background='light pink'
)

label_section=tk.Label(
    master=label_frame_input,
    text='enter section: ',
    background='light pink'
)
entry_rollno=tk.Entry(
    master=label_frame_input,
    background='light pink'
)
entry_name=tk.Entry(
    master=label_frame_input,
    background='light pink'
)
entry_marks=tk.Entry(
    master=label_frame_input,
    background='light pink'
)
entry_grade=tk.Entry(
    master=label_frame_input,
    background='light pink'
)
entry_section=tk.Entry(
    master=label_frame_input,
    background='light pink'
)
button_add_student=tk.Button(
    master=label_frame_input,
    text='Add Student',
    command=add_student,
    width=20,
    height=3
)
button_search_rollno=tk.Button(
    master=label_frame_input,
    text='Search roll number',
    command=search_rollno,
    width=20
)
button_search_name=tk.Button(
    master=label_frame_input,
    text='search name',
    command=search_name,
    width=20
)
button_search_marks=tk.Button(
    master=label_frame_input,
    text='Search marks',
    command=search_marks,
    width=20
)
button_search_grade=tk.Button(
    master=label_frame_input,
    text='search grade',
    command=search_grade,
    width=20
)
button_search_section=tk.Button(
    master=label_frame_input,
    text='Search section',
    command=search_section,
    width=20
)

button_display_students=tk.Button(
    master=label_frame_input,
    text='display all students',
    command=display,
    width=20,
    height=3
)

button_delete_rollno=tk.Button(
    master=label_frame_input,
    text='delete based on roll number',
    command=delete_row_rollno,
    background='red',
    foreground='white'
)
label_status_msg = tk.Label(
    master=frame_status,
    text='',
    background='Light pink'
)

treeview_display_students = ttk.Treeview(
    master=root_window,
    columns=(1, 2, 3, 4, 5),
    show='headings',
    height=5
)

treeview_display_students.heading(1, text='ROLL NO.')
treeview_display_students.heading(2, text='STUDENT NAME')
treeview_display_students.heading(3, text='MARKS')
treeview_display_students.heading(4, text='GRADE')
treeview_display_students.heading(5, text='SECTION')


frame1.pack()

label_rollno.grid(row=0, column=0, padx=10,pady=10)
label_name.grid(row=1, column=0, padx=10,pady=10)
label_marks.grid(row=2, column=0, padx=10,pady=10)
label_grade.grid(row=3, column=0, padx=10,pady=10)
label_section.grid(row=4, column=0, padx=10,pady=10)

entry_rollno.grid(row=0, column=1, padx=10,pady=10)
entry_name.grid(row=1, column=1, padx=10,pady=10)
entry_marks.grid(row=2, column=1, padx=10,pady=10)
entry_grade.grid(row=3, column=1, padx=10,pady=10)
entry_section.grid(row=4, column=1, padx=10,pady=10)

button_add_student.grid(row=5, column=1, padx=10, pady=10)
button_search_rollno.grid(row=0, column=2, padx=10, pady=10)
button_search_name.grid(row=1, column=2, padx=10, pady=10)
button_search_marks.grid(row=2, column=2, padx=10, pady=10)
button_search_grade.grid(row=3, column=2, padx=10, pady=10)
button_search_section.grid(row=4, column=2, padx=10, pady=10)
button_display_students.grid(row=5, column=2, padx=10, pady=10)
button_delete_rollno.grid(row=0, column=3, padx=10, pady=10)


label_heading.pack()
label_frame_input.pack(fill='both',expand=1,padx=10,pady=10)
frame_status.pack()
label_status_msg.pack()
treeview_display_students.pack(fill='both',expand=1,padx=10,pady=10)
tk.mainloop()
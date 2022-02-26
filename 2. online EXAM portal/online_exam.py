from tkinter import *
from tkinter import messagebox
import os

subject_name = "DATA STRUCTURE"
total_questions = 5
total_time= "30 minutes"
total_students = 1      #this will help in paper checking    #change student id, in function evaluation ,using loop
Admin_pass = "12345"    #teachers password to check papers

global screen2
global screen3

file_name=''
email=''
sname=''
s_id=''
i=0
def submit():
    screen3.destroy()
    if i==1:
        f = open(file_name, 'w')
        f.write(str(option.get()) + '\n')
        f.close()
    else:
        f = open(file_name,'a')
        f.write(str(option.get()) + '\n')
        f.close()
    showquestion()

def showquestion():
    global screen3,i, option
    option = IntVar()
    if i == total_questions:
        messagebox.showinfo('EXAM OVER',"WELL DONE !!! \n YOUR EXAM OVER SUCCESSFULLY")
        screen3.destroy()
        f = open(file_name,'a')
        f.write(f"STUDENT NAME  :  {sname}\nID  :  {s_id}\nEMAIL ID  :  {email}\n\n")
        f.close()
    else:
        screen3 = Toplevel()
        screen3.geometry(f"{width}x{height}+0+0")
        screen3.title(f" {subject_name} ")
        file = open("QUESTIONS.txt", "r")
        question = file.readlines()
        Label(screen3, text=question[i * 5]).pack(anchor='w')
        Radiobutton(screen3, text=question[i * 5 + 1], variable=option, value=1).pack(anchor='w', padx=30)
        Radiobutton(screen3, text=question[i * 5 + 2], variable=option, value=2).pack(anchor='w', padx=30)
        Radiobutton(screen3, text=question[i * 5 + 3], variable=option, value=3).pack(anchor='w', padx=30)
        Radiobutton(screen3, text=question[i * 5 + 4], variable=option, value=4).pack(anchor='w', padx=30)
        Button(screen3, text=' SUBMIT ', bg='royalblue1', command=submit).pack(anchor='w', padx=70, pady=10)
        file.close()
        i += 1

def login(event):       #done
    global screen2, file_name,sname,s_id,email

    sname = i2.get()
    s_id=i1.get()
    email = i3.get()
    file_name=i1.get()+'.txt'
    a=messagebox.showinfo("SUCCESSFULLY LOGIN","LOGIN SUCCESSFULL")
    screen2.destroy()
    if a=="ok":
        b=messagebox.showinfo("   final call   ",f"on clicking  'OK'  your exam will start \n There are {total_questions} mcq questions and\n you have to solve it in {total_time}")
    if b=="ok":
        showquestion()

def exam():   #done

    global screen2,i1,i2,i3,email, sname, s_id
    screen2 = Toplevel()
    screen2.geometry("500x500")
    screen2.title(" STUDENT LOGIN ")
    l = Label(screen2, text="*************  ENTER YOUR INFORMATION  *************", bg="red", fg="white", font = "comicsan 12 bold", padx = 20, pady=10,relief= GROOVE).pack(side=TOP,fill=X)

    Label(screen2, text="  ID  :  ",pady=10,font = "comicsan 10 bold").pack()
    i1 = Entry(screen2, bd=6)
    i1.pack(ipadx=40)
    Label(screen2, text="  NAME  :  ",pady=10,font = "comicsan 10 bold").pack()
    i2 = Entry(screen2, bd=7)
    i2.pack(ipadx=40)
    Label(screen2, text="  EMAIL ID  :  ",pady=10,font = "comicsan 10 bold").pack()
    i3 = Entry(screen2, bd=6)
    i3.pack(ipadx=40)
    b1=Button(screen2,text="  LOGIN  ",bg="black",fg="white",relief=SUNKEN,bd=7)
    b1.pack(pady=20)
    b1.bind('<Button-1>',login)

def evaluate():
    s_id = E3.get()
    marks=0
    ans = open("ANSWERS.txt",'r')
    right_answer = ans.readlines()
    ans_sheet=open(s_id+'.txt','r')
    s_answer = ans_sheet.readlines()

    for i in range(total_questions):
        if right_answer[i] == s_answer[i] :
            marks+=1
    ans.close()
    s_answer[8] = f"you got {marks} marks in this exam\n"
    ans_sheet2 = open(s_id + '.txt', 'w')
    new = "".join(s_answer)
    ans_sheet2.write(new)
    ans_sheet2.close()
    messagebox.showinfo('Evaluation done',f"Evaluation of id number {E3.get()} done")
    ans_sheet.close()
    return

Admin_pass="12345"
def f():
    global E3
    if (E2.get() == Admin_pass):
        Label(screen2, text="Enter id of student  :").pack()
        E3 = Entry(screen2, bd=6)
        E3.pack()
        Button(screen2, text="  SUBMIT  ", bg="black", fg="white", relief=SUNKEN, bd=7, command=evaluate).pack(
            pady=20)
    else:
        messagebox.showinfo("  --ERROR--  ", "WRONG teachers PASSWORD")
def check() :
    global E2,screen2
    screen2=Toplevel()
    screen2.geometry("250x300")
    screen2.title(" Teachers space ")
    Label(screen2, text="Enter TEACHER,S PASSWORD :").pack()
    E2 = Entry(screen2, bd=6, show='* ')
    E2.pack()
    Button(screen2, text="  SUBMIT  ", bg="black", fg="white", relief=SUNKEN, bd=7, command=f).pack(pady=20)

def showrmarks():
    s_id = i1.get()
    screen2.destroy()
    global screen3
    screen3 = Toplevel()
    screen3.geometry("400x400")
    screen3.title(" RUSULT ")
    ans_sheet = open(s_id + '.txt', 'r')
    s_answer = ans_sheet.readlines()
    Label(screen3,text=s_answer[5]+'\n'+s_answer[6]+'\n'+s_answer[7]+'\n'+s_answer[8],padx=40,pady=40,font="system 16 bold",bd=3,fg='black',bg='bisque').pack(anchor=CENTER)

def result() :
    global screen2,i1
    screen2 = Toplevel()
    screen2.geometry("500x500")
    screen2.title(" RESULT  LOGIN ")
    Label(screen2, text="*************  ENTER YOUR INFORMATION  *************", bg="red", fg="white",font="comicsan 12 bold", padx=20, pady=10, relief=GROOVE).pack(side=TOP, fill=X)

    Label(screen2, text="  ID  :  ", pady=10, font="comicsan 10 bold").pack()
    i1 = Entry(screen2, bd=6)
    i1.pack(ipadx=40)

    Button(screen2, text="  CHECK RESULT  ", bg="black", fg="white", relief=SUNKEN, bd=7,command=showrmarks).pack(pady=20)

root = Tk()
global width, height
w = root.winfo_screenwidth()
h= root.winfo_screenheight()
width = int(w)
height = int(h)
root.geometry("300x300+0+0")
root.minsize(300,300)
root.maxsize(300,300)
root.title(" MAIN WINDOW ")

Button(root, text=" EXAM ", bd=10, width="20", height="2", bg="#532e1c", fg="white", command=exam).pack(pady=15)
Button(root, text="PAPER CHECK", bd=10, width="20", height="2", bg="#532e1c", fg="white", command=check).pack(pady=15)
Button(root, text=" RESULT ", bd=10, width="20", height="2", bg="#532e1c", fg="white", command=result).pack(pady=15)

root.mainloop()
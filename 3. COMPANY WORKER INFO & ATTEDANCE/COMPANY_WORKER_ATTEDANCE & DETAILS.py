from tkinter import *
from tkinter import messagebox
import os
import random
import smtplib
from password_of_amdin_mail import *        #remove this line if you provide your mail_pass in this code
                                        # sender's password is stored in a file named password_of_amdin_mail
import requests
Admin_mail ='deveshdhote111@gmail.com'      #edit your gmail id here
Admin_pass = "12345"                        # Emailpassword = 'Provide your mail password here'

#worker id start from ZERO
f= open("total_worker.txt",'r')
data = f.readlines()
W_ID=int(data[0])
f.close();

def get_valid_Email(email_id):
    list_of_survice_provider_name = ["gmail", "yahoo", "outlook", "hotmail"]
    if '@' in email_id and ".co" in email_id:
        index_of_AT = email_id.find("@")
        index_of_dot = email_id.find(".")
        provider_name = email_id[index_of_AT + 1:index_of_dot]
        if provider_name in list_of_survice_provider_name:
            return False
        else:
            messagebox.showwarning("Invalid provider ", "we only provide service for gmail / yahoo / outlook / hotmail ")
            return True
    else:
        messagebox.showwarning("WRONG EMAIL ID", "email id must have @__survice_provider_name__.co in it ")
        return True
def get_valid_mob(mob_no):
    if mob_no<=1000000000 or mob_no>=9999999999:
        messagebox.showwarning(" WRONG MOBILE NUMBER ", "MOBILE NUMBER SHOULD HAVE 10 DIGITS")
        return True
    else:
        return False

def update(num):
    new = i.get()+'\n'
    cscreen.destroy()
    f = open(wid.get()+'.txt','r')
    data=f.readlines()
    if num==1:
        data[0]=new
    elif num==2:
        data[1] = new
    elif num==3:
        data[2] = new
    elif num==4:
        if get_valid_mob( int(i.get()) ):
            return
        else:
            data[3] = new
    elif num==5:
        if get_valid_Email(i.get()):
            return
        else:
            data[4] = new
    elif num==6:
        data[5] = new
    f2 = open(wid.get() + ".txt", 'w')
    new = "".join(data)
    f2.write(new)
    f2.close()
    messagebox.showinfo("UPDATED","  DATA ADDED SUCCESSFULLY  ")
    f.close()
def change(num): #new screen,ek entry madhun string input ghil,return entry.get() , check(line number)
    global cscreen, i
    cscreen = Toplevel()
    cscreen.geometry(f"200x200+{width//2+100}+100")
    cscreen.title(" UPDATE INFO ")
    label = Label(cscreen, text="ENTER NEW DATA").pack()
    i = Entry(cscreen, bd=6)
    i.pack()
    Button(cscreen, text="  SUBMIT  ", bg="black", fg="white", relief=SUNKEN, bd=7, command=lambda:update(num)).pack(pady=20)

def send_sms(otp):
    f = open(wid.get() +'.txt','r')
    data = f.readlines()
    mob_num = data[3]
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id=FSTSMS&language=english&route=qt&numbers={mob_num}&message=42194&variables=" + '{' + "#BB#"+'}'+f"&variables_values={otp}"
    headers = {
        'authorization': "0coJXH1ReiwrFtYyqxSANhKV57CEkgL4dzTuZpM26GlPaQ3vnjHQL6ZGrNTKW8amqEgObt2V1v5iXAYd",
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    f.close()
def send_mail(otp):
    global wid
    Subject = "PASSWORD CHANGE OTP"
    Message = f"YOUR OTP IS  \n\n {otp}"
    wid=wid.get()

    f = open(wid+'.txt','r')
    data = f.readlines()
    res_mail = data[4]            # RECEIVER EMAIL ID TAKA LAGAL
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(Admin_mail, Emailpassword)
    server.sendmail(Admin_mail, res_mail,("Subject: " + str(Subject) + "\n\n" + str(Message)))
    server.quit()
    f.close()

def otp_check():
    a = int(i22.get())
    if otp == a:
        change(5)
    else:
        messagebox.showwarning("OTP","WRONG OTP")
def otp_get():
    global scr,i22
    scr = Toplevel()
    scr.geometry(f"250x100+{width//2+100}+100")
    scr.title(" otp ")
    Label(scr, text="ENTER YOUR OTP:").pack()
    i22 = Entry(scr, bd=6,width=20)
    i22.pack()
    Button(scr, text="  LOGIN  ", bg="black", fg="white", relief=SUNKEN, bd=7,command=otp_check).pack()
def mail(otp):
    global wid
    if int( wid.get() )<0 or int( wid.get() )>=W_ID:
        messagebox.showwarning("warning", "wrong id ")
        return
    abc=messagebox.showinfo("  OTP SENT  ", "OTP SENT TO YOUR EMAIL PLZ CONFORM OTP ")
    send_mail(otp)

    if abc=="ok":
        otp_get()
def mob(otp):
    global wid
    if int( wid.get() )<0 or int( wid.get() )>=W_ID:
        messagebox.showwarning("warning", "wrong id ")
        return
    abc = messagebox.showinfo("  OTP SENT  ", "OTP SENT TO YOUR mobile number PLZ CONFORM OTP ")
    send_sms(otp)
    if abc == "ok":
        otp_get()
def forgot_pass():# worker forgot password
    global fscreen , wid
    fscreen = Toplevel()
    fscreen.geometry(f"400x400+{width//2+100}+100")
    fscreen.title(" Change Password ")
    Label(fscreen, text="***  ENTER YOUR ID  ***", bg="gold", fg="white", font="system 12 bold",padx=20, pady=10, relief=GROOVE).pack(side=TOP, fill=X, pady=20)
    wid = Entry(fscreen, bd=6)
    wid.pack()
    Label(fscreen, text="***  CHOOSE ONE WAY TO CHANGE PASSWORD  ***", bg="gold", fg="white", font="system 12 bold",padx=20, pady=10, relief=GROOVE).pack(side=TOP, fill=X, pady=20)
    global otp
    otp = random.randrange(100000, 1000000)
    b1 = Button(fscreen, text="  E-MAIL  ", bg="black", fg="white", relief=SUNKEN, bd=7,command=lambda: mail(otp))
    b1.pack(pady=20)
    b2 = Button(fscreen, text="  MOBILE_NUMBER  ", bg="black", fg="white", relief=SUNKEN, bd=7,command=lambda: mob(otp))
    b2.pack(pady=7)

def wf():
    screen5.destroy()
def check_w_info():
    screen4.destroy()
    f = open(wid.get() + '.txt', 'r')
    data = f.readlines()
    global screen5
    screen5 = Toplevel()
    screen5.geometry(f"{width}x{height}+0+0")
    screen5.title(" YOUR INFORMATION ")
    Label(screen5, text=f"First name    :  {data[0]} ").pack()
    Label(screen5, text=f"Last  name    :  {data[1]} ").pack()
    Label(screen5, text=f"Date Of Birth :  {data[2]} ").pack()
    Label(screen5, text=f"Mobile No.    :  {data[3]} ").pack()
    Label(screen5, text=f"Email_ID      :  {data[4]} ").pack()
    Label(screen5, text=f"Per_day_salary:  {data[6]} ").pack()
    Label(screen5, text=f"\ntotal working days  :  {data[7]} ").pack()
    f.close()
    Button(screen5, text="  QUIT  ", bd=10, width="10", height="1", bg="gray50", fg="black", font="comicsan 10 bold",command=quit).pack(side=RIGHT, anchor="sw", pady=50, padx=30)
def edit_w_info():
    screen4.destroy()
    f = open(wid.get() + '.txt', 'r')
    data = f.readlines()
    global screen5
    screen5 = Toplevel()
    screen5.geometry(f"{width//2}x{height}+{width // 2}+0")
    screen5.title(" EDIT INFORMATION ")

    Label(screen5,text='').pack()
    Label(screen5, text=f"First name    :  {data[0]} ", font="comicsan 10 bold").pack(pady=1)
    Button(screen5, text='  EDIT  ',bd=3, width="5", height="1", bg="gray80", command=lambda:change(1)).pack()

    Label(screen5, text='').pack()
    Label(screen5, text=f"Last  name    :  {data[1]} ", font="comicsan 10 bold").pack()
    Button(screen5, text='  EDIT  ', bd=3, width="5", height="1", bg="gray80", command=lambda:change(2)).pack()

    Label(screen5, text='').pack()
    Label(screen5, text=f"Date Of Birth :  {data[2]} ", font="comicsan 10 bold").pack()
    Button(screen5, text='  EDIT  ', bd=3, width="5", height="1", bg="gray80", command=lambda:change(3)).pack()

    Label(screen5, text='').pack()
    Label(screen5, text=f"Mobile No.    :  {data[3]} ", font="comicsan 10 bold").pack()
    Button(screen5, text='  EDIT  ', bd=3, width="5", height="1", bg="gray80", command=lambda:change(4)).pack()

    Label(screen5, text='').pack()
    Label(screen5, text=f"Email_ID      :  {data[4]} ", font="comicsan 10 bold").pack()
    Button(screen5, text='  EDIT  ', bd=3, width="5", height="1", bg="gray80", command=lambda:change(5)).pack()

    Label(screen5, text='').pack()
    Label(screen5, text="password      :  * * * * * * * ", font="comicsan 10 bold").pack()
    Button(screen5, text='  EDIT  ', bd=3, width="5", bg="gray80", height="1", command=lambda:change(6)).pack()

    f.close()
    Button(screen5, text="  QUIT  ", bd=10, width="10", height="1", bg="gray50", fg="black", font="comicsan 10 bold",command=wf).pack(side=RIGHT, anchor="sw", pady=50, padx=30)
def checkworkerpassword():
    if int( wid.get() )<0 or int( wid.get() )>=W_ID:
        messagebox.showwarning("warning", "wrong id ")
    else:
        f = open(wid.get()+'.txt','r')
        data=f.readlines()
        if wpass.get()+'\n' == data[5]:
            global screen4
            screen4 = Toplevel()
            screen4.geometry(f"{width//2}x{height}+{width//2}+0")
            screen4.title(" WORKER's SPACE ")
            Button(screen4, text="  CHECK YOUR INFO  ", bg="cyan", fg="black", relief=SUNKEN, bd=6,command = check_w_info).pack(pady=20)
            Button(screen4, text="  EDIT YOUR INFO  ", bg="cyan", fg="black", relief=SUNKEN, bd=6,command = edit_w_info).pack(pady=20)
        else:
            messagebox.showwarning("warning", "wrong password ")
        f.close()
def worker():
    global wpass, wid
    Label(root, text="  Enter your ID :  ",pady=10,font = "comicsan 10 bold").pack()
    wid= Entry(root, bd=6)
    wid.pack(ipadx=40)
    Label(root, text="  Enter your password :  ",pady=10,font = "comicsan 10 bold").pack()
    wpass = Entry(root, bd=6)
    wpass.pack(ipadx=40)

    Button(root,text="  LOGIN  ",bg="black",fg="white",relief=SUNKEN,bd=7,command = checkworkerpassword).pack(pady=20)
    Button(root, text="  forgot password  ", bg="green yellow", fg="black", relief=SUNKEN, bd=5,command = forgot_pass).pack(pady=10)
    Button(root, text="  QUIT  ", bd=10, width="10", height="1", bg="gray50", fg="black", font="comicsan 10 bold",command=quit).pack(side=RIGHT, anchor="sw", pady=50, padx=30)
def add_attedance_in_respective_file():
    if int( E2.get() )<0 or int( E2.get() )>=W_ID:
        messagebox.showwarning("warning", "wrong id ")
    else:
        file = open(E2.get()+".txt", "r")
        data = file.readlines()
        if data[5]==E3.get() +'\n':
            data[7] = str( int(data[7])+1 )
            f = open(E2.get()+".txt", 'w')
            new = "".join(data)
            f.write(new)
            f.close()
            messagebox.showinfo("SUCCESS", "ATTEDANCE ADDED SUCCESSFULLY")
            screen3.destroy()
        else:
            messagebox.showwarning("warning","wrong password ")
        file.close()
def attedance():
    global screen3,E2,E3
    screen3 = Toplevel()
    screen3.geometry(f"{width}x{height}+0+0")
    screen3.title(" ATTEDANCE ")

    Label(screen3, text="Enter your ID : ").pack()
    E2 = Entry(screen3, bd=6)
    E2.pack()
    Label(screen3, text="  TYPE YOUR PASSWORD  : ").pack()
    E3 = Entry(screen3, bd=6)
    E3.pack()
    Button(screen3, text="  Add Attedance  ", bg="black", fg="white", relief=SUNKEN, bd=7,command = add_attedance_in_respective_file).pack(pady=20)
    Button(screen3, text="  forgot password  ", bg="green yellow", fg="black", relief=SUNKEN, bd=5,command = forgot_pass).pack(pady=10)


def final_submit():
    global W_ID
    new_file = open(str(W_ID)+".txt", "a")
    new_file.write("Per_day_salary  : " + E3.get() + '\n')
    new_file.write("0" + '\n')
    new_file.close()
    screen2.destroy()
    W_ID += 1
    f = open("total_worker.txt", 'w')
    f.write(str(W_ID))
    f.close()
    messagebox.showinfo("  NEW WORKER ADDED  ", "   NEW WORKER ADDED SUCCESSFULLY ")
def f():
    global E3
    if (E2.get() == Admin_pass):
        Label(screen2, text=f"Enter per day salary of this worker whose id is  {W_ID} :").pack()
        E3 = Entry(screen2, bd=6)
        E3.pack()
        Button(screen2, text="  SUBMIT  ", bg="black", fg="white", relief=SUNKEN, bd=7, command=final_submit).pack(pady=20)
    else:
        messagebox.showinfo("  --ERROR--  ","WRONG ADMIN PASSWORD")
def set_W_ID():
    global screen2, E2
    screen2 = Toplevel()
    screen2.geometry(f"300x300+{width//2+100}+100")
    screen2.title(" NEW_WORKER ")
    Label(screen2, text="Enter ADMIN PASSWORD :").pack()
    E2 = Entry(screen2, bd=6, show='* ')
    E2.pack()
    Button(screen2, text="  SUBMIT  ", bg="black", fg="white", relief=SUNKEN, bd=7,command=f).pack(pady=20)
def new_w_added():
    if (i1.get() == "" or i2.get() == "" or i3.get() == "" or i4.get() == "" or i5.get() == "" or i6.get() == "") :
        messagebox.showerror("Error", "All fields are mandatory!")
    elif get_valid_Email(i5.get()):
        pass
    elif get_valid_mob(int(i4.get())):
        pass
    else:
        new_file = open(str(W_ID)+".txt", "w")
        new_file.write(i1.get() + '\n')
        new_file.write(i2.get() + '\n')
        new_file.write(i3.get() + '\n')
        new_file.write(i4.get() + '\n')
        new_file.write(i5.get() + '\n')
        new_file.write(i6.get() + '\n')
        new_file.close()
        m=messagebox.showinfo("  W E L C O M E  ", f"REGISTRATION SUCCESSFULL with \n\nID : {W_ID} \n\n NOTE YOUR ID & tell manager tu gave you per_day_salary_info")
        if m == "ok":
            screen.destroy()
            set_W_ID()
def addworker():
    global screen,i1,i2,i3,i4,i5,i6
    screen = Toplevel()
    screen.geometry(f"{width//2}x{height}+{width//2}+0")
    screen.title(" NEW_WORKER ")
    Label(screen, text="*************  ENTER WORKERS ALL DETAILS  *************", bg="red", fg="white",font="comicsan 12 bold", padx=20, pady=10, relief=GROOVE).pack(side=TOP, fill=X)
    label1 = Label(screen, text="Enter your first name:").pack()
    i1 = Entry(screen, bd=6)
    i1.pack()
    label2 = Label(screen, text="Enter your last name:").pack()
    i2 = Entry(screen, bd=6)
    i2.pack()
    label3 = Label(screen, text="Enter your Date Of Birth: in DD/MM/YYYY Format").pack()
    i3 = Entry(screen, bd=6)
    i3.pack()
    label4 = Label(screen, text="Enter your Mobile No.:").pack()
    i4 = Entry(screen, bd=6)
    i4.pack()
    label5 = Label(screen, text="Enter your Email:\nservice provide should be gmail / yahoo / outlook / hotmail").pack()
    i5 = Entry(screen, bd=6)
    i5.pack()
    label6 = Label(screen, text="SET YOUR PASSWORD:").pack()
    i6 = Entry(screen, bd=6)
    i6.pack()
    Button(screen, text="  LOGIN  ", bg="black", fg="white", relief=SUNKEN, bd=7,command = new_w_added).pack(pady=20)

def checkadminpassword():
    if (E1.get() == Admin_pass):
        Button(root, text="  ADD_NEW_WORKER  ", bd=10, width="30", height="1", bg="gold3", fg="white",command=addworker).pack(pady=10)
        Button(root, text="  START_ATTEDANCE  ", bd=10, width="30", height="1", bg="gold3", fg="white",command=attedance).pack(pady=10)
        Button(root, text="  QUIT  ", bd=10, width="10", height="1", bg="gray50", fg="black", font="comicsan 10 bold",command=quit).pack(side=RIGHT, anchor="sw", pady=50, padx=30)
    else:
        messagebox.showinfo("  --ERROR--  ","WRONG ADMIN PASSWORD")
def manager():
    global E1
    Label(root, text="  Enter admin password  :  ",pady=10,font = "comicsan 10 bold").pack()
    E1 = Entry(root, bd=6,show="* ")
    E1.pack(ipadx=40)
    Button(root,text="  LOGIN  ",bg="black",fg="white",relief=SUNKEN,bd=7,command = checkadminpassword).pack(pady=20)


root1 = Tk()
global width, height
w = root1.winfo_screenwidth()
h= root1.winfo_screenheight()
width = int(w)
height = int(h)

root1.geometry(f"150x100+{width-150}+0")
root1.title(" QUIT ")
Button(root1, text="  QUIT  ", bd=10, width="10", height="1", bg="gray50", fg="black", font="comicsan 10 bold",command=quit).pack(side=RIGHT, anchor="nw", pady=20, padx=20)
root = Toplevel()
root.geometry(f"{width//2}x{height}+0+0")
root.title(" MAIN WINDOW ")

Button(root, text="  MANAGER  ", bd=10, width="20", height="2", bg="#532e1c", fg="white", command=manager).pack(pady=15)
Button(root, text="  WORKER  ", bd=10, width="20", height="2", bg="#532e1c", fg="white", command=worker).pack(pady=15)

root1.mainloop()
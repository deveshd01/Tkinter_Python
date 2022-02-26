import smtplib , webbrowser
from tkinter import *
from tkinter import messagebox

def get_valid_Email(email_id):
    list_of_survice_provider_name = ["gmail", "yahoo", "outlook", "hotmail"]
    if '@' in email_id and ".co" in email_id:
        index_of_AT = email_id.find("@")
        index_of_dot = email_id.find(".")
        provider_name = email_id[index_of_AT + 1:index_of_dot]
        if provider_name in list_of_survice_provider_name:
            return provider_name
        else:
            messagebox.showwarning("Invalid provider ", "we only provide service for gmail / yahoo / outlook / hotmail ")
    else:
        messagebox.showwarning("WRONG EMAIL ID", "email id must have @__survice_provider_name__.co in it ")

def set_smtp_domain(provider_name):
    if provider_name == "gmail":
        return "smtp.gmail.com"
    elif provider_name == "outlook" or provider_name == "hotmail":
        return "smtp-mail.outlook.com"
    elif provider_name == "yahoo":
        return "smtp.mail.yahoo.com"

def fun():
    smtp_port_number = 465
    while True:
        try:
            smtp_domain = set_smtp_domain(provider_name)
            connection = smtplib.SMTP(smtp_domain, smtp_port_number)
            connection.ehlo()
            connection.starttls()
            connection.login(email_id, PASSWORD)
        except:
            if provider_name == "gmail":
                m=messagebox.showinfo('ERROR',"your password is wrong "+'\nor\n'+"ALLOW  'less secure app'  option in your gmail " )
                if m=='ok':
                    answer=messagebox.askquestion('Webpage connection',"  do you want to open webpage from where you can enable this option  ")
                if answer == "yes":
                    webbrowser.open("https://myaccount.google.com/lesssecureapps")
                    continue
                else:
                    messagebox.showinfo("we won't open webpage for you","go to 'https://myaccount.google.com/lesssecureapps' and enable the option ")
                    continue
            else:
                messagebox.showerror('ERROR',"your email id OR password is wrong ")
                continue
        else:
            messagebox.showinfo('success', ' LOGIN SUCCESSFULL ')
            break

def sent_mail():
    global email_id, res_email_id, PASSWORD
    email_id = email.get()
    res_email_id = r_mail.get()
    Subject = Sub.get()
    Message = Msg.get()
    PASSWORD = PASSW.get()
    provider_name = get_valid_Email(email_id)
    fun()

    connection.sendmail(email_id, res_email_id, ("Subject: " + Subject + "\n\n" + Message))
    messagebox.showinfo('success', 'Message SENT ')
    connection.quit()


root = Tk()
global width, height
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
root.title(" E-MAIL SENDER ")

global email, PASSW, r_mail, Sub, Msg
Label(text="enter YOUR E-MAIL ID ").pack()
email = Entry(root)
email.pack()
Label(text="enter YOUR PASSWORD ").pack()
PASSW = Entry(root)
PASSW.pack()

Label(text="enter RECEIVERS E-MAIL ID ").pack()
r_mail = Entry(root)
r_mail.pack()

Label(root,text='Subject').pack()
Sub = Entry(root)
Sub.pack()
Label(root,text='Message').pack()
Msg = Entry(root)
Msg.pack()

Button(root,text='  send  ',bg='blue',fg='black',command=sent_mail).pack()


root.mainloop()
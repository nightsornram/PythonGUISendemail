from tkinter import *
from tkinter import ttk
import tkinter.font as font
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = name
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(email, password)
	s.sendmail(email, receiver.split(','), msg.as_string())
	s.quit()


def submit():
	global email,password,name

	email = email_var.get()
	password = password_var.get()
	name = name_var.get()

	
	def submit2():

		#global emailre,subject,msg

		email_reciever = email_reciever_var.get()
		sub = subj_var.get()
		inputT=Entry_msg.get("1.0","end-1c")

		emailre = email_reciever
		subject = sub
		msg = inputT

		sendthai(emailre,subject,msg)



		print('Success')


	GUI_EMAIL = Toplevel()
	GUI_EMAIL.option_add("*Font", "consolas 20")
	GUI_EMAIL.geometry("1000x600")
	Label_send= ttk.Label(GUI_EMAIL,text='ส่งถึง : ')
	Label_send.grid(row=0,column=0,padx=50,pady=20)
	Label_subj= ttk.Label(GUI_EMAIL,text='หัวข้อ : ')
	Label_subj.grid(row=1,column=0,padx=50,pady=20)
	Label_msg= ttk.Label(GUI_EMAIL,text='ข้อความ : ')
	Label_msg.grid(row=2,column=0,padx=50,pady=20)
	Entry_send= ttk.Entry(GUI_EMAIL,textvariable = email_reciever_var)
	Entry_send.grid(row=0,column=1,padx=10,pady=20,ipadx=100)
	Entry_subj= ttk.Entry(GUI_EMAIL,textvariable = subj_var)
	Entry_subj.grid(row=1,column=1,padx=10,pady=20,ipadx=100)
	Entry_msg= Text(GUI_EMAIL,width=40, height=8,)
	Entry_msg.grid(row=2,column=1)
	Button_sub = ttk.Button(GUI_EMAIL,text='ส่ง',command=submit2)
	Button_sub.grid(row=3,column=1,padx=50,pady=20,ipadx=50,ipady=20)
	GUI_EMAIL.mainloop()


GUI = Tk()
GUI.option_add("*Font","consolas 20")
GUI.geometry("800x400")
style = ttk.Style()
myFont = font.Font(family='Helvetica',size=20)
email_var = StringVar()
password_var = StringVar()
name_var = StringVar()
email_reciever_var = StringVar()
subj_var = StringVar()
massage_var = StringVar()
Label0= ttk.Label(GUI,text='Name : ')
Label0.grid(row=0,column=0,padx=50,pady=20)
Label1= ttk.Label(GUI,text='Email : ')
Label1.grid(row=1,column=0,padx=50,pady=20)
Label2= ttk.Label(GUI,text='Password : ')
Label2.grid(row=2,column=0,padx=50,pady=20)
Entry0= ttk.Entry(GUI,textvariable = name_var)
Entry0.grid(row=0,column=1,padx=10,pady=20,ipadx=70)
Entry1= ttk.Entry(GUI,textvariable = email_var)
Entry1.grid(row=1,column=1,padx=10,pady=20,ipadx=70)
Entry2= ttk.Entry(GUI,textvariable = password_var)
Entry2.grid(row=2,column=1,padx=10,pady=20,ipadx=70)
Button1 = ttk.Button(GUI,text='Log IN',command=submit)
Button1.grid(row=3,column=1,padx=50,pady=20,ipadx=50,ipady=20)
GUI.mainloop()
 


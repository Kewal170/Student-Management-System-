from tkinter import *
from tkinter import ttk # provides us combo box
import pymysql
from tkinter import messagebox

class Student:
	def __init__(self , root):
		self.root = root
		self.root.title('Student Management System')
		self.root.geometry('1350x700+0+0')# window created

		title = Label(self.root ,text = "Student Management System",bd=10,relief=GROOVE, font=('times new roman',40,'bold'), bg = 'yellow', fg= 'red')
		# we created a label(where to print,text,border,which style,font(style,size,bold),bg = background,fg = font color)
		title.pack(side=TOP,fill = X) # side = where to place it  #fill = X ,means in a full line fill it

		# =============== all variables =========================
		self.Roll_no_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.dob_var=StringVar()
		self.search_by=StringVar()
		self.search_txt=StringVar()

#================== manage frame window ==================================

		Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg='crimson')# frame created
		Manage_Frame.place(x=20,y=90,width=450,height=600)# where to place

		m_title = Label(Manage_Frame,text='Manage Students',bg='crimson',fg='white',font=('times new roman',30,'bold'),)
		m_title.grid(row=0,columnspan=2,pady=20)

# roll no.
		lbl_roll=Label(Manage_Frame,text='Roll No.',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

		txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_no_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
		txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

# name
		lbl_name=Label(Manage_Frame,text='Name',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

		txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
		txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

# email
		lbl_email=Label(Manage_Frame,text='Email',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

		txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
		txt_email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

# gender
		lbl_gender=Label(Manage_Frame,text='Gender',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

		combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=('times new roman',13,'bold'),state='readonly') # drop down text     ttk.Combobox
		combo_gender['values']=['Male','Female','Others']                            # assigning values
		combo_gender.grid(row=4,column=1,padx=20,pady=10)

# contact
		lbl_contact=Label(Manage_Frame,text='Contact.',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

		txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
		txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

# date of birth
		lbl_DOB=Label(Manage_Frame,text='DOB',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky='w')

		txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
		txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky='w')

# address
		lbl_address=Label(Manage_Frame,text='Address',bg='crimson',fg='white',font=('times new roman',20,'bold'),)
		lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

		self.txt_address=Text(Manage_Frame,width=30,height=4,font=('',10,'bold'))                                # text box
		self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')  # we have written self.  to join in database

# button frame
		btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg='crimson')# frame created
		btn_Frame.place(x=15,y=520,width=420)# where to place

		Addbtn = Button(btn_Frame,text='Add',width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
		updatebtn = Button(btn_Frame,text='Update',width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
		deletebtn = Button(btn_Frame,text='Delete',width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
		clearbtn = Button(btn_Frame,text='Clear',width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)



#========================detail frame==================================

		Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
		Detail_Frame.place(x=500,y=90,width=827,height=600)
# search
		lbl_search = Label(Detail_Frame,text='Search By',bg='crimson',fg='white',font=('times new roman',20,'bold'))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

		combo_search = ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by,font=('times new roman',13,'bold'),state='readonly')
		combo_search['values']=['roll_no','name','contact']             # combo box
		combo_search.grid(row=0,column=1,padx=20,pady=10)

		txt_search = Entry(Detail_Frame,width=15,textvariable=self.search_txt,font=('times new roman',14,'bold'),bd=4,relief=GROOVE)
		txt_search.grid(row=0,column=2,padx=20,pady=10)

		searchbtn = Button(Detail_Frame,text='Search',command=self.search_data,pady=5,width=10).grid(row=0,column=3,padx=20,pady=10)
		showallbtn = Button(Detail_Frame,text='ShowAll',pady=5,command=self.fetch_data,width=10).grid(row=0,column=4,padx=20,pady=10)

# ========================= table frame ===============================
		Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg='crimson')
		Table_Frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
		self.Student_table=ttk.Treeview(Table_Frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading('roll',text='Roll No.')
		self.Student_table.heading('name',text='Name')
		self.Student_table.heading('email',text='Email')
		self.Student_table.heading('gender',text='Gender')
		self.Student_table.heading('contact',text='Contact')
		self.Student_table.heading('dob',text='Date of birth')
		self.Student_table.heading('address',text='Address')
		self.Student_table['show']='headings'
		self.Student_table.column('roll',width=100)
		self.Student_table.column('name',width=100)
		self.Student_table.column('email',width=100)
		self.Student_table.column('gender',width=100)
		self.Student_table.column('contact',width=100)
		self.Student_table.column('address',width=100)
		self.Student_table.column('dob',width=100)
		self.Student_table.column('address',width=150)
		self.Student_table.pack(fill=BOTH,expand=1)
		self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
		self.fetch_data()

	def add_students(self):   # Configure your database here using the fields names show below
		if self.Roll_no_var.get()=='' or self.name_var.get()=='':
			messagebox.showerror("Error","All fields are required!!!")
		else:
			con=pymysql.connect(host='localhost',user='<Your username>',password='<Your password>',database='<Your database name>')
			cur=con.cursor()
			cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
																			 self.name_var.get(),
																			 self.email_var.get(),
																			 self.gender_var.get(),
																			 self.contact_var.get(),
																			 self.dob_var.get(),
																			 self.txt_address.get("1.0",END),
																			))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Sucess","Record has been inserted!")
	
	def fetch_data(self):
		con=pymysql.connect(host='localhost',user='<Your username>',password='<Your password>',database='<Your database name>')
		cur=con.cursor()
		cur.execute("Select * from students")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()

	def clear(self):
		self.Roll_no_var.set('')
		self.name_var.set('')
		self.email_var.set('')
		self.gender_var.set('')
		self.contact_var.set('')
		self.dob_var.set('')
		self.txt_address.delete('1.0',END)

	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		content=self.Student_table.item(cursor_row)
		row=content['values']
		self.Roll_no_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.txt_address.delete('1.0',END)
		self.txt_address.insert(END,row[6])

	def update_data(self):
		con=pymysql.connect(host='localhost',user='<Your username>',password ='<Your password>',database='<Your database name>')
		cur=con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
																													self.name_var.get(),
																													self.email_var.get(),
																													self.gender_var.get(),
																													self.contact_var.get(),
																													self.dob_var.get(),
																													self.txt_address.get("1.0",END),
																													self.Roll_no_var.get()
																		))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def delete_data(self):
		con=pymysql.connect(host='localhost',user='<Your username>',password ='<Your password>',database='<Your database name>')
		cur=con.cursor()
		cur.execute("delete from students where roll_no=%s",self.Roll_no_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()
	
	def search_data(self):
		con=pymysql.connect(host='localhost',user='<Your username>',password ='<Your password>',database='<Your database name>')
		cur=con.cursor()

		cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%';")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()


root = Tk()
ob = Student(root)
root.mainloop()


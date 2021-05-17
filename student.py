from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import face_recognition
import numpy as np



# Student class
class Student:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=========Variables===========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_grade = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phn = StringVar()
        #self.var_photo = StringVar()
        
  
        

        # first image
        img1 = Image.open(r"E:\Jupyter\6SEM\image\student1.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root,image = self.photoimg1)
        f_label.place(x=0,y=0,width=500,height=130)

        #second image
        img2 = Image.open(r"E:\Jupyter\6SEM\image\student3.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root,image = self.photoimg2)
        f_label.place(x=500,y=0,width=500,height=130)

        #third image
        img3 = Image.open(r"E:\Jupyter\6SEM\image\student2.jpg")
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_label = Label(self.root,image = self.photoimg3)
        f_label.place(x=1000,y=0,width=500,height=130)

        #Background image
        img4 = Image.open(r"E:\Jupyter\6SEM\image\background.jpg")
        img4 = img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image = Label(self.root,image = self.photoimg4)
        bg_image.place(x=0,y=130,width=1530,height=710)

        title_label = Label(bg_image,text="Student Management System ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Main frame over the background
        main_frame = Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        #image inside the left frame
        img_left = Image.open(r"E:\Jupyter\6SEM\image\student_detail.jpg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(left_frame,image = self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)

        #current course frame inside the left frame
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)
        
        #Department
        #Label inside the current frame,here we use grid so that a frame with row and column are made
        dep_label = Label(current_course_frame,text='Department:',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        #Here we make a combo in front of dep_label, combo show the dropdown window
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"] = ("Select Department","CSE","IT","CIVIL","MECHANICAL","ECE")
        dep_combo.current(0) #current with zero index because we want show the dep_combo value with zero indexing
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame,text='Course:',font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"] = ("Select Course","B.tech","M.tech","B.sc","M.Sc","Phd")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_course_frame,text='Year:',font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"] = ("Select Year","2018-2022","2019-2021","2019-2023","2020-2022","2020-2023","2020-2022")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label = Label(current_course_frame,text='Semester:',font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo["values"] = ("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information Frame
        class_student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #Student Id
        #Student label inside the student frame
        student_id_label = Label(class_student_frame,text='Student ID:',font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        student_name_label = Label(class_student_frame,text='Student Name:',font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #University Roll No.
        roll_no_label = Label(class_student_frame,text='University Roll No.:',font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Grade
        grade_label = Label(class_student_frame,text='Grade:',font=("times new roman",12,"bold"),bg="white")
        grade_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        grade_combo = ttk.Combobox(class_student_frame,textvariable=self.var_grade,font=("times new roman",12,"bold"),width=18,state="readonly")
        grade_combo["values"] = ("Select grade","A","B","C")
        grade_combo.current(0)
        grade_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label = Label(class_student_frame,text='DOB:',font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_student_frame,text='Gender:',font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"] = ("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_student_frame,text='Email:',font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No.
        phone_no_label = Label(class_student_frame,text='Phone Number:',font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phn,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Radio Button
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=5,column=0)

        radio_btn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn2.grid(row=5,column=1)


        #Button frame1
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=180,width=715,height=35)
        
        #Save
        save_btn = Button(btn_frame1,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=10)
        #Update
        update_btn = Button(btn_frame1,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10)
        #Delete
        delete_btn = Button(btn_frame1,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=10)
        #Reset
        reset_btn = Button(btn_frame1,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10)

        #Button frame2
        btn_frame2 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=235,width=715,height=35)
        #Take Photo
        take_photo_btn = Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",width=36,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0,padx=10)
        #Update Photo
        update_photo_btn = Button(btn_frame2,command = self.upload,text="Update Photo",width=36,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1,padx=10)

        #Right label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=710,height=580)

        #image inside the left frame
        img_right = Image.open(r"E:\Jupyter\6SEM\image\database.jpg")
        img_right = img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_label = Label(right_frame,image = self.photoimg_right)
        f_label.place(x=5,y=0,width=720,height=130)

        # ========Search System =========

        # Search Frame inside the Right Frame
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700,height=70)

        #Search Label
        search_label = Label(search_frame,text='Search By:',font=("times new roman",15,"bold"),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        #Search Combo
        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"] = ("Select","Student Id","University Roll no","Phone","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Searching 
        search_entry = ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        #Search
        reset_btn = Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5)
        #Show All
        reset_btn = Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4,padx=5)

        #==========Table Frame =========
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=700,height=340)
        #Scroll
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        #Student Table
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","name","roll","grade","dob","gender","email","phn","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #Add function in Scroll
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        #Heading
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="University RollNo")
        self.student_table.heading("grade",text="Grade")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phn",text="Phone No")
        self.student_table.heading("photo",text="Photo")

        #Show heading
        self.student_table["show"]="headings"

        #Set Width of column
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("grade",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phn",width=100)
        self.student_table.column("photo",width=100)


        #Pack the table
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #============Functions Declaration===========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Kashyappayal@20",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_grade.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phn.get(),
                                                                                        self.var_radio1.get()

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    #==============Fetch Data ===============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Kashyappayal@20",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
         
    #=============Get Cursor============
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_grade.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phn.set(data[11]),
        #self.var_photo.set(data[12]),
        self.var_radio1.set(data[12])

    #=========Update Function==============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 

        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="Kashyappayal@20",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,stud_name=%s,roll=%s,grade=%s,dob=%s,gender=%s,email=%s,phone=%s,photo=%s where stud_id=%s",(

                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_grade.get(),
                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_phn.get(),
                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                    self.var_std_id.get(), 
                    ))
                else:
                    if not update:
                        return   
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #===========Delete Function===========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student details","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="Kashyappayal@20",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where stud_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
                
    #========Reset Function==========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_grade.set("Select grade")
        self.var_dob.set("")
        self.var_gender.set("Select gender")
        self.var_email.set("")
        self.var_phn.set("")
        self.var_radio1.set("")


        #Face Detection: it has the objective of finding the faces (location and size) in an image
        #  and probably extract them to be used by the face recognition algorithm.
        
        #Face Recognition: with the facial images already extracted, cropped, resized 
        # and usually converted to grayscale, the face recognition algorithm is responsible 
        # for finding characteristics which best describe the image.

    #=============Generate data set or Take photo sample =========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 

        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Kashyappayal@20",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                user_id=0
                for x in myresult:
                    user_id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,stud_name=%s,roll=%s,grade=%s,dob=%s,gender=%s,email=%s,phone=%s,photo=%s where stud_id=%s",(

                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_grade.get(),
                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_phn.get(),
                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                    self.var_std_id.get()==user_id+1 
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #======Load predefine data on face frontals from openCv=====

                #The Haar features for detecting these objects are stored as XML

                #Haar features is used for our object detection, by adding the file path to the CascadeClassifier() 
                # constructor, which uses pre-trained models for object detection:

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    #Convert color image into gray color
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    #Now, we can use this face_cascade object to detect faces in the Image:
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3 means that it can scale 30% down to try and match the faces better.
                    #Minimum Neighbour=5 parameter, it's used to control the number of false positives and false negatives

                    # Make a rectangular box
                    for (x,y,w,h) in faces:
                        face_crop = img[y:y+h,x:x+w]
                        return face_crop
                
                # Open camera 
                cap = cv2.VideoCapture(0)
                img_id=0
                #Infinite loop
                while True:
                    ret,my_frame = cap.read()
                    if face_crop(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_crop(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(user_id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complete successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    


    #=======Upload Photo==========
    def upload(self):
        path = 'upload'
        images=[]
        person_name=[]
        mylist = os.listdir(path)
        for curr_img in mylist:
            current_img = cv2.imread(f'{path}/{curr_img}')
            images.append(current_img)
            person_name.append(os.path.splitext(curr_img)[0])
        
        def faceEncodings(images):
            
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        
        encode_List_known = faceEncodings(images)
        messagebox.showinfo("success","All Encoding Complete!")

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            faces = cv2.resize(frame,(0,0),None,0.25,0.25)
            faces = cv2.cvtColor(faces,cv2.COLOR_RGB2BGR)

            faces_current_frame =face_recognition.face_location(faces)
            encode_current_frame = face_recognition.face_encodings(faces,faces_current_frame)

            #Face matching and location
            for encodeFace , faceLoc in zip(encode_current_frame,faces_current_frame):
                matches = face_recognition.compare_face(encode_List_known,encodeFace)
                faceDis = face_recognition.face_distance(encode_List_known,encodeFace)

                # Index values of min distance
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = person_name[matchIndex].upper()
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

            cv2.imshow("Camera",frame)
            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()


    
#Object of Student class
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
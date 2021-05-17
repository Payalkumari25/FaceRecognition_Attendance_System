from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

# Student class
class Attendance:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        #=======Variable===========
        self.var_atten_id =StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()
        

        # first image
        img1 = Image.open(r"E:\Jupyter\6SEM\image\student1.jpg")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root,image = self.photoimg1)
        f_label.place(x=0,y=0,width=800,height=200)

        #second image
        img2 = Image.open(r"E:\Jupyter\6SEM\image\student3.jpg")
        img2 = img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root,image = self.photoimg2)
        f_label.place(x=800,y=0,width=800,height=200)

        #Background image
        img4 = Image.open(r"E:\Jupyter\6SEM\image\background.jpg")
        img4 = img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image = Label(self.root,image = self.photoimg4)
        bg_image.place(x=0,y=200,width=1530,height=710)

        title_label = Label(bg_image,text="Attendance Management System ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Main frame over the background
        main_frame = Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendace Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        #image inside the left frame
        img_left = Image.open(r"E:\Jupyter\6SEM\image\student_detail.jpg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(left_frame,image = self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)

        #Frame inside left frame
        inside_left_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        inside_left_frame.place(x=0,y=135,width=720,height=400)

        #Label inside left frame
        #ID
        attendance_id_label = Label(inside_left_frame,text='Attendance Id',font=("times new roman",12,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name
        name_label = Label(inside_left_frame,text='Name:',font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Roll 
        roll_label = Label(inside_left_frame,text='Roll',font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Dep
        dep_label = Label(inside_left_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        time_label = Label(inside_left_frame,text='Time',font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label = Label(inside_left_frame,text='Date',font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry = ttk.Entry(inside_left_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Status
        status = Label(inside_left_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        status.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status = ttk.Combobox(inside_left_frame,width=20,textvariable=self.var_status,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Button frame1
        btn_frame1 = Frame(inside_left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        #Import
        import_btn = Button(btn_frame1,text="Import csv",command=self.import_csv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0,padx=10)
        #Export
        export_btn = Button(btn_frame1,text="Export csv",command=self.export_csv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1,padx=10)
        #Update
        update_btn = Button(btn_frame1,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2,padx=10)
        #Reset
        reset_btn = Button(btn_frame1,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10)


        #Right label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendace Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        #Table frame inside the right frame
        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        #=====Scroll bar table===
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #Attendance table
        self.Attendance_Report_table = ttk.Treeview(table_frame,column=("id","name","roll","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #Add function on scroll
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_Report_table.xview)
        scroll_y.config(command=self.Attendance_Report_table.yview)

        #Heading
        self.Attendance_Report_table.heading("id",text="Attendance Id")
        self.Attendance_Report_table.heading("name",text="Name")
        self.Attendance_Report_table.heading("roll",text="Roll")
        self.Attendance_Report_table.heading("dep",text="Department")
        self.Attendance_Report_table.heading("time",text="Time")
        self.Attendance_Report_table.heading("date",text="Date")
        self.Attendance_Report_table.heading("attendance",text="Attendance")

        #Show heading
        self.Attendance_Report_table["show"]="headings"

        #Set Width of column
        self.Attendance_Report_table.column("id",width=100)
        self.Attendance_Report_table.column("name",width=100)
        self.Attendance_Report_table.column("roll",width=100)
        self.Attendance_Report_table.column("dep",width=100)
        self.Attendance_Report_table.column("time",width=100)
        self.Attendance_Report_table.column("date",width=100)
        self.Attendance_Report_table.column("attendance",width=100)

        #Pack the table
        self.Attendance_Report_table.pack(fill=BOTH,expand=1)
        #Bind the get cursor function
        self.Attendance_Report_table.bind("<ButtonRelease>",self.get_cursor)

    #=======Fetch data=========
    def fetch_data(self,rows):
        self.Attendance_Report_table.delete(*self.Attendance_Report_table.get_children())
        for i in rows:
            self.Attendance_Report_table.insert("",END,values=i)

    #=======Import CSV========    
    def import_csv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csv_read= csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)
    
    #=======Export CSV========
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(file_name)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #======Get Cursor=====
    def get_cursor(self,event=""):
        cursor_row = self.Attendance_Report_table.focus()
        content = self.Attendance_Report_table.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_roll.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    #=======Reset Data======
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")
            

#Object of Student class
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
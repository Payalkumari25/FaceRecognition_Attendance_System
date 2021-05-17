from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import mysql.connector

class Face_Recognition_System:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img1 = Image.open(r"E:\Jupyter\6SEM\image\college1.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root,image = self.photoimg1)
        f_label.place(x=0,y=0,width=500,height=130)

        #second image
        img2 = Image.open(r"E:\Jupyter\6SEM\image\face.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root,image = self.photoimg2)
        f_label.place(x=500,y=0,width=500,height=130)

        #third image
        img3 = Image.open(r"E:\Jupyter\6SEM\image\college2.jpg")
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

        title_label = Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Student button
        img5 = Image.open(r"E:\Jupyter\6SEM\image\student.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image,image = self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img6 = Image.open(r"E:\Jupyter\6SEM\image\detect.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_image,image = self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_image,text="Detect Face",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Face button
        img7 = Image.open(r"E:\Jupyter\6SEM\image\Attendance.jpg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_image,image = self.photoimg7,command=self.attendance_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # #Help button
        # img8 = Image.open(r"E:\Jupyter\6SEM\image\help.jpg")
        # img8 = img8.resize((220,220),Image.ANTIALIAS)
        # self.photoimg8 = ImageTk.PhotoImage(img8)

        # b1 = Button(bg_image,image = self.photoimg8,cursor="hand2")
        # b1.place(x=1100,y=100,width=220,height=220)

        # b1_1 = Button(bg_image,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=300,width=220,height=40)


        #Train Face button
        img9 = Image.open(r"E:\Jupyter\6SEM\image\train.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_image,image = self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1 = Button(bg_image,text="Train Model",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Photo button
        img10 = Image.open(r"E:\Jupyter\6SEM\image\photo.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_image,image = self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1 = Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # #Developer button
        # img11 = Image.open(r"E:\Jupyter\6SEM\image\developer.jpg")
        # img11 = img11.resize((220,220),Image.ANTIALIAS)
        # self.photoimg11 = ImageTk.PhotoImage(img11)

        # b1 = Button(bg_image,image = self.photoimg11,cursor="hand2")
        # b1.place(x=800,y=380,width=220,height=220)

        # b1_1 = Button(bg_image,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=800,y=580,width=220,height=40)

        #Exit button
        img12 = Image.open(r"E:\Jupyter\6SEM\image\exit.jpg")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_image,image = self.photoimg12,command=self.exit,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1 = Button(bg_image,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

    #========Function for photo button======
    def open_img(self):
        os.startfile("data")

    #========Exit Button======
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return



    #========Function for student Button==========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    #========Function for train Button==========
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    #========Function for train Button==========
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    #========Function for train Button==========
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
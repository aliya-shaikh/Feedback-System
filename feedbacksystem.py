from tkinter import *
import re
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import db

class Feedback():
    def __init__(self,master):
        self.master = master
        self.master.geometry("1350x700+0+0")
        self.master.title("FEEDBACK SYSTEM")
        my_font = Font(family = "Comic Sans Ms", size = 30, underline = 1)
        self.bg_img = ImageTk.PhotoImage(file = "back.jpg")
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.back_img = Label(self.master,image = self.bg_img)
        self.back_img.pack()
        self.title = Label(self.master, text = "FEEDBACK SYSTEM", font = my_font, bg ="#efefef", fg="green", bd = 5, relief = RIDGE)
        self.title.place(x=0, y=0, relwidth = 1)
        self.homeframe = Frame(self.master,bd = 2, bg = "white")
        self.homeframe.place(x=260,y=120)
        self.adminframe = Frame(self.master,bd = 2, bg = "white")
        self.userframe = Frame(self.master,bd = 2, bg = "white")
        self.contactusframe = Frame(self.master,bd = 2, bg = "white")
        self.aboutusframe = Frame(self.master,bd = 2, bg = "white")
        self.adminloginframe = Frame(self.master,bd=2,bg="white")
        self.registerframe = Frame(self.master,bd=2,bg="white")
        self.userfeedbackframe = Frame(self.master,bd=2,bg="white")
        self.viewframe = Frame(self.master,bd=2,bg="white")
        self.categoryframe = Frame(self.master,bd=2,bg="white")
        self.travelframe = Frame(self.master,bd=2,bg="white")
        self.foodframe = Frame(self.master,bd=2,bg="white")
        self.educationframe = Frame(self.master,bd=2,bg="white")
        self.shopframe = Frame(self.master,bd=2,bg="white")
        self.cabframe = Frame(self.master,bd=2,bg="white")
        self.makemytripframe = Frame(self.master,bd =2,bg = "white")
        self.goibiboframe = Frame(self.master,bd =2,bg = "white")
        self.yatraframe = Frame(self.master,bd =2,bg = "white")
        self.easetripframe = Frame(self.master,bd =2,bg = "white")
        self.trivagoframe = Frame(self.master,bd =2,bg = "white")
        self.foodpandaframe = Frame(self.master,bd =2,bg = "white")
        self.zomatoframe = Frame(self.master,bd =2,bg = "white")
        self.swiggyframe = Frame(self.master,bd =2,bg = "white")
        self.freshmenuframe = Frame(self.master,bd =2,bg = "white")
        self.foodmingoframe = Frame(self.master,bd =2,bg = "white")
        self.khanacademyframe = Frame(self.master,bd =2,bg = "white")
        self.courseraframe = Frame(self.master,bd =2,bg = "white")
        self.w3schoolframe = Frame(self.master,bd =2,bg = "white")
        self.byjusframe = Frame(self.master,bd =2,bg = "white")
        self.codeacademyframe = Frame(self.master,bd =2,bg = "white")
        self.amazonframe = Frame(self.master,bd =2,bg = "white")
        self.flipkartframe = Frame(self.master,bd =2,bg = "white")
        self.ebayframe = Frame(self.master,bd =2,bg = "white")
        self.walmartframe = Frame(self.master,bd =2,bg = "white")
        self.alibabaframe = Frame(self.master,bd =2,bg = "white")
        self.uberframe = Frame(self.master,bd =2,bg = "white")
        self.olaframe = Frame(self.master,bd =2,bg = "white")
        self.meruframe = Frame(self.master,bd =2,bg = "white")
        self.savaariframe = Frame(self.master,bd =2,bg = "white")
        self.bharattaxiframe = Frame(self.master,bd =2,bg = "white")
        self.travelviewframe = Frame(self.master,bd =2,bg = "white")
        self.foodviewframe = Frame(self.master,bd =2,bg = "white")
        self.educationviewframe  = Frame(self.master,bd =2,bg = "white")
        self.shoppingviewframe  = Frame(self.master,bd =2,bg = "white")
        self.cabviewframe  = Frame(self.master,bd =2,bg = "white")
        self.ppframe = Frame(self.master,bd=2,bg="white")
        self.tandcframe = Frame(self.master,bd=2,bg="white")
        self.makemytripupdate = Frame(self.master,bd=2,bg="white")
        self.goibiboupdate = Frame(self.master,bd=2,bg="white")
        self.yatraupdate = Frame(self.master,bd=2,bg="white")
        self.easetripupdate = Frame(self.master,bd=2,bg="white")
        self.trivagoupdate = Frame(self.master,bd=2,bg="white")
        self.foodpandaupdate = Frame(self.master,bd=2,bg="white")
        self.zomatoupdate = Frame(self.master,bd=2,bg="white")
        self.swiggyupdate = Frame(self.master,bd=2,bg="white")
        self.freshmenuupdate = Frame(self.master,bd=2,bg="white")
        self.foodmingoupdate = Frame(self.master,bd=2,bg="white")
        self.khanacademyupdate = Frame(self.master,bd=2,bg="white")
        self.courseraupdate = Frame(self.master,bd=2,bg="white")
        self.w3schoolupdate = Frame(self.master,bd=2,bg="white")
        self.byjusupdate = Frame(self.master,bd=2,bg="white")
        self.codeacademyupdate = Frame(self.master,bd=2,bg="white")
        self.amazonupdate = Frame(self.master,bd=2,bg="white")
        self.flipkartupdate = Frame(self.master,bd=2,bg="white")
        self.ebayupdate = Frame(self.master,bd=2,bg="white")
        self.walmartupdate = Frame(self.master,bd=2,bg="white")
        self.alibabaupdate = Frame(self.master,bd=2,bg="white")
        self.uberupdate = Frame(self.master,bd=2,bg="white")
        self.olaupdate = Frame(self.master,bd=2,bg="white")
        self.meruupdate = Frame(self.master,bd=2,bg="white")
        self.savaariupdate = Frame(self.master,bd=2,bg="white")
        self.bharattaxiupdate = Frame(self.master,bd=2,bg="white")
        self.feed_img = Label(self.homeframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.homeframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.homeframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.homeframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.homeframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE ,command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.homeframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.homeframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.hometitle = Label(self.homeframe, text="THIS IS HOME PAGE", font=my_font,fg = "green")
        self.hometitle.place(x =0, y=40,relwidth=1)
        self.footer = Button(self.master, text = "Privacy Policy", font = ("Comic Sans Ms", 10), bg ="#efefef", fg="green", bd=2,relief = RIDGE,command=self.pp)
        self.footer.place(x=0, y=630,relwidth = 1)
        self.footer1 = Button(self.master, text = "Terms and Condition", font = ("Comic Sans Ms", 10), bg ="#efefef", fg="green", bd=2,relief = RIDGE,command=self.tandc)
        self.footer1.place(x=0, y=655,relwidth = 1)
        self.footer2 = Button(self.master, text = "Copyright All right Reserved Created by Aliya @aaliyashaikh4013@gmail.com ", font = ("Comic Sans Ms", 10) ,bg ="#efefef", fg="green", bd=2,relief = RIDGE)
        self.footer2.place(x=0, y=680, relwidth =1)
        
    def homepage(self):
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.cabframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.homeframe.place(x=260,y=120)

    def adminpage(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.adminframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.adminframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.adminframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.adminframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.adminframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.adminframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.adminframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.admintitle = Label(self.adminframe, text="THIS IS ADMIN PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.admintitle.place(x =0, y=40,relwidth=1)
        self.username = Label(self.adminframe,text ="USERNAME",font =("Comic Sans Ms",15,"bold"),fg = "green")
        self.username.place(x=250,y=150)
        self.usernameentry = Entry(self.adminframe)
        self.usernameentry.place(x=400,y=160)
        self.password = Label(self.adminframe,text ="PASSWORD",font =("Comic Sans Ms",15,"bold"),fg = "green")
        self.password.place(x=250,y=200)
        self.passwordentry = Entry(self.adminframe)
        self.passwordentry.place(x=400,y=210)
        self.loginbutton =Button(self.adminframe, text ="LOGIN", font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.adminlogin)
        self.loginbutton.place(x=370,y=250)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.viewframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.adminframe.place(x=260,y=120)

    def adminlogin(self):
        if self.usernameentry.get() == "" or self.passwordentry.get() == "":
            messagebox.showerror("error", "All Feilds are Required !!")
        elif self.usernameentry.get() == "root" and self.passwordentry.get() == "root":
            messagebox.showinfo("login","LOGIN SUCCESSFUL !!!")
            self.usernameentry.delete(0,END)
            self.passwordentry.delete(0,END)
            self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
            self.feed_img = Label(self.adminloginframe, image = self.feed_img)
            self.feed_img.pack()
            self.admintitle = Label(self.adminloginframe, text="WELCOME ADMIN", font=("Comic Sans Ms",30),fg = "green")
            self.admintitle.place(x =0, y=200,relwidth=1)
            self.navbar = Label(self.adminloginframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
            self.navbar.place(x=0,y=0,relwidth=1)
            self.homebutton = Button(self.adminloginframe, text = "VIEW FEEDBACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.view)
            self.homebutton.place(x=600, y=0)
            self.adminbutton = Button(self.adminloginframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminlogout)
            self.adminbutton.place(x=730, y=0)
            self.homeframe.place_forget()
            self.makemytripupdate.place_forget()
            self.goibiboupdate.place_forget()
            self.yatraupdate.place_forget()
            self.easetripupdate.place_forget()
            self.trivagoupdate.place_forget()
            self.foodpandaupdate.place_forget()
            self.zomatoupdate.place_forget()
            self.swiggyupdate.place_forget()
            self.freshmenuupdate.place_forget()
            self.foodmingoupdate.place_forget()
            self.khanacademyupdate.place_forget()
            self.courseraupdate.place_forget()
            self.w3schoolupdate.place_forget()
            self.byjusupdate.place_forget()
            self.codeacademyupdate.place_forget()
            self.amazonupdate.place_forget()
            self.flipkartupdate.place_forget()
            self.ebayupdate.place_forget()
            self.walmartupdate.place_forget()
            self.alibabaupdate.place_forget()
            self.uberupdate.place_forget()
            self.olaupdate.place_forget()
            self.meruupdate.place_forget()
            self.savaariupdate.place_forget()
            self.bharattaxiupdate.place_forget()
            self.adminframe.place_forget()
            self.userframe.place_forget()
            self.contactusframe.place_forget()
            self.aboutusframe.place_forget()
            self.registerframe.place_forget()
            self.viewframe.place_forget()
            self.ppframe.place_forget()
            self.tandcframe.place_forget()
            self.categoryframe.place_forget()
            self.travelframe.place_forget()
            self.foodframe.place_forget()
            self.educationframe.place_forget()
            self.shopframe.place_forget()
            self.cabframe.place_forget()
            self.makemytripframe.place_forget()
            self.goibiboframe.place_forget()
            self.yatraframe.place_forget()
            self.easetripframe.place_forget()
            self.trivagoframe.place_forget()
            self.foodpandaframe.place_forget()
            self.zomatoframe.place_forget()
            self.swiggyframe.place_forget()
            self.freshmenuframe.place_forget()
            self.foodmingoframe.place_forget()
            self.khanacademyframe.place_forget()
            self.courseraframe.place_forget()
            self.w3schoolframe.place_forget()
            self.byjusframe.place_forget()
            self.codeacademyframe.place_forget()
            self.amazonframe.place_forget()
            self.flipkartframe.place_forget()
            self.ebayframe.place_forget()
            self.walmartframe.place_forget()
            self.alibabaframe.place_forget()
            self.uberframe.place_forget()
            self.olaframe.place_forget()
            self.meruframe.place_forget()
            self.savaariframe.place_forget()
            self.bharattaxiframe.place_forget()
            self.travelviewframe.place_forget()
            self.foodviewframe.place_forget()
            self.educationviewframe.place_forget()
            self.shoppingviewframe.place_forget()
            self.cabviewframe.place_forget()
            self.userfeedbackframe.place_forget()
            self.adminloginframe.place(x=260,y=120)
        else:
            messagebox.showerror("error","Username or Password Incorrect !!")
            self.usernameentry.delete(0,END)
            self.passwordentry.delete(0,END)

    def view(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.viewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.viewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.backbutton = Button(self.viewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.viewback)
        self.backbutton.place(x=752, y=0)
        self.travelbutton= Button(self.viewframe, text = "TRAVEL", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.travelview)
        self.travelbutton.place(x=650,y=0)
        self.foodbutton= Button(self.viewframe, text = "FOOD", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.foodview)
        self.foodbutton.place(x=580,y=0)
        self.educationbutton= Button(self.viewframe, text = "EDUCATION", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.educationview)
        self.educationbutton.place(x=470,y=0)
        self.shoppingbutton= Button(self.viewframe, text = "SHOPPING", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.shoppingview)
        self.shoppingbutton.place(x=370,y=0)
        self.cabbutton= Button(self.viewframe, text = "CAB SERVICES", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.cabview)
        self.cabbutton.place(x=240,y=0)
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.viewframe.place(x=260,y=120)

    def viewback(self):
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.homeframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.viewframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place(x=260,y=120)
        
    def travelview(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.travelviewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.travelviewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.makemytripbutton = Button(self.travelviewframe,text ="MAKE MY TRIP",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.makemytripview)
        self.makemytripbutton.place(x=50,y=60)
        self.goibibobutton = Button(self.travelviewframe,text ="GOIBIBO",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.goibiboview)
        self.goibibobutton.place(x=240,y=60)
        self.yatrabutton = Button(self.travelviewframe,text ="YATRA",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.yatraview)
        self.yatrabutton.place(x=380,y=60)
        self.easetripbutton = Button(self.travelviewframe,text ="EASETRIP",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.easetripview)
        self.easetripbutton.place(x=500,y=60)
        self.trivagobutton = Button(self.travelviewframe,text ="TRIVAGO",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.trivagoview)
        self.trivagobutton.place(x=650,y=60)
        self.makegobutton = Button(self.travelviewframe,text = "MAKEMYTRIP vs GOIBIBO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.makego)
        self.makegobutton.place(x=50,y=150)
        self.makeyabutton = Button(self.travelviewframe,text = "MAKEMYTRIP vs YATRA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command =self.makeya)
        self.makeyabutton.place(x=50,y=200)
        self.makeeasebutton = Button(self.travelviewframe,text = "MAKEMYTRIP vs EASE TRIP",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.makeease)
        self.makeeasebutton.place(x=50,y=250)
        self.maketributton = Button(self.travelviewframe,text = "MAKEMYTRIP vs TRIVAGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.maketri)
        self.maketributton.place(x=50,y=300)
        self.goyabutton = Button(self.travelviewframe,text = "GOIBIBO vs YATRA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.goya)
        self.goyabutton.place(x=260,y=150)
        self.goeasebutton = Button(self.travelviewframe,text = "GOIBIBO vs EASE TRIP",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.goease)
        self.goeasebutton.place(x=260,y=200)
        self.gotributton = Button(self.travelviewframe,text = "GOIBIBO vs TRIVAGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.gotri)
        self.gotributton.place(x=260,y=250)
        self.yaeasebutton = Button(self.travelviewframe,text = "YATRA vs EASETRIP",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.yaease)
        self.yaeasebutton.place(x=440,y=150)
        self.yatributton = Button(self.travelviewframe,text = "YATRA vs TRIVAGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.yatri)
        self.yatributton.place(x=440,y=200)
        self.easetributton = Button(self.travelviewframe,text = "EASE TRIP vs TRIVAGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.easetri)
        self.easetributton.place(x=600,y=150)
        self.backbutton = Button(self.travelviewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.back)
        self.backbutton.place(x=752, y=0)
        self.viewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place(x=260,y=120)
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df2 = pd.DataFrame(makemytripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.refund_service = pd.to_numeric(df2.refund_service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2['makeall'] = pd.to_numeric(df2.support_staff + df2.service_quality + df2.refund_service + df2.comparison + df2.overall)
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df3 = pd.DataFrame(goibibodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.refund_service = pd.to_numeric(df3.refund_service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3['goall'] = pd.to_numeric(df3.support_staff + df3.service_quality + df3.refund_service + df3.comparison + df3.overall)
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df4 = pd.DataFrame(yatradata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.refund_service = pd.to_numeric(df4.refund_service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4['yaall'] = pd.to_numeric(df4.support_staff + df4.service_quality + df4.refund_service + df4.comparison + df4.overall)
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df['triall'] = pd.to_numeric(df.support_staff + df.service_quality + df.refund_service + df.comparison + df.overall)
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df1 = pd.DataFrame(easetripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.refund_service = pd.to_numeric(df1.refund_service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1['easeall'] = pd.to_numeric(df1.support_staff + df1.service_quality + df1.refund_service + df1.comparison + df1.overall)

        #piechart
        vall = "make my trip","goibibo","yatra","ease trip","trivago"
        val=[df.triall.mean(),df1.easeall.mean(),df2.makeall.mean(),df3.goall.mean(),df4.yaall.mean()]
        plt.pie(val,labels = vall,
        autopct ='% 1.1f %%', shadow = True)
        plt.title("TRAVEL")
        plt.show()

        #bar graph
        plt.bar(["MAKE MY TRIP"],df2.makeall.mean())
        plt.bar(["GOIBIBO"],df3.goall.mean())
        plt.bar(["YATRA"],df4.yaall.mean())
        plt.bar(['EASE TRIP'],df1.easeall.mean())
        plt.bar(['TRIVAGO'],df.triall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("OVERALL TRAVEL")
        plt.show()
        makemytripconn.close()
        goibiboconn.close()
        yatraconn.close()
        easetripconn.close()
        trivagoconn.close()
        
    def makemytripview(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df = pd.DataFrame(makemytripdata,columns = ['name','support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['refund_service'],df.refund_service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("MAKE MY TRIP")
        plt.show()
        makemytripconn.close()

    def goibiboview(self):
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df = pd.DataFrame(goibibodata,columns = ['name','support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['refund_service'],df.refund_service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("GOIBIBO")
        plt.show()
        goibiboconn.close()

    def yatraview(self):
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df = pd.DataFrame(yatradata,columns = ['name','support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['refund_service'],df.refund_service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("YATRA")
        plt.show()
        yatraconn.close()

    def easetripview(self):
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df = pd.DataFrame(easetripdata,columns = ['name','support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['refund_service'],df.refund_service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("EASE TRIP")
        plt.show()
        easetripconn.close()

    def trivagoview(self):
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['name','support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['refund_service'],df.refund_service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("TRIVAGO")
        plt.show()
        trivagoconn.close()

    def makego(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df2 = pd.DataFrame(makemytripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.refund_service = pd.to_numeric(df2.refund_service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.makeall = pd.to_numeric(df2.stack())
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df3 = pd.DataFrame(goibibodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.refund_service = pd.to_numeric(df3.refund_service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.goall = pd.to_numeric(df3.stack())
        plt.bar(["MAKE MY TRIP"],df2.makeall.mean())
        plt.bar(["GOIBIBO"],df3.goall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("MAKE MY TRIP vs GOIBIBO")
        plt.show()
        makemytripconn.close()
        goibiboconn.close()

    def makeya(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df2 = pd.DataFrame(makemytripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.refund_service = pd.to_numeric(df2.refund_service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.makeall = pd.to_numeric(df2.stack())
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df4 = pd.DataFrame(yatradata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.refund_service = pd.to_numeric(df4.refund_service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.yaall = pd.to_numeric(df4.stack())
        plt.bar(["MAKE MY TRIP"],df2.makeall.mean())
        plt.bar(["YATRA"],df4.yaall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("MAKE MY TRIP vs YATRA")
        plt.show()
        makemytripconn.close()
        yatraconn.close()

    def makeease(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df2 = pd.DataFrame(makemytripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.refund_service = pd.to_numeric(df2.refund_service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.makeall = pd.to_numeric(df2.stack())
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df1 = pd.DataFrame(easetripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.refund_service = pd.to_numeric(df1.refund_service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.easeall = pd.to_numeric(df1.stack())
        plt.bar(['EASE TRIP'],df1.easeall.mean())
        plt.bar(["MAKE MY TRIP"],df2.makeall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("MAKE MY TRIP vs EASE TRIP")
        plt.show()
        makemytripconn.close()
        easetripconn.close()

    def maketri(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        makemytripdata = pd.read_sql_query("select * from makemytrip",makemytripconn)
        df2 = pd.DataFrame(makemytripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.refund_service = pd.to_numeric(df2.refund_service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.makeall = pd.to_numeric(df2.stack())
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.triall = pd.to_numeric(df.stack())
        plt.bar(["MAKE MY TRIP"],df2.makeall.mean())
        plt.bar(["TRIVAGO"],df.triall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("MAKE MY TRIP vs TRIVAGO")
        plt.show()
        makemytripconn.close()
        trivagoconn.close()

    def goya(self):
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df3 = pd.DataFrame(goibibodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.refund_service = pd.to_numeric(df3.refund_service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.goall = pd.to_numeric(df3.stack())
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df4 = pd.DataFrame(yatradata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.refund_service = pd.to_numeric(df4.refund_service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.yaall = pd.to_numeric(df4.stack())
        plt.bar(["GOIBIBO"],df3.goall.mean())
        plt.bar(["YATRA"],df4.yaall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("GOIBIBO vs YATRA")
        plt.show()
        goibiboconn.close()
        yatraconn.close()

    def goease(self):
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df3 = pd.DataFrame(goibibodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.refund_service = pd.to_numeric(df3.refund_service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.goall = pd.to_numeric(df3.stack())
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df1 = pd.DataFrame(easetripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.refund_service = pd.to_numeric(df1.refund_service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.easeall = pd.to_numeric(df1.stack())
        plt.bar(["GOIBIBO"],df3.goall.mean())
        plt.bar(['EASE TRIP'],df1.easeall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("GOIBIBO vs EASE TRIP")
        plt.show()
        goibiboconn.close()
        easetripconn.close()        

    def gotri(self):
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        goibibodata = pd.read_sql_query("select * from goibibo",goibiboconn)
        df3 = pd.DataFrame(goibibodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.refund_service = pd.to_numeric(df3.refund_service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.goall = pd.to_numeric(df3.stack())
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.triall = pd.to_numeric(df.stack())
        plt.bar(["GOIBIBO"],df3.goall.mean())
        plt.bar(['TRIVAGO'],df.triall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("GOIBIBO vs TRIVAGO")
        plt.show()
        goibiboconn.close()
        trivagoconn.close()

    def yaease(self):
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df4 = pd.DataFrame(yatradata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.refund_service = pd.to_numeric(df4.refund_service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.yaall = pd.to_numeric(df4.stack())
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df1 = pd.DataFrame(easetripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.refund_service = pd.to_numeric(df1.refund_service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.easeall = pd.to_numeric(df1.stack())
        plt.bar(["YATRA"],df4.yaall.mean())
        plt.bar(['EASE TRIP'],df1.easeall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("YATRA vs EASE TRIP")
        plt.show()
        yatraconn.close()
        easetripconn.close() 

    def yatri(self):
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        yatradata = pd.read_sql_query("select * from yatra",yatraconn)
        df4 = pd.DataFrame(yatradata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.refund_service = pd.to_numeric(df4.refund_service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.yaall = pd.to_numeric(df4.stack())
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.triall = pd.to_numeric(df.stack())
        plt.bar(["YATRA"],df4.yaall.mean())
        plt.bar(['TRIVAGO'],df.triall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("YATRA vs TRIVAGO")
        plt.show()
        yatraconn.close()
        trivagoconn.close()        

    def easetri(self):
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        trivagodata = pd.read_sql_query("select * from trivago",trivagoconn)
        df = pd.DataFrame(trivagodata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.refund_service = pd.to_numeric(df.refund_service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.triall = pd.to_numeric(df.stack())
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        easetripdata = pd.read_sql_query("select * from easetrip",easetripconn)
        df1 = pd.DataFrame(easetripdata,columns = ['support_staff','service_quality','refund_service','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.refund_service = pd.to_numeric(df1.refund_service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.easeall = pd.to_numeric(df1.stack())
        plt.bar(['EASE TRIP'],df1.easeall.mean())
        plt.bar(['TRIVAGO'],df.triall.mean())
        plt.xlabel("TRAVEL")
        plt.ylabel("REVIEW")
        plt.title("EASE TRIP vs TRIVAGO")
        plt.show()
        easetripconn.close()
        trivagoconn.close()

    def foodview(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodviewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodviewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodpandabutton = Button(self.foodviewframe,text ="FOOD PANDA",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.foodpandaview)
        self.foodpandabutton.place(x=20,y=60)
        self.zomatobutton = Button(self.foodviewframe,text ="ZOMATO",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.zomatoview)
        self.zomatobutton.place(x=200,y=60)
        self.swiggybutton = Button(self.foodviewframe,text ="SWIGGY",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.swiggyview)
        self.swiggybutton.place(x=340,y=60)
        self.freshmenubutton = Button(self.foodviewframe,text ="FRESH MENU",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.freshmenuview)
        self.freshmenubutton.place(x=470,y=60)
        self.foodmingobutton = Button(self.foodviewframe,text ="FOOD MINGO",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.foodmingoview)
        self.foodmingobutton.place(x=640,y=60)
        self.foodmatobutton = Button(self.foodviewframe,text = "FOOD PANDA vs ZOMATO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.foodmato)
        self.foodmatobutton.place(x=20,y=150)
        self.foodiggybutton = Button(self.foodviewframe,text = "FOOD PANDA vs SWIGGY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command =self.foodiggy)
        self.foodiggybutton.place(x=20,y=200)
        self.foodmenubutton = Button(self.foodviewframe,text = "FOOD PANDA vs FRESH MENU",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.foodmenu)
        self.foodmenubutton.place(x=20,y=250)
        self.foodgobutton = Button(self.foodviewframe,text = "FOOD PANDA vs FOOD MINGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.foodgo)
        self.foodgobutton.place(x=20,y=300)
        self.zoggybutton = Button(self.foodviewframe,text = "ZOMATO vs SWIGGY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.zoggy)
        self.zoggybutton.place(x=230,y=150)
        self.zomenubutton = Button(self.foodviewframe,text = "ZOMATO vs FRESH MENU",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.zomenu)
        self.zomenubutton.place(x=230,y=200)
        self.zomingobutton = Button(self.foodviewframe,text = "ZOMATO vs FOOD MINGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.zomingo)
        self.zomingobutton.place(x=230,y=250)
        self.swimenubutton = Button(self.foodviewframe,text = "SWIGGY vs FRESH MENU",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.swimenu)
        self.swimenubutton.place(x=410,y=150)
        self.swimingobutton = Button(self.foodviewframe,text = "SWIGGY vs FOOD MINGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.swimingo)
        self.swimingobutton.place(x=410,y=200)
        self.freshmingobutton = Button(self.foodviewframe,text = "FRESH MENU vs FOOD MINGO",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.freshmingo)
        self.freshmingobutton.place(x=590,y=150)
        self.backbutton = Button(self.foodviewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.back)
        self.backbutton.place(x=752, y=0)
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.travelviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.foodviewframe.place(x=260,y=120)
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df['foodall'] = pd.to_numeric(df.support_staff + df.service_quality + df.food_quality + df.comparison + df.overall)
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df1 = pd.DataFrame(zomatodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.food_quality= pd.to_numeric(df1.food_quality)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1['zoall'] = pd.to_numeric(df1.support_staff + df1.service_quality + df1.food_quality + df1.comparison + df1.overall)
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df2 = pd.DataFrame(swiggydata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.food_quality= pd.to_numeric(df2.food_quality)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2['swiall'] = pd.to_numeric(df2.support_staff + df2.service_quality + df2.food_quality + df2.comparison + df2.overall)
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df3 = pd.DataFrame(freshmenudata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.food_quality= pd.to_numeric(df3.food_quality)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3['freshall'] = pd.to_numeric(df3.support_staff + df3.service_quality + df3.food_quality + df3.comparison + df3.overall)
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df4 = pd.DataFrame(foodmingodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.food_quality= pd.to_numeric(df4.food_quality)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4['mingoall'] = pd.to_numeric(df4.support_staff + df4.service_quality + df4.food_quality + df4.comparison + df4.overall)
        val1 = "food panda","zomato","swiggy","food mingo","fresh menu"
        val = [df.foodall.mean(),df1.zoall.mean(),df2.swiall.mean(),df4.mingoall.mean(),df3.freshall.mean()]
        plt.pie(val,labels = val1,
        autopct ='% 1.1f %%', shadow = True)
        plt.title("FOOD")
        plt.show()
        plt.bar(['food panda'],df.foodall.mean())
        plt.bar(["zomato"],df1.zoall.mean())
        plt.bar(["swiggy"],df2.swiall.mean())
        plt.bar(["food mingo"],df4.mingoall.mean())
        plt.bar(["fresh menu"],df3.freshall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD")
        plt.show()
        
    def foodpandaview(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['name','support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['food_quality'],df.food_quality.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD PANDA")
        plt.show()
        foodpandaconn.close()

    def zomatoview(self):
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df = pd.DataFrame(zomatodata,columns = ['name','support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['food_quality'],df.food_quality.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("ZOMATO")
        plt.show()
        zomatoconn.close()

    def swiggyview(self):
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df = pd.DataFrame(swiggydata,columns = ['name','support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['food_quality'],df.food_quality.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SWIGGY")
        plt.show()
        swiggyconn.close()

    def freshmenuview(self):
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df = pd.DataFrame(freshmenudata,columns = ['name','support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['food_quality'],df.food_quality.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FRESH MENU")
        plt.show()
        freshmenuconn.close()
                
    def foodmingoview(self):
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df = pd.DataFrame(foodmingodata,columns = ['name','support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['support_staff'],df.support_staff.mean())
        plt.bar(['service_quality'],df.service_quality.mean())
        plt.bar(['food_quality'],df.food_quality.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD MINGO")
        plt.show()
        foodmingoconn.close()

    def foodmato(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.foodall = pd.to_numeric(df.stack())
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df1 = pd.DataFrame(zomatodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.food_quality= pd.to_numeric(df1.food_quality)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.zoall = pd.to_numeric(df1.stack())
        plt.bar(['food panda'],df.foodall.mean())
        plt.bar(["zomato"],df1.zoall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD PANDA vs ZOMATO")
        plt.show()
        zomatoconn.close()
        foodpandaconn.close()

    def foodiggy(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.foodall = pd.to_numeric(df.stack())
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df2 = pd.DataFrame(swiggydata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.food_quality= pd.to_numeric(df2.food_quality)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.swiall = pd.to_numeric(df2.stack())
        plt.bar(['food panda'],df.foodall.mean())
        plt.bar(["swiggy"],df2.swiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD PANDA vs SWIGGY")
        plt.show()
        swiggyconn.close()
        foodpandaconn.close()

    def foodmenu(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.foodall = pd.to_numeric(df.stack())
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df3 = pd.DataFrame(freshmenudata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.food_quality= pd.to_numeric(df3.food_quality)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.freshall = pd.to_numeric(df3.stack())
        plt.bar(['food panda'],df.foodall.mean())
        plt.bar(["fresh menu"],df3.freshall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD PANDA vs FRESH MENU")
        plt.show()
        freshmenuconn.close()
        foodpandaconn.close()

    def foodgo(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        foodpandadata = pd.read_sql_query("select * from foodpanda",foodpandaconn)
        df = pd.DataFrame(foodpandadata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df.support_staff = pd.to_numeric(df.support_staff)
        df.service_quality = pd.to_numeric(df.service_quality)
        df.food_quality= pd.to_numeric(df.food_quality)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.foodall = pd.to_numeric(df.stack())
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df4 = pd.DataFrame(foodmingodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.food_quality= pd.to_numeric(df4.food_quality)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.mingoall = pd.to_numeric(df4.stack())
        plt.bar(['food panda'],df.foodall.mean())
        plt.bar(["food mingo"],df4.mingoall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FOOD PANDA vs FOOD MINGO")
        plt.show()
        foodmingoconn.close()
        foodpandaconn.close()

    def zoggy(self):
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df1 = pd.DataFrame(zomatodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.food_quality= pd.to_numeric(df1.food_quality)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.zoall = pd.to_numeric(df1.stack())
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df2 = pd.DataFrame(swiggydata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.food_quality= pd.to_numeric(df2.food_quality)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.swiall = pd.to_numeric(df2.stack())
        plt.bar(["zomato"],df1.zoall.mean())
        plt.bar(["swiggy"],df2.swiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("ZOMATO vs SWIGGY")
        plt.show()
        swiggyconn.close()
        zomatoconn.close()

    def zomenu(self):
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df1 = pd.DataFrame(zomatodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.food_quality= pd.to_numeric(df1.food_quality)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.zoall = pd.to_numeric(df1.stack())
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df3 = pd.DataFrame(freshmenudata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.food_quality= pd.to_numeric(df3.food_quality)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.freshall = pd.to_numeric(df3.stack())
        plt.bar(["zomato"],df1.zoall.mean())
        plt.bar(["fresh menu"],df3.freshall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("ZOMATO vs FRESH MENU")
        plt.show()
        freshmenuconn.close()
        zomatoconn.close()

    def zomingo(self):
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        zomatodata = pd.read_sql_query("select * from zomato",zomatoconn)
        df1 = pd.DataFrame(zomatodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df1.support_staff = pd.to_numeric(df1.support_staff)
        df1.service_quality = pd.to_numeric(df1.service_quality)
        df1.food_quality= pd.to_numeric(df1.food_quality)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.zoall = pd.to_numeric(df1.stack())
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df4 = pd.DataFrame(foodmingodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.food_quality= pd.to_numeric(df4.food_quality)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.mingoall = pd.to_numeric(df4.stack())
        plt.bar(["food mingo"],df4.mingoall.mean())
        plt.bar(["zomato"],df1.zoall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("ZOMATO vs FOOD MINGO")
        plt.show()
        foodmingoconn.close()
        zomatoconn.close()

    def swimenu(self):
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df2 = pd.DataFrame(swiggydata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.food_quality= pd.to_numeric(df2.food_quality)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.swiall = pd.to_numeric(df2.stack())
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df3 = pd.DataFrame(freshmenudata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.food_quality= pd.to_numeric(df3.food_quality)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.freshall = pd.to_numeric(df3.stack())
        plt.bar(["swiggy"],df2.swiall.mean())
        plt.bar(["fresh menu"],df3.freshall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SWIGGY vs FRESH MENU")
        plt.show()
        freshmenuconn.close()
        swiggyconn.close()

    def swimingo(self):
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        swiggydata = pd.read_sql_query("select * from swiggy",swiggyconn)
        df2 = pd.DataFrame(swiggydata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df2.support_staff = pd.to_numeric(df2.support_staff)
        df2.service_quality = pd.to_numeric(df2.service_quality)
        df2.food_quality= pd.to_numeric(df2.food_quality)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.swiall = pd.to_numeric(df2.stack())
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df4 = pd.DataFrame(foodmingodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.food_quality= pd.to_numeric(df4.food_quality)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.mingoall = pd.to_numeric(df4.stack())
        plt.bar(["food mingo"],df4.mingoall.mean())
        plt.bar(["swiggy"],df2.swiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SWIGGY vs FOOD MINGO")
        plt.show()
        foodmingoconn.close()
        swiggyconn.close()

    def freshmingo(self):
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        freshmenudata = pd.read_sql_query("select * from freshmenu",freshmenuconn)
        df3 = pd.DataFrame(freshmenudata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df3.support_staff = pd.to_numeric(df3.support_staff)
        df3.service_quality = pd.to_numeric(df3.service_quality)
        df3.food_quality= pd.to_numeric(df3.food_quality)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.freshall = pd.to_numeric(df3.stack())
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        foodmingodata = pd.read_sql_query("select * from foodmingo",foodmingoconn)
        df4 = pd.DataFrame(foodmingodata,columns = ['support_staff','service_quality','food_quality','comparison','overall'])
        df4.support_staff = pd.to_numeric(df4.support_staff)
        df4.service_quality = pd.to_numeric(df4.service_quality)
        df4.food_quality= pd.to_numeric(df4.food_quality)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.mingoall = pd.to_numeric(df4.stack())
        plt.bar(["food mingo"],df4.mingoall.mean())
        plt.bar(["fresh menu"],df3.freshall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FRESH MENU vs FOOD MINGO")
        plt.show()
        foodmingoconn.close()
        freshmenuconn.close()

    def educationview(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.educationviewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.educationviewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.khanacademybutton = Button(self.educationviewframe,text ="KHAN ACADEMY",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.khanacademyview)
        self.khanacademybutton.place(x=20,y=60)
        self.courserabutton = Button(self.educationviewframe,text ="COURSERA",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.courseraview)
        self.courserabutton.place(x=210,y=60)
        self.w3schoolbutton = Button(self.educationviewframe,text ="W3SCHOOL",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.w3schoolview)
        self.w3schoolbutton.place(x=360,y=60)
        self.byjusbutton = Button(self.educationviewframe,text ="BYJU'S",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.byjusview)
        self.byjusbutton.place(x=510,y=60)
        self.codeacademybutton = Button(self.educationviewframe,text ="CODE ACADEMY",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.codeacademyview)
        self.codeacademybutton.place(x=620,y=60)
        self.khanrabutton = Button(self.educationviewframe,text = "KHAN ACADEMY vs COURSERA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.khanra)
        self.khanrabutton.place(x=20,y=150)
        self.khanw3button = Button(self.educationviewframe,text = "KHAN ACADEMY vs W3SCHOOL",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command =self.khanw3)
        self.khanw3button.place(x=20,y=200)
        self.khanjusbutton = Button(self.educationviewframe,text = "KHAN ACADEMY vs BYJU'S",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.khanjus)
        self.khanjusbutton.place(x=20,y=250)
        self.khancodebutton = Button(self.educationviewframe,text = "KHAN ACADEMY vs CODE ACADEMY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.khancode)
        self.khancodebutton.place(x=20,y=300)
        self.cow3button = Button(self.educationviewframe,text = "COURSERA vs W3SCHOOL",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.cow3)
        self.cow3button.place(x=245,y=150)
        self.cojusbutton = Button(self.educationviewframe,text = "COURSERA vs BYJU'S",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.cojus)
        self.cojusbutton.place(x=245,y=200)
        self.cocodebutton = Button(self.educationviewframe,text = "COURSERA vs CODE ACADEMY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.cocode)
        self.cocodebutton.place(x=245,y=250)
        self.w3jusbutton = Button(self.educationviewframe,text = "W3SCHOOL vs BYJU'S",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.w3jus)
        self.w3jusbutton.place(x=430,y=150)
        self.w3codebutton = Button(self.educationviewframe,text = "W3SCHOOL vs CODE ACADEMY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.w3code)
        self.w3codebutton.place(x=430,y=200)
        self.bycodebutton = Button(self.educationviewframe,text = "BYJU'S vs CODE ACADEMY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.bycode)
        self.bycodebutton.place(x=600,y=150)
        self.backbutton = Button(self.educationviewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.back)
        self.backbutton.place(x=752, y=0)
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.educationviewframe.place(x=260,y=120)
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        df = pd.DataFrame(khanacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df['khanall'] = pd.to_numeric(df.teaching + df.userfriendly + df.service + df.comparison + df.overall)
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        df1 = pd.DataFrame(courseradata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df1.teaching = pd.to_numeric(df1.teaching)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.service= pd.to_numeric(df1.service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1['coall'] = pd.to_numeric(df1.teaching + df1.userfriendly + df1.service + df1.comparison + df1.overall)
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        df2 = pd.DataFrame(w3schooldata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df2.teaching = pd.to_numeric(df2.teaching)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.service= pd.to_numeric(df2.service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2['w3all'] = pd.to_numeric(df2.teaching + df2.userfriendly + df2.service + df2.comparison + df2.overall)
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        df3 = pd.DataFrame(byjusdata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df3.teaching = pd.to_numeric(df3.teaching)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.service= pd.to_numeric(df3.service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3['byall'] = pd.to_numeric(df3.teaching + df3.userfriendly + df3.service + df3.comparison + df3.overall)
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        df4 = pd.DataFrame(codeacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df4.teaching = pd.to_numeric(df4.teaching)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.service= pd.to_numeric(df4.service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4['codeall'] = pd.to_numeric(df4.teaching + df4.userfriendly + df4.service + df4.comparison + df4.overall)
        val1 = "khan academy","coursera","w3school","byju's","code academy"
        val = [df.khanall.mean(),df1.coall.mean(),df2.w3all.mean(),df3.byall.mean(),df4.codeall.mean()]
        plt.pie(val,labels = val1,
        autopct ='% 1.1f %%', shadow = True)
        plt.title("EDUCATION")
        plt.show()        
        plt.bar(["khan academy"],df.khanall.mean())
        plt.bar(["coursera"],df1.coall.mean())
        plt.bar(["w3school"],df2.w3all.mean())
        plt.bar(["byju's"],df3.byall.mean())
        plt.bar(["code academy"],df4.codeall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("EDUCATION")
        plt.show()
        khanacademyconn.close()
        courseraconn.close()        
        w3schoolconn.close()
        byjusconn.close()
        codeacademyconn.close()
        
    def khanacademyview(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        df = pd.DataFrame(khanacademydata,columns = ['name','teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['teaching'],df.teaching.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['service'],df.service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("KHAN ACADEMY")
        plt.show()
        khanacademyconn.close()

    def courseraview(self):
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        df = pd.DataFrame(courseradata,columns = ['name','teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['teaching'],df.teaching.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['service'],df.service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("COURSERA")
        plt.show()
        courseraconn.close()

    def w3schoolview(self):
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        df = pd.DataFrame(w3schooldata,columns = ['name','teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['teaching'],df.teaching.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['service'],df.service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("W3SCHOOL")
        plt.show()
        w3schoolconn.close()

    def byjusview(self):
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        df = pd.DataFrame(byjusdata,columns = ['name','teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['teaching'],df.teaching.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['service'],df.service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("BYJU'S")
        plt.show()
        byjusconn.close()

    def codeacademyview(self):
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        df = pd.DataFrame(codeacademydata,columns = ['name','teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['teaching'],df.teaching.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['service'],df.service.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("CODE ACADEMY")
        plt.show()
        codeacademyconn.close()

    def khanra(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        print(khanacademydata)
        df = pd.DataFrame(khanacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.khanall = pd.to_numeric(df.stack())
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        print(courseradata)
        df1 = pd.DataFrame(courseradata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df1.teaching = pd.to_numeric(df1.teaching)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.service= pd.to_numeric(df1.service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.coall = pd.to_numeric(df1.stack())
        plt.bar(["khan academy"],df.khanall.mean())
        plt.bar(["coursera"],df1.coall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("KHAN ACADEMY vs COURSERA")
        plt.show()
        khanacademyconn.close()
        courseraconn.close()        

    def khanw3(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        print(khanacademydata)
        df = pd.DataFrame(khanacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.khanall = pd.to_numeric(df.stack())
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        print(w3schooldata)
        df2 = pd.DataFrame(w3schooldata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df2.teaching = pd.to_numeric(df2.teaching)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.service= pd.to_numeric(df2.service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.w3all = pd.to_numeric(df2.stack())
        plt.bar(["khan academy"],df.khanall.mean())
        plt.bar(["w3school"],df2.w3all.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("KHAN ACADEMY vs W3SCHOOL")
        plt.show()
        khanacademyconn.close()    
        w3schoolconn.close()

    def khanjus(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        print(khanacademydata)
        df = pd.DataFrame(khanacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.khanall = pd.to_numeric(df.stack())
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        print(byjusdata)
        df3 = pd.DataFrame(byjusdata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df3.teaching = pd.to_numeric(df3.teaching)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.service= pd.to_numeric(df3.service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.byall = pd.to_numeric(df3.stack())
        plt.bar(["khan academy"],df.khanall.mean())
        plt.bar(["byju's"],df3.byall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("KHAN ACADEMY vs BYJU'S")
        plt.show()
        khanacademyconn.close()
        byjusconn.close()

    def khancode(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        khanacademydata = pd.read_sql_query("select * from khanacademy",khanacademyconn)
        print(khanacademydata)
        df = pd.DataFrame(khanacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df.teaching = pd.to_numeric(df.teaching)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.service= pd.to_numeric(df.service)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.khanall = pd.to_numeric(df.stack())
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        print(codeacademydata)
        df4 = pd.DataFrame(codeacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df4.teaching = pd.to_numeric(df4.teaching)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.service= pd.to_numeric(df4.service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.codeall = pd.to_numeric(df4.stack())
        plt.bar(["khan academy"],df.khanall.mean())
        plt.bar(["code academy"],df4.codeall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("KHAN ACADEMY vs CODE ACADEMY")
        plt.show()
        khanacademyconn.close()
        codeacademyconn.close()

    def cow3(self):
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        print(courseradata)
        df1 = pd.DataFrame(courseradata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df1.teaching = pd.to_numeric(df1.teaching)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.service= pd.to_numeric(df1.service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.coall = pd.to_numeric(df1.stack())
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        print(w3schooldata)
        df2 = pd.DataFrame(w3schooldata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df2.teaching = pd.to_numeric(df2.teaching)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.service= pd.to_numeric(df2.service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.w3all = pd.to_numeric(df2.stack())
        plt.bar(["coursera"],df1.coall.mean())
        plt.bar(["w3school"],df2.w3all.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("COURSERA vs W3SCHOOL")
        plt.show()
        courseraconn.close()        
        w3schoolconn.close()
        
    def cojus(self):
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        print(courseradata)
        df1 = pd.DataFrame(courseradata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df1.teaching = pd.to_numeric(df1.teaching)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.service= pd.to_numeric(df1.service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.coall = pd.to_numeric(df1.stack())
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        print(byjusdata)
        df3 = pd.DataFrame(byjusdata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df3.teaching = pd.to_numeric(df3.teaching)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.service= pd.to_numeric(df3.service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.byall = pd.to_numeric(df3.stack())
        plt.bar(["coursera"],df1.coall.mean())
        plt.bar(["byju's"],df3.byall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("COURSERA vs BYJU'S")
        plt.show()
        courseraconn.close()        
        byjusconn.close()

    def cocode(self):
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        courseradata = pd.read_sql_query("select * from coursera",courseraconn)
        print(courseradata)
        df1 = pd.DataFrame(courseradata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df1.teaching = pd.to_numeric(df1.teaching)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.service= pd.to_numeric(df1.service)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.coall = pd.to_numeric(df1.stack())
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        print(codeacademydata)
        df4 = pd.DataFrame(codeacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df4.teaching = pd.to_numeric(df4.teaching)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.service= pd.to_numeric(df4.service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.codeall = pd.to_numeric(df4.stack())
        plt.bar(["coursera"],df1.coall.mean())
        plt.bar(["code academy"],df4.codeall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("COURSERA vs CODE ACADEMY")
        plt.show()
        courseraconn.close()        
        codeacademyconn.close()

    def w3jus(self):
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        print(w3schooldata)
        df2 = pd.DataFrame(w3schooldata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df2.teaching = pd.to_numeric(df2.teaching)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.service= pd.to_numeric(df2.service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.w3all = pd.to_numeric(df2.stack())
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        print(byjusdata)
        df3 = pd.DataFrame(byjusdata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df3.teaching = pd.to_numeric(df3.teaching)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.service= pd.to_numeric(df3.service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.byall = pd.to_numeric(df3.stack())
        plt.bar(["w3school"],df2.w3all.mean())
        plt.bar(["byju's"],df3.byall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("W3SCHOOL vs BYJU'S")
        plt.show()    
        w3schoolconn.close()
        byjusconn.close()

    def w3code(self):
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        w3schooldata = pd.read_sql_query("select * from w3school",w3schoolconn)
        print(w3schooldata)
        df2 = pd.DataFrame(w3schooldata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df2.teaching = pd.to_numeric(df2.teaching)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.service= pd.to_numeric(df2.service)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.w3all = pd.to_numeric(df2.stack())
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        print(codeacademydata)
        df4 = pd.DataFrame(codeacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df4.teaching = pd.to_numeric(df4.teaching)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.service= pd.to_numeric(df4.service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.codeall = pd.to_numeric(df4.stack())
        plt.bar(["w3school"],df2.w3all.mean())
        plt.bar(["code academy"],df4.codeall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("W3SCHOOL vs CODE ACADEMY")
        plt.show()     
        w3schoolconn.close()
        codeacademyconn.close()

    def bycode(self):
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        byjusdata = pd.read_sql_query("select * from byjus",byjusconn)
        print(byjusdata)
        df3 = pd.DataFrame(byjusdata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df3.teaching = pd.to_numeric(df3.teaching)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.service= pd.to_numeric(df3.service)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.byall = pd.to_numeric(df3.stack())
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        codeacademydata = pd.read_sql_query("select * from codeacademy",codeacademyconn)
        print(codeacademydata)
        df4 = pd.DataFrame(codeacademydata,columns = ['teaching','userfriendly','service','comparison','overall'])
        df4.teaching = pd.to_numeric(df4.teaching)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.service= pd.to_numeric(df4.service)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.codeall = pd.to_numeric(df4.stack())
        plt.bar(["byju's"],df3.byall.mean())
        plt.bar(["code academy"],df4.codeall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("BYJU'S vs CODE ACADEMY")
        plt.show()
        byjusconn.close()
        codeacademyconn.close()

    def shoppingview(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.shoppingviewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.shoppingviewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.amazonbutton = Button(self.shoppingviewframe,text ="AMAZON",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.amazonview)
        self.amazonbutton.place(x=35,y=60)
        self.flipkartbutton = Button(self.shoppingviewframe,text ="FLIPKART",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.flipkartview)
        self.flipkartbutton.place(x=200,y=60)
        self.ebaybutton = Button(self.shoppingviewframe,text ="EBAY",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.ebayview)
        self.ebaybutton.place(x=360,y=60)
        self.walmartbutton = Button(self.shoppingviewframe,text ="WALMART",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.walmartview)
        self.walmartbutton.place(x=470,y=60)
        self.alibababutton = Button(self.shoppingviewframe,text ="ALI BABA",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.alibabaview)
        self.alibababutton.place(x=650,y=60)
        self.amakartbutton = Button(self.shoppingviewframe,text = "AMAZON vs FLIPKART",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.amakart)
        self.amakartbutton.place(x=50,y=150)
        self.amabaybutton = Button(self.shoppingviewframe,text = "AMAZON  vs EBAY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command =self.amabay)
        self.amabaybutton.place(x=50,y=200)
        self.amartbutton = Button(self.shoppingviewframe,text = "AMAZON  vs WALMART",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.amart)
        self.amartbutton.place(x=50,y=250)
        self.amababutton = Button(self.shoppingviewframe,text = "AMAZON  vs ALIBABA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.amaba)
        self.amababutton.place(x=50,y=300)
        self.flibaybutton = Button(self.shoppingviewframe,text = "FLIPKART vs EBAY",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.flibay)
        self.flibaybutton.place(x=250,y=150)
        self.fliartbutton = Button(self.shoppingviewframe,text = "FLIPKART vs WALMART",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.fliart)
        self.fliartbutton.place(x=250,y=200)
        self.flibabutton = Button(self.shoppingviewframe,text = "FLIPKART vs ALIBABA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.fliba)
        self.flibabutton.place(x=250,y=250)
        self.emartbutton = Button(self.shoppingviewframe,text = "EBAY vs WALMART",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.emart)
        self.emartbutton.place(x=440,y=150)
        self.ebababutton = Button(self.shoppingviewframe,text = "EBAY vs ALIBABA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.ebaba)
        self.ebababutton.place(x=440,y=200)
        self.wababutton = Button(self.shoppingviewframe,text = "WALMART vs ALIBABA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.waba)
        self.wababutton.place(x=600,y=150)
        self.backbutton = Button(self.shoppingviewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.back)
        self.backbutton.place(x=752, y=0)
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.travelviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.shoppingviewframe.place(x=260,y=120)
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        df = pd.DataFrame(amazondata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df['amaall'] = pd.to_numeric(df.service + df.userfriendly + df.customer_care + df.comparison + df.overall)
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        df1 = pd.DataFrame(flipkartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df1.service = pd.to_numeric(df1.service)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1['fliall'] = pd.to_numeric(df1.service + df1.userfriendly + df1.customer_care + df1.comparison + df1.overall)
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        df2 = pd.DataFrame(ebaydata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df2.service = pd.to_numeric(df2.service)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2['ebayall'] = pd.to_numeric(df2.service + df2.userfriendly + df2.customer_care + df2.comparison + df2.overall)
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        df3 = pd.DataFrame(walmartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df3.service = pd.to_numeric(df3.service)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3['walall'] = pd.to_numeric(df3.service + df3.userfriendly + df3.customer_care + df3.comparison + df3.overall)
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        df4 = pd.DataFrame(alibabadata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df4.service = pd.to_numeric(df4.service)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4['aliall'] = pd.to_numeric(df4.service + df4.userfriendly + df4.customer_care + df4.comparison + df4.overall)
        val1 = "amazon","flipkart","ebay","walmart","alibaba"
        val = [df.amaall.mean(),df1.fliall.mean(),df2.ebayall.mean(),df3.walall.mean(),df4.aliall.mean()]
        plt.pie(val,labels = val1,
        autopct ='% 1.1f %%', shadow = True)
        plt.title("SHOPPING")
        plt.show()        
        plt.bar(["amazon"],df.amaall.mean())
        plt.bar(["flipkart"],df1.fliall.mean())
        plt.bar(["ebay"],df2.ebayall.mean())
        plt.bar(["walmart"],df3.walall.mean())
        plt.bar(["alibaba"],df4.aliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SHOPPING")
        plt.show()
        amazonconn.close()
        flipkartconn.close()
        ebayconn.close()
        walmartconn.close()
        alibabaconn.close()
        
    def amazonview(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        df = pd.DataFrame(amazondata,columns = ['name','service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['service'],df.service.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("AMAZON")
        plt.show()
        amazonconn.close()

    def flipkartview(self):
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        df = pd.DataFrame(flipkartdata,columns = ['name','service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['service'],df.service.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FLIPKART")
        plt.show()
        flipkartconn.close()
        
    def ebayview(self):
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        df = pd.DataFrame(ebaydata,columns = ['name','service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['service'],df.service.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("EBAY")
        plt.show()
        ebayconn.close()

    def walmartview(self):
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        df = pd.DataFrame(walmartdata,columns = ['name','service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['service'],df.service.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("WALMART")
        plt.show()
        walmartconn.close()

    def alibabaview(self):
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        df = pd.DataFrame(alibabadata,columns = ['name','service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['service'],df.service.mean())
        plt.bar(['userfriendly'],df.userfriendly.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("ALIBABA")
        plt.show()
        alibabaconn.close()

    def amakart(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        df = pd.DataFrame(amazondata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.amaall = pd.to_numeric(df.stack())
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        df1 = pd.DataFrame(flipkartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df1.service = pd.to_numeric(df1.service)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.fliall = pd.to_numeric(df1.stack())
        plt.bar(["amazon"],df.amaall.mean())
        plt.bar(["flipkart"],df1.fliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("AMAZON vs FLIPKART")
        plt.show()
        amazonconn.close()
        flipkartconn.close()
        
    def amabay(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        df = pd.DataFrame(amazondata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.amaall = pd.to_numeric(df.stack())
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        df2 = pd.DataFrame(ebaydata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df2.service = pd.to_numeric(df2.service)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.ebayall = pd.to_numeric(df2.stack())
        plt.bar(["amazon"],df.amaall.mean())
        plt.bar(["ebay"],df2.ebayall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("AMAZON vs EBAY")
        plt.show()
        amazonconn.close()
        ebayconn.close()

    def amart(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        print(amazondata)
        df = pd.DataFrame(amazondata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.amaall = pd.to_numeric(df.stack())
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        print(walmartdata)
        df3 = pd.DataFrame(walmartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df3.service = pd.to_numeric(df3.service)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.walall = pd.to_numeric(df3.stack())
        plt.bar(["amazon"],df.amaall.mean())
        plt.bar(["walmart"],df3.walall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("AMAZON vs WALMART")
        plt.show()
        amazonconn.close()
        walmartconn.close()

    def amaba(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        amazondata = pd.read_sql_query("select * from amazon",amazonconn)
        print(amazondata)
        df = pd.DataFrame(amazondata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df.service = pd.to_numeric(df.service)
        df.userfriendly = pd.to_numeric(df.userfriendly)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.amaall = pd.to_numeric(df.stack())
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        print(alibabadata)
        df4 = pd.DataFrame(alibabadata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df4.service = pd.to_numeric(df4.service)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.aliall = pd.to_numeric(df4.stack())
        plt.bar(["amazon"],df.amaall.mean())
        plt.bar(["alibabab"],df4.aliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("AMAZON vs ALIBABA")
        plt.show()
        amazonconn.close()
        alibabaconn.close()

    def flibay(self):
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        print(flipkartdata)
        df1 = pd.DataFrame(flipkartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df1.service = pd.to_numeric(df1.service)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.fliall = pd.to_numeric(df1.stack())
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        print(ebaydata)
        df2 = pd.DataFrame(ebaydata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df2.service = pd.to_numeric(df2.service)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.ebayall = pd.to_numeric(df2.stack())
        plt.bar(["flipkart"],df1.fliall.mean())
        plt.bar(["ebay"],df2.ebayall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FLIPKART vs EBAY")
        plt.show()
        flipkartconn.close()
        ebayconn.close()

    def fliart(self):
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        print(flipkartdata)
        df1 = pd.DataFrame(flipkartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df1.service = pd.to_numeric(df1.service)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.fliall = pd.to_numeric(df1.stack())
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        print(walmartdata)
        df3 = pd.DataFrame(walmartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df3.service = pd.to_numeric(df3.service)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.walall = pd.to_numeric(df3.stack())
        plt.bar(["flipkart"],df1.fliall.mean())
        plt.bar(["walmart"],df3.walall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FLIPKART vs WALMART")
        plt.show()
        flipkartconn.close()
        walmartconn.close()

    def fliba(self):
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        flipkartdata = pd.read_sql_query("select * from flipkart",flipkartconn)
        print(flipkartdata)
        df1 = pd.DataFrame(flipkartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df1.service = pd.to_numeric(df1.service)
        df1.userfriendly = pd.to_numeric(df1.userfriendly)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.fliall = pd.to_numeric(df1.stack())
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        print(alibabadata)
        df4 = pd.DataFrame(alibabadata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df4.service = pd.to_numeric(df4.service)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.aliall = pd.to_numeric(df4.stack())
        plt.bar(["flipkart"],df1.fliall.mean())
        plt.bar(["alibabab"],df4.aliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("FLIPKART vs ALIBABA")
        plt.show()
        flipkartconn.close()
        alibabaconn.close()

    def emart(self):
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        print(ebaydata)
        df2 = pd.DataFrame(ebaydata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df2.service = pd.to_numeric(df2.service)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.ebayall = pd.to_numeric(df2.stack())
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        print(walmartdata)
        df3 = pd.DataFrame(walmartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df3.service = pd.to_numeric(df3.service)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.walall = pd.to_numeric(df3.stack())
        plt.bar(["ebay"],df2.ebayall.mean())
        plt.bar(["walmart"],df3.walall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("EBAY vs WALMART")
        plt.show()
        ebayconn.close()
        walmartconn.close()

    def ebaba(self):
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        ebaydata = pd.read_sql_query("select * from ebay",ebayconn)
        print(ebaydata)
        df2 = pd.DataFrame(ebaydata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df2.service = pd.to_numeric(df2.service)
        df2.userfriendly = pd.to_numeric(df2.userfriendly)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.ebayall = pd.to_numeric(df2.stack())
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        print(alibabadata)
        df4 = pd.DataFrame(alibabadata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df4.service = pd.to_numeric(df4.service)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.aliall = pd.to_numeric(df4.stack())
        plt.bar(["ebay"],df2.ebayall.mean())
        plt.bar(["alibabab"],df4.aliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("EBAY vs ALIBABA")
        plt.show()
        ebayconn.close()
        alibabaconn.close()

    def waba(self):
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        walmartdata = pd.read_sql_query("select * from walmart",walmartconn)
        print(walmartdata)
        df3 = pd.DataFrame(walmartdata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df3.service = pd.to_numeric(df3.service)
        df3.userfriendly = pd.to_numeric(df3.userfriendly)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.walall = pd.to_numeric(df3.stack())
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        alibabadata = pd.read_sql_query("select * from alibaba",alibabaconn)
        print(alibabadata)
        df4 = pd.DataFrame(alibabadata,columns = ['service','userfriendly','customer_care','comparison','overall'])
        df4.service = pd.to_numeric(df4.service)
        df4.userfriendly = pd.to_numeric(df4.userfriendly)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.aliall = pd.to_numeric(df4.stack())
        plt.bar(["walmart"],df3.walall.mean())
        plt.bar(["alibabab"],df4.aliall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("WALMART vs ALIBABA")
        plt.show()
        walmartconn.close()
        alibabaconn.close()

    def cabview(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.cabviewframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.cabviewframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.uberbutton = Button(self.cabviewframe,text ="UBER",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.uberview)
        self.uberbutton.place(x=35,y=60)
        self.olabutton = Button(self.cabviewframe,text ="OLA",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.olaview)
        self.olabutton.place(x=170,y=60)
        self.merubutton = Button(self.cabviewframe,text ="MERU",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.meruview)
        self.merubutton.place(x=290,y=60)
        self.savaaributton = Button(self.cabviewframe,text ="SAVAARI",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.savaariview)
        self.savaaributton.place(x=420,y=60)
        self.bharattaxibutton = Button(self.cabviewframe,text ="BHARAT TAXI",font=("Comic Sans Ms",15),bg="#efefef",fg="green",bd=5,relief = RIDGE,command = self.bharattaxiview)
        self.bharattaxibutton.place(x=600,y=60)
        self.uolabutton = Button(self.cabviewframe,text = "UBER vs OLA",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.uola)
        self.uolabutton.place(x=50,y=150)
        self.umerubutton = Button(self.cabviewframe,text = "UBER  vs MERU",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command =self.umeru)
        self.umerubutton.place(x=50,y=200)
        self.uvaaributton = Button(self.cabviewframe,text = "UBER  vs SAVAARI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.uvaari)
        self.uvaaributton.place(x=50,y=250)
        self.utaxibutton = Button(self.cabviewframe,text = "UBER  vs BHARAT TAXI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.utaxi)
        self.utaxibutton.place(x=50,y=300)
        self.olamerubutton = Button(self.cabviewframe,text = "OLA vs MERU",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.olameru)
        self.olamerubutton.place(x=220,y=150)
        self.olavaaributton = Button(self.cabviewframe,text = "OLA vs SAVAARI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.olavaari)
        self.olavaaributton.place(x=220,y=200)
        self.olataxibutton = Button(self.cabviewframe,text = "OLA vs BHARAT TAXI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.olataxi)
        self.olataxibutton.place(x=220,y=250)
        self.mevaaributton = Button(self.cabviewframe,text = "MERU vs SAVAARI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.mevaari)
        self.mevaaributton.place(x=400,y=150)
        self.metaxibutton = Button(self.cabviewframe,text = "MERU vs BHARAT TAXI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.metaxi)
        self.metaxibutton.place(x=400,y=200)
        self.sataxibutton = Button(self.cabviewframe,text = "SAVAARI vs BHARAT TAXI",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg="green",relief=RIDGE,command = self.sataxi)
        self.sataxibutton.place(x=600,y=150)
        self.backbutton = Button(self.cabviewframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.back)
        self.backbutton.place(x=752, y=0)
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.travelviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.cabviewframe.place(x=260,y=120)
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        df = pd.DataFrame(uberdata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df['uberall'] = pd.to_numeric(df.convenient + df.drivers + df.customer_care + df.comparison + df.overall)
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        df1 = pd.DataFrame(oladata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df1.convenient = pd.to_numeric(df1.convenient)
        df1.drivers = pd.to_numeric(df1.drivers)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1['olaall'] = pd.to_numeric(df1.convenient + df1.drivers + df1.customer_care + df1.comparison + df1.overall)
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        df2 = pd.DataFrame(merudata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df2.convenient = pd.to_numeric(df2.convenient)
        df2.drivers = pd.to_numeric(df2.drivers)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2['meruall'] = pd.to_numeric(df2.convenient + df2.drivers + df2.customer_care + df2.comparison + df2.overall)
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        df3 = pd.DataFrame(savaaridata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df3.convenient = pd.to_numeric(df3.convenient)
        df3.drivers = pd.to_numeric(df3.drivers)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3['vaariall'] = pd.to_numeric(df3.convenient + df3.drivers + df3.customer_care + df3.comparison + df3.overall)
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        df4 = pd.DataFrame(bharattaxidata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df4.convenient = pd.to_numeric(df4.convenient)
        df4.drivers = pd.to_numeric(df4.drivers)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4['taxiall'] = pd.to_numeric(df4.convenient + df4.drivers + df4.customer_care + df4.comparison + df4.overall)
        val1 = "uber","ola","meru","savaari","bharattaxi"
        val = [df.uberall.mean(),df1.olaall.mean(),df2.meruall.mean(),df3.vaariall.mean(),df4.taxiall.mean()]
        plt.pie(val,labels = val1,
        autopct ='% 1.1f %%', shadow = True)
        plt.title("CAB SERVICES")
        plt.show()        
        plt.bar(["UBER"],df.uberall.mean())
        plt.bar(["OLA"],df1.olaall.mean())
        plt.bar(["MERU"],df2.meruall.mean())
        plt.bar(["SAVAARI"],df3.vaariall.mean())
        plt.bar(["BHARAT TAXI"],df4.taxiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("CAB SERVICES")
        plt.show()
        uberconn.close()
        olaconn.close()
        meruconn.close()
        savaariconn.close()
        bharattaxiconn.close()
        
    def uberview(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        df = pd.DataFrame(uberdata,columns = ['name','convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['convenient'],df.convenient.mean())
        plt.bar(['drivers'],df.drivers.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("UBER")
        plt.show()
        uberconn.close()

    def olaview(self):
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        df = pd.DataFrame(oladata,columns = ['name','convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['convenient'],df.convenient.mean())
        plt.bar(['drivers'],df.drivers.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("OLA")
        plt.show()
        olaconn.close()

    def meruview(self):
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        df = pd.DataFrame(merudata,columns = ['name','convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['convenient'],df.convenient.mean())
        plt.bar(['drivers'],df.drivers.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("MERU")
        plt.show()
        meruconn.close()

    def savaariview(self):
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        df = pd.DataFrame(savaaridata,columns = ['name','convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['convenient'],df.convenient.mean())
        plt.bar(['drivers'],df.drivers.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SAVAARI")
        plt.show()
        savaariconn.close()

    def bharattaxiview(self):
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        df = pd.DataFrame(bharattaxidata,columns = ['name','convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        plt.bar(['convenient'],df.convenient.mean())
        plt.bar(['drivers'],df.drivers.mean())
        plt.bar(['customer_care'],df.customer_care.mean())
        plt.bar(['comparison'],df.comparison.mean())
        plt.bar(['overall'],df.overall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("BHARAT TAXI")
        plt.show()
        bharattaxiconn.close()

    def uola(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        print(uberdata)
        df = pd.DataFrame(uberdata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.uberall = pd.to_numeric(df.stack())
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        print(oladata)
        df1 = pd.DataFrame(oladata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df1.convenient = pd.to_numeric(df1.convenient)
        df1.drivers = pd.to_numeric(df1.drivers)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.olaall = pd.to_numeric(df1.stack())
        plt.bar(["UBER"],df.uberall.mean())
        plt.bar(["OLA"],df1.olaall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("UBER vs OLA")
        plt.show()
        uberconn.close()
        olaconn.close()

    def umeru(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        print(uberdata)
        df = pd.DataFrame(uberdata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.uberall = pd.to_numeric(df.stack())
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        print(merudata)
        df2 = pd.DataFrame(merudata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df2.convenient = pd.to_numeric(df2.convenient)
        df2.drivers = pd.to_numeric(df2.drivers)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.meruall = pd.to_numeric(df2.stack())
        plt.bar(["UBER"],df.uberall.mean())
        plt.bar(["MERU"],df2.meruall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("UBER vs MERU")
        plt.show()
        uberconn.close()
        meruconn.close()

    def uvaari(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        print(uberdata)
        df = pd.DataFrame(uberdata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.uberall = pd.to_numeric(df.stack())
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        print(savaaridata)
        df3 = pd.DataFrame(savaaridata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df3.convenient = pd.to_numeric(df3.convenient)
        df3.drivers = pd.to_numeric(df3.drivers)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.vaariall = pd.to_numeric(df3.stack())
        plt.bar(["UBER"],df.uberall.mean())
        plt.bar(["SAVAARI"],df3.vaariall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("UBER vs SAVAARI")
        plt.show()
        uberconn.close()
        savaariconn.close()

    def utaxi(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        uberdata = pd.read_sql_query("select * from uber",uberconn)
        print(uberdata)
        df = pd.DataFrame(uberdata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df.convenient = pd.to_numeric(df.convenient)
        df.drivers = pd.to_numeric(df.drivers)
        df.customer_care= pd.to_numeric(df.customer_care)
        df.comparison = pd.to_numeric(df.comparison)
        df.overall = pd.to_numeric(df.overall)
        df.uberall = pd.to_numeric(df.stack())
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        print(bharattaxidata)
        df4 = pd.DataFrame(bharattaxidata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df4.convenient = pd.to_numeric(df4.convenient)
        df4.drivers = pd.to_numeric(df4.drivers)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.taxiall = pd.to_numeric(df4.stack())
        plt.bar(["UBER"],df.uberall.mean())
        plt.bar(["BHARAT TAXI"],df4.taxiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("UBER vs BHARAT TAXI")
        plt.show()
        uberconn.close()
        bharattaxiconn.close()

    def olameru(self):
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        print(oladata)
        df1 = pd.DataFrame(oladata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df1.convenient = pd.to_numeric(df1.convenient)
        df1.drivers = pd.to_numeric(df1.drivers)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.olaall = pd.to_numeric(df1.stack())
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        print(merudata)
        df2 = pd.DataFrame(merudata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df2.convenient = pd.to_numeric(df2.convenient)
        df2.drivers = pd.to_numeric(df2.drivers)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.meruall = pd.to_numeric(df2.stack())
        plt.bar(["OLA"],df1.olaall.mean())
        plt.bar(["MERU"],df2.meruall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("OLA vs MERU")
        plt.show()
        olaconn.close()
        meruconn.close()

    def olavaari(self):
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        print(oladata)
        df1 = pd.DataFrame(oladata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df1.convenient = pd.to_numeric(df1.convenient)
        df1.drivers = pd.to_numeric(df1.drivers)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.olaall = pd.to_numeric(df1.stack())
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        print(savaaridata)
        df3 = pd.DataFrame(savaaridata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df3.convenient = pd.to_numeric(df3.convenient)
        df3.drivers = pd.to_numeric(df3.drivers)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.vaariall = pd.to_numeric(df3.stack())
        plt.bar(["OLA"],df1.olaall.mean())
        plt.bar(["SAVAARI"],df3.vaariall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("OLA vs SAVAARI")
        plt.show()
        olaconn.close()
        savaariconn.close()

    def olataxi(self):
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        oladata = pd.read_sql_query("select * from ola",olaconn)
        print(oladata)
        df1 = pd.DataFrame(oladata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df1.convenient = pd.to_numeric(df1.convenient)
        df1.drivers = pd.to_numeric(df1.drivers)
        df1.customer_care= pd.to_numeric(df1.customer_care)
        df1.comparison = pd.to_numeric(df1.comparison)
        df1.overall = pd.to_numeric(df1.overall)
        df1.olaall = pd.to_numeric(df1.stack())
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        print(bharattaxidata)
        df4 = pd.DataFrame(bharattaxidata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df4.convenient = pd.to_numeric(df4.convenient)
        df4.drivers = pd.to_numeric(df4.drivers)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.taxiall = pd.to_numeric(df4.stack())
        plt.bar(["OLA"],df1.olaall.mean())
        plt.bar(["BHARAT TAXI"],df4.taxiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("OLA vs BHARAT TAXI")
        plt.show()
        olaconn.close()
        bharattaxiconn.close()

    def mevaari(self):
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        print(merudata)
        df2 = pd.DataFrame(merudata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df2.convenient = pd.to_numeric(df2.convenient)
        df2.drivers = pd.to_numeric(df2.drivers)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.meruall = pd.to_numeric(df2.stack())
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        print(savaaridata)
        df3 = pd.DataFrame(savaaridata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df3.convenient = pd.to_numeric(df3.convenient)
        df3.drivers = pd.to_numeric(df3.drivers)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.vaariall = pd.to_numeric(df3.stack())
        plt.bar(["MERU"],df2.meruall.mean())
        plt.bar(["SAVAARI"],df3.vaariall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("MERU vs SAVAARI")
        plt.show()
        meruconn.close()
        savaariconn.close()

    def metaxi(self):
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        merudata = pd.read_sql_query("select * from meru",meruconn)
        print(merudata)
        df2 = pd.DataFrame(merudata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df2.convenient = pd.to_numeric(df2.convenient)
        df2.drivers = pd.to_numeric(df2.drivers)
        df2.customer_care= pd.to_numeric(df2.customer_care)
        df2.comparison = pd.to_numeric(df2.comparison)
        df2.overall = pd.to_numeric(df2.overall)
        df2.meruall = pd.to_numeric(df2.stack())
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        print(bharattaxidata)
        df4 = pd.DataFrame(bharattaxidata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df4.convenient = pd.to_numeric(df4.convenient)
        df4.drivers = pd.to_numeric(df4.drivers)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.taxiall = pd.to_numeric(df4.stack())
        plt.bar(["MERU"],df2.meruall.mean())
        plt.bar(["BHARAT TAXI"],df4.taxiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("MERU vs BHARAT TAXI")
        plt.show()
        meruconn.close()
        bharattaxiconn.close()

    def sataxi(self):
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        savaaridata = pd.read_sql_query("select * from savaari",savaariconn)
        print(savaaridata)
        df3 = pd.DataFrame(savaaridata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df3.convenient = pd.to_numeric(df3.convenient)
        df3.drivers = pd.to_numeric(df3.drivers)
        df3.customer_care= pd.to_numeric(df3.customer_care)
        df3.comparison = pd.to_numeric(df3.comparison)
        df3.overall = pd.to_numeric(df3.overall)
        df3.vaariall = pd.to_numeric(df3.stack())
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        bharattaxidata = pd.read_sql_query("select * from bharattaxi",bharattaxiconn)
        print(bharattaxidata)
        df4 = pd.DataFrame(bharattaxidata,columns = ['convenient','drivers','customer_care','comparison','overall'])
        df4.convenient = pd.to_numeric(df4.convenient)
        df4.drivers = pd.to_numeric(df4.drivers)
        df4.customer_care= pd.to_numeric(df4.customer_care)
        df4.comparison = pd.to_numeric(df4.comparison)
        df4.overall = pd.to_numeric(df4.overall)
        df4.taxiall = pd.to_numeric(df4.stack())
        plt.bar(["SAVAARI"],df3.vaariall.mean())
        plt.bar(["BHARAT TAXI"],df4.taxiall.mean())
        plt.xlabel("CATEGORY")
        plt.ylabel("REVIEW")
        plt.title("SAVARI vs BHARAT TAXI")
        plt.show()
        savaariconn.close()
        bharattaxiconn.close() 
        
    def back(self):
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.adminloginframe.place_forget()
        self.travelframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.viewframe.place(x=260,y=120)

    def adminlogout(self):
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.viewframe.place_forget()
        self.categoryframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.adminframe.place(x=260,y=120)
        
    def userpage(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.userframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.userframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.userframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.userframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.userframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.userframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.userframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.usertitle = Label(self.userframe, text="THIS IS USER PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.usertitle.place(x =0, y=40,relwidth=1)
        self.nameentry = Label(self.userframe,text ="USERNAME",font =("Comic Sans Ms",15,"bold"),fg = "green")
        self.nameentry.place(x=250,y=150)
        self.nameentry = Entry(self.userframe)
        self.nameentry.place(x=400,y=160)
        self.password = Label(self.userframe,text ="PASSWORD",font =("Comic Sans Ms",15,"bold"),fg = "green")
        self.password.place(x=250,y=200)
        self.passentry = Entry(self.userframe)
        self.passentry.place(x=400,y=210)
        self.loginbutton = Button(self.userframe, text ="LOGIN", font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command=self.userlogin)
        self.loginbutton.place(x=250,y=250)
        self.registerbutton = Button(self.userframe,text ="REGISTER",font=("Comic Sans Ms",10),bg="#efefef", bd=5,fg="green",relief = RIDGE, command=self.register)
        self.registerbutton.place(x=450,y=250)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.userframe.place(x=260,y=120)

    def register(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.registerframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.registerframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.registerframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.registerframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.registerframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.registerframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.registerframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.registertitle = Label(self.registerframe, text="THIS IS REGISTER PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.registertitle.place(x =0, y=40,relwidth=1)
        self.username = Label(self.registerframe,text ="USERNAME",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.username.place(x=200,y=100)
        self.usernameentry = Entry(self.registerframe)
        self.usernameentry.place(x=450,y=100)
        self.password = Label(self.registerframe,text ="PASSWORD",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.password.place(x=200,y=150)
        self.validpass = Label(self.registerframe,text="At least 1 letter between [a-z] and [A-Z].\n At least 1 number between [0-9]. \nAt least 1 character from [$#@].\nMinimum length 6 characters. \nMaximum length 20 characters",font =("Comic Sans Ms",8),fg = "green")
        self.validpass.place(x=600,y=150)
        self.passwordentry = Entry(self.registerframe)
        self.passwordentry.place(x=450,y=150)
        self.confpassword = Label(self.registerframe,text ="Re-type PASSWORD",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.confpassword.place(x=200,y=200)
        self.confpasswordentry = Entry(self.registerframe)
        self.confpasswordentry.place(x=450,y=200)
        self.phoneno = Label(self.registerframe,text ="PHONE NO",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.phoneno.place(x=200,y=250)
        self.phonenoentry = Entry(self.registerframe)
        self.phonenoentry.place(x=450,y=250)
        self.email = Label(self.registerframe,text ="E-MAIL",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.email.place(x=200,y=300)
        self.emailentry = Entry(self.registerframe)
        self.emailentry.place(x=450,y=300)
        self.loginbutton = Button(self.registerframe, text ="REGISTER", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command=self.userregister)
        self.loginbutton.place(x=350,y=360)
        self.adminframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.categoryframe.place_forget()
        self.aboutusframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.registerframe.place(x=260,y=120)

    def userregister(self):
        data=(self.usernameentry.get(),)
        adata=(self.emailentry.get(),)
        pdata=(self.phonenoentry.get(),)
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not (re.search(regex,self.emailentry.get())) :
            messagebox.showerror("email","ENTER VALID EMAIL !!!")
        regx ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
        if not (re.search(regx,self.phonenoentry.get())):
            messagebox.showerror("phone no","ENTER VALID NUMBER !!!")
        pregx ='((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20})'
        if not (re.search(pregx,self.passwordentry.get())):
            messagebox.showerror("password","ENTER VALID PASSWORD !!")
            self.passwordentry.delete(0,END)
            self.confpasswordentry.delete(0,END)
        elif self.usernameentry.get()=="" or self.passwordentry.get()=="" or self.confpasswordentry.get()=="" or self.phonenoentry.get()=="" or self.emailentry.get()=="":
            messagebox.showerror("error","ALL FEILDS ARE REQUIRED !!")
        elif self.passwordentry.get() != self.confpasswordentry.get():
            messagebox.showerror("error","PASSWORD NOT MATCHING !!!")
        else:
            res = db.user_exist(data)
            ges = db.email_exist(adata)
            pes = db.phone_exist(pdata)
            if res:
                messagebox.showerror("register","USERNAME ALREADY EXIST")
            elif ges:
                messagebox.showerror("register","E-MAIL ALREADY EXIST")
            elif pes:
                messagebox.showerror("register","PHONE NO ALREADY USED BY SOMEONE")
            else:
                con = mysql.connector.connect(host = "localhost", user="root", passwd="1234", database="feedback")
                mycursor = con.cursor()
                mycursor.execute("insert into user values('"+ self.usernameentry.get() +"','"+ self.passwordentry.get() +"','"+ self.confpasswordentry.get() +"','"+ self.phonenoentry.get() +"','"+ self.emailentry.get()+"')")
                mycursor.execute("commit")
                messagebox.showinfo("register", "REGISTRATION SUCCESSFULL !!!")
                con.close()
                self.makemytripupdate.place_forget()
                self.goibiboupdate.place_forget()
                self.yatraupdate.place_forget()
                self.easetripupdate.place_forget()
                self.trivagoupdate.place_forget()
                self.foodpandaupdate.place_forget()
                self.zomatoupdate.place_forget()
                self.swiggyupdate.place_forget()
                self.freshmenuupdate.place_forget()
                self.foodmingoupdate.place_forget()
                self.khanacademyupdate.place_forget()
                self.courseraupdate.place_forget()
                self.w3schoolupdate.place_forget()
                self.byjusupdate.place_forget()
                self.codeacademyupdate.place_forget()
                self.amazonupdate.place_forget()
                self.flipkartupdate.place_forget()
                self.ebayupdate.place_forget()
                self.walmartupdate.place_forget()
                self.alibabaupdate.place_forget()
                self.uberupdate.place_forget()
                self.olaupdate.place_forget()
                self.meruupdate.place_forget()
                self.savaariupdate.place_forget()
                self.bharattaxiupdate.place_forget()
                self.adminframe.place_forget()
                self.ppframe.place_forget()
                self.tandcframe.place_forget()
                self.userfeedbackframe.place_forget()
                self.homeframe.place_forget()
                self.adminloginframe.place_forget()
                self.registerframe.place_forget()
                self.contactusframe.place_forget()
                self.aboutusframe.place_forget()
                self.categoryframe.place_forget()
                self.viewframe.place_forget()
                self.travelframe.place_forget()
                self.foodframe.place_forget()
                self.educationframe.place_forget()
                self.shopframe.place_forget()
                self.cabframe.place_forget()
                self.makemytripframe.place_forget()
                self.goibiboframe.place_forget()
                self.yatraframe.place_forget()
                self.easetripframe.place_forget()
                self.trivagoframe.place_forget()
                self.foodpandaframe.place_forget()
                self.zomatoframe.place_forget()
                self.swiggyframe.place_forget()
                self.freshmenuframe.place_forget()
                self.foodmingoframe.place_forget()
                self.khanacademyframe.place_forget()
                self.courseraframe.place_forget()
                self.w3schoolframe.place_forget()
                self.byjusframe.place_forget()
                self.codeacademyframe.place_forget()
                self.amazonframe.place_forget()
                self.flipkartframe.place_forget()
                self.ebayframe.place_forget()
                self.walmartframe.place_forget()
                self.alibabaframe.place_forget()
                self.uberframe.place_forget()
                self.olaframe.place_forget()
                self.meruframe.place_forget()
                self.savaariframe.place_forget()
                self.bharattaxiframe.place_forget()
                self.travelviewframe.place_forget()
                self.foodviewframe.place_forget()
                self.educationviewframe.place_forget()
                self.shoppingviewframe.place_forget()
                self.cabviewframe.place_forget()
                self.userframe.place(x=260,y=120)
            
    def userlogin(self):
        self.name = self.nameentry.get()
        data=(self.nameentry.get(),self.passentry.get())
        if self.nameentry.get()=="" or self.passentry.get()=="":
            messagebox.showerror("login","ALL FIELDS ARE REQUIRED !!!")
        else:
            res=db.user_login(data)
            if not res:
                messagebox.showerror( "login", "USERNAME OR PASSWORD IS INCORRECT !!!" )
            else:
                messagebox.showinfo( "login","LOGIN SUCEESSFULL !!!!" )
                self.nameentry.delete(0,END)
                self.passentry.delete(0,END)
                self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
                self.feed_img = Label(self.categoryframe, image = self.feed_img)
                self.feed_img.pack()
                self.navbar = Label(self.categoryframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
                self.navbar.place(x=0,y=0,relwidth=1)
                self.categorytitle = Label(self.categoryframe, text="FEEDBACK CATEGORY PAGE", font=("Comic Sans Ms",25),fg = "green")
                self.categorytitle.place(x =0, y=40,relwidth=1)
                self.logoutbutton = Button(self.categoryframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
                self.logoutbutton.place(x=730, y=0)
                self.travelbutton= Button(self.categoryframe, text = "TRAVEL", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.travel)
                self.travelbutton.place(x=650,y=0)
                self.foodbutton= Button(self.categoryframe, text = "FOOD", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.food)
                self.foodbutton.place(x=580,y=0)
                self.educationbutton= Button(self.categoryframe, text = "EDUCATION", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.education)
                self.educationbutton.place(x=470,y=0)
                self.shoppingbutton= Button(self.categoryframe, text = "SHOPPING", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.shop)
                self.shoppingbutton.place(x=370,y=0)
                self.cabbutton= Button(self.categoryframe, text = "CAB SERVICES", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.cab)
                self.cabbutton.place(x=240,y=0)
                self.userframe.place_forget()
                self.makemytripupdate.place_forget()
                self.goibiboupdate.place_forget()
                self.yatraupdate.place_forget()
                self.easetripupdate.place_forget()
                self.trivagoupdate.place_forget()
                self.foodpandaupdate.place_forget()
                self.zomatoupdate.place_forget()
                self.swiggyupdate.place_forget()
                self.freshmenuupdate.place_forget()
                self.foodmingoupdate.place_forget()
                self.khanacademyupdate.place_forget()
                self.courseraupdate.place_forget()
                self.w3schoolupdate.place_forget()
                self.byjusupdate.place_forget()
                self.codeacademyupdate.place_forget()
                self.amazonupdate.place_forget()
                self.flipkartupdate.place_forget()
                self.ebayupdate.place_forget()
                self.walmartupdate.place_forget()
                self.alibabaupdate.place_forget()
                self.uberupdate.place_forget()
                self.olaupdate.place_forget()
                self.meruupdate.place_forget()
                self.savaariupdate.place_forget()
                self.bharattaxiupdate.place_forget()
                self.userfeedbackframe.place_forget()
                self.adminframe.place_forget()
                self.homeframe.place_forget()
                self.adminloginframe.place_forget()
                self.registerframe.place_forget()
                self.contactusframe.place_forget()
                self.aboutusframe.place_forget()
                self.viewframe.place_forget()
                self.ppframe.place_forget()
                self.tandcframe.place_forget()
                self.foodframe.place_forget()
                self.educationframe.place_forget()
                self.shopframe.place_forget()
                self.cabframe.place_forget()
                self.travelframe.place_forget()
                self.makemytripframe.place_forget()
                self.goibiboframe.place_forget()
                self.yatraframe.place_forget()
                self.easetripframe.place_forget()
                self.trivagoframe.place_forget()
                self.foodpandaframe.place_forget()
                self.zomatoframe.place_forget()
                self.swiggyframe.place_forget()
                self.freshmenuframe.place_forget()
                self.foodmingoframe.place_forget()
                self.khanacademyframe.place_forget()
                self.courseraframe.place_forget()
                self.w3schoolframe.place_forget()
                self.byjusframe.place_forget()
                self.codeacademyframe.place_forget()
                self.amazonframe.place_forget()
                self.flipkartframe.place_forget()
                self.ebayframe.place_forget()
                self.walmartframe.place_forget()
                self.alibabaframe.place_forget()
                self.uberframe.place_forget()
                self.olaframe.place_forget()
                self.meruframe.place_forget()
                self.savaariframe.place_forget()
                self.bharattaxiframe.place_forget()
                self.travelviewframe.place_forget()
                self.foodviewframe.place_forget()
                self.educationviewframe.place_forget()
                self.shoppingviewframe.place_forget()
                self.cabviewframe.place_forget()
                self.categoryframe.place(x=260,y=120)
            
    def travel(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.travelframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.travelframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.traveltitle = Label(self.travelframe, text="TRAVEL FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.traveltitle.place(x =0, y=40,relwidth=1)
        self.travelbackbutton = Button(self.travelframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travelback)
        self.travelbackbutton.place(x=750, y=0)
        self.makemytripbutton= Button(self.travelframe, text = "MAKE MY TRIP", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.makemytrip)
        self.makemytripbutton.place(x=620,y=0)
        self.goibibobutton= Button(self.travelframe, text = "GO IBIBO", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.goibibo)
        self.goibibobutton.place(x=520,y=0)
        self.yatrabutton= Button(self.travelframe, text = "YATRA", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.yatra)
        self.yatrabutton.place(x=440,y=0)
        self.easetripbutton= Button(self.travelframe, text = "EASE TRIP", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE, command = self.easetrip)
        self.easetripbutton.place(x=335,y=0)
        self.trivagobutton= Button(self.travelframe, text = "TRIVAGO", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.trivago)
        self.trivagobutton.place(x=235,y=0)
        self.logoutbutton = Button(self.travelframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.travelframe.place(x=260,y=120)
        
    def travelback(self):
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.categoryframe.place(x=260,y=120)
        
    def goibibo(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.goibiboframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.goibiboframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.goibibotitle = Label(self.goibiboframe, text="GO IBIBO FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.goibibotitle.place(x =0, y=40,relwidth=1)
        self.goibibobackbutton = Button(self.goibiboframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.goibibobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.goibiboframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.goibiboframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.goibiboframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.goibiboframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.goibiboframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.goibiboframe,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.goibiboframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.goibiboframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.goibiboframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.goibiboframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.goibiboframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.goibibosubmitbutton = Button(self.goibiboframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.goibibosubmit)
        self.goibibosubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.travelframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.goibiboframe.place(x=260,y=120)

    def goibibosubmit(self):
        self.updatebutton = Button(self.goibiboframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command = self.goibiboupdates)
        self.updatebutton.place(x=420,y=360)
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        goibibocursor.execute("insert into goibibo values('"+self.name+"','"+str(self.support)+"','"+str(self.service)+"','"+str(self.refund)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        goibibocursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        goibiboconn.close()

    def goibiboupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.goibiboupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.goibiboupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.goibibotitle = Label(self.goibiboupdate, text="GO IBIBO FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.goibibotitle.place(x =0, y=40,relwidth=1)
        self.goibibobackbutton = Button(self.goibiboupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.goibibobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.goibiboupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.goibiboupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.goibiboupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.goibiboupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.goibiboupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.goibiboupdate,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.goibiboupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.goibiboupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.goibiboupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.goibiboupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.goibiboupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.goibibosubmitbutton = Button(self.goibiboupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.goibiboupsubmit)
        self.goibibosubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place(x=260,y=120)
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.travelframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.goibiboframe.place_forget()

    def goibiboupsubmit(self):
        goibiboconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        goibibocursor = goibiboconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        goibibocursor.execute("update goibibo set support_staff ='"+str(self.support)+"', service_quality='"+str(self.service)+"',refund_service='"+str(self.refund)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name ='"+self.name+"'")
        goibibocursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED")
        goibiboconn.close()
        
    def makemytrip(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.makemytripframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.makemytripframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.makemytriptitle = Label(self.makemytripframe, text="MAKE MY TRIP FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.makemytriptitle.place(x =0, y=40,relwidth=1)
        self.makemytripbackbutton = Button(self.makemytripframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.makemytripbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.makemytripframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.makemytripframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.makemytripframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.makemytripframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.makemytripframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.makemytripframe,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.makemytripframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.makemytripframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.makemytripframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.makemytripframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.makemytripframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.makemytripsubmitbutton = Button(self.makemytripframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.makemytripsubmit)
        self.makemytripsubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.travelframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.makemytripframe.place(x=260,y=120)

    def makemytripsubmit(self):
        self.updatebutton = Button(self.makemytripframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command = self.makemytripupdates)
        self.updatebutton.place(x=420,y=360)
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        makemytripcursor.execute("insert into makemytrip values('"+self.name+"','"+str(self.support)+"','"+str(self.service)+"','"+str(self.refund)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        makemytripcursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        makemytripconn.close()

    def makemytripupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.makemytripupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.makemytripupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.makemytriptitle = Label(self.makemytripupdate, text="MAKE MY TRIP FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.makemytriptitle.place(x =0, y=40,relwidth=1)
        self.makemytripbackbutton = Button(self.makemytripupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.makemytripbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.makemytripupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.makemytripupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.makemytripupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.makemytripupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.makemytripupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.makemytripupdate,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.makemytripupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.makemytripupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.makemytripupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.makemytripupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.makemytripupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.makemytripsubmitbutton = Button(self.makemytripupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.makemyupsubmit)
        self.makemytripsubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place(x=260,y=120)
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.aboutusframe.place_forget()
        self.ppframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.viewframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.tandcframe.place_forget()

    def makemyupsubmit(self):
        makemytripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        makemytripcursor = makemytripconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        makemytripcursor.execute("update makemytrip set support_staff ='"+str(self.support)+"', service_quality='"+str(self.service)+"',refund_service='"+str(self.refund)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name ='"+self.name+"'")
        makemytripcursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED")
        makemytripconn.close()


    def yatra(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.yatraframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.yatraframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.yatratitle = Label(self.yatraframe, text="YATRA FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.yatratitle.place(x =0, y=40,relwidth=1)
        self.yatrabackbutton = Button(self.yatraframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.yatrabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.yatraframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.yatraframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.yatraframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.yatraframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.yatraframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.yatraframe,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.yatraframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.yatraframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.yatraframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.yatraframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.yatraframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.yatrasubmitbutton = Button(self.yatraframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.yatrasubmit)
        self.yatrasubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.travelframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.yatraframe.place(x=260,y=120)
                                        
    def yatrasubmit(self):
        self.updatebutton = Button(self.yatraframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command = self.yatraupdates)
        self.updatebutton.place(x=420,y=360)
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        yatracursor.execute("insert into yatra values('"+self.name+"','"+str(self.support)+"','"+str(self.service)+"','"+str(self.refund)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        yatracursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        yatraconn.close()

    def yatraupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.yatraupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.yatraupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.yatratitle = Label(self.yatraupdate, text="YATRA FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.yatratitle.place(x =0, y=40,relwidth=1)
        self.yatrabackbutton = Button(self.yatraupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.yatrabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.yatraupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.yatraupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.yatraupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.yatraupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.yatraupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.yatraupdate,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.yatraupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.yatraupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.yatraupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.yatraupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.yatraupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.yatrasubmitbutton = Button(self.yatraupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.yatraupsubmit)
        self.yatrasubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place(x=260,y=120)
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.travelframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.yatraframe.place_forget()
                                        
    def yatraupsubmit(self):
        yatraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        yatracursor = yatraconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        yatracursor.execute("update yatra set support_staff ='"+str(self.support)+"', service_quality='"+str(self.service)+"',refund_service='"+str(self.refund)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name ='"+self.name+"'")
        yatracursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED")
        yatraconn.close()

    def easetrip(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.easetripframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.easetripframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.easetriptitle = Label(self.easetripframe, text="EASE TRIP FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.easetriptitle.place(x =0, y=40,relwidth=1)
        self.easetripbackbutton = Button(self.easetripframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.easetripbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.easetripframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.easetripframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.easetripframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.easetripframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.easetripframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.easetripframe,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.easetripframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.easetripframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.easetripframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.easetripframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.easetripframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.easetripsubmitbutton = Button(self.easetripframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.easetripsubmit)
        self.easetripsubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.travelframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.easetripframe.place(x=260,y=120)

    def easetripsubmit(self):
        self.updatebutton = Button(self.easetripframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.easetripupdates)
        self.updatebutton.place(x=420,y=360)
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        easetripcursor.execute("insert into easetrip values('"+self.name+"','"+str(self.support)+"','"+str(self.service)+"','"+str(self.refund)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        easetripcursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        easetripconn.close()
        
    def easetripupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.easetripupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.easetripupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.easetriptitle = Label(self.easetripupdate, text="EASE TRIP FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.easetriptitle.place(x =0, y=40,relwidth=1)
        self.easetripbackbutton = Button(self.easetripupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.easetripbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.easetripupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.easetripupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.easetripupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.easetripupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.easetripupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.easetripupdate,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.easetripupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.easetripupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.easetripupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.easetripupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.easetripupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.easetripsubmitbutton = Button(self.easetripupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.easetripupsubmit)
        self.easetripsubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place(x=260,y=120)
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.travelframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()        
        self.easetripframe.place_forget()

    def easetripupsubmit(self):
        easetripconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        easetripcursor = easetripconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        easetripcursor.execute("update easetrip set support_staff ='"+str(self.support)+"', service_quality='"+str(self.service)+"',refund_service='"+str(self.refund)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name ='"+self.name+"'")
        easetripcursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED")
        easetripconn.close()
        
    def trivago(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.trivagoframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.trivagoframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.trivagotitle = Label(self.trivagoframe, text="TRIVAGO FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.trivagotitle.place(x =0, y=40,relwidth=1)
        self.trivagobackbutton = Button(self.trivagoframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.trivagobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.trivagoframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.trivagoframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.trivagoframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.trivagoframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.trivagoframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.trivagoframe,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.trivagoframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.trivagoframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.trivagoframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.trivagoframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.trivagoframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.trivagosubmitbutton = Button(self.trivagoframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.trivagosubmit)
        self.trivagosubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.travelframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.trivagoframe.place(x=260,y=120)
        
    def trivagosubmit(self):
        self.updatebutton = Button(self.trivagoframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.trivagoupdates)
        self.updatebutton.place(x=420,y=360)
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        trivagocursor.execute("insert into trivago values('"+self.name+"','"+str(self.support)+"','"+str(self.service)+"','"+str(self.refund)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        trivagocursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        trivagoconn.close()

    def trivagoupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.trivagoupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.trivagoupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.trivagotitle = Label(self.trivagoupdate, text="TRIVAGO FEEDBACK", font=("Comic Sans Ms",25),fg = "green")
        self.trivagotitle.place(x =0, y=40,relwidth=1)
        self.trivagobackbutton = Button(self.trivagoupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.travel)
        self.trivagobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.trivagoupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.trivagoupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.trivagoupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.trivagoupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.trivagoupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.trivagoupdate,text ="REFUND SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.trivagoupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.trivagoupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.trivagoupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.trivagoupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.trivagoupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.trivagosubmitbutton = Button(self.trivagoupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.trivagoupsubmit)
        self.trivagosubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place(x=260,y=120)
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.travelframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.trivagoframe.place_forget()
        
    def trivagoupsubmit(self):
        trivagoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "travel")
        trivagocursor = trivagoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.support = 5
        if self.first.get() == "GOOD":
            self.support = 4
        if self.first.get() == "AVERAGE":
            self.support = 3
        if self.first.get() == "BAD":
            self.support = 2
        if self.first.get() == "WORST":
            self.support = 1
        if self.second.get == "EXCELLENT":
            self.service = 5
        if self.second.get() == "GOOD":
            self.service = 4
        if self.second.get() == "AVERAGE":
            self.service = 3
        if self.second.get() == "BAD":
            self.service = 2
        if self.second.get() == "WORST":
            self.service = 1
        if self.third.get() == "EXCELLENT":
            self.refund = 5
        if self.third.get() == "GOOD":
            self.refund = 4
        if self.third.get() == "AVERAGE":
            self.refund = 3
        if self.third.get() == "BAD":
            self.refund = 2
        if self.third.get() == "WORST":
            self.refund = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        trivagocursor.execute("update trivago set support_staff ='"+str(self.support)+"', service_quality='"+str(self.service)+"',refund_service='"+str(self.refund)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name ='"+self.name+"'")
        trivagocursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED")
        trivagoconn.close()


    def food(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodtitle = Label(self.foodframe, text="FOOD FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.foodtitle.place(x =0, y=40,relwidth=1)
        self.foodbackbutton = Button(self.foodframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.foodback)
        self.foodbackbutton.place(x=750, y=0)
        self.foodpandabutton= Button(self.foodframe, text = "FOOD PANDA", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.foodpanda)
        self.foodpandabutton.place(x=625,y=0)
        self.zomatobutton= Button(self.foodframe, text = "ZOMATO", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.zomato)
        self.zomatobutton.place(x=530,y=0)
        self.swiggybutton= Button(self.foodframe, text = "SWIGGY", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE, command = self.swiggy)
        self.swiggybutton.place(x=430,y=0)
        self.freshmenubutton= Button(self.foodframe, text = "FRESH MENU", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.freshmenu)
        self.freshmenubutton.place(x=305,y=0)
        self.foodmingobutton= Button(self.foodframe, text = "FOOD MINGO", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.foodmingo)
        self.foodmingobutton.place(x=180,y=0)
        self.logoutbutton = Button(self.foodframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.foodframe.place(x=260,y=120)

    def foodback(self):
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.categoryframe.place(x=260,y=120)
        
    def foodpanda(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodpandaframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodpandaframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodpandatitle = Label(self.foodpandaframe, text="FOOD PANDA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.foodpandatitle.place(x =0, y=40,relwidth=1)
        self.foodpandabackbutton = Button(self.foodpandaframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.foodpandabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.foodpandaframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.foodpandaframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.foodpandaframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.foodpandaframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.foodpandaframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.foodpandaframe,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.foodpandaframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.foodpandaframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.foodpandaframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.foodpandaframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.foodpandaframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.foodpandasubmitbutton = Button(self.foodpandaframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.foodpandasubmit)
        self.foodpandasubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.foodpandaframe.place(x=260,y=120)

    def foodpandasubmit(self):
        self.updatebutton = Button(self.foodpandaframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.foodpandaupdates)
        self.updatebutton.place(x=420,y=360)
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        foodpandacursor.execute("insert into foodpanda values('"+self.name+"','"+str(self.supportstaff)+"','"+str(self.servicequality)+"','"+str(self.foodquality)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        foodpandacursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        foodpandaconn.close()

    def foodpandaupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodpandaupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodpandaupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodpandatitle = Label(self.foodpandaupdate, text="FOOD PANDA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.foodpandatitle.place(x =0, y=40,relwidth=1)
        self.foodpandabackbutton = Button(self.foodpandaupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.foodpandabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.foodpandaupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.foodpandaupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.foodpandaupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.foodpandaupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.foodpandaupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.foodpandaupdate,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.foodpandaupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.foodpandaupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.foodpandaupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.foodpandaupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.foodpandaupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.foodpandasubmitbutton = Button(self.foodpandaupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.foodpandaupsubmit)
        self.foodpandasubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place(x=260,y=120)
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.foodpandaframe.place_forget()

    def foodpandaupsubmit(self):
        foodpandaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodpandacursor = foodpandaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        foodpandacursor.execute("update foodpanda set support_staff='"+str(self.supportstaff)+"',service_quality='"+str(self.servicequality)+"',food_quality='"+str(self.foodquality)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        foodpandacursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!")
        foodpandaconn.close()

        
    def zomato(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.zomatoframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.zomatoframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.zomatotitle = Label(self.zomatoframe, text="ZOMATO FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.zomatotitle.place(x =0, y=40,relwidth=1)
        self.zomatobackbutton = Button(self.zomatoframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.zomatobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.zomatoframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.zomatoframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.zomatoframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.zomatoframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.zomatoframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.zomatoframe,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.zomatoframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.zomatoframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.zomatoframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.zomatoframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.zomatoframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.zomatosubmitbutton = Button(self.zomatoframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.zomatosubmit)
        self.zomatosubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.foodframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.zomatoframe.place(x=260,y=120)

    def zomatosubmit(self):
        self.updatebutton = Button(self.zomatoframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.zomatoupdates)
        self.updatebutton.place(x=420,y=360)
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        zomatocursor.execute("insert into zomato values('"+self.name+"','"+str(self.supportstaff)+"','"+str(self.servicequality)+"','"+str(self.foodquality)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        zomatocursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        zomatoconn.close()

    def zomatoupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.zomatoupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.zomatoupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.zomatotitle = Label(self.zomatoupdate, text="ZOMATO FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.zomatotitle.place(x =0, y=40,relwidth=1)
        self.zomatobackbutton = Button(self.zomatoupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.zomatobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.zomatoupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.zomatoupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.zomatoupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.zomatoupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.zomatoupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.zomatoupdate,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.zomatoupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.zomatoupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.zomatoupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.zomatoupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.zomatoupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.zomatosubmitbutton = Button(self.zomatoupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.zomatoupsubmit)
        self.zomatosubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place(x=260,y=120)
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.foodframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.zomatoframe.place_forget()

    def zomatoupsubmit(self):
        zomatoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        zomatocursor = zomatoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        zomatocursor.execute("update zomato set support_staff='"+str(self.supportstaff)+"',service_quality='"+str(self.servicequality)+"',food_quality='"+str(self.foodquality)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        zomatocursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!")
        zomatoconn.close()

    def swiggy(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.swiggyframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.swiggyframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.swiggytitle = Label(self.swiggyframe, text="SWIGGY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.swiggytitle.place(x =0, y=40,relwidth=1)
        self.swiggybackbutton = Button(self.swiggyframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.swiggybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.swiggyframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.swiggyframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.swiggyframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.swiggyframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.swiggyframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.swiggyframe,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.swiggyframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.swiggyframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.swiggyframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.swiggyframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.swiggyframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.swiggysubmitbutton = Button(self.swiggyframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.swiggysubmit)
        self.swiggysubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.foodframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.swiggyframe.place(x=260,y=120)

    def swiggysubmit(self):
        self.updatebutton = Button(self.swiggyframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.swiggyupdates)
        self.updatebutton.place(x=420,y=360)
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        swiggycursor.execute("insert into swiggy values('"+self.name+"','"+str(self.supportstaff)+"','"+str(self.servicequality)+"','"+str(self.foodquality)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        swiggycursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        swiggyconn.close()

    def swiggyupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.swiggyupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.swiggyupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.swiggytitle = Label(self.swiggyupdate, text="SWIGGY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.swiggytitle.place(x =0, y=40,relwidth=1)
        self.swiggybackbutton = Button(self.swiggyupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.swiggybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.swiggyupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.swiggyupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.swiggyupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.swiggyupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.swiggyupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.swiggyupdate,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.swiggyupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.swiggyupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.swiggyupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.swiggyupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.swiggyupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.swiggysubmitbutton = Button(self.swiggyupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.swiggyupsubmit)
        self.swiggysubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place(x=260,y=120)
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.foodframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.swiggyframe.place_forget()

    def swiggyupsubmit(self):
        swiggyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        swiggycursor = swiggyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        swiggycursor.execute("update swiggy set support_staff='"+str(self.supportstaff)+"',service_quality='"+str(self.servicequality)+"',food_quality='"+str(self.foodquality)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        swiggycursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!")
        swiggyconn.close()


    def freshmenu(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.freshmenuframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.freshmenuframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.freshmenutitle = Label(self.freshmenuframe, text="FRESH MENU FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.freshmenutitle.place(x =0, y=40,relwidth=1)
        self.freshmenubackbutton = Button(self.freshmenuframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.freshmenubackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.freshmenuframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.freshmenuframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.freshmenuframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.freshmenuframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.freshmenuframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.freshmenuframe,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.freshmenuframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.freshmenuframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.freshmenuframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.freshmenuframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.freshmenuframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.freshmenusubmitbutton = Button(self.freshmenuframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.freshmenusubmit)
        self.freshmenusubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.foodframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.freshmenuframe.place(x=260,y=120)

    def freshmenusubmit(self):
        self.updatebutton = Button(self.freshmenuframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.freshmenuupdates)
        self.updatebutton.place(x=420,y=360)
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        freshmenucursor.execute("insert into freshmenu values('"+self.name+"','"+str(self.supportstaff)+"','"+str(self.servicequality)+"','"+str(self.foodquality)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        freshmenucursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        freshmenuconn.close()
        
    def freshmenuupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.freshmenuupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.freshmenuupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.freshmenutitle = Label(self.freshmenuupdate, text="FRESH MENU FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.freshmenutitle.place(x =0, y=40,relwidth=1)
        self.freshmenubackbutton = Button(self.freshmenuupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.freshmenubackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.freshmenuupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.freshmenuupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.freshmenuupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.freshmenuupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.freshmenuupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.freshmenuupdate,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.freshmenuupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.freshmenuupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.freshmenuupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.freshmenuupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.freshmenuupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.freshmenusubmitbutton = Button(self.freshmenuupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.freshmenuupsubmit)
        self.freshmenusubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place(x=260,y=120)
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.foodframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.freshmenuframe.place_forget()

    def freshmenuupsubmit(self):
        freshmenuconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        freshmenucursor = freshmenuconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        freshmenucursor.execute("update freshmenu set support_staff='"+str(self.supportstaff)+"',service_quality='"+str(self.servicequality)+"',food_quality='"+str(self.foodquality)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        freshmenucursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!")
        freshmenuconn.close()


    def foodmingo(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodmingoframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodmingoframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodmingotitle = Label(self.foodmingoframe, text="FOOD MINGO FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.foodmingotitle.place(x =0, y=40,relwidth=1)
        self.foodmingobackbutton = Button(self.foodmingoframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.foodmingobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.foodmingoframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.foodmingoframe,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.foodmingoframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.foodmingoframe,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.foodmingoframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.foodmingoframe,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.foodmingoframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.foodmingoframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.foodmingoframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.foodmingoframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.foodmingoframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.foodmingosubmitbutton = Button(self.foodmingoframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.foodmingosubmit)
        self.foodmingosubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.foodmingoframe.place(x=260,y=120)

    def foodmingosubmit(self):
        self.updatebutton = Button(self.foodmingoframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.foodmingoupdates)
        self.updatebutton.place(x=420,y=360)
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        foodmingocursor.execute("insert into foodmingo values('"+self.name+"','"+str(self.supportstaff)+"','"+str(self.servicequality)+"','"+str(self.foodquality)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        foodmingocursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        foodmingoconn.close()

    def foodmingoupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.foodmingoupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.foodmingoupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.foodmingotitle = Label(self.foodmingoupdate, text="FOOD MINGO FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.foodmingotitle.place(x =0, y=40,relwidth=1)
        self.foodmingobackbutton = Button(self.foodmingoupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.food)
        self.foodmingobackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.foodmingoupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.foodmingoupdate,text ="SUPPORT STAFF",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.foodmingoupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.foodmingoupdate,text ="SERVICE QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.foodmingoupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.foodmingoupdate,text ="FOOD QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.foodmingoupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.foodmingoupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.foodmingoupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.foodmingoupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.foodmingoupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.foodmingosubmitbutton = Button(self.foodmingoupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.foodmingoupsubmit)
        self.foodmingosubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place(x=260,y=120)
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.foodmingoframe.place_forget()

    def foodmingoupsubmit(self):
        foodmingoconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "food")
        foodmingocursor = foodmingoconn.cursor()
        if self.first.get == "EXCELLENT":
            self.supportstaff = 5
        if self.first.get() == "GOOD":
            self.supportstaff = 4
        if self.first.get() == "AVERAGE":
            self.supportstaff = 3
        if self.first.get() == "BAD":
            self.supportstaff = 2
        if self.first.get() == "WORST":
            self.supportstaff = 1
        if self.second.get == "EXCELLENT":
            self.servicequality = 5
        if self.second.get() == "GOOD":
            self.servicequality = 4
        if self.second.get() == "AVERAGE":
            self.servicequality = 3
        if self.second.get() == "BAD":
            self.servicequality = 2
        if self.second.get() == "WORST":
            self.servicequality = 1
        if self.third.get() == "EXCELLENT":
            self.foodquality = 5
        if self.third.get() == "GOOD":
            self.foodquality = 4
        if self.third.get() == "AVERAGE":
            self.foodquality = 3
        if self.third.get() == "BAD":
            self.foodquality = 2
        if self.third.get() == "WORST":
            self.foodquality = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        foodmingocursor.execute("update foodmingo set support_staff='"+str(self.supportstaff)+"',service_quality='"+str(self.servicequality)+"',food_quality='"+str(self.foodquality)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        foodmingocursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!")
        foodmingoconn.close()


    def education(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.educationframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.educationframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.educationtitle = Label(self.educationframe, text="EDUCATION FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.educationtitle.place(x =0, y=40,relwidth=1)
        self.educationbackbutton = Button(self.educationframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.educationback)
        self.educationbackbutton.place(x=750, y=0)
        self.khanacademybutton= Button(self.educationframe, text = "KHAN ACADEMY", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.khanacademy)
        self.khanacademybutton.place(x=620,y=0)
        self.courserabutton= Button(self.educationframe, text = "COURSERA", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.coursera)
        self.courserabutton.place(x=520,y=0)
        self.w3schoolbutton= Button(self.educationframe, text = "W3 SCHOOL", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.w3school)
        self.w3schoolbutton.place(x=410,y=0)
        self.byjusbutton= Button(self.educationframe, text = "BYJU'S", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.byjus)
        self.byjusbutton.place(x=325,y=0)
        self.codeacademybutton= Button(self.educationframe, text = "CODE ACADEMY", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.codeacademy)
        self.codeacademybutton.place(x=190,y=0)
        self.logoutbutton = Button(self.educationframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.educationframe.place(x=260,y=120)

    def educationback(self):
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.categoryframe.place(x=260,y=120)
        
    def khanacademy(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.khanacademyframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.khanacademyframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.khanacademytitle = Label(self.khanacademyframe, text="KHAN ACADEMY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.khanacademytitle.place(x =0, y=40,relwidth=1)
        self.khanacademybackbutton = Button(self.khanacademyframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.khanacademybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.khanacademyframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.khanacademyframe,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.khanacademyframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.khanacademyframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.khanacademyframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.khanacademyframe,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.khanacademyframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.khanacademyframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.khanacademyframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.khanacademyframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.khanacademyframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.khanacademysubmitbutton = Button(self.khanacademyframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.khanacademysubmit)
        self.khanacademysubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.educationframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.khanacademyframe.place(x=260,y=120)

    def khanacademysubmit(self):
        self.updatebutton = Button(self.khanacademyframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.khanacademyupdates)
        self.updatebutton.place(x=420,y=360)
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        khanacademycursor.execute("insert into khanacademy values('"+self.name+"','"+str(self.teaching)+"','"+str(self.userfriendly)+"','"+str(self.service)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        khanacademycursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        khanacademyconn.close()

    def khanacademyupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.khanacademyupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.khanacademyupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.khanacademytitle = Label(self.khanacademyupdate, text="KHAN ACADEMY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.khanacademytitle.place(x =0, y=40,relwidth=1)
        self.khanacademybackbutton = Button(self.khanacademyupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.khanacademybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.khanacademyupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.khanacademyupdate,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.khanacademyupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.khanacademyupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.khanacademyupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.khanacademyupdate,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.khanacademyupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.khanacademyupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.khanacademyupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.khanacademyupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.khanacademyupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.khanacademysubmitbutton = Button(self.khanacademyupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.khanacademyupsubmit)
        self.khanacademysubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place(x=260,y=120)
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.educationframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.khanacademyframe.place_forget()

    def khanacademyupsubmit(self):
        khanacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        khanacademycursor = khanacademyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        khanacademycursor.execute("update khanacademy set teaching='"+str(self.teaching)+"',userfriendly='"+str(self.userfriendly)+"',service='"+str(self.service)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        khanacademycursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!!")
        khanacademyconn.close()


    def coursera(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.courseraframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.courseraframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.courseratitle = Label(self.courseraframe, text="COURSERA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.courseratitle.place(x =0, y=40,relwidth=1)
        self.courserabackbutton = Button(self.courseraframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.courserabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.courseraframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.courseraframe,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.courseraframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.courseraframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.courseraframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.courseraframe,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.courseraframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.courseraframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.courseraframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.courseraframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.courseraframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.courserasubmitbutton = Button(self.courseraframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.courserasubmit)
        self.courserasubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.educationframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.courseraframe.place(x=260,y=120)

    def courserasubmit(self):
        self.updatebutton = Button(self.courseraframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.courseraupdates)
        self.updatebutton.place(x=420,y=360)
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        courseracursor.execute("insert into coursera values('"+self.name+"','"+str(self.teaching)+"','"+str(self.userfriendly)+"','"+str(self.service)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        courseracursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        courseraconn.close()

    def courseraupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.courseraupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.courseraupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.courseratitle = Label(self.courseraupdate, text="COURSERA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.courseratitle.place(x =0, y=40,relwidth=1)
        self.courserabackbutton = Button(self.courseraupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.courserabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.courseraupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.courseraupdate,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.courseraupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.courseraupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.courseraupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.courseraupdate,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.courseraupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.courseraupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.courseraupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.courseraupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.courseraupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.courserasubmitbutton = Button(self.courseraupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.courseraupsubmit)
        self.courserasubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place(x=260,y=120)
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.educationframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.courseraframe.place_forget()
        
    def courseraupsubmit(self):
        courseraconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        courseracursor = courseraconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        courseracursor.execute("update coursera set teaching='"+str(self.teaching)+"',userfriendly='"+str(self.userfriendly)+"',service='"+str(self.service)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        courseracursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!!")
        courseraconn.close()

    def w3school(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.w3schoolframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.w3schoolframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.w3schooltitle = Label(self.w3schoolframe, text="W3 SCHOOL FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.w3schooltitle.place(x =0, y=40,relwidth=1)
        self.w3schoolbackbutton = Button(self.w3schoolframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.w3schoolbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.w3schoolframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.w3schoolframe,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.w3schoolframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.w3schoolframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.w3schoolframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.w3schoolframe,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.w3schoolframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.w3schoolframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.w3schoolframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.w3schoolframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.w3schoolframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.w3schoolsubmitbutton = Button(self.w3schoolframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.w3schoolsubmit)
        self.w3schoolsubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.educationframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.w3schoolframe.place(x=260,y=120)

    def w3schoolsubmit(self):
        self.updatebutton = Button(self.w3schoolframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.w3schoolupdates)
        self.updatebutton.place(x=420,y=360)
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        w3schoolcursor.execute("insert into w3school values('"+self.name+"','"+str(self.teaching)+"','"+str(self.userfriendly)+"','"+str(self.service)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        w3schoolcursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        w3schoolconn.close()

    def w3schoolupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.w3schoolupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.w3schoolupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.w3schooltitle = Label(self.w3schoolupdate, text="W3 SCHOOL FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.w3schooltitle.place(x =0, y=40,relwidth=1)
        self.w3schoolbackbutton = Button(self.w3schoolupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.w3schoolbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.w3schoolupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.w3schoolupdate,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.w3schoolupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.w3schoolupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.w3schoolupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.w3schoolupdate,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.w3schoolupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.w3schoolupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.w3schoolupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.w3schoolupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.w3schoolupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.w3schoolsubmitbutton = Button(self.w3schoolupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.w3schoolupsubmit)
        self.w3schoolsubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place(x=260,y=120)
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.educationframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.w3schoolframe.place_forget()

    def w3schoolupsubmit(self):
        w3schoolconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        w3schoolcursor = w3schoolconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        w3schoolcursor.execute("update w3school set teaching='"+str(self.teaching)+"',userfriendly='"+str(self.userfriendly)+"',service='"+str(self.service)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        w3schoolcursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!!")
        w3schoolconn.close()
        
    def byjus(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.byjusframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.byjusframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.byjustitle = Label(self.byjusframe, text="BYJU'S FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.byjustitle.place(x =0, y=40,relwidth=1)
        self.byjusbackbutton = Button(self.byjusframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.byjusbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.byjusframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.byjusframe,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.byjusframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.byjusframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.byjusframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.byjusframe,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.byjusframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.byjusframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.byjusframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.byjusframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.byjusframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.byjussubmitbutton = Button(self.byjusframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command = self.byjussubmit)
        self.byjussubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.educationframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.byjusframe.place(x=260,y=120)

    def byjussubmit(self):
        self.updatebutton = Button(self.byjusframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.byjusupdates)
        self.updatebutton.place(x=420,y=360)
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        byjuscursor.execute("insert into byjus values('"+self.name+"','"+str(self.teaching)+"','"+str(self.userfriendly)+"','"+str(self.service)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        byjuscursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        byjusconn.close()

    def byjusupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.byjusupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.byjusupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.byjustitle = Label(self.byjusupdate, text="BYJU'S FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.byjustitle.place(x =0, y=40,relwidth=1)
        self.byjusbackbutton = Button(self.byjusupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.byjusbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.byjusupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.byjusupdate,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.byjusupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.byjusupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.byjusupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.byjusupdate,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.byjusupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.byjusupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.byjusupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.byjusupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.byjusupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.byjussubmitbutton = Button(self.byjusupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command = self.byjusupsubmit)
        self.byjussubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place(x=260,y=120)
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.educationframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.byjusframe.place_forget()

    def byjusupsubmit(self):
        byjusconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        byjuscursor = byjusconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        byjuscursor.execute("update byjus set teaching='"+str(self.teaching)+"',userfriendly='"+str(self.userfriendly)+"',service='"+str(self.service)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        byjuscursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!!")
        byjusconn.close()
        
    def codeacademy(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.codeacademyframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.codeacademyframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.codeacademytitle = Label(self.codeacademyframe, text="CODE ACADEMY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.codeacademytitle.place(x =0, y=40,relwidth=1)
        self.codeacademybackbutton = Button(self.codeacademyframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.codeacademybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.codeacademyframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.codeacademyframe,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.codeacademyframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.codeacademyframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.codeacademyframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.codeacademyframe,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.codeacademyframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.codeacademyframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.codeacademyframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.codeacademyframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.codeacademyframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.codeacademysubmitbutton = Button(self.codeacademyframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.codeacademysubmit)
        self.codeacademysubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.educationframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.codeacademyframe.place(x=260,y=120)
        
    def codeacademysubmit(self):
        self.updatebutton = Button(self.codeacademyframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.codeacademyupdates)
        self.updatebutton.place(x=420,y=360)
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        codeacademycursor.execute("insert into codeacademy values('"+self.name+"','"+str(self.teaching)+"','"+str(self.userfriendly)+"','"+str(self.service)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        codeacademycursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        codeacademyconn.close()

    def codeacademyupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.codeacademyupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.codeacademyupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.codeacademytitle = Label(self.codeacademyupdate, text="CODE ACADEMY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.codeacademytitle.place(x =0, y=40,relwidth=1)
        self.codeacademybackbutton = Button(self.codeacademyupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.education)
        self.codeacademybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.codeacademyupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.codeacademyupdate,text ="TEACHING QUALITY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.codeacademyupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.codeacademyupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.codeacademyupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.codeacademyupdate,text ="SERVICE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.codeacademyupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.codeacademyupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.codeacademyupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.codeacademyupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.codeacademyupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.codeacademysubmitbutton = Button(self.codeacademyupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.codeacademyupsubmit)
        self.codeacademysubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place(x=260,y=120)
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.foodframe.place_forget()
        self.travelframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.educationframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.codeacademyframe.place_forget()
        
    def codeacademyupsubmit(self):
        codeacademyconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "education")
        codeacademycursor = codeacademyconn.cursor()
        if self.first.get == "EXCELLENT":
            self.teaching = 5
        if self.first.get() == "GOOD":
            self.teaching = 4
        if self.first.get() == "AVERAGE":
            self.teaching = 3
        if self.first.get() == "BAD":
            self.teaching = 2
        if self.first.get() == "WORST":
            self.teaching = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.service = 5
        if self.third.get() == "GOOD":
            self.service = 4
        if self.third.get() == "AVERAGE":
            self.service = 3
        if self.third.get() == "BAD":
            self.service = 2
        if self.third.get() == "WORST":
            self.service = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        codeacademycursor.execute("update codeacademy set teaching='"+str(self.teaching)+"',userfriendly='"+str(self.userfriendly)+"',service='"+str(self.service)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        codeacademycursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED !!!")
        codeacademyconn.close()

    def shop(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.shopframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.shopframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.shoptitle = Label(self.shopframe, text="SHOP FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.shoptitle.place(x =0, y=40,relwidth=1)
        self.shopbackbutton = Button(self.shopframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shopback)
        self.shopbackbutton.place(x=750, y=0)
        self.amazonbutton= Button(self.shopframe, text = "AMAZON", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.amazon)
        self.amazonbutton.place(x=650,y=0)
        self.flipkartbutton= Button(self.shopframe, text = "FLIPKART", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.flipkart)
        self.flipkartbutton.place(x=550,y=0)
        self.ebaybutton= Button(self.shopframe, text = "EBAY", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.ebay)
        self.ebaybutton.place(x=480,y=0)
        self.walmartbutton= Button(self.shopframe, text = "WALMART", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.walmart)
        self.walmartbutton.place(x=380,y=0)
        self.alibababutton= Button(self.shopframe, text = "ALI BABA", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.alibaba)
        self.alibababutton.place(x=280,y=0)
        self.logoutbutton = Button(self.shopframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.shopframe.place(x=260,y=120)

    def shopback(self):
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.categoryframe.place(x=260,y=120)

    def amazon(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.amazonframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.amazonframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.amazontitle = Label(self.amazonframe, text="AMAZON FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.amazontitle.place(x =0, y=40,relwidth=1)
        self.amazonbackbutton = Button(self.amazonframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.amazonbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.amazonframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.amazonframe,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.amazonframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.amazonframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.amazonframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.amazonframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.amazonframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.amazonframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.amazonframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.amazonframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.amazonframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.amazonsubmitbutton = Button(self.amazonframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.amazonsubmit)
        self.amazonsubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.shopframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.amazonframe.place(x=260,y=120)
        
    def amazonsubmit(self):
        self.updatebutton = Button(self.amazonframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command = self.amazonupdates)
        self.updatebutton.place(x=420,y=360)
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        amazoncursor.execute("insert into amazon values('"+self.name+"','"+str(self.service)+"','"+str(self.userfriendly)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        amazoncursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        amazonconn.close()

    def amazonupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.amazonupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.amazonupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.amazontitle = Label(self.amazonupdate, text="AMAZON FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.amazontitle.place(x =0, y=40,relwidth=1)
        self.amazonbackbutton = Button(self.amazonupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.amazonbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.amazonupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.amazonupdate,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.amazonupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.amazonupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.amazonupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.amazonupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.amazonupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.amazonupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.amazonupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.amazonupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.amazonupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.amazonsubmitbutton = Button(self.amazonupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.amazonupsubmit)
        self.amazonsubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place(x=260,y=120)
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.shopframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.amazonframe.place_forget()
        
    def amazonupsubmit(self):
        amazonconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        amazoncursor = amazonconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        amazoncursor.execute("update amazon set service='"+str(self.service)+"',userfriendly='"+str(self.userfriendly)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        amazoncursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!")
        amazonconn.close()
        
    def flipkart(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.flipkartframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.flipkartframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.flipkarttitle = Label(self.flipkartframe, text="FLIPKART FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.flipkarttitle.place(x =0, y=40,relwidth=1)
        self.flipkartbackbutton = Button(self.flipkartframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.flipkartbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.flipkartframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.flipkartframe,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.flipkartframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.flipkartframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.flipkartframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.flipkartframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.flipkartframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.flipkartframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.flipkartframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.flipkartframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.flipkartframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.flipkartsubmitbutton = Button(self.flipkartframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.flipkartsubmit)
        self.flipkartsubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.shopframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.flipkartframe.place(x=260,y=120)

    def flipkartsubmit(self):
        self.updatebutton = Button(self.flipkartframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.flipkartupdates)
        self.updatebutton.place(x=420,y=360)
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        flipkartcursor.execute("insert into flipkart values('"+self.name+"','"+str(self.service)+"','"+str(self.userfriendly)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        flipkartcursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        flipkartconn.close()

    def flipkartupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.flipkartupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.flipkartupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.flipkarttitle = Label(self.flipkartupdate, text="FLIPKART FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.flipkarttitle.place(x =0, y=40,relwidth=1)
        self.flipkartbackbutton = Button(self.flipkartupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.flipkartbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.flipkartupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.flipkartupdate,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.flipkartupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.flipkartupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.flipkartupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.flipkartupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.flipkartupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.flipkartupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.flipkartupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.flipkartupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.flipkartupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.flipkartsubmitbutton = Button(self.flipkartupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.flipkartupsubmit)
        self.flipkartsubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place(x=260,y=120)
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.shopframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.flipkartframe.place_forget()

    def flipkartupsubmit(self):
        flipkartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        flipkartcursor = flipkartconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        flipkartcursor.execute("update flipkart set service='"+str(self.service)+"',userfriendly='"+str(self.userfriendly)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        flipkartcursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!")
        flipkartconn.close()        

    def ebay(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.ebayframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.ebayframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.ebaytitle = Label(self.ebayframe, text="E-BAY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.ebaytitle.place(x =0, y=40,relwidth=1)
        self.ebaybackbutton = Button(self.ebayframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.ebaybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.ebayframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.ebayframe,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.ebayframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.ebayframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.ebayframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.ebayframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.ebayframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.ebayframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.ebayframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.ebayframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.ebayframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.ebaysubmitbutton = Button(self.ebayframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.ebaysubmit)
        self.ebaysubmitbutton.place(x=200,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.shopframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.ebayframe.place(x=260,y=120)

    def ebaysubmit(self):
        self.updatebutton = Button(self.ebayframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.ebayupdates)
        self.updatebutton.place(x=420,y=360)
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        ebaycursor.execute("insert into ebay values('"+self.name+"','"+str(self.service)+"','"+str(self.userfriendly)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        ebaycursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        ebayconn.close()

    def ebayupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.ebayupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.ebayupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.ebaytitle = Label(self.ebayupdate, text="E-BAY FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.ebaytitle.place(x =0, y=40,relwidth=1)
        self.ebaybackbutton = Button(self.ebayupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.ebaybackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.ebayupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.ebayupdate,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.ebayupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.ebayupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.ebayupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.ebayupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.ebayupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.ebayupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.ebayupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.ebayupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.ebayupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.ebaysubmitbutton = Button(self.ebayupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.ebayupsubmit)
        self.ebaysubmitbutton.place(x=360,y=360)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place(x=260,y=120)
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.shopframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.ebayframe.place_forget()

    def ebayupsubmit(self):
        ebayconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        ebaycursor = ebayconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        ebaycursor.execute("update ebay set service='"+str(self.service)+"',userfriendly='"+str(self.userfriendly)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        ebaycursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!")
        ebayconn.close()
        
    def walmart(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.walmartframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.walmartframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.walmarttitle = Label(self.walmartframe, text="WALMART FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.walmarttitle.place(x =0, y=40,relwidth=1)
        self.walmartbackbutton = Button(self.walmartframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.walmartbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.walmartframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.walmartframe,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.walmartframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.walmartframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.walmartframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.walmartframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.walmartframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.walmartframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.walmartframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.walmartframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.walmartframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.walmartsubmitbutton = Button(self.walmartframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.walmartsubmit)
        self.walmartsubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.shopframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.walmartframe.place(x=260,y=120)

    def walmartsubmit(self):
        self.updatebutton = Button(self.walmartframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.walmartupdates)
        self.updatebutton.place(x=420,y=360)
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        walmartcursor.execute("insert into walmart values('"+self.name+"','"+str(self.service)+"','"+str(self.userfriendly)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        walmartcursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        walmartconn.close()

    def walmartupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.walmartupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.walmartupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.walmarttitle = Label(self.walmartupdate, text="WALMART FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.walmarttitle.place(x =0, y=40,relwidth=1)
        self.walmartbackbutton = Button(self.walmartupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.walmartbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.walmartupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.walmartupdate,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.walmartupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.walmartupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.walmartupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.walmartupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.walmartupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.walmartupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.walmartupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.walmartupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.walmartupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.walmartsubmitbutton = Button(self.walmartupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.walmartupsubmit)
        self.walmartsubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place(x=260,y=120)
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.shopframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.walmartframe.place_forget()

    def walmartupsubmit(self):
        walmartconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        walmartcursor = walmartconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        walmartcursor.execute("update walmart set service='"+str(self.service)+"',userfriendly='"+str(self.userfriendly)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        walmartcursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!")
        walmartconn.close()       

    def alibaba(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.alibabaframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.alibabaframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.alibabatitle = Label(self.alibabaframe, text="ALI BABA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.alibabatitle.place(x =0, y=40,relwidth=1)
        self.alibababackbutton = Button(self.alibabaframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.alibababackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.alibabaframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.alibabaframe,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.alibabaframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.alibabaframe,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.alibabaframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.alibabaframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.alibabaframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.alibabaframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.alibabaframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.alibabaframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.alibabaframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.alibabasubmitbutton = Button(self.alibabaframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command = self.alibabasubmit)
        self.alibabasubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.shopframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.alibabaframe.place(x=260,y=120)
        
    def alibabasubmit(self):
        self.updatebutton = Button(self.alibabaframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.alibabaupdates)
        self.updatebutton.place(x=420,y=360)
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        alibabacursor.execute("insert into alibaba values('"+self.name+"','"+str(self.service)+"','"+str(self.userfriendly)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        alibabacursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        alibabaconn.close()

    def alibabaupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.alibabaupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.alibabaupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.alibabatitle = Label(self.alibabaupdate, text="ALI BABA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.alibabatitle.place(x =0, y=40,relwidth=1)
        self.alibababackbutton = Button(self.alibabaupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.shop)
        self.alibababackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.alibabaupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.alibabaupdate,text ="SERVICES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.alibabaupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.alibabaupdate,text ="USER FRIENDLY",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.alibabaupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.alibabaupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.alibabaupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.alibabaupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.alibabaupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.alibabaupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.alibabaupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.alibabasubmitbutton = Button(self.alibabaupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE, command = self.alibabaupsubmit)
        self.alibabasubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place(x=260,y=120)
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.shopframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.alibabaframe.place_forget()
        
    def alibabaupsubmit(self):
        alibabaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "shop")
        alibabacursor = alibabaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.service = 5
        if self.first.get() == "GOOD":
            self.service = 4
        if self.first.get() == "AVERAGE":
            self.service = 3
        if self.first.get() == "BAD":
            self.service = 2
        if self.first.get() == "WORST":
            self.service = 1
        if self.second.get == "EXCELLENT":
            self.userfriendly = 5
        if self.second.get() == "GOOD":
            self.userfriendly = 4
        if self.second.get() == "AVERAGE":
            self.userfriendly = 3
        if self.second.get() == "BAD":
            self.userfriendly = 2
        if self.second.get() == "WORST":
            self.userfriendly = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        alibabacursor.execute("update alibaba set service='"+str(self.service)+"',userfriendly='"+str(self.userfriendly)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        alibabacursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!")
        alibabaconn.close()
        
    def cab(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.cabframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.cabframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.cabtitle = Label(self.cabframe, text="CAB FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.cabtitle.place(x =0, y=40,relwidth=1)
        self.cabbackbutton = Button(self.cabframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cabback)
        self.cabbackbutton.place(x=750, y=0)
        self.uberbutton= Button(self.cabframe, text = "UBER", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.uber)
        self.uberbutton.place(x=680,y=0)
        self.olabutton= Button(self.cabframe, text = "OLA", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.ola)
        self.olabutton.place(x=615,y=0)
        self.merubutton= Button(self.cabframe, text = "MERU", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.meru)
        self.merubutton.place(x=540,y=0)
        self.savaaributton= Button(self.cabframe, text = "SAVAARI", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.savaari)
        self.savaaributton.place(x=445,y=0)
        self.bharattaxibutton= Button(self.cabframe, text = "BHARAT TAXI", font = ("Comic Sans Ms",10),bg = "#efefef",fg="green",bd = 5, relief = RIDGE,command = self.bharattaxi)
        self.bharattaxibutton.place(x=315,y=0)
        self.logoutbutton = Button(self.cabframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.homeframe.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.cabframe.place(x=260,y=120)

    def cabback(self):
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.userframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.categoryframe.place(x=260,y=120)
        
    def uber(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.uberframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.uberframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.ubertitle = Label(self.uberframe, text="UBER FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.ubertitle.place(x =0, y=40,relwidth=1)
        self.uberbackbutton = Button(self.uberframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.uberbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.uberframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)        
        self.questionone = Label(self.uberframe,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.uberframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.uberframe,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.uberframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.uberframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.uberframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.uberframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.uberframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.uberframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.uberframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.ubersubmitbutton = Button(self.uberframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.ubersubmit)
        self.ubersubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.cabframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.uberframe.place(x=260,y=120)

    def ubersubmit(self):
        self.updatebutton = Button(self.uberframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.uberupdates)
        self.updatebutton.place(x=420,y=360)
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        ubercursor.execute("insert into uber values('"+self.name+"','"+str(self.convenient)+"','"+str(self.drivers)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        ubercursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        uberconn.close()

    def uberupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.uberupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.uberupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.ubertitle = Label(self.uberupdate, text="UBER FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.ubertitle.place(x =0, y=40,relwidth=1)
        self.uberbackbutton = Button(self.uberupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.uberbackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.uberupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)        
        self.questionone = Label(self.uberupdate,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.uberupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.uberupdate,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.uberupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.uberupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.uberupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.uberupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.uberupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.uberupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.uberupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.ubersubmitbutton = Button(self.uberupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.uberupsubmit)
        self.ubersubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place(x=260,y=120)
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.cabframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.uberframe.place_forget()

    def uberupsubmit(self):
        uberconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        ubercursor = uberconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        ubercursor.execute("update uber set convenient='"+str(self.convenient)+"',drivers='"+str(self.drivers)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        ubercursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!!")
        uberconn.close()        

    def ola(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.olaframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.olaframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.olatitle = Label(self.olaframe, text="OLA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.olatitle.place(x =0, y=40,relwidth=1)
        self.olabackbutton = Button(self.olaframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.olabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.olaframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.olaframe,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.olaframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.olaframe,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.olaframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.olaframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.olaframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.olaframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.olaframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.olaframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.olaframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.olasubmitbutton = Button(self.olaframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.olasubmit)
        self.olasubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.cabframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.shopframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.olaframe.place(x=260,y=120)

    def olasubmit(self):
        self.updatebutton = Button(self.olaframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.olaupdates)
        self.updatebutton.place(x=420,y=360)
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        olacursor.execute("insert into ola values('"+self.name+"','"+str(self.convenient)+"','"+str(self.drivers)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        olacursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        olaconn.close()

    def olaupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.olaupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.olaupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.olatitle = Label(self.olaupdate, text="OLA FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.olatitle.place(x =0, y=40,relwidth=1)
        self.olabackbutton = Button(self.olaupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.olabackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.olaupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.olaupdate,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.olaupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.olaupdate,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.olaupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.olaupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.olaupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.olaupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.olaupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.olaupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.olaupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.olasubmitbutton = Button(self.olaupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.olaupsubmit)
        self.olasubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place(x=260,y=120)
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.cabframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.shopframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.olaframe.place_forget()

    def olaupsubmit(self):
        olaconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        olacursor = olaconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        olacursor.execute("update ola set convenient='"+str(self.convenient)+"',drivers='"+str(self.drivers)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        olacursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!!")
        olaconn.close()        
        
    def meru(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.meruframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.meruframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.merutitle = Label(self.meruframe, text="MERU FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.merutitle.place(x =0, y=40,relwidth=1)
        self.merubackbutton = Button(self.meruframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.merubackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.meruframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.meruframe,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.meruframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.meruframe,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.meruframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.meruframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.meruframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.meruframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.meruframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.meruframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.meruframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.merusubmitbutton = Button(self.meruframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.merusubmit)
        self.merusubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.cabframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.meruframe.place(x=260,y=120)

    def merusubmit(self):
        self.updatebutton = Button(self.meruframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.meruupdates)
        self.updatebutton.place(x=420,y=360)
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        merucursor.execute("insert into meru values('"+self.name+"','"+str(self.convenient)+"','"+str(self.drivers)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        merucursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        meruconn.close()

    def meruupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.meruupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.meruupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.merutitle = Label(self.meruupdate, text="MERU FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.merutitle.place(x =0, y=40,relwidth=1)
        self.merubackbutton = Button(self.meruupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.merubackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.meruupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.meruupdate,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.meruupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.meruupdate,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.meruupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.meruupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.meruupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.meruupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.meruupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.meruupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.meruupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.merusubmitbutton = Button(self.meruupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.meruupsubmit)
        self.merusubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place(x=260,y=120)
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.cabframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.meruframe.place_forget()

    def meruupsubmit(self):
        meruconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        merucursor = meruconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        merucursor.execute("update meru set convenient='"+str(self.convenient)+"',drivers='"+str(self.drivers)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        merucursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!!")
        meruconn.close()       

    def savaari(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.savaariframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.savaariframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.savaarititle = Label(self.savaariframe, text="SAVAARI FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.savaarititle.place(x =0, y=40,relwidth=1)
        self.savaaribackbutton = Button(self.savaariframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.savaaribackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.savaariframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.savaariframe,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.savaariframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.savaariframe,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.savaariframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.savaariframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.savaariframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.savaariframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.savaariframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.savaariframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.savaariframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.savaarisubmitbutton = Button(self.savaariframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.savaarisubmit)
        self.savaarisubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()       
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.cabframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.savaariframe.place(x=260,y=120)

    def savaarisubmit(self):
        self.updatebutton = Button(self.savaariframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.savaariupdates)
        self.updatebutton.place(x=420,y=360)
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        savaaricursor.execute("insert into savaari values('"+self.name+"','"+str(self.convenient)+"','"+str(self.drivers)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        savaaricursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        savaariconn.close()

    def savaariupdates(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.savaariupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.savaariupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.savaarititle = Label(self.savaariupdate, text="SAVAARI FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.savaarititle.place(x =0, y=40,relwidth=1)
        self.savaaribackbutton = Button(self.savaariupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.savaaribackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.savaariupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.savaariupdate,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.savaariupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.savaariupdate,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.savaariupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.savaariupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.savaariupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.savaariupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.savaariupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.savaariupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.savaariupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.savaarisubmitbutton = Button(self.savaariupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.savaariupsubmit)
        self.savaarisubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.tandcframe.place_forget()       
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place(x=260,y=120)
        self.bharattaxiupdate.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.cabframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.savaariframe.place_forget()

    def savaariupsubmit(self):
        savaariconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        savaaricursor = savaariconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        savaaricursor.execute("update savaari set convenient='"+str(self.convenient)+"',drivers='"+str(self.drivers)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        savaaricursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!!")
        savaariconn.close()        
        
    def bharattaxi(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.bharattaxiframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.bharattaxiframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.bharattaxititle = Label(self.bharattaxiframe, text="BHARAT TAXI FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.bharattaxititle.place(x =0, y=40,relwidth=1)
        self.bharattaxibackbutton = Button(self.bharattaxiframe, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.bharattaxibackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.bharattaxiframe, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.bharattaxiframe,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.bharattaxiframe,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.bharattaxiframe,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.bharattaxiframe,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.bharattaxiframe,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.bharattaxiframe,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.bharattaxiframe,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.bharattaxiframe,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.bharattaxiframe,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.bharattaxiframe,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.bharattaxisubmitbutton = Button(self.bharattaxiframe, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.bharattaxisubmit)
        self.bharattaxisubmitbutton.place(x=200,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.cabframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.bharattaxiframe.place(x=260,y=120)

    def bharattaxisubmit(self):
        self.updatebutton = Button(self.bharattaxiframe,text = "EDIT REVIEW", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg="green",relief = RIDGE,command=self.bharattaxiupdates)
        self.updatebutton.place(x=420,y=360)
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        bharattaxicursor.execute("insert into bharattaxi values('"+self.name+"','"+str(self.convenient)+"','"+str(self.drivers)+"','"+str(self.customer)+"','"+str(self.comparison)+"','"+str(self.overall)+"')")
        bharattaxicursor.execute("commit")
        messagebox.showinfo("submit","THANKS FOR FEEDBACK")
        bharattaxiconn.close()

    def bharattaxiupdates(self):        
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.bharattaxiupdate, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.bharattaxiupdate, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.bharattaxititle = Label(self.bharattaxiupdate, text="BHARAT TAXI FEEDBACK PAGE", font=("Comic Sans Ms",25),fg = "green")
        self.bharattaxititle.place(x =0, y=40,relwidth=1)
        self.bharattaxibackbutton = Button(self.bharattaxiupdate, text = "BACK", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.cab)
        self.bharattaxibackbutton.place(x=750, y=0)
        self.logoutbutton = Button(self.bharattaxiupdate, text = "LOGOUT", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.userlogout)
        self.logoutbutton.place(x=0, y=0)
        self.questionone = Label(self.bharattaxiupdate,text ="CONVENIENT",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionone.place(x=200,y=100)
        self.first = StringVar()
        self.first.set("SELECT ONE")
        self.answerone = OptionMenu(self.bharattaxiupdate,self.first,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerone.place(x=450,y=100)
        self.questiontwo = Label(self.bharattaxiupdate,text ="DRIVERS",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questiontwo.place(x=200,y=150)
        self.second = StringVar()
        self.second.set("SELECT ONE")
        self.answertwo = OptionMenu(self.bharattaxiupdate,self.second,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answertwo.place(x=450,y=150)
        self.questionthree = Label(self.bharattaxiupdate,text ="CUSTOMER CARE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionthree.place(x=200,y=200)
        self.third = StringVar()
        self.third.set("SELECT ONE")
        self.answerthree = OptionMenu(self.bharattaxiupdate,self.third,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerthree.place(x=450,y=200)
        self.questionfour = Label(self.bharattaxiupdate,text ="COMPARE TO OTHER SITES",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfour.place(x=200,y=250)
        self.fourth = StringVar()
        self.fourth.set("SELECT ONE")
        self.answerfour = OptionMenu(self.bharattaxiupdate,self.fourth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfour.place(x=450,y=250)
        self.questionfive = Label(self.bharattaxiupdate,text ="OVERALL EXPERIENCE",font =("Comic Sans Ms",13,"bold"),fg = "green")
        self.questionfive.place(x=200,y=300)
        self.fifth = StringVar()
        self.fifth.set("SELECT ONE")
        self.answerfive = OptionMenu(self.bharattaxiupdate,self.fifth,"EXCELLENT","GOOD","AVERAGE","BAD","WORST")
        self.answerfive.place(x=450,y=300)
        self.bharattaxisubmitbutton = Button(self.bharattaxiupdate, text ="SUBMIT", font=("Comic Sans Ms",13),bg ="#efefef",bd=5,fg = "green",relief = RIDGE,command = self.bharattaxiupsubmit)
        self.bharattaxisubmitbutton.place(x=360,y=360)
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place(x=260,y=120)
        self.tandcframe.place_forget()        
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.aboutusframe.place_forget()
        self.registerframe.place_forget()
        self.adminframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.travelframe.place_forget()
        self.educationframe.place_forget()
        self.foodframe.place_forget()
        self.shopframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.cabframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.bharattaxiframe.place_forget()

    def bharattaxiupsubmit(self):
        bharattaxiconn = mysql.connector.connect(host = "localhost", user = "root",passwd="1234", database = "cab")
        bharattaxicursor = bharattaxiconn.cursor()
        if self.first.get == "EXCELLENT":
            self.convenient = 5
        if self.first.get() == "GOOD":
            self.convenient = 4
        if self.first.get() == "AVERAGE":
            self.convenient = 3
        if self.first.get() == "BAD":
            self.convenient = 2
        if self.first.get() == "WORST":
            self.convenient = 1
        if self.second.get == "EXCELLENT":
            self.drivers = 5
        if self.second.get() == "GOOD":
            self.drivers = 4
        if self.second.get() == "AVERAGE":
            self.drivers = 3
        if self.second.get() == "BAD":
            self.drivers = 2
        if self.second.get() == "WORST":
            self.drivers = 1
        if self.third.get() == "EXCELLENT":
            self.customer = 5
        if self.third.get() == "GOOD":
            self.customer = 4
        if self.third.get() == "AVERAGE":
            self.customer = 3
        if self.third.get() == "BAD":
            self.customer = 2
        if self.third.get() == "WORST":
            self.customer = 1
        if self.fourth.get() == "EXCELLENT":
            self.comparison = 5
        if self.fourth.get() == "GOOD":
            self.comparison = 4
        if self.fourth.get() == "AVERAGE":
            self.comparison = 3
        if self.fourth.get() == "BAD":
            self.comparison = 2
        if self.fourth.get() == "WORST":
            self.comparison = 1
        if self.fifth.get() == "EXCELLENT":
            self.overall = 5
        if self.fifth.get() == "GOOD":
            self.overall = 4
        if self.fifth.get() == "AVERAGE":
            self.overall = 3
        if self.fifth.get() == "BAD":
            self.overall = 2
        if self.fifth.get() == "WORST":
            self.overall = 1
            
        bharattaxicursor.execute("update bharattaxi set convenient='"+str(self.convenient)+"',drivers='"+str(self.drivers)+"',customer_care='"+str(self.customer)+"',comparison='"+str(self.comparison)+"',overall='"+str(self.overall)+"' where name='"+self.name+"'")
        bharattaxicursor.execute("commit")
        messagebox.showinfo("submit","FEEDBACK UPDATED!!!")
        bharattaxiconn.close()
            
    def userlogout(self):
        self.ppframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.tandcframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminframe.place_forget()
        self.homeframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.contactusframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.travelframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.userframe.place(x=260,y=120)       

    def contactuspage(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.contactusframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.contactusframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.contactusframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.contactusframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.contactusframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.contactusframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.contactusframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.contacttitle = Label(self.contactusframe, text="THIS IS CONTACT US PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.contacttitle.place(x =0, y=40,relwidth=1)
        self.mytitle = Label(self.contactusframe,text ="PUT WHATEVER YOU WANT HERE :)",font=("Comic Sans Ms",15),fg="blue")
        self.mytitle.place(x=20, y=100,relwidth=1)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.aboutusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.viewframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.contactusframe.place(x=260,y=120)

    def aboutuspage(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.aboutusframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.aboutusframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.aboutusframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.aboutusframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.aboutusframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.aboutusframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.aboutusframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.aboutustitle = Label(self.aboutusframe, text="THIS IS ABOUT US PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.aboutustitle.place(x =0, y=40,relwidth=1)
        self.mytitle = Label(self.aboutusframe,text ="PUT WHATEVER YOU WANT HERE :)",font=("Comic Sans Ms",15),fg="blue")
        self.mytitle.place(x=20, y=100,relwidth=1)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.ppframe.place_forget()
        self.tandcframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.viewframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.aboutusframe.place(x=260,y=120)
    
    def pp(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.ppframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.ppframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.ppframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.ppframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.ppframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.ppframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.ppframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.pptitle = Label(self.ppframe, text="THIS IS PRIVATE POLICY POLICY", font=("Comic Sans Ms",15),fg = "green")
        self.pptitle.place(x =0, y=40,relwidth=1)
        self.mytitle = Label(self.ppframe,text ="PUT PRIVATE POLICIES HERE :)",font=("Comic Sans Ms",15),fg="blue")
        self.mytitle.place(x=20, y=100,relwidth=1)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.aboutusframe.place_forget()
        self.tandcframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.viewframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.ppframe.place(x=260,y=120)

    def tandc(self):
        self.feed_img = ImageTk.PhotoImage(file = "paper.jpg")
        self.feed_img = Label(self.tandcframe, image = self.feed_img)
        self.feed_img.pack()
        self.navbar = Label(self.tandcframe, text = "", font = ("Comic Sans Ms",15), bg ="#efefef" ,fg="white", bd=5, relief = RIDGE)
        self.navbar.place(x=0,y=0,relwidth=1)
        self.homebutton = Button(self.tandcframe, text = "HOME", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command=self.homepage)
        self.homebutton.place(x=2, y=0)
        self.adminbutton = Button(self.tandcframe, text = "ADMIN", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.adminpage)
        self.adminbutton.place(x=80, y=0)
        self.userbutton = Button(self.tandcframe, text = "USER", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.userpage)
        self.userbutton.place(x = 165, y=0)
        self.contactusbutton = Button(self.tandcframe, text = "CONTACT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE, command = self.contactuspage)
        self.contactusbutton.place(x=240, y =0)
        self.aboutusbutton = Button(self.tandcframe, text = "ABOUT US", font = ("Comic Sans Ms",10), bg ="#efefef", fg="green", bd = 5, relief = RIDGE,command = self.aboutuspage)
        self.aboutusbutton.place(x=360, y=0)
        self.tandctitle = Label(self.tandcframe, text="THIS IS TERMS AND CONDITIONS PAGE", font=("Comic Sans Ms",15),fg = "green")
        self.tandctitle.place(x =0, y=40,relwidth=1)
        self.mytitle = Label(self.tandcframe,text ="PUT TERMS AND CONDITIONS HERE :)",font=("Comic Sans Ms",15),fg="blue")
        self.mytitle.place(x=20, y=100,relwidth=1)
        self.homeframe.place_forget()
        self.makemytripupdate.place_forget()
        self.goibiboupdate.place_forget()
        self.yatraupdate.place_forget()
        self.easetripupdate.place_forget()
        self.trivagoupdate.place_forget()
        self.foodpandaupdate.place_forget()
        self.zomatoupdate.place_forget()
        self.swiggyupdate.place_forget()
        self.freshmenuupdate.place_forget()
        self.foodmingoupdate.place_forget()
        self.khanacademyupdate.place_forget()
        self.courseraupdate.place_forget()
        self.w3schoolupdate.place_forget()
        self.byjusupdate.place_forget()
        self.codeacademyupdate.place_forget()
        self.amazonupdate.place_forget()
        self.flipkartupdate.place_forget()
        self.ebayupdate.place_forget()
        self.walmartupdate.place_forget()
        self.alibabaupdate.place_forget()
        self.uberupdate.place_forget()
        self.olaupdate.place_forget()
        self.meruupdate.place_forget()
        self.savaariupdate.place_forget()
        self.bharattaxiupdate.place_forget()
        self.aboutusframe.place_forget()
        self.ppframe.place_forget()
        self.adminframe.place_forget()
        self.userframe.place_forget()
        self.contactusframe.place_forget()
        self.userfeedbackframe.place_forget()
        self.adminloginframe.place_forget()
        self.viewframe.place_forget()
        self.registerframe.place_forget()
        self.categoryframe.place_forget()
        self.travelframe.place_forget()
        self.foodframe.place_forget()
        self.educationframe.place_forget()
        self.shopframe.place_forget()
        self.cabframe.place_forget()
        self.makemytripframe.place_forget()
        self.goibiboframe.place_forget()
        self.yatraframe.place_forget()
        self.easetripframe.place_forget()
        self.trivagoframe.place_forget()
        self.foodpandaframe.place_forget()
        self.zomatoframe.place_forget()
        self.swiggyframe.place_forget()
        self.freshmenuframe.place_forget()
        self.foodmingoframe.place_forget()
        self.khanacademyframe.place_forget()
        self.courseraframe.place_forget()
        self.w3schoolframe.place_forget()
        self.byjusframe.place_forget()
        self.codeacademyframe.place_forget()
        self.amazonframe.place_forget()
        self.flipkartframe.place_forget()
        self.ebayframe.place_forget()
        self.walmartframe.place_forget()
        self.alibabaframe.place_forget()
        self.uberframe.place_forget()
        self.olaframe.place_forget()
        self.meruframe.place_forget()
        self.savaariframe.place_forget()
        self.bharattaxiframe.place_forget()
        self.travelviewframe.place_forget()
        self.foodviewframe.place_forget()
        self.educationviewframe.place_forget()
        self.shoppingviewframe.place_forget()
        self.cabviewframe.place_forget()
        self.tandcframe.place(x=260,y=120)

root = Tk()
feed = Feedback(root)
root.mainloop()

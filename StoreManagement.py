#importing statements
from tkinter import *
from fpdf import FPDF
import numpy as np
import mysql.connector as msc
import pandas as pd
import webbrowser

#making first screen(welcome screen)
v1 = "firebrick1"
tk = Tk()
tk.title("Store Management")
tk.configure(background=v1)
tk.state("zoomed")

#defining main function or functioning of program on which it runs
def main_func():
    t0 = Tk()
    t0.title("Store Management")
    t0.configure(background=v1)
    t0.state("zoomed")
    l1=Label(text = "Select your choice:\n",font = ("arial",72,"bold"),
            bg = v1,activeforeground = "blue2",
             activebackground = v1,
           fg ="blue2",width = 24,height=3,)
    l1.pack()
    b1 = Button(text = "View store items and their details",font = ("arial",36,"bold"),
                bg = v1,activeforeground = "blue2",
                activebackground = v1,
               fg ="blue2",width = 40,height=2,
                command=lambda:one())
    b1.pack()
    b2 = Button(text = "Add new item in store",font = ("arial",36,"bold"),
                bg = v1,activeforeground = "blue2",
                activebackground = v1,
               fg ="blue2",width = 40,height=2,
                command=lambda:two())
    b2.pack()
    b3 = Button(text = "Costumer transaction",font = ("arial",36,"bold"),
                bg = v1,activeforeground = "blue2",
                activebackground = v1,
               fg ="blue2",width = 40,height=2,
                command=lambda:three())
    b3.pack()
    
    #defining primary functioning through which we can saw stock items and their details  
    def one():
    #creating a new screen for function which gives stock details
        t0.destroy()        
        t1 = Tk()
        t1.title("Store Management")
        t1.configure(background=v1)
        t1.state("zoomed")
        l1 = Label(text = "Store items and their details:",
                   font = ("arial",48,"bold"),
                    bg = v1,activeforeground = "blue2",
                   activebackground = v1,
                    fg ="blue2",width = 40,height=2)
        l1.pack()
        #assigning working for function which gives stock details
        cursor.execute("select * from product")
        product_data = cursor.fetchall()
        product = pd.DataFrame(product_data,columns = ['PID','Item','Quantity','Cost PI'])
        v4 = int(product.iloc[-1:,-4])
        l1 = list(product_data)
        l2 = Label(text ='Product ID         Quantity      Cost Per Item        Item Name ',
                   font = ("arial",36,"bold"),
                   bg = v1, fg ="black",
                   width = 56,height=1)
        l2.pack()
        lb1 = Listbox(master=t1,height = 8,width = 104,
                font=("arial",36,"bold"),bg=v1)
        for x in range(v4):
            s1 = str(l1[x][0]).rjust(16)+str(l1[x][2]).rjust(28)+str(l1[x][3]).rjust(20)+l1[x][1].rjust(30)
            lb1.insert(END,s1)   
        lb1.pack()
        
        #this function put user on main menu
        def home():
            t1.destroy()
            main_func()
        b1 = Button(text = "Main Menu",font = ("arial",36,"bold"),
                    bg = v1,activeforeground = "blue2",
                    activebackground = v1,
                    fg ="blue2",width = 20,height=1,
                    command=lambda:home())
        b1.pack(side = "left")
        b2 = Button(text = "Exit",font = ("arial",36,"bold"),
                    bg = v1,activeforeground = "blue2",
                    activebackground = v1,
                    fg ="blue2",width = 20,height=1,
                    command=lambda:exit())
        b2.pack(side = "right")

    #defining primary functioning through which we can add new stock items and their details   
    def two():
        #sructure assinging or screen formation
        t0.destroy()
        two = Tk()
        two.title("Store Management")
        two.configure(background=v1)
        two.state("zoomed")

        #working        
        def sumbit():
            cursor.execute("select * from product")
            product_data = cursor.fetchall()
            product = pd.DataFrame(product_data,columns = ['PID','Item','Quantity','Cost PI'])
            v1 = str(t1.get(1.0,'end'))
            v2 = int(t2.get(1.0,'end'))
            v3 = int(t3.get(1.0,'end'))
            v4 = int(product.iloc[-1:,-4])
            s1 = "insert into product values({},'{}',{},{})".format(v4 +1 ,v1,v2,v3)
            cursor.execute(s1)
            obj.commit()
            t1.delete("1.0",END)
            t2.delete("1.0",END)
            t3.delete("1.0",END)
            
        #this function put user on main menu    
        def home():
            two.destroy()
            main_func()
            
        #sructure desgining for screen and its components  
        l0 = Label(text = "New item entery", font = ("arial",72,"bold"),
                    bg = v1,activeforeground =
                   "blue2",activebackground = v1,
                    fg ="blue2",width = 16,height=2)
        l0.grid(row=0,column=1)
        l1 = Label(text = "Item name",font = ("arial",56,"bold"),
                    bg = "yellow",activeforeground = "blue2",
                   activebackground = v1,
                    fg ="blue2",width = 20,height=1)
        l1.grid(row=1,column=1)
        t1 = Text(height = 1,width=12,font = ("arial",56,"bold"),
                  bg = "firebrick1" )
        t1.grid(row=1,column=2)
        l2 = Label(text = "Quantity of item",
                   font = ("arial",56,"bold"),
                    bg = "black",activeforeground = "blue2",
                   activebackground = v1,
                    fg ="blue2",width = 20,height=1)
        l2.grid(row=2,column=1)
        t2 = Text(height = 1,width=12,font = ("arial",56,"bold"),
                  bg = "firebrick1")
        t2.grid(row=2,column=2)
        l3 = Label(text = "Cost of item",font = ("arial",56,"bold"),
                    bg = "green",activeforeground = "blue2",
                   activebackground = v1,
                    fg ="blue2",width = 20,height=1)
        l3.grid(row=3,column=1)
        t3 = Text(height = 1,width=12,font = ("arial",56,"bold"),
                  bg = "firebrick1")
        t3.grid(row=3,column=2)
        l4 = Label(text = " ",font = ("arial",56,"bold"),
                    bg = v1,activeforeground = "blue2",
                   activebackground = v1,
                    fg ="blue2",width = 20,height=1)
        l4.grid(row=4,column=1)
        b1 = Button(text = "Sumbit",font = ("arial",36,"bold"),
                    bg = v1,activeforeground = "blue2",
                    activebackground = v1,
                    fg ="blue2",width = 20,height=1,
                    command=lambda:sumbit())
        b1.grid(row=5,column=1)
        b2 = Button(text = "Main Menu",font = ("arial",36,"bold"),
                    bg = v1,activeforeground = "blue2",
                    activebackground = v1,
                    fg ="blue2",width = 20,height=1,
                    command=lambda:home())
        b2.grid(row=5,column=2)

    #this function gives functionality for customer transaction    
    def three():
        t0.destroy()
        t3 = Tk()
        t3.title("Store Management")
        t3.configure(background=v1)
        t3.state("zoomed")
        l1 = Label(text = "Transaction",
                   font = ("arial",42,"bold"), bg = v1,
                   activeforeground = "blue2",
                   activebackground = v1,
                fg ="blue2",width = 12,height=1).pack()

        #this function put user on main menu
        def home():
            t3.destroy()
            main_func()
            
        #genrating customer purchase and updating of stock   
        def sumbit():
            v9 = int(tx1.get(1.0,'end'))
            v11=int(tx2.get(1.0,'end'))
            tx3.delete("1.0",END)
            cursor.execute("select quantity,item,Cost_Item from product where P_ID = {}".format(v9))
            v15 = cursor.fetchall()
            v12 = int(v15[0][0])
            v16 = v15[0][1]
            v17 = int(v15[0][2])
            cursor.execute("update product set quantity = {} where P_ID = {}".format(v12-v11,v9))
            obj.commit()
            cursor.execute("insert into bill values('{}',{},{},{})".format(v16,v11,v17,v11*v17))
            obj.commit()
            cursor.execute("select * from bill")
            bill_data = cursor.fetchall()
            l1 = list(bill_data)
            lb2 = Listbox(f3,height = 6,width = 49,
                font=("arial",24,"bold"),bg=v1)
            lb2.grid(row=3,column=1)
            for x in range(len(l1)):
                s1 = str(l1[x][3]).rjust(16)+str(l1[x][1]).rjust(20)+str(l1[x][2]).rjust(24)+str(l1[x][0]).rjust(20)
                lb2.insert(END,s1)   
            lb2.grid(row=3,column=1)
            tx1.delete("1.0",END)
            tx2.delete("1.0",END)
            bill = pd.DataFrame(bill_data,columns = ['Item','Quantity','Cost PI','Total C'])
            total = sum(bill['Total C'])
            tx3.insert("end",total)

        #this will clear customer choices    
        def clear():
            tx1.delete("1.0",END)
            tx2.delete("1.0",END)

        #this will cancel customer choicesand genrate a new choice   
        def cancel():
            cursor.execute("truncate table bill")
            obj.commit()
            lb2 = Listbox(f3,height = 6,width = 49,
                font=("arial",24,"bold"),bg=v1)
            lb2.grid(row=3,column=1)
            clear()

        #it will genrate a final bill for customer    
        def show_pdf():
            cursor.execute("select * from bill")
            bill_data = cursor.fetchall()
            bill = pd.DataFrame(bill_data,columns = ['Item','Quantity','Cost PI','Total C'])
            L=[]
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=16)
            pdf.cell(0,10,"GENRAL STORE CUSTOMER TRANSACTION BILL", ln=1, align="C")
            pdf.cell(0,4,"-----------------------------------------------------------------------------------------------",ln=1,align="L")
            pdf.cell(0,10,"   ITEM NAME      COST/ITEM     QUANTITY    TOTAL COST",ln=1,align="L")
            pdf.cell(0,0,"-----------------------------------------------------------------------------------------------",0,1,align="L")
            for i in bill_data:
                L.append(i)
                pdf.cell(12,8," ",0,0, align="C")
                pdf.cell(36,8,str(i[0]),0,0, align="L")
                pdf.cell(35,8,str(i[2]),0,0, align="C")
                pdf.cell(32,8,str(i[1]),0,0, align="C")
                pdf.cell(48,8,str(i[3]),0,1, align="C")
            pdf.cell(0,0,"-----------------------------------------------------------------------------------------------",ln=1,align="L")
            total = sum(bill['Total C'])
            msg1="GRAND TOTAL IS Rs "+ str(total)
            pdf.cell(160,20,str(msg1),ln=1,align="L")
            pdf_name="Customer_Bill.pdf"
            pdf.output(pdf_name)
            webbrowser.open(pdf_name)
            cursor.execute("truncate table bill")
            obj.commit()
            
        #screen desging and its component assembling
        #Main Frames
        f0 = Frame(width=950, height=900, bd=8,
                   relief='raise',bg = v1)
        f0.pack(side = LEFT)
        f1 = Frame(width=650, height=900, bd=8,
                   relief='raise',bg = v1)
        f1.pack(side = RIGHT)
        
        #Frame 01
        f2 = Frame(f0,width=900, height=650, bd=8,
                   relief='raise')
        f2.grid(row=1,column=1)
        l2 = Label(f2,text ='Store Items ',
                    font = ("arial",28,"bold"),bg = "pink",
                    fg ="black",width = 12,height=1)
        l2.grid(row=1,column=1)
        l3 = Label(f2,text = 'Product ID            Cost Per Item        Item Name',
                    font = ("arial",24,"bold"),bg = v1,
                    fg ="black",width = 46,height=1)
        l3.grid(row=2,column=1)
        cursor.execute("select * from product")
        product_data = cursor.fetchall()
        product = pd.DataFrame(product_data,columns = ['PID','Item','Quantity','Cost PI'])
        v4 = int(product.iloc[-1:,-4])
        l1 = list(product_data)
        lb1 = Listbox(f2,height = 5,width = 49,
                font=("arial",24,"bold"),bg=v1)
        lb1.grid(row=3,column=1)
        for x in range(v4): 
            s1 =  str(l1[x][0]).rjust(16) + str(l1[x][3]).rjust(33) + str(l1[x][1]).rjust(28) 
            lb1.insert(END,s1)
        l4 = Label(f0,text ='       ',
                    font = ("arial",28,"bold"),bg = v1,
                    fg ="black",width = 12,height=2)
        l4.grid(row=2,column=1)
        
        #Frame 02
        f3 = Frame(f0,width=1534, height=1200, bd=8, relief='raise')
        f3.grid(row=3,column=1)
        l5 = Label(f3,text ='Customer Bill ',
                    font = ("arial",28,"bold"),bg = "pink",
                    fg ="black",width = 12,height=1)
        l5.grid(row=1,column=1)
        l6 = Label(f3,text = 'Total C.       Quantity           Cost P.I.           Item',
                    font = ("arial",24,"bold"),bg = v1,
                    fg ="black",width = 46,height=1,justify = "right")
        l6.grid(row=2,column=1)
        lb2 = Listbox(f3,height = 6,width = 49,
            font=("arial",24,"bold"),bg=v1)
        lb2.grid(row=3,column=1)
        #Frame 03
        l12 = Label(f1,text ='   ',
                    font = ("arial",20,"bold"),bg = v1,
                    fg ="black",width = 14,height=1)
        l12.grid(row=0,column=2)
        f4 = Frame(f1,width=500, height=650, bd=8, relief='raise')
        f4.grid(row=1,column=2)
        l7 = Label(f4,text ='Choose Product',
                    font = ("arial",28,"bold"),bg = "pink",
                    fg ="black",width = 14,height=1)
        l7.grid(row=1,column=1)
        l8= Label(f4,text ='PID',
                    font = ("arial",28,"bold"),bg = "blue",
                    fg ="black",width = 14,height=1).grid(row=2,column=1) 
        l8 = Label(f4,text ='Quantity',
                    font = ("arial",28,"bold"),bg = "yellow",
                    fg ="black",width = 14,height=1).grid(row=3,column=1) 
        tx1 = Text(f4,height = 1,width=15,bg = "firebrick1",
                   font = ("arial",28,"bold") )
        tx1.grid(row=2,column=2)
        tx2 = Text(f4,height = 1,width=15,bg = "firebrick1",
                   font = ("arial",28,"bold") )
        tx2.grid(row=3,column=2)
        b1 = Button(f4,text ='Sumbit',
                    font = ("arial",18,"bold"),bg = "pink",
                    fg ="black",width = 21,height=1,
                    command=lambda:sumbit())
        b1.grid(row=4,column=1)
        f5 = Frame(f4,width=500, height=650)
        f5.grid(row  =4,column=2)
        b2 = Button(f5,text = "Clear",font = ("arial",18,"bold"),
                    bg = v1,activeforeground = "blue2",activebackground = v1,
                    fg ="blue2",width = 10,height=1,
                    command=lambda:clear())
        b2.grid(row=4,column=2)
        b3 = Button(f5,text = "Main Menu",font = ("arial",18,"bold"),
                    bg = v1,activeforeground = "blue2",activebackground = v1,
                    fg ="blue2",width = 10,height=1,
                    command=lambda:home())
        b3.grid(row=4,column=3)
        l9 = Label(f1,text ='       ',
                    font = ("arial",28,"bold"),bg = v1,
                    fg ="black",width = 12,height=1)
        l9.grid(row=2,column=2)
        f6 = Frame(f1,width=500, height=650,bg = "black")
        f6.grid(row=3,column=2)
        l10 = Label(f6,text ='Grand Total',
                    font = ("arial",28,"bold"),bg = "grey",
                    fg ="black",width = 16,height=1)
        l10.grid(row=1,column=1)
        tx3 = Text(f6,height = 1,width=8,bg = "firebrick1",
                   font = ("arial",28,"bold") )
        tx3.grid(row=1,column=2)
        l11 = Label(f1,text ='       ',
                    font = ("arial",28,"bold"),bg = v1,
                    fg ="black",width = 12,height=1)
        l11.grid(row=4,column=2)
        
        #Frame 04
        f7 = Frame(f1,width=500, height=650, bd=8,
                   bg = "white",relief='raise')
        f7.grid(row=5,column=2)
        b4 = Button(f7,text ='Print',
                    font = ("arial",32,"bold"),bg = "pink",
                    fg ="black",width = 21,height=1,
                    command=lambda:show_pdf())
        b4.grid(row=1,column=1)
        l12 = Label(f7,text ='   ',
                    font = ("arial",10,"bold"),bg = "white",
                    fg ="black",width = 14,height=1)
        l12.grid(row=2,column=1)
        b5 = Button(f7,text ='Cancel',
                    font = ("arial",32,"bold"),bg = "blue",
                    fg ="black",width = 21,height=1,
                    command=lambda:cancel())
        b5.grid(row=3,column=1)
        l13 = Label(f7,text ='   ',
                    font = ("arial",10,"bold"),bg = "white",
                    fg ="black",width = 14,height=1)
        l13.grid(row=4,column=1)
        b6 = Button(f7,text ='Exit',
                    font = ("arial",32,"bold"),bg = "yellow",
                    fg ="black",width = 21,height=1,
                    command=lambda:exit())
        b6.grid(row=5,column=1)
        
#this function helps user to go back or quiting the program        
def home():
    tk.destroy()
    main_func()
    
#with help of this by clicking on screen we procced in our software
b1 = Button(text = "WELCOME\nTO\nSTORE MANAGEMENT",
            font = ("arial",96,"bold"),
            bg = v1,activeforeground = "blue2",
            activebackground = v1,
           fg ="blue2",width = 40,height=8,
            command=lambda:home())
b1.pack()

#here we give option to enter password thats why our software provide cross-platform
pswrd = input("Enter password of your mysql: ")

#for handling exceptions and errors
#checkpoint-from here project begins

try:
#if data is already in pc
    obj = msc.connect(host = "localhost",
                  user = "root",
                  passwd = pswrd,
                  database = "Store_Management")
    cursor = obj.cursor()

#if we run it new system than it give us demo data to represent it self    
#some data is inserted here for demo purpose as it is a school project
    
except:
    obj = msc.connect(host = "localhost",
                      user = "root",
                      passwd = pswrd,
                      database = "mysql")
    cursor = obj.cursor()
    s1 = "insert into product values(1,'Sugar',20,45),(2,'Floar',80,25),(3,'Rice',20,60),(4,'Meda',20,28),(5,'Suji',20,18);"
    s2 = "insert into product values(6,'Moong Daal',20,55),(7,'Udad Daal',20,60),(8,'Rajma',20,65),(9,'Salt',20,20),(10,'S.Biscuit',40,10);"
    cursor.execute("create database Store_Management;")
    cursor.execute("use Store_Management;")
    cursor.execute("create table product(P_ID int,Item varchar(40),Quantity int,Cost_Item int);")
    cursor.execute("create table bill(Item varchar(40),Quantity int,Cost_PI int,T_Cost int);")
    cursor.execute(s1)
    cursor.execute(s2)
    obj.commit()

mainloop()













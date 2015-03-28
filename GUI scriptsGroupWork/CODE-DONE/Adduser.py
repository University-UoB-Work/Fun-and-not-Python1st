from Tkinter import *
import tkMessageBox
import tkFont
import MySQLdb
class AddUser():

        def __init__(self, parent, FirstSV, LastSV):

                GUIFrame = Frame(parent,width = 350, height = 250)
                GUIFrame.pack(expand = False, anchor = CENTER)
                self.parent=parent
        ################################################################
        #################### Input String Elements #####################

                self.firstSV = StringVar()
                self.lastSV = StringVar()
                self.campusSV = StringVar()
                self.emailSV = StringVar()
                self.genderSV = StringVar()
                self.telSV = StringVar()
                

            
            
        ################################################################
        ####################### Label Elements ########################

                self.lastlbl = Label(parent,font = ("Times", "12", "bold"), text = 'Last Name')
                self.lastlbl.place(x = 10, y = 10)

                self.firstlbl = Label(parent,font = ("Times", "12", "bold"), text = 'First Name')
                self.firstlbl.place(x = 10, y = 40)

                self.campuslbl = Label(parent,font = ("Times", "12", "bold"), text = 'Location')
                self.campuslbl.place(x = 10, y = 70)

                self.emaillbl = Label(parent,font = ("Times", "12", "bold"), text = 'Email Address')
                self.emaillbl.place(x = 10, y = 100)

                self.genderlbl = Label(parent,font = ("Times", "12", "bold"), text = 'Gender')
                self.genderlbl.place(x = 10, y = 130)

                self.contactnumber = Label(parent,font = ("Times", "12", "bold"), text = 'Telephone Number')
                self.contactnumber.place(x = 10, y = 160)

        ################################################################
        ####################### Entry Elements ########################

                self.firstent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.firstSV)
                self.firstent.place(x = 150, y = 38)
                self.firstent.insert(0, FirstSV)

                self.lastent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.lastSV)
                self.lastent.place(x = 150, y = 8)
                self.lastent.insert(0, LastSV)

                self.campusent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.campusSV)
                self.campusent.place(x = 150, y = 68)

                self.emailent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.emailSV)
                self.emailent.place(x = 150, y = 98)

                self.genderent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.genderSV)
                self.genderent.place(x = 150, y = 128)

                self.tel = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.telSV)
                self.tel.place(x = 150, y = 158)
        ################################################################
        ####################### Button Elements ########################
                
                self.submit = Button(parent,borderwidth= 3,relief = 'raised', text = 'New Passenger', command = self.new_passanger)
                self.submit.place(x = 80, y = 190)
                
                self.submit = Button(parent,borderwidth= 3,relief = 'raised', text = '    New Driver   ', command = self.new_driver)
                self.submit.place(x = 180, y = 190)
                
                self.exit = Button(parent,borderwidth= 3,relief = 'raised', text = 'Exit', command = self.close)
                self.exit.place(x = 280, y = 190)

                self.FirstSV=FirstSV
                self.LastSV=LastSV
        ################################################################
        ###################### Button Functions ########################

        def close(self):
                self.parent.destroy()
                            
        def new_driver(self):
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                cursor = db.cursor()
                self.mail=self.emailSV.get()
                
                passanger = ("""INSERT INTO `driver` ( `First_Name`, `Last_Name`,`email_adress`, `Telephone_number`, `Gender`) VALUES( '%s','%s','%s','%s','%s')"""%\
                                (self.FirstSV,self.LastSV,self.mail,self.telSV.get(),self.genderSV.get() ))

                cursor.execute(passanger)
                 
                test = ("""SELECT `ID`, `First_Name`,\n
                                `email_adress` FROM `driver`\n
                                WHERE `First_Name`='%s'  AND `email_adress`='%s'"""%\
                                (self.FirstSV,self.mail))
                cursor.execute(test)
                resul = cursor.fetchall()
                x=0
                for row in resul:
                        ID = row[0]
                        x=x+1
                if x==0:
                        print" hmm you didnt insert anything"
                else:
                        message1='Your Driver ID is: ',ID
                        tkMessageBox.showinfo(message = message1)

        def new_passanger(self):
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                cursor = db.cursor()
                self.loc=self.campusSV.get()
                self.mail=self.emailSV.get()
                
                passanger = ("""INSERT INTO `passanger` ( `Current_Position`, `First_Name`, `Last_Name`,`email_adress`, `Telephone_number`, `Gender`) VALUES( '%s','%s','%s','%s','%s','%s')"""%\
                                (self.loc,self.FirstSV,self.LastSV,self.mail,self.telSV.get(),self.genderSV.get() ))

                cursor.execute(passanger)
                 
                test = ("""SELECT `ID`,`Current_Position`, `First_Name`,\n
                                `email_adress`, `Telephone_number`, `Gender` FROM `passanger`\n
                                WHERE `Current_Position`='%s' AND `First_Name`='%s'  AND `email_adress`='%s'"""%\
                                (self.loc,self.FirstSV,self.mail))
                cursor.execute(test)
                resul = cursor.fetchall()
                x=0
                for row in resul:
                        ID = row[0]
                        x=x+1
                if x==0:
                        print" hmm you didn't insert anything"
                else:
                        message1='Your passanger ID is: ',ID
                        tkMessageBox.showinfo(message = message1)
                
                        

def Create(FirstSV, LastSV):
        root = Tk()
        root.geometry('+470+260') 
        MainFrame =AddUser(root, FirstSV , LastSV)
        root.title('Create User')
        root.mainloop()

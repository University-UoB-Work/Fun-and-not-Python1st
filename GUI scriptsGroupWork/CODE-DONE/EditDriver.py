from Tkinter import *
import tkMessageBox
import MySQLdb
class EditDriver():
        
        def exitToLogin(self):
                self.parent.destroy()                                     
                import Login

        def __init__(self, parent,username):            
            self.parent = parent
            self.username=username
            GUIFrame = Frame(parent,width = 305, height = 190)
            GUIFrame.pack(expand = False, anchor = CENTER)
            
            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            print "I am connected to localhost"
            cursor = db.cursor()
            ID=self.username
            sql = ("""SELECT * FROM `driver` WHERE `ID`=%s"""%\
                   (ID))
            cursor.execute(sql)
            print "got current driver data"
            data =cursor.fetchall()
  #put this values inside the text fields
            for row in data:
                            
                    ID = row[0]
                    First_Name = row[1]
                    Last_Name = row[2]
                    email_adress = row[3]
                    Telephone_number= row[4]
                    Gender= row[5]
                    Password= row[8]
                    print "%s, %s, %s, %s, %s , %s, %s" %\
                      (ID,First_Name,Last_Name,email_adress,Telephone_number,Gender,Password)

            db.commit()
            cursor.close()
            db.close()
            self.password=Password
            self.firstSV = StringVar()
            
            self.firstSV.set(First_Name)

            self.lastSV = StringVar()
            self.lastSV.set(Last_Name)

            self.emailSV = StringVar()
            self.emailSV.set(email_adress)

            self.genderSV = StringVar()
            self.genderSV.set(Telephone_number)

            self.passSV = StringVar()
            self.passSV.set("")
################################################################################### labels
            self.firstlbl = Label(text = 'First Name: ')
            self.firstlbl.place(x = 10, y = 10)

            self.lastlbl = Label(text = 'Last Name: ')
            self.lastlbl.place(x = 10, y = 30)
            
            self.emaillbl = Label(text = 'Email Address: ')
            self.emaillbl.place(x = 10, y = 50)

            self.contactnumber = Label(text = 'Contact Number: ')
            self.contactnumber.place(x = 10, y = 70)

 #################################################################################### entry boxes
            self.firstent = Entry(textvariable = self.firstSV)
            self.firstent.place(x = 160, y = 10)
            self.lastent = Entry(textvariable = self.lastSV)
            self.lastent.place(x = 160, y = 30)


            self.emailent = Entry(textvariable = self.emailSV)
            self.emailent.place(x = 160, y = 50)

            self.genderent = Entry(textvariable = self.genderSV)
            self.genderent.place(x = 160, y = 70)
    

#################################################################################### buttons
           
            self.back = Button(parent, text = ' Back ', command = self.gotoMain)
            self.back.place(x = 130, y = 120)

            self.submit = Button(parent, text = 'Submit', command = self.update)
            self.submit.place(x = 45, y = 120)

            self.exit = Button(parent, text = ' Exit  ', command = self.exitToLogin)
            self.exit.place(x = 205, y = 120)
            print self.username

#################################################################################### functions
        def gotoMain(self):
                self.parent.destroy()
                import Driver
                Driver.create(self.username)

        def update(self):
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                print "I am connected to localhost"
                cursor = db.cursor()
                ID=self.username
                #data =cursor.fetchall()
                sql1 = ("""UPDATE `driver` SET `First_Name`='%s',`Last_Name`='%s',`email_adress`='%s',`Telephone_number`='%s'\n
                        WHERE `ID`=%s"""%\
                      (self.firstSV.get() ,self.lastSV.get() ,self.emailSV.get() ,self.genderSV.get(),ID))

                cursor.execute(sql1)
                print"You have succesfuly updated detils!"
                db.commit()
                cursor.close()
                db.close()         

def create(user):
        root = Tk()
        MainFrame =EditDriver(root,user)
        root.geometry('+470+260')
        root.title('Driver-Edit information')
        root.mainloop()

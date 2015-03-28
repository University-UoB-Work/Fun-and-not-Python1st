from Tkinter import *
import tkMessageBox
import MySQLdb
class EditPassanger(Frame):
        
        def exitToLogin(self):
                self.parent.destroy()                             
                import Login

        def __init__(self, parent,username):            
            Frame.__init__(self, parent)
            self.parent = parent
            self.username=username
            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            print "I am connected to localhost"
            cursor = db.cursor()
            ID=self.username
            sql = ("""SELECT * FROM `passanger` WHERE `ID`=%s"""%\
                   (ID))
            cursor.execute(sql)
            print "got current user data"
            data =cursor.fetchall()
            for row in data:
                            
                    ID = row[0]
                    Current_Position = row[1]
                    First_Name = row[2]
                    Last_Name = row[3]
                    email_adress = row[4]
                    Telephone_number= row[5]
                    Gender= row[6]
                    Password= row[7]
                    print "%s, %s, %s, %s, %s , %s, %s, %s" %\
                      (ID,Current_Position,First_Name,Last_Name,email_adress,Telephone_number,Gender,Password)
            db.commit()
            cursor.close()
            db.close()
            self.password=Password
            self.firstSV = StringVar()
            
            self.firstSV.set(First_Name)

            self.lastSV = StringVar()
            self.lastSV.set(Last_Name)

            self.campusSV = StringVar()
            self.campusSV.set(Current_Position)

            self.emailSV = StringVar()
            self.emailSV.set(email_adress)

            self.genderSV = StringVar()
            self.genderSV.set(Gender)

            self.passSV = StringVar()
            self.passSV.set("")
    
################################################################################### labels
            self.firstlbl = Label(text = 'First Name: ')
            self.firstlbl.place(x = 10, y = 10)

            self.lastlbl = Label(text = 'Last Name: ')
            self.lastlbl.place(x = 10, y = 30)
            self.campuslbl = Label(text = 'What campus are you in: ')
            self.campuslbl.place(x = 10, y = 50)

            self.emaillbl = Label(text = 'Email Address: ')
            self.emaillbl.place(x = 10, y = 70)

            self.genderlbl = Label(text = 'Gender: ')
            self.genderlbl.place(x = 10, y = 90)

            self.passwordLVL = Label(text = ' Current password: ')
            self.passwordLVL.place(x = 10, y = 110)

#################################################################################### entry boxes
            self.firstent = Entry(textvariable = self.firstSV)
            self.firstent.place(x = 160, y = 10)
            self.lastent = Entry(textvariable = self.lastSV)
            self.lastent.place(x = 160, y = 30)

            self.campusent = Entry(textvariable = self.campusSV)
            self.campusent.place(x = 160, y = 50)

            self.emailent = Entry(textvariable = self.emailSV)
            self.emailent.place(x = 160, y = 70)

            self.genderent = Entry(textvariable = self.genderSV)
            self.genderent.place(x = 160, y = 90)
            self.passw = Entry(textvariable = self.passSV)
            self.passw.place(x = 160, y = 110)    

#################################################################################### buttons
           
            self.back = Button(parent, text = 'Back', command = self.gotoMain)
            self.back.place(x = 80, y = 150)

            self.submit = Button(parent, text = 'Submit', command = self.update)
            self.submit.place(x = 30, y = 150)

            self.exit = Button(parent, text = 'Exit', command = self.exitToLogin)
            self.exit.place(x = 190, y = 150)
            print self.username

#################################################################################### functions
        def gotoMain(self):
                self.parent.destroy()
                import Passenger
                Passenger.create(self.username)

        def update(self):
                print self.password
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                print "I am connected to localhost"
                cursor = db.cursor()
                ID=self.username
                
                #data =cursor.fetchall()
                sql1 = ("""UPDATE `passanger` SET `Password`='%s',`First_Name`='%s',`Last_Name`='%s',`email_adress`='%s',`Gender`='%s',\n
                       `Current_Position`='%s' WHERE `ID`=%s"""%\
                      ( self.passSV.get(), self.firstSV.get() ,self.lastSV.get() ,self.emailSV.get() ,self.genderSV.get() , self.campusSV.get(),ID))

                if self.passSV.get()!=self.password:
                        print "you are not allowed to update information!"
                        print "Type your password"
                elif self.passSV.get()==self.password: 
                        cursor.execute(sql1)
                        print"You have succesfuly updated detils!"
                        db.commit()
                        cursor.close()
                        db.close() 

def create(user):
        root = Tk()
        MainFrame2 =EditPassanger(root,user)
        MainFrame2.pack()
        root.geometry('300x200')
        root.title('Passenger-Edit information')
        root.mainloop()

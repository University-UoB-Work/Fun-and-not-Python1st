from Tkinter import *
import tkMessageBox
import MySQLdb


class Login():
        def __init__(self, parent):
                
                GUIFrame = Frame(parent,width = 220, height = 100)
                GUIFrame.pack(expand = False, anchor = CENTER)
########################################################################## setting stringvars              
                self.userSV = StringVar()
                self.userSV.set("")

                self.passwordSV = StringVar()
                self.passwordSV.set("")
########################################################################## labels
                self.userlbl = Label(text = 'Login: ')
                self.userlbl.place(x = 10, y = 10)

                self.passwordlbl = Label(text = 'Password: ')
                self.passwordlbl.place(x = 10, y = 40)

########################################################################## entry boxes     
                self.user = Entry(textvariable = self.userSV)
                self.user.place(x = 70, y = 10)

                self.password = Entry(textvariable = self.passwordSV, show = "*")
                self.password.place(x = 70, y = 40) 
########################################################################## buttons     
                               
                self.login = Button(parent, text = 'Login', command = self.LogIn)
                self.login.place(x = 75, y = 65)

                self.exit = Button(parent, text = 'Exit', command = self.end)
                self.exit.place(x = 130, y = 65)

########################################################################## functions
        def LogIn(self):
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                print "I am connected to localhost"
                cursor = db.cursor()
                ID=self.userSV.get()
                Password=self.passwordSV.get()

                sqlPassanger = ("""SELECT ID FROM passanger\n
                           WHERE ID='%s' AND Password='%s'"""%\
                       ( ID, Password))

                sqlDriver = ("""SELECT ID FROM driver\n
                           WHERE ID='%s' AND Password='%s'"""%\
                       ( ID, Password))

                sqlAdmin = ("""SELECT ID FROM admin\n
                           WHERE ID='%s' AND Password='%s'"""%\
                       ( ID, Password))

                status=""
                cursor.execute(sqlPassanger)
                data =cursor.fetchall()
                if len(data) > 0:
                    status="Passenger"
                else:
                    cursor.execute(sqlDriver)
                    data =cursor.fetchall()
                    if len(data) > 0: 
                            status="Driver"
                    else:
                         cursor.execute(sqlAdmin)
                         data =cursor.fetchall()
                         if len(data) > 0:
                            status="Admin"
                      
                if status=="Passenger" :
                                root.destroy()
                                Passangerz = self.userSV.get()                                
                                import Passenger
                                Passenger.create(Passangerz)
                        
                elif status=="Driver":
                                root.destroy()
                                Drivers = self.userSV.get()                                
                                import Driver
                                Driver.create(Drivers)

                elif status=="Admin":
                                root.destroy()                               
                                import Admin
                                Admin.create()
                else:
                        tkMessageBox.showinfo(message = 'Incorrect Username or Password!')                                               
                db.commit()
                cursor.close()
                db.close()  


        def end(self):
                root.destroy()
                
 
root = Tk()
MainFrame =Login(root)
root.title('Login')
root.mainloop()

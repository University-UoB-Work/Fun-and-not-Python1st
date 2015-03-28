from Tkinter import *
import tkMessageBox
import MySQLdb


class DriverContactDetils():

        def __init__(self, parent, username):
            self.parent=parent
            ID=username
            GUIFrame = Frame(parent,width = 350, height = 200)
            GUIFrame.pack(expand = False, anchor = CENTER)
            
################################################################################### labels
            self.userlbl = Label(text = 'Driver Contact Details', fg = 'red',font =('Times New Roman', 20))
            self.userlbl.place(x = 80, y = 10)

            self.namelbl = Label(text = 'Name', fg = 'black',font =('Times New Roman', 10))
            self.namelbl.place(x = 20, y = 40)

            self.phonelbl = Label(text = 'Phone Number', fg = 'black',font =('Times New Roman', 10))
            self.phonelbl.place(x = 150, y = 40)

            self.emaillbl = Label(text = 'E-mail', fg = 'black',font =('Times New Roman', 10))
            self.emaillbl.place(x = 80, y = 40)



####################################################################

            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python")
            cursor = db.cursor()

            sql = ("""SELECT First_Name,Last_Name,email_adress,Telephone_number FROM `driver` WHERE ID= %s"""%\
                   (ID))            
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                    fName = row[0]
                    lName = row[1]
                    eMail = row[2]
                    pNumber = row[3]
            self.infolbl = Label(text = (fName , lName , eMail , pNumber), fg = 'black',font =('Times New Roman', 10))
            self.infolbl.place(x = 20, y = 60)
            
################################################################################### buttons
            self.exit = Button(parent, text = 'Exit', command = self.exitToLogin)
            self.exit.place(x = 180, y = 120)

            self.back = Button(parent, text = 'Back', command = self.goBack)
            self.back.place(x = 120,y = 120)
########################################################################## functions
        def exitToLogin(self):
                self.parent.destroy()
                import Login

        def goBack(self):
                self.parent.destroy()
                import Passenger
                Passenger.create(self)

def create(username):
        root = Tk()
        MainFrame =DriverContactDetils(root,username)
        root.geometry('+470+260')
        root.title('Driver Contact details')
        root.mainloop()


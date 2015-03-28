from Tkinter import *
import tkMessageBox
import MySQLdb

class OfferPlaceDriver(Frame):
        def gotoMain(self):
                self.parent.destroy()             
                import Driver
                Driver.create(self.username)
                
        def exitToLogin(self):
                self.parent.destroy()
                import Login

        def offer_a_place(self):
            
            startTime=self.timeSV.get()
            point=self.Start_pointSV.get()
            destination=self.Stop_pointSV.get()
            ID=self.username
            if  (startTime=="") or (point=="") or (destination==""):
                    tkMessageBox.showinfo(message = 'Invalid  data !')
            else:
                    
                    db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                    cursor = db.cursor()

        #INSERT INTO `traveling`(`ID`, `DriverID`, `Starting_Date_and_time`, `Start_Point`, `Stop_Point`,

                    
                    SQL = ("""INSERT INTO  traveling ( DriverID, Starting_Date_and_time, Start_Point, Stop_Point) VALUES (%s,'%s','%s','%s')"""%\
                               (ID,startTime,point,destination))
                    
                    cursor.execute(SQL)                     
                    db.commit()
                    cursor.close()
                    db.close()
                    tkMessageBox.showinfo(message = 'You have submited your Journey')

        def __init__(self, parent,username):
            Frame.__init__(self, parent)
            self.username=username
            self.parent=parent                
            #GUIFrame.pack(expand = False, anchor = CENTER)
##################################################################################

            self.travellbl = Label(text = 'Create a new Journey', fg = 'red', font = ('Times New Roman', 20))
            self.travellbl.place(x = 20, y = 3)
#################################################################################
#######DB CONNECTION#####
            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            print "I am connected to localhost"
            cursor = db.cursor()
            sqlAllTravels = ("""SELECT DriverID,Starting_Date_and_time, Start_Point,Stop_Point FROM `traveling` """)
            cursor.execute(sqlAllTravels)                 
            data =cursor.fetchall()

            self.timeSV = StringVar()
            self.timeSV.set("")

            self.Start_pointSV = StringVar()
            self.Start_pointSV.set("")
            self.Stop_pointSV = StringVar()
            self.Stop_pointSV.set("")

########################################################################## labels
            self.Timelbl = Label(text = 'Time (incl.Date) : ').place(x = 3, y = 40)
            self.Start_Pointlbl = Label(text = 'Current postion : ').place(x = 3, y = 60)
            self.Stop_Pointlbl = Label(text = 'Destination : ').place(x = 3, y = 80)
########################################################################## entry boxes     
            self.Time = Entry(textvariable = self.timeSV).place(x = 100, y = 40)
            self.Start_P = Entry(textvariable = self.Start_pointSV).place(x = 100, y = 60)
            self.Stop_P = Entry(textvariable = self.Stop_pointSV).place(x = 100, y = 80)
#################################################################################

            self.submit = Button(parent, text = 'Submit!', command  = self.offer_a_place)
            self.submit.place(x = 40, y = 120)
                               
            self.backBT = Button(parent, text = 'Back', command  = self.gotoMain)
            self.backBT.place(x = 140, y = 120)
            
            self.exit = Button(parent, text = 'Exit', command  = self.exitToLogin)
            self.exit.place(x = 190, y = 120)
        
##################################################################################
      
def create(username):
        root = Tk()
        Mainframe3 = OfferPlaceDriver(root,username)
        Mainframe3.pack()
        root.geometry('280x160')
        root.title('Offer a lift')
        root.mainloop()

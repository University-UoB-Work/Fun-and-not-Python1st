from Tkinter import *
import tkMessageBox
import MySQLdb
##############on the end of program! after submit

###########
class HistoryDriver(Frame):
        def gotoMain(self):
                self.parent.destroy()             
                import Driver
                Driver.create(self.username)
                
        def exitToLogin(self):
                self.parent.destroy()
                import Login

        def __init__(self, parent,username):
            Frame.__init__(self, parent)
            self.username=username
            self.parent=parent                
            #GUIFrame.pack(expand = False, anchor = CENTER)
##################################################################################

            self.travellbl = Label(text = 'List of your trips', fg = 'red', font = ('Times New Roman', 18))
            self.travellbl.place(x = 50, y = 10)
##################################################################################

            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            cursor = db.cursor()
            self.driver = Listbox(parent,width = 55, height = 10)
            self.driver.place(x = 10, y = 50)
#######DB CONNECTION#####
            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            print "I am connected to localhost"
            cursor = db.cursor()
            sqlAllTravels = ("""SELECT Starting_Date_and_time, Start_Point,Stop_Point FROM `traveling` \n
                        WHERE DriverID=%s"""%\
                             (self.username))
            cursor.execute(sqlAllTravels)               
            data =cursor.fetchall()
  #put this values inside the text fields
            x=0
            for row in data: 
        
                            Starting_Date_and_time = row[0]
                            Start_Point = row[1]
                            Stop_Point = row[2]
                            
                            message=Start_Point," to" ,Stop_Point," at ",Starting_Date_and_time
                            self.driver.insert(x,message)
                            x=x+1
                            print "%s, %s, %s" %\
                              ( Starting_Date_and_time, Start_Point, Stop_Point)
            if x==0:
                 tkMessageBox.showinfo(message = 'You didnt offer any place.')
#################################################################################
                               
            self.backBT = Button(parent, text = 'Back', command  = self.gotoMain)
            self.backBT.place(x = 140, y = 220)
            
            self.exit = Button(parent, text = 'Exit', command  = self.exitToLogin)
            self.exit.place(x = 190, y = 220)
        
##################################################################################
      
def create(username):
        root = Tk()
        Mainframe3 = HistoryDriver(root,username)
        Mainframe3.pack()
        root.geometry('360x270')
        root.title('View History of your trips')
        root.mainloop()

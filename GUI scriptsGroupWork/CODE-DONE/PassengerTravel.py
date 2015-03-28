from Tkinter import *
import tkMessageBox
import MySQLdb
##############on the end of program! after submit

###########
class PassengerTravel(Frame):
        def gotoMain(self):
                self.parent.destroy()             
                import Passenger
                Passenger.create(self.username)

        def driverContact(self):
                if self.did!="0":
                        self.parent.destroy()
                        import DriverContactDetils
                        DriverContactDetils.create(self.did)
                else:
                       tkMessageBox.showinfo(message = "Please choose a desired journey.")

        def exitToLogin(self):
                self.parent.destroy()
                import Login

        def assign_to_car(self):
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                cursor = db.cursor()
                cursor1=db.cursor()
                items = self.driver.curselection()
                self.items = self.driver.curselection()
                name = self.username
                select=items
                                #for loop ,select passangers ID 1-4 ,if null skip and assign current passanger to next one!
                driv = ("""SELECT `DriverID` FROM traveling WHERE ID=%s"""%
                        (select))
                cursor1.execute(driv)
                resul = cursor1.fetchall()   
                for row in resul:
                        DriverID = row[0]
                
                self.did=DriverID
               # print select,'to gowno!'
                int1 = select[0]
                #print 'mhm',int1
                InPass1 = ("""UPDATE `traveling` SET `PassangerID1`='%s' WHERE `ID` = %s """% (str(name),str(int1))  )
                InPass2 = ("""UPDATE `traveling` SET `PassangerID2`='%s' WHERE ID='%s'"""%(str(name),str(int1))  )
                InPass3 = ("""UPDATE `traveling` SET `PassangerID3`='%s' WHERE ID='%s'"""%(str(name),str(int1))  )
                InPass4 = ("""UPDATE `traveling` SET `PassangerID4`='%s' WHERE ID='%s'"""%(str(name),str(int1))  )

                          #      InPass4 = ("""UPDATE `traveling` SET `PassangerID4`=%s WHERE ID=%s"""%\
                          # (self.username,select))
                PassSQL = ("""SELECT `PassangerID1`, `PassangerID2`, `PassangerID3`, `PassangerID4` FROM  `traveling` WHERE ID=%s"""%\
                          (select))
                cursor.execute(PassSQL)
                results = cursor.fetchall()   
                for row in results:
                        Pass1 = row[0]
                        Pass2 = row[1]
                        Pass3 = row[2]
                        Pass4 = row[3]
                        global tes
                        tes=0
       #         print Pass1,Pass2,Pass3,Pass4,"test"
                if Pass1:
                        print"booked already 1"
                else:
                        cursor.execute(InPass1)
                        tkMessageBox.showinfo(message = 'You are succesfully registered.')
                        tes=1
                        
                if Pass2 or( tes==1):
                        print"booked already 2"
                else:  
                        cursor.execute(InPass2)
                        tkMessageBox.showinfo(message = 'You are succesfully registered.2')
                        tes=1

                if Pass3 or tes==1:
                        print"booked already 3"
                else:
                        cursor.execute(InPass3)
                        tkMessageBox.showinfo(message = 'You are succesfully registered.')
                        tes=1

                if Pass4 or tes==1:
                        print"booked already 4"
                else:
                        cursor.execute(InPass4)
                        tkMessageBox.showinfo(message = 'You are succesfully registered.')
                        tes=1

                db.commit()
                cursor.close()
                db.close()

        def __init__(self, parent,username):
            Frame.__init__(self, parent)
            self.username=username
            self.parent=parent
            self.did="0"
            #GUIFrame.pack(expand = False, anchor = CENTER)
##################################################################################

            self.travellbl = Label(text = 'Travel', fg = 'red', font = ('Times New Roman', 20))
            self.travellbl.place(x = 80, y = 10)
##################################################################################
            self.driver = Listbox(parent,width = 55, height = 10, selectmode=EXTENDED)
            self.driver.place(x = 10, y = 50)
#######DB CONNECTION#####
            db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
            print "I am connected to localhost"
            cursor = db.cursor()
            sqlAllTravels = ("""SELECT DriverID,Starting_Date_and_time, Start_Point,Stop_Point FROM `traveling` """)
            cursor.execute(sqlAllTravels)                 
            data =cursor.fetchall()
  #put this values inside the text fields
            x=1
            self.driver.insert(0,"")
            for row in data: 
                            DriverID = row[0]
                            Starting_Date_and_time = row[1]
                            Start_Point = row[2]
                            Stop_Point = row[3]
                            
                            message="Driver :",DriverID,Start_Point," to ",Stop_Point," at ",Starting_Date_and_time
                            self.driver.insert(x,message)
                            x=x+1
                            print "%s, %s, %s, %s" %\
                              (DriverID, Starting_Date_and_time, Start_Point, Stop_Point)

#################################################################################

            self.submit = Button(parent, text = 'Take a journey!', command  = self.assign_to_car)
            self.submit.place(x = 40, y = 220)   
            self.backBT = Button(parent, text = 'Back', command  = self.gotoMain)
            self.backBT.place(x = 140, y = 220)
            self.exit = Button(parent, text = 'Exit', command  = self.exitToLogin)
            self.exit.place(x = 190, y = 220)
            self.viewdriv = Button(parent, text = 'View driver contact', command = self.driverContact)
            self.viewdriv.place(x = 190, y = 10)
        
##################################################################################
      
def create(username):
        root1 = Tk()
        Mainframe3 = PassengerTravel(root1,username)
        Mainframe3.pack()
        root1.geometry('360x270')
        root1.title('View Avaible cars')
        root1.mainloop()

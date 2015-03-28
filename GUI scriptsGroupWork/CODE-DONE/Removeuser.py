from Tkinter import *
import tkMessageBox
import tkFont
import MySQLdb
class RemoveUser():
        
        def __init__(self, parent, FirstSV, LastSV):
                
                def removeDriver():
                        
                        print"unfinished"
                        db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                        print "I am connected to localhost"
                        cursor = db.cursor()
                        items = self.listbox2.curselection()
                        self.items = self.listbox2.curselection()
                       # DELETE FROM `driver` WHERE ID =%s
                        deldriver = ("""DELETE FROM `driver` WHERE ID =%s """%\
                                    (items))
                        cursor.execute(deldriver)
                        print" you have deleted  driver number",items
                        self.listbox2.delete(items)
                        db.commit()
                        cursor.close()
                        db.close()

                def removePassanger():
                         
                        print"unfinished"
                        db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                        print "I am connected to localhost"
                        cursor = db.cursor()
                        item = self.listbox1.curselection()
                        self.item = self.listbox1.curselection()
                        int1 = item[0]
                        print int1,'to '
                       # DELETE FROM `driver` WHERE ID =%s
                        delpassenger = ("""DELETE FROM `passanger` WHERE ID =%s """%\
                                    (str(int1)))
                        print delpassenger
                        cursor.execute(delpassenger)
                        print" you have deleted  driver number",int1
                        self.listbox1.delete(item)
                        db.commit()
                        cursor.close()
                        db.close()

                GUIFrame = Frame(parent,width = 385, height = 280)
                GUIFrame.pack(expand = False, anchor = CENTER)
                self.parent=parent
   
        ################################################################
        #################### Input String Elements #####################

            #    self.firstSV = StringVar()
                #self.firstSV.set("")

             #   self.lastSV = StringVar()
                #self.lastSV.set("")

                self.campusSV = StringVar()
                #self.campusSV.set("")

                self.emailSV = StringVar()
                #self.emailSV.set("")

                self.genderSV = StringVar()
                #self.genderSV.set("")

                self.contribSV = StringVar()
               # self.contribSV.set("")
  
        ################################################################
        ####################### Label Elements ########################

                self.WelcomeHeader = Label(parent,font = ("Times", "19", "bold", "underline"), text = 'Please Select User to Remove')
                self.WelcomeHeader.place(x = 30, y = 4)

                self.DriverHeader = Label(parent,font = ("Times", "16", "bold"), text = 'Driver')
                self.DriverHeader.place(x = 250, y = 45)

                self.PassengerHeader = Label(parent,font = ("Times", "16", "bold"), text ='Passenger')
                self.PassengerHeader.place(x = 60, y = 45)
              
        ################################################################
        ####################### Entry Elements #########################

##                self.firstent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.firstSV)
##                self.firstent.place(x = 150, y = 38)
##                self.firstent.insert(0, FirstSV)
##
##                self.lastent = Entry(parent, font = ("Times", "12", "bold"), textvariable = self.lastSV)
##                self.lastent.place(x = 150, y = 8)
##                self.lastent.insert(0, LastSV)

        ################################################################
        ###################### List Box Element ########################

                self.listbox1 = Listbox(parent, width = 30 , height = 8, xscrollcommand = True, yscrollcommand = True, selectmode=BROWSE)
                self.listbox1.place( x = 10, y = 75)

                self.listbox2 = Listbox(parent, width = 30 , height = 8, xscrollcommand = True, yscrollcommand = True, selectmode=BROWSE)
                self.listbox2.place( x = 190, y = 75)
#DRIVER##############
                db = MySQLdb.connect(host = "127.0.0.1",user = "root",passwd = "",db = "python" )
                print "I am connected to localhost"
                cursor = db.cursor()
                seldrivers = ("""SELECT First_Name,Last_Name, ID FROM `driver` """)
                cursor.execute(seldrivers)                 
                data =cursor.fetchall()
                x=1
                self.listbox2.insert(0,"")
                for row in data:
                        
                        First_Name = row[0]
                        Last_Name = row[1]
                        ID = row[2]
                        message=First_Name,Last_Name,'(',ID,')'
                        self.listbox2.insert(x,message)
                        x=x+1
####PASSANGER#############################################################################
                selpassangers = ("""SELECT First_Name,Last_Name, ID FROM `passanger` """)
                cursor.execute(selpassangers)                 
                data1 =cursor.fetchall()
                x=1
                self.listbox1.insert(0,"")
                for row in data1:
                        
                        First_Name = row[0]
                        Last_Name = row[1]
                        ID = row[2]
                        message=First_Name,Last_Name,'(',ID,')'
                        self.listbox1.insert(x,message)
                        x=x+1
        ################################################################
        ####################### Button Elements ########################
                self.DeleteDriver = Button(parent,borderwidth= 3,relief = 'raised', text = 'Delete Driver',command=removeDriver)
                #command=lambda listbox1= self.listbox1: listbox1.delete(ANCHOR))
                self.DeleteDriver.place(x = 250, y = 220 )
                self.DeletePassenger = Button(parent,borderwidth= 3,relief = 'raised', text = 'Delete Passenger',command=removePassanger)
                #command=lambda listbox1= self.listbox1: listbox1.delete(ANCHOR))
                self.DeletePassenger.place(x = 50, y = 220)
                self.exit = Button(parent,borderwidth= 3,relief = 'raised', text = '  Exit  ', command = self.close)
                self.exit.place(x = 180, y = 220)
                db.commit()
                cursor.close()
                db.close()
        ################################################################
        ###################### Button Functions ########################

        def close(self):
                self.parent.destroy()


def Create(FirstSV, LastSV):
        root = Tk()
        root.geometry('+470+260') 
        MainFrame =RemoveUser(root, FirstSV , LastSV)
        root.title('Remove User')
        root.mainloop()

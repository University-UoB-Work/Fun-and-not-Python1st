
from Tkinter import *
import tkMessageBox
import MySQLdb
class Passenger(Frame):

        def __init__(self, parent, username):
            self.username=username
            
            GUIFrame = Frame(parent,width = 267, height = 175)
            GUIFrame.pack(expand = False, anchor = CENTER)
            self.parent = parent
################################################################################### labels
            self.userlbl = Label(text = "  Welcome \n Passenger",justify = CENTER,font = ("Gothic Copperplate Light", "17"))
            self.userlbl.place(x = 75, y = 4)
            
################################################################################### buttons

            self.editpass = Button(parent,font = ("Gothic Copperplate Bold", "10", "bold"), text = 'Personal Information', command = self.edit_Personal_Info)
            self.editpass.place(x = 62, y = 69)

            self.travel = Button(parent,font = ("Gothic Copperplate Bold", "10", "bold"), text = 'Available Routes', command = self.new_trip)
            self.travel.place(x = 5, y = 100)
            
            self.Hist = Button(parent,font = ("Gothic Copperplate Bold", "10", "bold"), text = ' Destination Log ', command = self.history_of_trips)
            self.Hist.place(x = 140, y = 100)

            self.exit = Button(parent,font = ("Gothic Copperplate Bold", "10", "bold"),text = 'Return to Login', command = self.exitToLogin)
            self.exit.place(x = 80, y = 131)

            
           # print self.username                 
########################################################################## functions

        def edit_Personal_Info(self):
                self.parent.destroy()
                import EditPassanger
                EditPassanger.create(self.username)
                
        def history_of_trips(self):
                self.parent.destroy()
                import HistoryPassanger
                HistoryPassanger.create(self.username)

        def exitToLogin(self):
                self.parent.destroy()
                import Login

        def new_trip(self):
                self.parent.destroy()              
                import PassengerTravel
                PassengerTravel.create(self.username)
                
def create(username):    
        root = Tk()
        root.geometry('+470+260')
        root.resizable(width = False, height = False)
        MainFrame =Passenger(root,username)
        root.title('Passenger Home')
        root.mainloop()


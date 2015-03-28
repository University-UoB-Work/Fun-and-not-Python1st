from Tkinter import *
import MySQLdb

class Driver():
        
        def Update_Personal_Info(self):
                 self.parent.destroy()              
                 import EditDriver
                 EditDriver.create(self.username)

        def Offer_a_Place(self):
                self.parent.destroy()              
                import OfferPlaceDriver
                OfferPlaceDriver.create(self.username)

        def exitToLogin(self):
                self.parent.destroy()              
                import Login
                        

        def HistoryOfDriver(self):
                
                self.parent.destroy()              
                import HistoryDriver
                HistoryDriver.create(self.username)

        def __init__(self, parent,username):

            self.username=username
            self.parent=parent
            
            GUIFrame = Frame(parent,width = 270, height = 200)
            GUIFrame.pack(expand = False, anchor = CENTER)

            self.welcome="Welcome driver ",self.username
################################################################################### labels
            self.userlbl = Label(parent, text = self.welcome, fg = 'red',font =('Times New Roman', 20))
            self.userlbl.place(x = 5, y = 25)

################################################################################### buttons

            self.editpass = Button(parent, text = ' Offer a Place ',command = self.Offer_a_Place)
            self.editpass.place(x = 90, y = 80)

            self.travel = Button(parent, text = 'Edit Personal Details',command = self.Update_Personal_Info)#EditDriver
            self.travel.place(x = 5, y = 110)

            
            self.editpass = Button(parent, text = '   Journey Log   ',command = self.HistoryOfDriver)
            self.editpass.place(x = 140, y = 110)

            self.exit = Button(parent, text = ' Return to Login ',command = self.exitToLogin)
            self.exit.place(x = 85, y = 140)


    
def create(username):
        root = Tk()
        Mainframe = Driver(root,username)
        root.geometry('+470+260')
        root.title('Driver - Main Screen')
        root.mainloop()

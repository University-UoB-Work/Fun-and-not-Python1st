from Tkinter import *


class Admin:

        def __init__(self, parent):
        ############################ Frame #############################
                GUIFrame = Frame(parent,width = 370, height = 250)
                GUIFrame.pack(expand = False, anchor = CENTER)
                self.parent = parent
        #################### Input String Elements #####################
                self.firstSV = StringVar()
                self.firstSV.set("")
                self.lastSV = StringVar()
                self.lastSV.set("")
        ################################################################
        ####################### Entry Elements ########################

                self.lastent = Entry(parent, font = ("Times", "12", "bold"), width = 15, textvariable = self.lastSV)
                self.lastent.place(x = 100, y = 100)

                self.firstent = Entry(parent, font = ("Times", "12", "bold"), width = 15,  textvariable = self.firstSV)
                self.firstent.place(x = 100, y = 130)

        ################################################################
        ####################### Label Elements ########################

                self.Welcome = Label(parent, font = ("Copperplate Gothic Bold", "18", "bold", "underline"), text = 'Welcome Administrator')
                self.Welcome.place( x = 10, y = 10)
                
                self.Query = Label(parent, font = ("Copperplate Gothic Bold", "16", "bold", "underline"), text = 'User Query')
                self.Query.place( x = 90, y = 60)

                self.lastlbl = Label(parent,font = ("Times", "12", "bold"), text = 'Lasts Name')
                self.lastlbl.place(x = 10, y = 100)

                self.firstlbl = Label(parent,font = ("Times", "12", "bold"), text = 'First Name')
                self.firstlbl.place(x = 10, y = 130)

        ################################################################
        ####################### MultiForm Buttons ######################
                self.Createuser = Button(parent, text = 'Create User', width=8, height=1,borderwidth= 3,relief = 'raised', command = self.CreateUserQuery)
                self.Createuser.place(x = 260, y = 98)

                self.Deleteuser = Button(parent, text = 'Delete User', width=8, height=1,borderwidth= 3,relief = 'raised', command = self.DeleteUserQuery)
                self.Deleteuser.place(x = 260, y = 128)

                self.Logout = Button(parent, text = 'Logout', width=8, height=1,borderwidth= 3,relief = 'raised', command = self.close)
                self.Logout.place(x = 260, y = 158)

        ################################################################
        ####################### Button Event Calls #####################

        def DeleteUserQuery(self):
        
                first = self.firstSV.get()
                last = self.lastSV.get()
                import Removeuser
                Removeuser.Create(first, last)

        def close(self):
                self.parent.destroy()
                import Login

        def CreateUserQuery(self):

                first = self.firstSV.get()
                last = self.lastSV.get()
                import Adduser
                Adduser.Create(first, last)

def create():
        root = Tk()
        root.geometry('+470+260')
        Mainframe = Admin(root)
        root.title('Administrator')
        root.mainloop()

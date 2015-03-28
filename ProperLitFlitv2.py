Users = [
    ("User","1234"),#0
    ("Alex","pass1"),#1
    ]
Administrators= [
                ("Admin","root"),#0
                ("root","toor"),#1
                 ]
Books = [
	
    ("Alexander Drabek","Security perspective of our lives"),#0
    ("Alex Masakra","potter harry party vol 1."),#1
    ("Alex Masakra","potter harry party vol 2."),#2
    ("Alex Masakra","potter harry party vol 3."),#3
    ("Maciek Zembrzycki","How to be a good cook...")#4
    ]

FavouriteBooks= [    ["alex","alex","User"],["user","user1"], ["User","user1"] ,[""] , [""] ]#there should be corresponding list
#----------------------------------------
    #NEW CLASSS and FUNCTIONS
#----------------------------------------
class Litflit():
    
    def __init__(self) :
        self.LogIn(Users,Administrators)
        global part
        self.part=0

    def Logoff(self):
        print ""
        print"You have successfully log off."
        print ""
        self.LogIn(Users,Administrators)
       

    def LogIn(self,Users,Administrators):
        print""
        print"Please provide your details."
        self.nme = raw_input("Enter Username: ")
        self.psword = raw_input("Enter Password: ")
        if (self.nme,self.psword) in Administrators:
            print'You succesfully login as an Administrator'
            self=Admin(self.nme)
        elif(self.nme,self.psword) in Users:
            print""
            print'You succesfully login as an User'
            self=User(self.nme)
        else:
            print"Wrong username or password"
            
            self.LogIn(Users,Administrators)

    def ListBooks(self):
        
        print ""
        print "List of All books."
        counter=0
        for i in Books:
            counter=counter+1
            auth,tit= i
            print counter , auth ,',' , tit
        print ""
        if self.part==1:
            print""#I am in function so I will not invoke menu
            self.part=0
        else:
            self.Menu()

#----------------------------------------
    #NEW CLASSS and FUNCTIONS       
#----------------------------------------    
class Admin(Litflit):

    def __init__(self, name):
        self.nme = name;
        global part
        self.part=0
        self.Menu()
       

    def Menu(self):
        print "\n1)Add user" 
        print "2)Delete User"
        print "3)Add a new book to the system"
        print "4)List all books"
        print "5)List all users"
        print "6)Log off" 
        print "7)Exit\n"

        while True:
            try:
                optAdmin= int(raw_input("Please choose an option:\n"))
                break
            #handling strings which can not be parsed into numbers
            except ValueError:
                    print "Type correct number."
        options = {
               1 : self.AddUser,
               2 : self.DelUser,
               3 : self.AddBook,
               4 : self.ListBooks,
               5 : self.ListUsers,
               6 : self.Logoff,
               7 : exit,
               }

        if optAdmin>0 and optAdmin<=7:
            options[optAdmin]()
        else:
            print"Type correct number"
            self.Menu()


    def AddUser(self):
        us=raw_input("\nCreate new username : ")
        passw=raw_input("Enter new user's Password :  ")
        Users.append((us,passw))
        print "You successfully created new user account!!!\n"
        self.Menu()

   
    def DelUser(self):
        us=raw_input("Enter username to delete:\n")
        for i in Users:
            usernme,passw=i
            if us==usernme:
                Users.remove((us,passw))
                print "User Successfully removed."
                self.Menu()
        if us!=usernme:
            print"No such user on the system record's\n"    
            cont=raw_input("Do you want to try again? Y/N")
            cont=cont.lower()
            if cont=='y' :
                self.DelUser()
            self.Menu()

    def ListUsers(self):
        print "\nList of all users."
        counter=0
        for i in Users:
            counter=counter+1
            user,tit= i
            print counter , user ,"\n"
        self.Menu()



    def AddBook(self) :
        print"\nAdding a new book"
        author=raw_input("Type a Author of a book  ")
        title=raw_input("Type a title of a book  ")
        Books.append((author,title))
        print "You successfully add new book to the list!!!\n"
        FavouriteBooks.append([""])
        while True:
            try:
                nx= int(raw_input("Press '1' if you want view all the books\n"))
                break
            #handling strings which can not be parsed into numbers
            except ValueError:
                    print "Type correct number."
        if nx==1:
            self.ListBooks()
        print ""
        self.Menu()

#----------------------------------------
    #NEW CLASSS and FUNCTIONS



#----------------------------------------
class User(Litflit):

    def __init__(self, name):
        self.nme = name;
        global part
        self.part=0
        self.Menu()

    def Menu(self):
        print "\n1)Add a book to a favourite list"
        print "2)Remove a book from the favourite list"
        print "3)List all books"
        print "4)List common books"
        print "5)List your favourite books"
        print "6)Change password"
        print "7)Log off"
        print "8)Exit\n"
        while True:
            try:
                optUsers= int(raw_input("Please choose an option:"))
                break
            #handling strings which can not be parsed into numbers
            except ValueError:
                    print "Type correct number."

        optionse = {
               1 : self.AddBookFav,
               2 : self.RemoveBookFav,
               3 : self.ListBooks,
               4 : self.ListComBooks,
               5 : self.ListFavBooks,
               6 : self.ChangePassword,
               7 : self.Logoff,
               8 : exit,
               }

        if optUsers>0 and optUsers<=8:
            optionse[optUsers]()
        else:
            print"Type correct number"
            self.Menu()


    def ListFavBooks(self):
        print'List of Your favourite books\n'
        present=False
        for i in range(len(FavouriteBooks)):
            if self.nme in FavouriteBooks[i]:
                auth,tit= Books[i]
                print ""
                present=True
                print i+1,'.',auth ,', ' , tit
        if present==False:
            print"\nYour list is empty!\n"
        if self.part==1:
            self.part=0
        else:
            self.Menu()

    def AddBookFav(self) :
        print"Choose the book from library"
        self.part=1
        self.ListBooks()#listing all possibilities
        self.part=0
        while True:
            try:
                test= int(raw_input("Type the number of the book :\n"))
                test=test-1
                break
            except ValueError:
                    print "Type correct number."

        if len(FavouriteBooks)>=test and test>=0:
            FavouriteBooks[test].append(self.nme)
            print "You successfully add new book to the list!!!"
        else:
            print" Error! Provide correct number!"
        
        nx=raw_input("Type 'Y' if you want to add another book,else type 'N' to go to main menu ")
        print""
        nx=nx.lower()
        if nx=="y":
            self.part=1
            self.AddBookFav()
            print ""
        self.Menu()

    def RemoveBookFav(self):
        print ""
        print"Removing a book"
        self.part=1
        
        self.ListFavBooks()
        while True:
            
            try:
                number= int(raw_input("Type the number of the book:\n"))
                break
            except ValueError:
                print "Type correct number."
        number=number-1
        if number<=len(FavouriteBooks)and number>0:
            FavouriteBooks[number].remove(self.nme)
            print "You successfully remove a book from the list!!!\n"
        else:
            print" Error,no such book\n"
       
        self.Menu()


#list common books
    def ListComBooks(self):
        #printing the list of book
        print ""
        print "List of common books."
        for i in range(len(FavouriteBooks)):
            
            if self.nme in FavouriteBooks[i]:
                auth,tit= Books[i]
                print ""
                print'The book : ',auth ,', ' , tit
                result = sorted(list(set(FavouriteBooks[i])))
                for user in result:
                    print  ' is in favourite list of :  ' , user
        self.Menu()

    def ChangePassword(self):
            
        oldPass = raw_input('Enter your old password to continue:\n') 
        correct = False
        for nme, password in Users:
            if password == oldPass: 
                correct = True
                break
        if correct:
            newPassword = raw_input('Enter new password:\n') 
            Users.remove((nme, password))    
            Users.append((nme, newPassword))
            print"You have successfully changed your password"
            self.Menu()	
        else:
            print 'Incorrect password'
            cont=raw_input('Do you want to try again Y/N: \n' )
            if cont.lower()=="y" :
                self.ChangePassword()
            #security : it should be delay between tries!
            self.Menu()


#main
print "WELCOME in the LitFlit"
mainObject= Litflit()


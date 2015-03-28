#---------------------
#Lists of tuples....--
#---------------------
from collections import OrderedDict
#list(OrderedDict.fromkeys('abracadabra'))
Users = [
    ("User","1234"),#0
    ("Alex","pass1"),#1
    ("Admin","pass2")#2
    ]

Books = [
	
    ("Alexander Drabek","Security perspective of our lives"),#0
    ("Alex Masakra","potter harry party vol 1."),#1
    ("Maciek Zembrzycki","How to be a good cook...")#2
    ]

List_favourite=[
                 #('bookID','userid'),
                 (0,1),
                 (2,1),
                 (2,2),
                 (1,2),
                 (0,2)
                    ]
list_favourite_books=[]
list_temp_users=[]

def match():
    print"listing user with common books"
    counter=0
    for x in List_favourite:
        bookID,userID=x
        if userID==hehname:
            list_favourite_books.append(bookID)
#ok mamy liste ksiazek ulubionych usera!idenxy
    for i in List_favourite:
        bookID,userID=i
        if userID!=hehname :
            for xz in list_favourite_books:
                if bookID==list_favourite_books[xz]:
                    list_temp_users.append(userID)
                    list_temp_users=list(OrderedDict.fromkeys(list_temp_users))#not sure if it is proper syntax
                    counter=counter+1
    for q in list_temp_users:
        print list_temp_users[q]

    print counter+"users has got at least 1 book in common"

#potrzebna porownac indexy ksiazek z nazwami albo user id z nazwa usera


        

#-----------------
#--Main functions:-
#-----------------
global nam
def WelcomeScreen( nam,x):
    if x!="ok":
        return 0
    global hehname# cos spiepszone XD
    hehname= nam
    print ""
    print "Welcome to the program,",nam
    print "Choose an option:"
   # print "1)Add a book to favourite list"
   # print "1)Remove a book from favourite list"
    print "1)Add a book" #Only admin can!
    print "2)Remove a book"#only administrator can!
    print "3)List all books"
    print "4)Match books with other users" # def .......
    print "5)Change password"
    print "6)Log off" 
    print "7)Exit"
    print ""
    
    optUsers = input("Enter number of chosen option ")
    optionse = {
           1 : AddBook , 
           2 : RemoveBook,
           3 : ListBooks,
           #missing function 4
           5 : ChangePassword,
           6 : Logoff,
           7 : exit,
           }
    optionse[optUsers]()
   


def WelcomeScreenAdmin(name,z):
    if z!="admin-secret":
        return 0
    print ""
    print "Welcome to the program,",name
    print "You are the most powerful user here!"
    print "What you want to do ?"
    print "1)Manage User Files" # def .....
    print "2)Add user" 
    print "3)Delete User" 
    print "4)Log off" 
    print "5)Exit"
    print ""
    optAdmin = input("Enter number of chosen option ")
    options = {
           #1 : manage,
           2 : AddUser,
           3 : DelUser,
           4 : Logoff,
           5 : exit,
           #change password!
           }
    options [optAdmin]()

#User functions:
def AddBook() :
    print ""
    print"Adding a new book"
    author=raw_input("Type a Author of a book ")
    title=raw_input("Type a title of a book")
    Books.append((author,title))
    print "You successfully add new book to the list!!!"
    print ""
    nx=raw_input("Press 1 if you want view all the books ")
    if nx=="1":
        ListBooks()
    print ""
    WelcomeScreen(hehname,"OK")

def RemoveBook():#it should remove if we type author or a book title !
    print ""
    print"Removing a book"
    author=raw_input("Type a Author of a book ")
    title=raw_input("Type a title of a book")
    author=lowercase(author)
   
   
    for x in Books:
        bookTitle,bookAuthor=x
        bookTitle=lowercase(bookTitle)
        bookAuthor=lowercase(bookAuthor)
        
        if  bookTitle==title | bookAuthor==author:
            Books.remove((author,title))
    print "You successfully remove a book from the list!!!"
    print ""
    WelcomeScreen(hehname,"OK")

def ListBooks():
    print ""
    print "List of All books."
    for i in Books:
        auth,tit= i
        print auth,',',tit
    print ""
    WelcomeScreen(hehname,"OK")


def ChangePassword() :
    print "incomplete"
    
    new_password=raw_input("")
    Logoff()
    Users.remove(hehname)
    
#



#---------------------
#--Shared functions:--
#---------------------
def Logoff():
    x="nie ok"
    z="abc"
    print ""
    print"You have successfully log off."
    print ""
    global test
    test=False
    while test==False :
         LogIn(Users)

def LogIn(liste):
    nme = raw_input("Enter User Name: ")
    psword = raw_input("Enter Password: ")
    for i in liste:
        name,password = i 
        if nme == name:
            if psword == password:
               print "Login Successful"
               global test
               test=True
               if name=="Admin":
                   z="admin-secret"
                   WelcomeScreenAdmin(name,z)
               else: 
                    x="ok"
                    WelcomeScreen(name,x)
               
            else:
                print "Login Invalid"
                global test
                test=False



#---------------------------
#Administrators Functions:--
#---------------------------
def AddUser():
    print ""
    print"Creating a new User :"
    us=raw_input("Enter new user name :  ")
    passw=raw_input("Enter new user Password :  ")
    Users.append((us,passw))
    print "You successfully create new User!!!"
    print ""
    WelcomeScreenAdmin("Admin","admin-secret")

def DelUser():
    print ""
    print"Removing existing User. )"
    us=raw_input("Enter name of user which you want to delete")
    passw=raw_input("Enter password for this user ")# not necessary! Admin should have ability to remove without knowing the user password!
    Users.remove((us,passw))
    print "You successfully remove user from the list!!!"
    print ""
    WelcomeScreenAdmin("Admin","admin-secret")



#-Main program
print "Hello"
global test
test=False
while test==False :
    LogIn(Users)





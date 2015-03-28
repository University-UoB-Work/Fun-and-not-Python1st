import random
from Tkinter import *
import pyttsx #need to be installed !
engine = pyttsx.init()


#I consider fortune cookie name as something that happen time to time
#not strictly after Computer saying.I decided to randomize answer 

global comp
comp=-2
class Saying():
    engine = pyttsx.init()
    now=0
    last =0
    answ=[]
    def __init__(self, answ_in):
        self.answ=answ_in
        global comp
        comp=-2
        self.last = len(answ_in)-1

    def getMessage(self):
        if self.now<self.last:
            self.now=self.now+1
        else:
            self.now=0
        return self.answ[self.now]
    
    def getLMessage(self):
        if self.now<=0:
            print"There was nothing before this"
            
        else:
           # print "test inside last...",self.now,"and comp is",comp
            if self.now<self.last:
                self.now=self.now-1
            else:
                self.now=0
            return self.answ[self.now]

    def getRdMessage(self):
        if self.now<self.last:
            self.now=random.randint(0,self.last)
        else:
            self.now=0
        return self.answ[self.now]

Computer_sayings = ["When the program is being tested, it is too late to make design changes.","A well-written program is its own heaven; a poorly-written program is its own hell.","Though a program be but three lines long, someday it will have to be maintained.","Without the wind, the grass does not move. Without software, hardware is useless.","A program should follow the `Law of Least Astonishment'.  It should always respond to the user in the way that astonishes him least.","A program, no matter how complex, should act as a single unit. The program should be directed by the logic within rather than by outward appearances."]
next_CS_saing = Saying(Computer_sayings)
FortuneCookies_saying = ["Rivers need springs.","A single conversation with a wise man is better than ten years of study.","Happiness is often a rebound from hard work. ","The world may be your oyster, but that doesn't mean you'll get it's pearl.","Do not follow where the path may lead. Go where there is no path...and leave a trail","Do not be covered in sadness or be fooled in happiness they both must exist","All progress occurs because people dare to be different.","Your ability for accomplishment will be followed by success.","We can't help everyone. But everyone can help someone.","Whenever possible, keep it simple."]  
nxt_fs_saying = Saying(FortuneCookies_saying)

def NextSaying():
    global comp
    engine = pyttsx.init()
    if random.randrange(0,10)>=5:
        showMessage = next_CS_saing.getMessage()
        comp=1
        print"Computer saying"
    else:
        showMessage = nxt_fs_saying.getMessage()
        comp=0
        print"Fortune cookie saying"

    saying.set(showMessage)

    print showMessage
    engine.say(showMessage)
    engine.startLoop()
    engine.endLoop()

def RandomSaying():
    global comp
#random chosen list with answ and random chosing inside list
    if random.randrange(0,10)>=5:
        showMessage = next_CS_saing.getRdMessage()
        print"Computer saying"
        comp=1
    else:
        showMessage = nxt_fs_saying.getRdMessage()
        comp=0
        print"Fortune cookie saying"
    
    saying.set(showMessage)
   # engine.say(showMessage)
    #engine.StartLoop()
    #engine.endLoop()

def LastSaying():
    global comp
    if comp==1:
        showMessage = next_CS_saing.getLMessage()
        print"Computer saying"
        comp=-2
    elif comp==0:
        showMessage = nxt_fs_saying.getLMessage()
        print"Fortune cookie saying"
        comp=-2
    else:
        print" You have already get previous message.\nClick next to obtain next message."
        comp=-2
        showMessage = "NONE"
    saying.set(showMessage)
    #engine.say(showMessageCS)
    #engine.startLoop()
  #  engine.endLoop()



#########################
#      Main Program 
############################
tkinte = Tk()
tkinte.title("More Sayings.")
saying = StringVar()
saying.set("Welcome.\nClick one of the button.")
dispMessage = Label(tkinte, textvariable = saying, font = ("Arial", 10, "bold")).pack()
buttonNext = Button(tkinte, text = "Next", font=("Arial", 10, "bold"), command=NextSaying).pack()
buttonLast = Button(tkinte, text = "Last", font=("Arail", 10, "bold"), command=LastSaying).pack()
buttonRandom = Button(tkinte, text = "Random", font=("Airal", 10, "bold"), command=RandomSaying).pack()
mainloop()


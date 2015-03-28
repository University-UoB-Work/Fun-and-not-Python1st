from Tkinter import *
import random
import pyttsx #need to be instaled !
engine = pyttsx.init()


#The task require
#however i consider fortune cookie name as something that happen time to time
#not stricly after Computer saying.I decided to randomize answer 


#engine.say('something')
#engine.startLoop()
global which
class Saying():
    engine = pyttsx.init()
    current=0
    last =0
    answers=[]
    def __init__(self, answers_in):
        self.answers=answers_in
        self.last = len(answers_in)-1

    def getMessage(self):
        if self.current<self.last:
            self.current=self.current+1
        else:
            self.current=0
        return self.answers[self.current]
    
    def getLastMessage(self):
        if self.current<=0:
            print"There was nothing before this"
        else:
            
            if self.current<self.last:
                self.current=self.current-1
            else:
                self.current=0
            return self.answers[self.current]

    def getRandomMessage(self):
        if self.current<self.last:# czy powinno byc rowne?
            self.current=random.randint(0,self.last)
        else:
            self.current=0
        return self.answers[self.current]

Computer_sayings = ["When the program is being tested, it is too late to make design changes.","A well-written program is its own heaven; a poorly-written program is its own hell.","Though a program be but three lines long, someday it will have to be maintained.","Without the wind, the grass does not move. Without software, hardware is useless.","A program should follow the `Law of Least Astonishment'.  It should always respond to the user in the way that astonishes him least.","A program, no matter how complex, should act as a single unit. The program should be directed by the logic within rather than by outward appearances."]
next_CS_saing = Saying(Computer_sayings)
FortuneCookies_saying = ["Rivers need springs.","A single conversation with a wise man is better than ten years of study.","Happiness is often a rebound from hard work. ","The world may be your oyster, but that doesn't mean you'll get it's pearl.","Do not follow where the path may lead. Go where there is no path...and leave a trail","Do not be covered in sadness or be fooled in happiness they both must exist","All progress occurs because people dare to be different.","Your ability for accomplishment will be followed by success.","We can't help everyone. But everyone can help someone.","Whenever possible, keep it simple."]  
next_FS_saing = Saying(FortuneCookies_saying)

def Next():
   # engine = pyttsx.init()
    if random.randrange(0,10)>=5:
        showMessage = next_CS_saing.getMessage()
        print"Computer saying"
    else:
        showMessage = next_FS_saing.getMessage()
        print"Fortune cookie saying"

    sayingOne.set(showMessage)
  #  sayingTwo.set(showMessageFS)

    print showMessage
    #engine.say(showMessageCS)
    #engine.startLoop()
   #engine.endLoop()
   # engine.say(showMessageFS)
    #engine.startLoop()
   # engine.endLoop()

def Last():
    if random.randrange(0,10)>=5:#zlokalizuj poprzednia odpowiedz!!! x?
        showMessage = next_CS_saing.getLastMessage()
        print"Computer saying"
    else:
        showMessage = next_FS_saing.getLastMessage()
        print"Fortune cookie saying"
    sayingOne.set(showMessage)
    #engine.say(showMessageCS)
    #engine.startLoop()
  #  engine.endLoop()

def Random():
#random chosen list with answers and random chosing inside list
    if random.randrange(0,10)>=5:
        showMessage = next_CS_saing.getRandomMessage()
        print"Computer saying"
    else:
        showMessage = next_FS_saing.getRandomMessage()
        print"Fortune cookie saying"
    
    sayingOne.set(showMessage)
   # engine.say(showMessage)
    #engine.StartLoop()
    #engine.endLoop()

#########################
#      Main Program 
############################
tk = Tk()
tk.title("More Sayings")
sayingOne = StringVar()
sayingOne.set("Computer Sayings")
displayMessage1 = Label(tk, textvariable = sayingOne, font = ("Arial", 10, "bold")).pack()
btnNext = Button(tk, text = "Next", font=("Arial", 10, "bold"), command=Next).pack()
btnRandom = Button(tk, text = "Random", font=("Airal", 10, "bold"), command=Random).pack()
btnLast = Button(tk, text = "Last", font=("Arail", 10, "bold"), command=Last).pack()

mainloop()

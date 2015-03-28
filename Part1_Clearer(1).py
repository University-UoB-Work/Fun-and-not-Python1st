#######
class Coin:
    #This class lets us create Coin objects

    ##Members  
    showing_heads=True #By default the coin shows "heads"
    value=1#By default the coin has the value 1p

      ##Methods
    def show(self):
        #Returns a string to indicate which face of the coin is showing
        if (self.showing_heads==True):
            return "Heads"
        else:
            return "Tails"

    def turn(self):
        #Turns the coin over
        if (self.showing_heads==True):
              self.showing_heads=False
        else:
            self.showing_heads=True
#######

      
def run_part1():
      coin1=Coin()
      coin2=Coin()

      print "This is coin1"
      print coin1.show()
      print "This is coin2"
      print coin2.show()
      print "We turn them over"
      coin1.turn()
      coin2.turn()
      print "This is coin1"
      print coin1.show()
      print "This is coin2"
      print coin2.show()

# Define the basè class player
class player:
    def play(self):
        print("the player is playing cricket.")
      
# Define the derived class Batsman
class Batsman(player):
    def play(self):
        print("the Batsman is batting.")

# Define the derived class Bowler
class Bowler(player):
    def play(self):
        print("the Bowler is bowling.")

# create objects of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()


class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Creating objects of Batsman and Bowler classes and calling play() method for each object
my_batsman = Batsman()
my_bowler = Bowler()

my_batsman.play()
my_bowler.play()
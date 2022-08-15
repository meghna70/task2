import random

class NumberGuessing:

    def __init__(self):
       
        self.lower= 1
        self.upper= 100

   
    def get_random_number(self):
        return random.randint(self.lower, self.upper)

 
    def start(self):
       
        r = self.get_random_number()
        score=100

        print("Guess the number:")

       
        chances = 10
        while chances>=0:
            guess = int(input("Enter the guessed number: "))
            if guess == r:
                print("\n you got it right")
                break
            elif guess < r:
                print("\n Your number is less than the random number")
                score-=10
            else:
                score-=10
                print("\n Your number is greater than the random number")
            chances -= 1

        if(chances<0):
            print("the number was ", r)
        
        print("\n Final score: ", score)
        
   
numberGuessing = NumberGuessing()
numberGuessing.start()

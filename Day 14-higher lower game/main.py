import random
import art
import game_data
from replit import clear

def getrandomacc():
  return random.choice(game_data.data)
def printinformat(account):
  name=account["name"]
  description=account["description"]
  country=account["country"]
  return f"{name}, a/an {description}, from {country}"
def compare(A,B):
  
  
  if(A["follower_count"]>B["follower_count"]):
    return 'A'
  else:
   return 'B'

def game():
  is_game_over=False
  score=0
  A=getrandomacc()
  B=getrandomacc()
  while(is_game_over==False):
    
    print(art.logo)
    print("Compare A:")
    print(printinformat(A))
    print(art.vs)
    print("Compare B:")
    print(printinformat(B))
    print("Who do you think has a higher number of followers: ")
    choice=input(("Type 'A' or 'B': "))
    if choice == compare(A,B) and choice=='A':
      score+=1;
      print(f"A: {A['follower_count']}")
      print(f"B: {B['follower_count']}")
      print(f"You're right, current score: {score}")
      B=getrandomacc()
      
      
    elif choice == compare(A,B) and choice=='B':
      score+=1;
      print(f"A: {A['follower_count']}")
      print(f"B: {B['follower_count']}")
      print(f"You're right, current score: {score}")
      A=B
      B=getrandomacc()
      
      
   
    else: 
      print(f"You're wrong! Your score is: {score} ")
      is_game_over=True
game()

  
  





 



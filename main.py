import random

print('Welcome Player To Rock,Paper and Scissors',"\U0001F60D")
print('Kindy pick Rock(R), Paper(P), Scissors(S)')
opt = {'R':'Rock',
'S': 'Scissors', 'P':'Paper'}

while True:
  
  user_input = input("Enter a choice R, P, S: ")
  computer_action = ["R", "P", "S"]
  computer_choice = random.choice(computer_action)
  if user_input not in (opt):
            
            print('Invalid input! Please enter a valid input')
            continue
  
  print(f"Player's choice ({opt.get(user_input)}) : CPU choice ({opt.get(computer_choice)})")
  
  
  if user_input == computer_choice:
    print(f"Both players selected {user_input}. It's a tie!","\U0001F600" )
    continue
  elif user_input == "R":
    if computer_choice == "S":
        print("Rock smashes scissors! You win!" ,"\U0001F60D")
        break
    else:
        print("Paper covers rock! CPU wins! You lose." ,"\U0001F605")
  elif user_input == "P":
    if computer_choice == "R)":
        print("Paper covers rock! You win!","\U0001F60D" )
        break
    else:
        print("Scissors cuts paper! CPU wins! You lose.", "\U0001F605")
  elif user_input == "S":
    if computer_choice == "P)":
        print("Scissors cuts paper! You win!","\U0001F605" )
        break
    else:
        print("Rock smashes scissors! CPU wins! You lose.","\U0001F605")
  print("Do you want to play again? (Y/N)","\U0001F607")
  ans = input ()
 
 
    
  if ans == 'n' or ans == 'N':
      break
   

print("\nThanks for playing")
print("\nThanks for playing", "\U0001F60D")
        

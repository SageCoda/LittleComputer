from ASCII import ceaserlogo
from ASCII import hangedmanlogo
from ASCII import hangmanlogo
from ASCII import hangmandictionary
from ASCII import chest
from ASCII import todologo
from ASCII import rockimg
from ASCII import paperimg
from ASCII import scissorsimg
import random
import time 

#  CIPHER FUNCTION
def cipher():
    logo = ceaserlogo
    alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(crypt,plain_text,shift_amount):
    
            w=[]
            for i in (text):
                if i in alphabet:
                    if crypt == 'encode':
                        cypher='encryption'
                        w.append(alphabet[(alphabet.index(i)+shift_amount)%27])
                    elif crypt == 'decode':
                        cypher='decryption'
                        w.append(alphabet[(alphabet.index(i)-shift_amount)%27])
                else:
                    w.append(i)
        
            word="".join(w)
            print(f'The {cypher} reads: {word}')
    

    ceaser(crypt=direction,plain_text=text,shift_amount=shift)

    restart=input("Type yes if you want to go again else type no ").lower()
    if restart !='no':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(crypt=direction,plain_text=text,shift_amount=shift)
        restart=input("Type yes if you want to go again else type no ")
    elif restart=="No".lower():
        start_up()
# CIPHER FUNCTION ENDS
# HANGMAN FUNCTION 1.0
def hangmanz():
    hangman=hangedmanlogo
    hang=list(hangman)


    logo = hangmanlogo
    def get_word():
        words = hangmandictionary
        word=random.choice(words)
        return word

    print(logo)
    print(hang[0])

    print("Let's PLAY!!")
    def empty():
        blank=[]
        for _ in range(word_len):
            blank+='_'
        print(blank)
        return blank  

    word=get_word()
    word_len=len(word)
    blank=empty()

    lives=6
    hang_l=1

        
    while "_" in blank and lives>0 and hang_l<=7 :
        time.sleep(1)
        print('!!###Guess a letter,just one letter')
        time.sleep(1.5)
        print('More than one will cost you a life') 
        time.sleep(1)
        guess=input('Guess: ').lower()
        for position in range(word_len):
        
            if  word[position] == guess:
                blank[position]=guess
        blanke=' '.join(blank)        
        print(blanke)
        if len(guess) >1 or guess is int :
            print("You either just used more than one letter or you used a number.")
            time.sleep(1)
            print("Dont do it again.")
            time.sleep(2)
        if guess not in word:
            lives-=1
            hang_l+=1
            print( hang[hang_l])
            if lives==1:
                print(f'****You have {lives} life left.Try again****')
            elif lives==0:
                print("You've been hung!")
                time.sleep(1)
                print(f'The word was "{word}" ')
                time.sleep(1)
                print('Game Over!')
            else:
                print(f'you have {lives} lives left.Try again')
        
        
        if '_' not in blank:
            print("You guessed it! WELL DONE!:)")
            stop=input("Do you wanna play again? Yes or No? ").lower()
            if stop=="Yes".lower():
                hangmanz()
            else:
                start_up()

#HANGMAN FUNCTION 

# STORY FUNCTION
def story():
   print(chest)
   print("Welcome to Treasure Island.")
   print("Your mission is to find the treasure.") 

   direction=input("Where do you want to go?...\n")
   if direction.lower()=="right":
        print("Ha!You went RIGHT over a cliff.Adventurers these day tsk tsk")
        print("****You fell over a cliff.Game Over****")
   elif direction.lower()=="left":
        action=input("You come come out of the bushes, before you lies a lake.Do you wait or swim?...\n ")
        if action.lower()=="Swim":
            print("Oh, the crocdiles gobble you in one fell snap.You are dead.Game over,adventurer")
        elif action.lower()=="wait":
            print("What's that cave over there? Doors of some sort?")
            door=input("Red, Blue and Green door, which door do you go through?\n ")
            if door.lower()=="blue":
             print("Alas,adventurer, that is but the door of flames")
             print("*****You burned to a crisp.Game Over.*****")
            elif door.lower()=="red":
             print("Such a grave decision adventurer,the wraiths of the underworld claim your soul for  + the end of the ends")
             print("*****The underworld has claimed your soullll.Game Over.*****")
            else:
               print("It couldnt be...it is...the treasure- The treasure of Azbureth!!")
               print("You did it adventurer, you found the treasure!")
               print("*****Congratulations.You found the treasure.******")
               print("***FIN***")
               stop=input("Do you wanna play again? Yes or No? ").lower()
               if stop=="Yes".lower():
                story()
               else:
                start_up()
# STORY FUNCTOIN END

# TODOO LIST FUNCTION
def todo():
 header = todologo
 print(header)

 todos = []
 completed = []
 while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
        
    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        start_up()
        break
        
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todos) or idx <1 :
            print("THERE IS NO TODO WITH THAT NUMBER!")
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    elif command==" ":
        print("TODO cannot be empty")
    else: 
        todos.append(command)
    # Print todos from list
 if completed:
    print(f"You completed {len(completed)} todos today: ")
    for todo in completed:
        print(f"* {todo}")
    stop=input("Are you done? Yes or No? ").lower()
    if stop=="No".lower():
       todo()
    else:
      start_up()
# TODOO LIST FUNCTIon ENDS

# SNAKE EYE FUNCTION
def snake_eyes():
  def rolls():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(roll1, roll2)

    if roll1 == 1 or roll2 == 1:
        score = 0
        print("Awww, snake eye! Your score for this round is 0.")
    else:
        score = roll1 + roll2
        print(f"Your score for this round is {score}.")
    
    return score

  def play_game_2_players():
    player1_score = 0
    player2_score = 0

    while True:
        print(f"{player1}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
            player1_score = 0
        else:
            player1_score += score
            print(f"{player1}'s total score: {player1_score}")
            if player1_score >= 50:
                print(f"{player1} wins!")
                break
            roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
                    player1_score = 0
                    break
                player1_score += score
                print(f"{player1}'s total score: {player1_score}")
                if player1_score >= 50:
                    print(f"{player1} wins!")
                    break
                roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")

        if player1_score >= 50:
            break

        print(f"{player2}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
            player2_score = 0
        else:
            player2_score += score
            print(f"{player2}'s total score: {player2_score}")
            if player2_score >= 50:
                print(f"{player2} wins!")
                break
            roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
                    player2_score = 0
                    break
                player2_score += score
                print(f"{player2}'s total score: {player2_score}")
                if player2_score >= 50:
                    print(f"{player2} wins!")
                    break
                roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")

        if player2_score >= 50:
            break

  def play_game_3_players():
    player1_score = 0
    player2_score = 0
    player3_score = 0

    while True:
        print(f"{player1}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
            player1_score = 0
        else:
            player1_score += score
            print(f"{player1}'s total score: {player1_score}")
            if player1_score >= 50:
                print(f"{player1} wins!")
                break
            roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
                    player1_score = 0
                    break
                player1_score += score
                print(f"{player1}'s total score: {player1_score}")
                if player1_score >= 50:
                    print(f"{player1} wins!")
                    break
                roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")

        if player1_score >= 50:
            break

        print(f"{player2}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player3}'s turn.")
            player2_score = 0
        else:
            player2_score += score
            print(f"{player2}'s total score: {player2_score}")
            if player2_score >= 50:
                print(f"{player2} wins!")
                break
            roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player3}'s turn.")
                    player2_score = 0
                    break
                player2_score += score
                print(f"{player2}'s total score: {player2_score}")
                if player2_score >= 50:
                    print(f"{player2} wins!")
                    break
                roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")

        if player2_score >= 50:
            break

        print(f"{player3}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
            player3_score = 0
        else:
            player3_score += score
            print(f"{player3}'s total score: {player3_score}")
            if player3_score >= 50:
                print(f"{player3} wins!")
                break
            roll_again = input(f"{player3}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
                    player3_score = 0
                    break
                player3_score += score
                print(f"{player3}'s total score: {player3_score}")
                if player3_score >= 50:
                    print(f"{player3} wins!")
                    break
                roll_again = input(f"{player3}, do you want to roll again? (yes/no): ")


  print("Let's play the dice game!")
  player_num = input("How many players are there?")
  if player_num == str(2):
        player1 = input("Player 1, what's your name? ")
        player2 = input("Player 2, what's your name? ")
        play_game_2_players()
  elif player_num == str(3):
        player1 = input("Player 1, what's your name? ")
        player2 = input("Player 2, what's your name? ")
        player3 = input("Player 3, what's your name? ")
        play_game_3_players()
#SNAKE EYE FUNCTION ENDS

# BMI FUNCTION
def bmi():
    height=int(input("Well, alright.Give me your height(in inches)"))
    weight= int(input("Give me your weight(in pounds)"))
    bmii=(weight*703)/(height**2)
    bmii=round(bmii,1)
    if bmii>39.9:
      print(f"Your BMI of {bmii} makes you Morbidly Obese")
    elif bmii>35.0:
     print(f"Your BMI of {bmii} makes you Severely Obese")
    elif bmii>30.0:
     print(f"Your BMI of {bmii} makes you Moderately Obese")
    elif bmii>25.0:
     print(f"Your BMI of {bmii} makes you Overweight")
    elif bmii>18.5:
     print(f"Your BMI of {bmii} makes you Normal")
    elif bmii>16.0:
     print(f"Your BMI of {bmii} makes you Underweight")
    else:
     print(f"Your BMI of {bmii} makes you Severely Underweight")
    stop=input("Do you wanna check again? Yes or No? " ).lower()
    if stop=="No".lower():
      start_up()
    else:
      bmi()
 #  BMI FUNCTION ENDS
# BMI FUNCTION ENDS

# Rock paper scissor function STARTS
def rps():
    rock = rockimg
    paper = paperimg
    scissors = scissorsimg
# Assign the player's move to an ASCII


    move= input("Enter your move(Rock, Paper or Scissors) ").lower()
    if move=="Rock".lower().lower():
     print("YOUR MOVE:"  )
     print(rock)
    elif move=="Paper".lower().lower():
     print("YOUR MOVE:"  )
     print(paper)
    elif move=="Scissors".lower().lower():
     print("YOUR MOVE:"  )
     print(scissors)

# Turn that random number into the computer's RPS move
    num = random.randint(1,3)
    if num ==1:
     print("COMPUTER MOVE:"  )      
     print(rock)
    elif num ==2:
      print("COMPUTER MOVE:"  )
      print(paper)
    else:
      print("COMPUTER MOVE:"  )
      print(scissors)


# Comparing the User and Computer's move
    if move=="Rock".lower() and num==1:
     print("Its a Tie")
     print("Let's go again.I won't lose!")
    elif move=="Rock".lower() and num==2:
      print("Paper beats rock.You lose!")
      print("HAHA! VICTORY!")
    elif move=="Rock".lower() and num==3:
      print("Rock beats Scissors .You win! :)")
      print("I'll take the next win though")

    elif move=="Paper".lower() and num==1:
     print("Paper beats Rock.You Win")
     print("Tsk,I'll take the next Win")
    elif move=="Paper".lower() and num==2:
     print("Its a Tie.")
     print("Let's go again.I won't lose!")
    elif move=="Paper".lower() and num==3:
     print("Scissors beats Paper.You lose!")
     print("HAHA! VICTORY!")

    elif move=="Scissors".lower() and num==3:
     print("Its a Tie")
     print("Let's go again.I won't lose!")
    elif move=="Scissors".lower() and num==2:
     print("Scissors beats Paper.You Win")
     print("Tsk,I'll take the next Win")
    elif move=="Scissors".lower() and num==1:
     print("Rock beats Scissors.You lose!")
     print("HAHA! VICTORY!")
    else:
     print("Invalid Move!Try again")
    
    stop=input("Do you wanna stop? Yes or No? ").lower() 
    if stop=="No".lower():
       rps()
    else:
      start_up()
# #  END OF RPS FUNCTION

# START_UP FUNCTION allows a loop from after something is 
# chosen from menu is chosen to after a the program is exited from
def start_up():
    # decisions stage
  print("*****MENU*****")
  print(menu)
  decide=input("What would you like to do now? ").lower()
  if decide=="RPS".lower():
   print("Alright, let's play!")
   rps()
  elif decide=="BMI".lower():
   print("OOOO Boyy 👀")
   bmi()
  elif decide=="Snake eyes".lower():
     snake_eyes()
  elif decide=="Todo".lower():
     todo()
  elif decide=="Story".lower():
   story()
  elif decide=="Hangman".lower():
   hangmanz()
  elif decide=="Cipher".lower():
   cipher()
# START_UP FUNCTION ENDS


#ORIGINAL STARTUP FUNCTION FOR [LIL COMP.]

menu= ["RPS","BMI","Snake Eyes","Todo","Story","Cipher "]
# Wake up AI
user=input("Say hi to wake me up! ")
while user !="hi":
  user=input("Please try again.Say hi ")
  print("Hi,nice to meet you! ")
  name=input("What's your name? ")
day=input("How was your day? ")
print("Ahh... A day will go how a day will go I suppose ")
time.sleep(1)
# Decisions stage by giving a menu of choices
print("****MENU****")
print(menu)
print("Here's our menu today.")
decide=input("What would you like to do? ").lower()
if decide=="RPS".lower():
   print("Alright, let's play!")
   rps()
elif decide=="BMI".lower():
   print("OOOO Boyy 👀")
   bmi()
elif decide=="Snake eyes".lower():
   snake_eyes()
elif decide=="Todo".lower():
   todo()
elif decide=="Story".lower():
   story()
elif decide=="Hangman".lower():
   hangmanz()
elif decide=="Cipher".lower():
   cipher()

  










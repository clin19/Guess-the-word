import random

words = ["python", "strings", "integers", "indexes", ]
words = random.choice(words) #picks random word from the list
print(words) #REMEMBER TO DELETE AFTER COMPLETION
print("Guess the characters, Good luck!")


guesses = " " #Empty string 
tries = 12

while tries > 0:   #while loop begins
    wrong_guess = 0
    for char in words:   #Iterate every character in chosen word
        if char in words:
            if char in guesses:  #insert character into empty string (guesses)
                print(char, end = " ")
            if char not in guesses:
                print("_",end= " ") 
                wrong_guess +=1
    if wrong_guess == 0:
        print("you win!")
        print("the word is:" , words)
        break
    guess = input("guess a character: ")
    guesses += guess
    if guess.lower() == "quit": #User wants to quit
        print("You chose to quit")
        print("The word was:", words)
        break
    if guess not in words:
        tries -= 1
        print("Wrong, you have",tries, "more guesses" )
        if tries == 0:
            print("you lose")
   
    

#add lower (methods)/ Force input into lowercase
 # method that does not take inputs other than letters
 # Change quit option into =
 #Remember to delete to delete the print(words) statement in line 5.

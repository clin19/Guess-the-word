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
   
    

#add lower (methods)/ Force input into lowercase

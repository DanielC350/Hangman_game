#create a list of letters with
answer= input("Insert your word: \n")

answer_letters = list(answer.lower())

blank = ["_"]* len(answer_letters)
print(blank)

counter = 0

win= False

letters_guessed =" "
letters_guessed_intro ="Letters guessed: \n"
def listToString(list):
    str1 = ""
    return(str1.join(list))

def check_guess(guess):
    if len(guess) == 1:
        letter_guessed = guess[0]
        letter_guessed =letter_guessed.lower()
        global letters_guessed
        if letter_guessed in letters_guessed:
            print("you have already guessed that letter")
            return True
        letters_guessed += letter_guessed + ", "
        if letter_guessed in answer_letters:
            letter_location = [i for i, x in enumerate(answer_letters) if x == letter_guessed]
            for i in letter_location:
                print(i)
                blank[int(i)] = letter_guessed
            print(listToString(blank))
            return True
        else:
            global counter
            print("Try again. You have " + str(4-counter) + " more Tries:"), print(letters_guessed_intro + letters_guessed.rstrip(", "))
            return False
    if len(guess) > 1:
        if listToString(guess).lower() == answer.lower():
            global win
            win = True
        else:
            print("Try again. You have " + str(4-counter) + " more Tries:"), print(letters_guessed)
            return False


while counter != 5:
    users_guess = input("Guess a letter, or a word: ")
    guess_letters = list(users_guess)
    if check_guess(guess_letters) == False:
        counter += 1
    if counter == 5:
        print("Sorry, you ran our of Guesses. You Lose :(")
    if blank== answer_letters:
        win = True
    if win == True:
        print("You guessed it! The word was: " + answer)
        counter = 5

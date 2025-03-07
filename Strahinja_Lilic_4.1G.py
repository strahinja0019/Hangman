import time
import random
import sys

#time was imported for time.sleep()
#radom was imported for random.randint()
#sys was imported for sys.exit()

def updateUI(FilePath):
    """UptadeUI is used to get the hangman picture
       based on the number of wrong guesses,
       it returns the hangman picture which will be printed with loadGameUIImages"""
    try:
        hangman_file = open(FilePath + "/Hangman.txt", "r")
        hangman_content = hangman_file.read()
        hangman_file.close()
        hangmen = hangman_content.split('\n\n')#splits every hangman in a list by every \n\n which happens if you skip a line 2 times thus making a blank space
        
        if wrong_guess < len(hangmen): #Check if there are still hangman images available for the current wrong guess count
            return hangmen[wrong_guess]
        else:
            return "Hangman image not found for guess:", wrong_guess

    except FileNotFoundError:
        #Default hangman images if the file is not found
        hangmen = ["""
 +---+
 |   
 |    
===  """],["""
 +---+
 |   0
 |    
===  """],["""
 +---+
 |   0
 |   | 
===  """],["""
 +---+
 |   0
 |  /| 
===  """],["""
 +---+
 |   0
 |  /|\\ 
===  """],["""
 +---+
 |   0
 |  /|\\ 
=== /"""],["""
 +---+
 |   0
 |  /|\\ 
=== / \\ """]
        return hangmen[wrong_guess][0]


def loadGameUIImages(FilePath):
    """loadGameUIImages takes the returned value from updateUI and prints
       a different hangman picture based on the ammount of wrong guesses
       which is calculated in updateUI

       It takes the parameter FilePath which is used to find the project file"""

    # Retrieve the hangman image content based on the number of wrong guesses
    hangman_image = updateUI(FilePath)
    print(hangman_image)

def clear():
    """clear is used to add 50 blank lines so that it looks more neat"""
    temp_rand = 0
    while True:
        if temp_rand == 50:
            break
        print("")
        temp_rand = temp_rand + 1

def displayTitle(titleFilePath):
    """displayTitle is used to locate the file of the project
       by going in File Explorer and
       at the top it would say for example: C:/Users/PCname/Desktop/My project

       It takes the parameter titleFilePath which is used to find the project file"""
    try:    
        title = open(titleFilePath+"\Title.txt")
        print(title.read())
        title.close()
    except FileNotFoundError:
        print("Your file directory couldn't be found")
        print("")
        print("")
        print("")
        print("HANGMAN") 

def displayMenu():
    """displayMenu displays options to be selected by the user ranging from
       asking for user information all to exit the game"""
    time.sleep(1)
    clear()
    print("Choose your option")
    print("")
    print("Input your data -I")
    print("Play the game -P")
    print("Add more words -A")
    print("Display the leadboard -D")
    print("Exit the game -E")

def displayDifficulty():
    """displayDifficulty displays 3 different difficulties that can be be
       selected by the user based on his skill level like easy / normal / hard"""
    print("")
    print("")
    print("")
    print("")
    print("Choose your difficulty")
    print("")
    print("Easy [5 words] -E")
    print("Normal [7 words] -N")
    print("Hard [10 words] -H")

def generateRandomWord(wordinput,value_min,value_max):
    """generateRandomWord would open the text file located in the project,
       the program will read content of the text and split it line by line,
       then based on users selected difficulty will randomly select one of the
       words which the user will have to guess

       It takes parameters wordinput which is used to find the project file,
       value_min which is used to act as the minimum value for a random word,
       value_max which is ysed to act as the maximum vakye fir a random word"""
    try:
        words_opened_file = open(wordinput+"\ListOfWords.txt")
        words = words_opened_file.read().split()
        words_opened_file.close()
        if value_max != 59:
            random_number = random.randint(value_min, value_max)
        else:
            list_of_words = (len(words) - 1)
            random_number = random.randint(value_min,list_of_words)
        
    except FileNotFoundError:
        print("Your file directory coudlnt be found, resorting to backup words")
        words = ["abruptly","buffalo","cricket","duplex","fashion","galaxy"]
        random_number = random.randint(0, 5)
    word = words[random_number]
    return word

def check_letter(generated_word,guessed_letter):
    """check_letter takes the users input and checks if it is in the random
       generated word,if it is the score goes up,
       if it isnt the score goes down

       It takes parameters generated_word which is the actual word,
       guessed_letter which is the user's input"""
    global score
    global wrong_guess
    global correct_guess
    if guessed_letter == "":
        print("You need to input a letter")
    else:
        if len(guessed_letter) == 1:
            if guessed_letter in previous_guess:
                print("You can only guess new letters")
            elif guessed_letter in generated_word:
                for temp in generated_word:
                    if temp == guessed_letter:
                        correct_guess = correct_guess + 1
                        if len(generated_word) == 5:
                            score = score+50
                        elif len(generated_word) == 7:
                            score = score+75
                        elif len(generated_word) == 10:
                            score = score+100
                        else:
                            score = score+50
                print("----Letter guessed correctly----")
                print("")
                print("")
            else:
                wrong_guess = wrong_guess +1
                score = score - 25
                print("----Letter guessed incorrectly----")
        else:
            print("Only 1 letter per time")
        if guessed_letter not in previous_guess:
            previous_guess.append(guessed_letter)
        return correct_guess,wrong_guess,previous_guess

def nextTurn():
    """nextTurn is used to simulate the actual gameplay
       by showing the unguessed spacesand then filling them with
       guessed letters"""
    global guessed_letter
    global total_score
    guessed_letter = "$"
    underscores = "_ "*len(generated_word)
    while wrong_guess <6:
        if correct_guess != len(generated_word):
            loadGameUIImages(titleinput) #Displays the hangman at the beginning of every round
            for i in range(len(generated_word)):
                if guessed_letter in generated_word[i]:
                    underscores = underscores[:i+i] + guessed_letter + underscores[i+i+1:]
                     #It checks if the guessed_letter is equal to any letter in generated_word by going one by one through them,
                     #if is is it replaces the underscore with the guessed letter by
                     #replacing underscores variable with first underscores[2x i] letters
                     #(since every 2nd space in underscores is a " " so it is i+i) so underscores[:i+i]  
                     #and adding the actual letter user inputed, then everything after the [2x i] so [i+i+1]
            print(underscores)
            while True:
                print("Previous guesses were: ",previous_guess)
                guessed_letter = input("Enter your guess: ")
                if guessed_letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
                    print("Only a letter in the aplhabet")
                elif guessed_letter.lower() in "abcdefghijklmnopqrstuvwxyz":
                        break
            check_letter(generated_word,guessed_letter)
            print("Correctly guessed: ",correct_guess)
            print("Wrongly guessed: ",wrong_guess)
            print("")
            print("")
            time.sleep(3)
        elif correct_guess == len(generated_word):
            print("You win")
            time.sleep(2)
            break
    if wrong_guess == 6:
        loadGameUIImages(titleinput)
    total_score = total_score + score
    print("")
    print("Your score this round is: ",score)
    print("The word was ",generated_word)
    print("")
    time.sleep(1)
    print("Your total score is: ",total_score)
    time.sleep(1)
        


titleinput = input("Enter your Project filepath: ")
displayTitle(titleinput)
score = 0
total_score = 0
wrong_guess = 0
correct_guess = 0
previous_guess = []
guessed_letter = "$"
datainput = ""



while True:
    displayMenu()
    choice = input(">").upper()
    if choice == "I":
        datainput = input("Enter your name and surename in this way: NameSurename\n>")
    elif choice == "P":
        displayDifficulty()
        while True:
            difficulty = input(">").upper()
            if difficulty == "E":
                minimum = 0
                maximum = 19
                break
            elif difficulty == "N":
                minimum = 20
                maximum = 39
                break
            elif difficulty == "H":
                minimum = 40
                maximum = 59
                break
            else:
                print("Choose one of the options")
        wrong_guess = 0
        correct_guess = 0
        previous_guess = []
        generated_word = generateRandomWord(titleinput,minimum,maximum)
        underscores = len(generated_word)
        nextTurn()
    elif choice == "D":
        try:
            a_i = 0
            leaderboard_lines = open(titleinput+"\Leaderboard.txt")
            leaderboard = leaderboard_lines.readlines()
            sorted_leaderboard = sorted(leaderboard, key=lambda number: int(number.split()[0]), reverse=True)
            # Leaderboard is split line by line, for every line there are 2 words, first word score(a number),second word NameSurename(letters)
            #by using key = lambda amd making another temporary value number, number is leaderboard but is only using the first word(score) because it is number.split()[0]
            # so then leaderboard can be sorted by using the first number. 
            for line in sorted_leaderboard:
                if a_i >9:
                    break
                print(line.strip())
                a_i = a_i +1
            leaderboard_lines.close()
        except FileNotFoundError:
            print("FileDirectory couldnt be found")

    elif choice == "A":
        try:
            while True:
                try:
                    number_of_words = int(input("How many words do you want to add: "))
                    break
                except ValueError:
                    print("It needs to be a whole number")
            for current_number in range(number_of_words):
                while True:
                    word_to_add = input("Input the word with 10 characters: ").lower()
                    if len(word_to_add) == 10 and all(char in "abcdefghijklmnopqrstuvwxyz" for char in word_to_add):
                    #all(char in "" for char in word_to_add)  checks if all letters in
                    #word_to_add are actual letters allowed,
                    #if all but one letter are in allowed letters
                    #it still doesnt pass the condition
                        words = open(titleinput+"\ListOfWords.txt", "a")
                        words.write("\n"+word_to_add)
                        words.close()
                        break
                    else:
                        print("It needs to be 10 letters and only letters in the aplhabet")
        except FileNotFoundError:
            print("You cant add words since your file couldnt be found, restart the program")
    elif choice == "E":
        print("Do you wish to upload your score to the leaderboard")
        print("Yes -Y")
        print("No -N")
        while True:
            save = input(">")
            if save.upper() == "Y":
                while True:
                    if datainput == "":
                        print("Enter your name and surename in this way: NameSurename")
                        datainput = input(">")
                    else:
                        try:
                            leaderboard_write = open(titleinput+"\Leaderboard.txt", "a")
                            leaderboard_write.write("\n"+str(total_score)+" "+datainput)
                            leaderboard_write.close()
                            sys.exit()
                        except FileNotFoundError:
                            print("Your leaderboard folder couldnt be found")
                            sys.exit()
            elif save.upper() == "N":
                sys.exit()
            else:
                print("choose either Y or N")

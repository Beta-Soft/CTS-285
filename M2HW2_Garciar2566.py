# CTS 285
# DATAMAN Sprint 2
# Rebecca Garcia

#-----------------------------------------------------------------------------#       
        #display menu
def main():
   
    repeat = True
    while repeat == True:
        print("__________________________________")
        print("     Main Menu                    ")
        print("-----------------------           ")
        print("1. Answer Checker                 ") 
        print("2. Memory Bank                    ")
        print("3. Number Guesser                 ")
        print("4. Exit                           ")
        # input from user
        print("__________________________________")
        choice = input("Enter a number: ")
        # check if choice is one of four options
        if choice == '1':
                answerCheckerMenu()
    
        elif choice == '2':
                memoryBankMenu()
    
        elif choice == '3':
                numberGuesserMenu()
                
        elif choice == '4':
                print("Goodbye!")
                repeat = False
        else:
            print("Invalid Input")

#-----------------------------------------------------------------------------#
def answerCheckerMenu():
    inputList  = []  #list where user input is stored
    answerList = []  #list where correct answers are stored
    correct    = 0   #count correct input
    incorrect  = 0   #counts incorrect input
    qcount     = 0   #count for how many questions have been answered
    
    
    print("__________________________________")
    print("     Answer Checker               ")   
    print("-----------------------           ")
    print("- Enter equations as 'Number1 ? Number2'\nreplacing '?' with desired operator")
    print("-'q' to Quit") #TODO: q or Q to quit Answer checker
    print("-----------------------------------")
    while qcount < 10:
        userInput = input ("> ")
        if userInput == "q":
            print("\n", correct, "correct,", incorrect, "incorrect : out of", qcount)    
            return

        else:
            inputList.append(userInput) 
            answer = math(userInput)       #sends to MATH then splits/puts into list
            answerList.append(answer[2])   #adds answer to list
               
            #formats
            qFormat =  (str(userInput)+" = ")
            answerGuess =  float(input (qFormat))          
            
            #loops for correct/incorrect
            if answerGuess == answer[2]:
                print("\n Correct!")
                correct += 1
                qcount += 1
            if answerGuess != answer[2]:
                print("\n Try Again!")
                answerGuess =  float(input (qFormat))
                if answerGuess == answer[2]:
                    print("\n Correct!")
                    correct += 1
                    qcount += 1
                else:
                    print("\n E   E   E \nIncorrect! Answer is:", str(userInput)+" = ", answer[2])
                    incorrect += 1
                    qcount += 1
                    
    print("\n", correct, "correct,", incorrect, "incorrect: out of", qcount)    
    
#-----------------------------------------------------------------------------#
def memoryBankMenu():
    print("     Memory Bank")
#-----------------------------------------------------------------------------#
def numberGuesserMenu():
    print("     Number Guesser")                    
#-----------------------------------------------------------------------------#            
def math(entry):
   
    entrySplit = []
    mathList = []
    # add               ~~~~~~~~~~~~~~~~
    if "+" in entry: #checks operator
      entrySplit = entry.split("+") #takes operator out ex. 4 + 5 would be '4 5' 4 index0, 5 index1
      x = int(entrySplit[0])        #left of operator is assigned x, indexed 0 in list
      y = int(entrySplit[1])        #right of operator is assigned y, indexed 1 in list
      z = x + y                     #assigns z to answer, indexed 2 in list
      mathList.extend((x,y,z))      #adds to end
      mathList.append("+")          #adds to end, operator indexed 3
      return mathList
    # sub               ~~~~~~~~~~~~~~~~
    elif "-" in entry:
      entrySplit = entry.split("-")
      x = int(entrySplit[0])
      y = int(entrySplit[1])
      z = x - y
      mathList.extend((x,y,z))
      mathList.append("-")
      return mathList
    # div               ~~~~~~~~~~~~~~~~ 
    elif "/" in entry:
      entrySplit = entry.split("/") #TODO: display Remainder ex. 10/4 = 2 r2
      x = int(entrySplit[0])
      y = int(entrySplit[1])
      try:
          z = x / y
          mathList.extend((x,y,z))
          mathList.append("/")
          return mathList
      except ZeroDivisionError:
          print("You cannot divide by zero!")
      return
    # prod               ~~~~~~~~~~~~~~~~
    elif "*" in entry:
      entrySplit = entry.split("*")
      x = int(entrySplit[0])
      y = int(entrySplit[1])
      z = x * y
      mathList.extend((x,y,z))
      mathList.append("*")
      return mathList
      
    elif entry == "exit" or "quit":
       return mathList
    else:
        print("Not Valid!")            
            
#-----------------------------------------------------------------------------#       
main() 
# CTS 285
# DATAMAN Sprint 1
# Rebecca Garcia

#-----------------------------------------------------------------------------#       
        #display menu
def main():
   
    repeat = True
    while repeat == True:
        print("\n     Main Menu")
        print("------------------")
        print("1. Answer Checker")
        print("2. Memory Bank")
        print("3. Number Guesser")
        print("4. Exit")
        # input from user
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
    inputList = []
    answerList = []
    correct = 0
    incorrect = 0
    qcount = 0
    
    print("\nAnswer Checker")
        
    print("Enter equations with format: \nNumber1+Number2|q to Quit") #TODO: q or Q to quit Answer checker
    userInput = input ("> ")
    inputList.append(userInput) 
    answer = math(userInput)       #splits & sends to MATH
    answerList.append(answer[2]) #adds answer to list
       
    #LOOP##
    qFormat =  (str(userInput)+" = ")
    answerGuess =  float(input (qFormat))
   
    
    if answerGuess != answer[2]:
        print("\nIncorrect")
        answerGuess =  float(input (qFormat))
    if answerGuess == answer[2]:
        print("\nThat is correct!")
        correct += 1
        qcount += 1
    else:
        print("Incorrect...answer is:", answerList[0],"\n")
        incorrect += 1
        qcount += 1
            
          
    print("\nYou got", correct, "correct,", incorrect, "incorrect out of 10")
    
#-----------------------------------------------------------------------------#
def memoryBankMenu():
    print("Memory Bank")
#-----------------------------------------------------------------------------#
def numberGuesserMenu():
    print("Number Guesser")            
            
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
expenses = []

#Example expenses

expense1 = {'amount': '51.00', 'category': 'shirt'} #Test categories and expenses and dolar amount
expenses.append(expense1)
expense2 =  {'amount': '21.55', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense(): #Function to remove an expense
  while True: #In case user enters something invalid
    listExpenses() #Lists expenses available to be deleted
    print("What expense would you like to remove?")
    try: #Gathers user input or failure to cast input to int
      expenseToRemove = int(input(">")) #User enters number so casts into int so user can delete any incorrect expenses
      del expenses[expenseToRemove] 
      break #Added break to avoid being stuck in loop of removing expenses
    except:
      print("invalid input. Please try again.")

#Function to add an expense
def addExpense(amount, category): 
  expense = {'amount': amount, 'category': category} # Temporary object to store expenses
  expenses.append(expense)

def printMenu(): #Function to print menu 
  print("Please choose from one of the following options...")
  print("1. Add A New Expense")
  print("2. Remove An Expense")
  print("3. List All Expenses")

def listExpenses(): #This is a function to list all expenses
  print("\nHere is a list of your expenses...")
  print("-----------------------------------") # Seperator for a friendly user experience set up
  counter = 0 #Number that user can reference
  for expense in expenses:
    print("#", counter, " - ", expense['amount'], " - ", expense['category']) # Prints the expenses
    counter += 1
  print("\n\n") #Double line break for spacing


if __name__ == "__main__":  #Layout of code and Main function
  while True:
### Prompt the user
    printMenu() #Gives user options to choose from
    optionSelected = input(">") #User enters option
    
    if optionSelected == "1": 
      print("How much was this expense?") 
      while True:
       try: #Incase any issues with user input 
          amountToAdd = input("> ") 
          break #Assuming everything entered is correct it will break out  
       except:
         print("Invalid input. Please try again.")
         
      print("What category was this expense?")
      while True:
        try:
          category = input("> ")
          break
        except:
          print("Invalid input. Please try again.") #Alerts user there is an input error
        
      addExpense(amountToAdd, category) #Adds expense to list
    elif(optionSelected == "2"):
     removeExpense() #Removes expense from list
    elif(optionSelected == "3"):
     listExpenses() #Lists all expenses 
    else: 
     print("Invalid input. Please try again.")
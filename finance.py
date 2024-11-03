"""
FINANCE TRACKER SYSTEM

requirements 
1. Menu screen to display all features
2. Input income
3. Input expense
4. Count total (expense, income, and net balance)

software requirements
1. a dictionary as a database ✅
2. dbhandler to query the database ✅
3. save function to handle data saving ✅
4. read function to get data ✅
5. income feature ✅
6. expense feature ✅
7. count total income, expence, and net balance
8. a renderer ✅
9. a main menu

BIG PROBLEM
i think the renderer should just be replaced with a refresher (SOLVED)
"""
import os
import datetime

# -- models ---

database = {"income": [
  {"amount" : 1081},
  {"amount" : 1081},
  {"amount" : 1081}
], "expense": [
  {"amount" : 521},
  {"amount" : 521},
  {"amount" : 521}
]}


def dbHandler(table):  # to query data from the database
  global database
  return database[table]


def save(table, data):  #save data to database
  database[table].append(data)


def read(table, index=None, range=None):
  table = dbHandler(table)
  if range is not None:  #return data if range specified
    return table[index:range]

  if index is not None:  # return data on index if specified
    return table[index]

  return table  #if nothing is specified, then return all data


# -- controllers ---


def income(): # income feature
  state = 0

  # data we will fill in later
  amount = None
  source = None
  date = None
  global database

  while 1 < 2:  # state machine
    refresh()
    header()
    drawLine()
    print('Add income')
    drawLine()
    print('')
    if amount is not None:
      print(f'Income amount: ${amount}')

    if source is not None:
      print(f'Source of income: {source}')

    if date is not None:
      print(f'Date of income: {date}')

    print('')


    if state == 0:  # -- input amount state
      amount = input('Enter amount: ')

      if amount.isnumeric(): # validate if input is number
        amount = int(amount)
        state = 1
      else:
        amount = None

    elif state == 1:  # -- input source state
      source = input('Enter source: ')

      if not source == '': 
        state = 2 # validate if source is not empty string
      else:
        source = None
    elif state == 2:  # -- input date state
      date = input('Date of income (yy-mm-dd): ')
      try:
          # date = datetime.date.fromisoformat(date)
          datetime.date.fromisoformat(date)
          state = 3
      except ValueError:
          date = None

    elif state == 3: # -- store data state
      save('income', {"amount" : amount, "source" : source, "date" : date})
      state = 4
    elif state == 4: # -- results screen
      print('Data saved successfully!')
      drawLine()
      print('Would you like to add more data?')
      print('')
      print('(1) Add more data')
      print('(2) Back to main menu')
      drawLine()
      selection = input('Input selection number: ')

      if selection == '1': # reset if add more data
        state = 0
        amount = source = date = None

      if selection == '2':
        return


def expense(): # expense feature
  state = 0

  # data we will fill in later
  amount = None
  source = None
  date = None
  global database

  while 1 < 2:  # state machine
    refresh()
    header()
    drawLine()
    print('Add expense')
    drawLine()
    print('')
    if amount is not None:
      print(f'Expense amount: ${amount}')

    if source is not None:
      print(f'Type of expense: {source}')

    if date is not None:
      print(f'Date of expense: {date}')

    print('')


    if state == 0:  # -- input amount state
      amount = input('Enter amount: ')

      if amount.isnumeric(): # validate if input is number
        amount = int(amount)
        state = 1
      else:
        amount = None

    elif state == 1:  # -- input source state
      source = input('Enter type of expense: ')

      if not source == '': 
        state = 2 # validate if source is not empty string
      else:
        source = None
    elif state == 2:  # -- input date state
      date = input('Date of expense (yy-mm-dd): ')
      try:
          # date = datetime.date.fromisoformat(date)
          datetime.date.fromisoformat(date)
          state = 3
      except ValueError:
          date = None

    elif state == 3: # -- store data state
      save('expense', {"amount" : amount, "type" : source, "date" : date})
      state = 4
    elif state == 4: # -- results screen
      print('Data saved successfully!')
      drawLine()
      print('Would you like to add more data?')
      print('')
      print('(1) Add more data')
      print('(2) Back to main menu')
      drawLine()
      selection = input('Input selection number: ')

      if selection == '1': # reset if add more data
        state = 0
        amount = source = date = None

      if selection == '2':
        return



def countBalance():
  # -- countn income
  incomes = read("income")
  totalIncome = 0
  for income in incomes:
    totalIncome += income["amount"]

  # -- count expense
  expenses = read("expense")
  totalExpense = 0
  for expense in expenses:
    totalExpense += expense["amount"]
  print(totalIncome - totalExpense)

  input("tesy")

# -- views ---

def refresh(): # clear the screen
  os.system('clear')

def header(): # add a header to the screen
  print("""
================================

    PERSONAL FINANCE MANAGER

================================
  """)

def drawLine(): # draw a seperator line to the screen
  print('--------------------------------')


# -- main --

def main():
  while 1 < 3:
    refresh()
    header()
    print("Main menu")
    print('')
    print ("(1) Add income")
    print ("(2) Add expense")
    print ("(3) Count Balance")
    print("")
    drawLine()
    select = input("Please select action: ")

    if select == "1": # income feature state
      income()
    elif select == "2": # expense feature state
      expense()
    elif select == "3": # count balance state
      countBalance()
    elif select == "4": # exit program state
      return


#main()
countBalance()



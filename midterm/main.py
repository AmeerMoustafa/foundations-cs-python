###########
# Imports #
###########

#Importing Python's built in OS method to read from files and create a clear function for tidiness purposes.

import os

# Importing Regex to isolate integers from strings for sorting purposes

import re

# Importing the date module from datetime to get today's date.

from datetime import date


#######################
# Main Data Structure #
#######################

# My programs main data structure, I've chosen a 2D array. This will be built by our importTickets function

ticket_structure = []

####################
# Helper Functions #
####################


# A simple function to clear the screen, for OCD purposes. O(1)
def clear():
  # If statement used to check if the system is windows or not
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')


#############################
# Merge sort implementation #
#############################

# O(N*LogN) N being the size of the array we're sorting


# I have chosen merge sort as my algorithm of choice because O(NlogN) is faster than O(N^2) when N is over 100 according to my research. Since the number of tickets could very well go over 100. I have chosen Merge sort.

# Research Reference:
# https://stackoverflow.com/questions/23329234/which-is-better-on-log-n-or-on2
# Video showed me a cleaner implementation, learned it before but decided to include it here regardless.
# https://www.youtube.com/watch?v=iR1CXiC7OQc


def merge(left, right):  # This function will handle the merging part of our merge sort implementation
  merged_array = []
  index_left = 0
  index_right = 0

  while index_left < len(left) and index_right < len(right):
    if left[index_left] < right[index_right]:
      merged_array.append(left[index_left])
      index_left += 1
    else:
      merged_array.append(right[index_right])
      index_right += 1

  merged_array += left[index_left:]
  merged_array += right[index_right:]

  return merged_array


def mergeSort(list):  # This function will handle the splitting of the arrays in our implementation

  if len(list) <= 1:
    return list

  mid = len(list) // 2
  left = mergeSort(list[:mid])
  right = mergeSort(list[mid:])

  return merge(left, right)


# A function that will sort tickets using regex, will be used to auto increment ticket IDs when booking

# O(N*logN) is our worse case scenario, N being the amount of tickets we need to sort.

def sortTickets():

  ticket_list = []

  # Extracting numbers from our ticket IDs and appending to ticket_list for easier sorting
  for row in range(len(ticket_structure)):
    numbers = re.findall('[0-9]+', ticket_structure[row][0])
    for number in numbers:
      ticket_list.append(int(number))

  # Applying mergeSort to our ticket_list, for easy incrementation
  ticket_list = mergeSort(ticket_list)
  largest_ticket = ticket_list[len(ticket_list) - 1]
  return largest_ticket


##################
# Menu functions #
##################

# Initial display function and log-in form.

# O(1)

def displayMenu():  
  print("""
  
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝\n""")
  print("Welcome to ticketer, please login to continue\n")

  username = input("Enter your username: ")

  if username == "admin":
    attempts = 5
    password = input("Enter your password: ")

    while password != "admin123123":
      clear()
      print(f"Incorrect password, please try again. {attempts} remaining.")
      attempts -= 1
      password = input("Attempt entering your password again: ")

      if attempts == 0:
        clear()
        return print(
          "Allowed password attempts exceeded, Incident will be reported")
    displayAdmin()
  
  else:
    displayUser(username)


# Admin display menu

# O(N) N being the amount of times we have to write to the file if the admin chooses to save

def displayAdmin():

  clear()
  print("""
  
████████╗██╗░█████╗░██╗░░██╗███████╗████████╗███████╗██████╗░
╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print("""Welcome Administrator:\n
            [1] Display Statistics
            [2] Book a Ticket
            [3] Display all tickets
            [4] Change Ticket's priority
            [5] Disable Ticket
            [6] Run Events
            [7] Exit\n""")


  choice = int(input("Please select a number to continue: "))
  if choice == 1:
    getStatistics()
  elif choice == 2:
    bookTicketAdmin()
  elif choice == 3:
    displayTickets()
  elif choice == 4:
    changePriority()
  elif choice == 5:
    removeTicket()
  elif choice == 6:
    runEvents()
  elif choice == 7:
    choice2 = input("Press Y if you would like to save your changes, any other button to discard and exit: ")
    if choice2 == "y" or choice2 == "Y":
      writeTickets()
      print("[-] Exiting")
      return
    else:
      print("[-] Exiting")
      return



# User display Menu

# O(N) N being the amount of times we have to write to the file when the user exists

def displayUser(username):
  clear()
  print("""
  
████████╗██╗░█████╗░██╗░░██╗███████╗████████╗███████╗██████╗░
╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print(f"""Welcome {username}, Please select a function:\n
              [1] Book a Ticket
              [2] Exit\n""")
  
  choice = int(input("Please select a number to continue: "))
  if choice == 1:
    bookTicketUser(username)
  elif choice == 2:
    writeTickets()
    print("[-] Exiting")
    return


#########################
# Main program functions#
#########################

# A function to import our data and build our data structure.

# O(N) N representing how many lines we need to import from our text file


def importTickets():
  with open('data.txt', 'r') as data:
    for line in data:
      # Remove spaces from a line and split every line into an array
      line_array = line.replace(' ', '').split(',')
      # Remove "\n" from the end of every array returned and convert our priority string into an integer
      line_array[-1] = int(line_array[-1].strip())
      ticket_structure.append(line_array)


# Resources used for this function:
# https://realpython.com/read-write-files-python/ - To learn how to read and write files as well as iterate through.


# A function to write our modified structure into our text file

# O(N) N representing how many lines we need to write to our text file

def writeTickets():
  with open('data.txt', 'w') as data:
    for row in ticket_structure:
        data.write(', '.join([str(col) for col in row]) + '\n')

# Resources used for this function:
# https://stackoverflow.com/questions/60692703/how-to-write-a-matrix-2d-array-to-a-text-file-python
# Found a function that does exactly what I needed here, list comprehension is also very cool


# Function to display the event ID with the highest number of tickets

# O(N) N in this case being the size of the list we're running our max() function on.

def getStatistics():
  clear()
  print(f"""

░██████╗████████╗░█████╗░████████╗██╗░██████╗████████╗██╗░█████╗░░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝╚══██╔══╝██║██╔══██╗██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░██║╚█████╗░░░░██║░░░██║██║░░╚═╝╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░╚═══██╗░░░██║░░░██║██║░░██╗░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░██║██████╔╝░░░██║░░░██║╚█████╔╝██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═════╝░
        \n""")

  event_list = []

  # Iterating through our main structure and appending our events to the event_list list.
  for row in range(len(ticket_structure)):
    event_list.append(ticket_structure[row][1])
  
  # Using max() to count how many times an event appears withint our event_list. The event that appears the most has the most tickets
  most_popular_event = max(event_list)
  
  print(f"{most_popular_event} is the event with the highest ticket sales\n")


  choice = input("Please enter Y to check statistics again or any other key to return to the main menu: ")
  if choice == "y" or choice == "Y":
    getStatistics()
  else:
    displayAdmin()


# Resources for this function:
# I used the below link, to learn about the max() function, which I used to return the most repeated value in the array
# https://bobbyhadz.com/blog/python-find-most-common-element-in-list


# A function allowing the admin to book tickets

# O(N*logN) due to our sortTickets() function being called using mergeSort under the hood and the amount of tickets we need to sort.

def bookTicketAdmin():
  clear()
  print(f"""

██████╗░░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
██████╦╝██║░░██║██║░░██║█████═╝░██║██╔██╗██║██║░░██╗░
██╔══██╗██║░░██║██║░░██║██╔═██╗░██║██║╚████║██║░░╚██╗
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
        \n""")
  
  # Getting the largest ticket from our sortTickets function
  largest_ticket = sortTickets()

  # Getting input for the user and saving it in a ticket array with the ticket ID incremeneted
  print("Please fill out the below prompts to book a new ticket to the system:\n")

  username = str(input("Please enter a username to append: "))
  print()
  eventID = str(input("Please enter an eventID in the following format (ex: ev001, ev002): "))
  print()
  eventDate = str(input("Please enter the event date in the following format (ex: 2023-08-03): ")).replace('-','')
  print()
  priority = int(input("Enter the ticket holder's priority in the following format (ex: 0): "))
  print()

  ticket = [f"tick{largest_ticket + 1}", eventID, username, eventDate, priority]

  print(f"""
        ######################
        # Your current Ticket#
        ######################
        
        Ticket ID: {largest_ticket + 1}        
        EventID: {eventID}
        Username: {username}      
        EventDate: {eventDate}
        Priority: {priority}
        """)

  # Asking the admin if they would like to save their ticket to the system and appending the ticket to the main structure if so.
  choice1 = input(str("Press Y to book your ticket or any other key to discard it and return to the main menu: "))
  if(choice1 == "Y" or choice1 == "y"):
    ticket_structure.append(ticket)
    print()
    print("Your ticket has been added to the system\n")
    choice2 = str(input("Press Y to add another ticket or any other key to return to the main menu: "))
    if(choice2 == "Y" or choice2 == "y"):
      bookTicketAdmin()
    else:
      displayAdmin()
  else:
    displayAdmin()

# Resources used for this function
# I knew about regex before, but used this to figure out how to do what I needed to do
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html


# A function allowing the user to book a ticket as opposed to the admin. Does almost the same thing as the function above.

# O(N*logN) due to calling merge sort, same as our above function.

def bookTicketUser(username):
  clear()
  print(f"""

██████╗░░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
██████╦╝██║░░██║██║░░██║█████═╝░██║██╔██╗██║██║░░██╗░
██╔══██╗██║░░██║██║░░██║██╔═██╗░██║██║╚████║██║░░╚██╗
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
        \n""")
  largest_ticket = sortTickets()

  print("Please fill out the below prompts to book a new ticket to the system:\n")
  eventID = str(input("Please enter an eventID in the following format (ex: ev001, ev002): "))
  print()
  eventDate = str(input("Please enter the event date in the following format (ex: 2023-08-03): ")).replace('-','')

  ticket = [f"tick{largest_ticket + 1}", eventID, username, eventDate, 0]

  print(f"""
        #######################
        # {username}'s Ticket     #
        #######################
        
        Ticket ID: {largest_ticket + 1}        
        EventID: {eventID}
        Username: {username}      
        EventDate: {eventDate}
        Priority: {0}
        \n""")
  
  choice1 = input(str("Press Y to book your ticket or any other key to discard it and return to the main menu: "))
  if(choice1 == "Y" or choice1 == "y"):
    ticket_structure.append(ticket)
    print()
    print("Your ticket has been added to the system\n")
    choice2 = str(input("Press Y to add another ticket or any other key to return to the main menu: "))
    if(choice2 == "Y" or choice2 == "y"):
      bookTicketUser(username)
    else:
      displayUser(username)
  else:
      displayUser(username)


# A function that sorts and display every ticket from today onwards sorted by date and event ID

# The big O of our function is O(N^2 * logN), The most expensive thing is iterating through the rows of our array and applying mergesort to every inner row.

def displayTickets():
  clear()
  print(f"""

████████╗██╗░█████╗░██╗░░██╗███████╗████████╗░██████╗
╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝
░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░╚█████╗░
░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░░╚═══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░██████╔╝
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░\n""")

  # Getting today's date and formatting it for easier sorting and comparison.
  today = str(date.today()).replace('-', '')

  sorted_tickets = []
  # Iterating through our main structure and appending any tickets with todays date or a future date into a new array.
  for row in range(len(ticket_structure)):
    if ticket_structure[row][3] >= today:
      sorted_tickets.append(ticket_structure[row].copy())

  # Appending "!" to the necessary columns for sorting then applying merge sort on the rows of our 2D array.
  for row in range(len(sorted_tickets)):
    sorted_tickets[row][1] = f'!{sorted_tickets[row][1]}'
    sorted_tickets[row][3] = f'!{sorted_tickets[row][3]}'
    sorted_tickets[row][4] = str(sorted_tickets[row][4])
    sorted_tickets[row] = mergeSort(sorted_tickets[row])
  
  # Applying merge sort to our sorted_tickets structure as a whole
  sorted_tickets = mergeSort(sorted_tickets)

  print("[-] Now displaying tickets sorted by date and event ID\n")

  # Formatting and displaying tickets sorted by date and event ID.
  for row in range(len(sorted_tickets)):
    ticket_date = sorted_tickets[row][0]
    eventID = sorted_tickets[row][1]
    print(f"{ticket_date[7:9] + ' / ' + ticket_date[5:7] + ' / ' + ticket_date[1:5] } - Event ID: {eventID[1:len(eventID)]} - Ticket ID: {sorted_tickets[row][4]} - Username: {sorted_tickets[row][3]} - Priority: {sorted_tickets[row][2]}\n")

  choice = input("Press Y to display tickets again or any key to return to the main menu: ")
  if(choice == "y" or choice == "Y"):
    displayTickets()
  else:
    displayAdmin()

# Resources used for this function:
# Used the below website to learn about the date object and it's today method in datetime
# https://realpython.com/python-datetime/
# Had a strange bug with this statement that altered the original list sorted_tickets.append(ticket_structure[row])
# added copy() to create a copy of the list, but not exactly sure why bug was happening.
# I couldn't understand why appending to a new array, modified the original array, maybe because of aliasing.


# Function to change the priority of our ticket. 

# O(N) N being the amount of rows we have to loop through in our main structure.

def changePriority():
  clear()
  print(f"""

██████╗░██████╗░██╗░█████╗░██████╗░██╗████████╗██╗░░░██╗
██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝
██████╔╝██████╔╝██║██║░░██║██████╔╝██║░░░██║░░░░╚████╔╝░
██╔═══╝░██╔══██╗██║██║░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░
██║░░░░░██║░░██║██║╚█████╔╝██║░░██║██║░░░██║░░░░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
        \n""")

  ticket_id = str(input("Enter your ticket ID with the following order (ex: tick1, tick11): "))
  priority = int(input("Enter your tickets priority number: (ex: 0): "))

  ticket_flag = False

  # Iterate through the main structure and search for a ticket that matches our criteria. set our ticket_flag to true if a ticket is found and change it's priority.
  for row in range(len(ticket_structure)):
    if ticket_structure[row][0] == ticket_id and ticket_structure[row][4] == priority:
      ticket_flag = True

      new_priority = int(input("Your ticket has been found, please enter a new priority number: "))
      ticket_structure[row][4] = new_priority

      print("Ticket priority has been changed \n")
      print()

      choice = input("Press Y to change another ticket's priority or any other key to return to the main menu: ")
      if(choice == "Y" or choice == "y"):
        changePriority()
      else:
        displayAdmin()

  # Go into this loop if our ticket_flag remains false, meaning a ticket has not been found
  if not ticket_flag:
    choice = input("Your ticket has not been found, press Y to search for another ticket or any key to return to the main menu: ")
    if(choice == "Y" or choice == "y"):
      changePriority()
    else:
      displayAdmin()



# A function to find and delete tickets

# O(N) N being the amount of tickets we need to iterate through.

def removeTicket():
  clear()
  print("""
██████╗░███████╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗  ████████╗██╗░█████╗░██╗░░██╗███████╗████████╗
██╔══██╗██╔════╝████╗░████║██╔══██╗██║░░░██║██╔════╝  ╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
██████╔╝█████╗░░██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░  ░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░
██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░  ░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░
██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗  ░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░
        \n""")

  ticket_id = str(input("Enter a ticket to delete using the following format (ex: tick1, tick2): "))
  print()

  found_ticket = False

  # Iterate through the main ticket structure and find the ticket_ID taken from the user.
  for row in range(len(ticket_structure)):
    if ticket_structure[row][0] == ticket_id:
      to_remove = row
      found_ticket = True
  
  # If a ticket is found, remove it and ask the admin if they would like to search for another ticket
  if found_ticket:
    ticket_structure.pop(to_remove)
    print("Ticket with the provided ID has been found and has been deleted")
    choice = input("Press Y to search for and delete another ticket or any other key to return to the main menu: ")
    if choice == "Y" or choice == "y":
      removeTicket()
    else:
      displayAdmin()
  else:
    print("Ticket with the provided ID has not been found")
    choice = input("Press Y to search for another ticket or any other key to return to the main menu: ")
    if choice == "Y" or choice == "y":
      removeTicket()
    else:
      displayAdmin()


# A function that will display today's events sorted by priority then remove them from the structure.

# The big O of our function is O(N^2 * logN), The most expensive thing is iterating through the rows of our array and applying mergesort to every inner row.

def runEvents():
  print("""

██████╗░██╗░░░██╗███╗░░██╗  ███████╗██╗░░░██╗███████╗███╗░░██╗████████╗░██████╗
██╔══██╗██║░░░██║████╗░██║  ██╔════╝██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔════╝
██████╔╝██║░░░██║██╔██╗██║  █████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░╚█████╗░
██╔══██╗██║░░░██║██║╚████║  ██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░░╚═══██╗
██║░░██║╚██████╔╝██║░╚███║  ███████╗░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░██████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝  ╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░\n""")
  
  today = str(date.today()).replace('-', '')

  todays_tickets = []

  # Iterate through a copy of our main structure, used a copy to be able to iterate through and delete from the original array without any bugs.
  # Append today's tickets to a new array for sorting and remove them from the original array.
  for row in ticket_structure.copy():
    if row[3] == today:
      todays_tickets.append(row)
      ticket_structure.remove(row)
  
  print("Todays events:\n")

  if not todays_tickets:
      print()
      error_message = input("[-] Todays events have been ran, press any button to return to the main menu: ")
      return displayAdmin()

  # Iterate through todays tickets and add '!' to the necessary strings for easier sorting, then applying merge sort to the inner rows
  for row in range(len(todays_tickets)):
    todays_tickets[row][1] = f'!{todays_tickets[row][1]}'
    todays_tickets[row][4] = str(f'!{todays_tickets[row][4]}')
    todays_tickets[row] = mergeSort(todays_tickets[row])

  # Apply merge sort on the outer array.
  sorted_list = mergeSort(todays_tickets)

  # Iterate through the sorted list and format the tickets for display.
  for row in sorted_list:
    priority = row[0]
    eventID = row[1]
    print(f'Priority: {priority[1:len(priority)]} - event ID: {eventID[1:len(eventID)]} - Username: {row[3]} - ticket ID: {row[4]}\n')
  
  choice = input("Events are running, press Y to run events again or any other button to return to the main menu: ")

  if choice == "y" or choice == "Y":
    runEvents()
  else:
    displayAdmin()
    


# References for this function:
# learned how to delete elements from a list while iterating through it from here and how for..in works vs for..in..range()
# https://bobbyhadz.com/blog/python-for-loop-remove-elements-from-list#remove-elements-from-a-list-while-iterating-in-python
  


# The worst case runtime of our program is O(N^2 * logN)

#############      
# Main loop #
#############
def main():
  importTickets()
  displayMenu()




main()

#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  # ## DATE OBJECTS
  # # Get today's date from the simple today() method from the date class
  # today = date.today()
  # print("Today's date is", today)

  # # print out the date's individual components
  # print("Date compoents:", today.day, today.month, today.year)
  
  # # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("Todays Weekday number:", today.weekday())
  # days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  # print("which is a: ", days[today.weekday()])
  # ## DATETIME OBJECTS
  # # Get today's date from the datetime class
  today = datetime.now()
  print(today)
  
  # Get the current time
  t = datetime.time((datetime.now()))
 

  
if __name__ == "__main__":
  main();
  
#Title of program
print("What day is it program")
#accept an input and store it as a variable
day = input("What day is it? ")
#Change input to lower case

day = day.lower()

#compare day to text
if day == "monday":
  print("Today is 1")
  choice = input("Are you sure?")

  if choice == "Yes":
    print("Yeet")
  else:
    print("No Yeet")
  
#compare day to text 
elif day == "tuesday":
  print("Today is 2")

#if unable to compare to anything print the following
else:
  print("Im not sure try again")



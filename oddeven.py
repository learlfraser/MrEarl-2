#Take user input
inp_num = input("Enter a number: ")

#Convert string to int
inp_num = int(inp_num)

if inp_num == 0:
  print(inp_num, "is Even")
elif inp_num%2==0:
  print(inp_num, "is Even")
else:
  print(inp_num, "is Odd")
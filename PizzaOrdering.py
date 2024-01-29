print("Welcome to the Pizza Ordering System!")
size = input("Enter the size of pizza S M L : ")
extra_pepperoni = input("Do you want extra pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if size == "S":
  bill += 5
elif size == "M":
  bill += 10
else:
  bill += 15

if extra_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 4
if extra_cheese =="Y":
  bill += 1
print(f"Your bill is {bill}")
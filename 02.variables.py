# Variable = A container for a value (string, integer, float,boolean)
#            A variable behaves as if it was the value it contains

#Strings
first_name = "John"
last_name = "Doe"
food = "pizza"
email = "Bro123@fake.com"

print(f"Hello {first_name}")    # f-string
print(f"You like {food}")
print(f"Your email is: {email}")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#Integer
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You're buying {3} items")
print(f"Your class has {30} students")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is: ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance} kilometers")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# Boolean
is_student = False

if is_student:
    print("You're a student")
else:
    print("You're not a student")

for_sale = True

if for_sale:
    print("That item is for sale.")
else:
    print("That item is NOT available!")

is_online = True

if is_online:
    print("You're online.")
else:
    print("You're offline.")
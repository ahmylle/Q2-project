import random
#welcome
print("Welcome to my guessing game about cars")
#list
print ("this is the list of cars you can use") 
cars=["hellcat","trackhawk","skylineGTR","Honda civic","G Wagon","Corvette C6", "BMW I8"]
print(cars)
#users question
userCar=input("choose a car of your choice")
userQ=input("create a question for your car")
print(userQ)
if userQ ==userCar:
#randomize the questions
    random=["guess","guess2","guess3","guess4","guess5", "guess6","guess7" ]

#q1
car1="hellcat"
for attempt in range(3):
    guess = input(f"this car has a 8 cylinder supercharged hemi v8? (try {attempt+1}/3) ")
    if guess.strip()== car1:
        print("Congrats")
        break
else:
    print(f"thats not it. The car was {car1}")

#Q2
car2="trackhawk"
for attempt in range(3):
    guess2 = input(f"this car has the same engine as the hellcat but its made by jeep? (try {attempt+1}/3) ")
    if guess2.strip() == car2:
        print("congrats you got it right")
        break
else:
    print(f"you got it wrong it was {car2}")
    
#q3
car3="skylineGTR"
for attempt in range(3):
    guess3 = input(f"this car is famous for being paul walkers car in fast and furious? (try {attempt+1}/3) ")
    if guess3.strip() == car3:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car3}")

#q4
car4="Honda civic"
for attempt in range(3):
    guess4 = input(f"this car has a inline 4 engine and is known for being a good reliable first car? (try {attempt+1}/3) ")
    if guess4.strip() == car4:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car4}")

#q5 
car5="G Wagon"
for attempt in range(3):
    guess5=input(f"this SUV is known for being a luxary car and is mentioned alot in music? (try {attempt+1}/3) ")
    if guess5.strip() == car5:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car5}")

#q6
car6= "Corvette C6"
for attempt in range(3):
    guess6=input(f"This car is known for being the same car as Lightning Mcqueen from cars? (try {attempt+1}/3) ")
    if guess6.strip() == car6:
        print("you got it right")
        break
else:
    print(f"you got it wrong it was {car6}")

#q7
car7="BMW I8"
for attempt in range(3):
    guess7=input(f" This BMW is known for its butterfly doors and its supercharged 3 cylinder engine. (try {attempt+1}/3) ")
    if guess7.strip() == car7:
        print("you got it right")
        break
else:
    print(f"you got it wrong it was {car7}")
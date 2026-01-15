import random
#welcome
print("Welcome to my guessing game about cars")
#list
print ("this is the list of cars you can use") 
cars=["hellcat","trackhawk","skylineGTR","Honda civic","G Wagon","Corvette C6", "BMW I8", "press eneter if you need a hint"]
print(cars)
# #users question
# userCar=input("choose a car of your choice")
# userQ=input("create a question for your car")
# print(userQ)
# if userQ ==userCar:


#q1
car1="hellcat"
for attempt in range(3):
    guess = input(f"this car has a 8 cylinder supercharged hemi v8? (try {attempt+1}/3) ")
    hint1=input("do you want a hint? (yes/no) ")
    if hint1=="yes":
        print("its a dodge car")
    if guess.strip()== car1:
        print("Congrats")
        break
else:
    print(f"thats not it. The car was {car1}")

#Q2
car2="trackhawk"
for attempt in range(3):
    guess2 = input(f"this car has the same engine as the hellcat but its made by jeep? (try {attempt+1}/3) ")
    hint2=input("do you want a hint? (yes/no) ")
    if hint2=="yes":
        print("its an an upgraded jeep grand cherokee")
    if guess2.strip() == car2:
        print("congrats you got it right")
        break
else:
    print(f"you got it wrong it was {car2}")
    
#q3
car3="skylineGTR"
for attempt in range(3):
    guess3 = input(f"this car is famous for being paul walkers car in fast and furious? (try {attempt+1}/3) ")
    hint3=input("do you want a hint? (yes/no) ")
    if hint3=="yes":
        print("its a nissan")
    if guess3.strip() == car3:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car3}")

#q4
car4="Honda civic"
for attempt in range(3):
    guess4 = input(f"this car has a inline 4 engine and is known for being a good reliable first car? (try {attempt+1}/3) ")
    hint4=input("do you want a hint? (yes/no) ")
    if hint4=="yes":
        print("its a japanese car thats very common in the us but it can be modded a lot")
    if guess4.strip() == car4:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car4}")

#q5 
car5="G Wagon"
for attempt in range(3):
    guess5=input(f"this SUV is known for being a luxary vehicle? (try {attempt+1}/3) ")
    hint5=input("do you want a hint? (yes/no) ")
    if hint5=="yes":
        print("its made by mercedes benz")
    if guess5.strip() == car5:
        print("correct")
        break
else:
    print(f"you got it wrong it was {car5}")

#q6
car6= "Corvette C6"
for attempt in range(3):
    guess6=input(f"This car is known for being the same car as Lightning Mcqueen from cars? (try {attempt+1}/3) ")
    hint6=input("do you want a hint? (yes/no) ")
    if hint6=="yes":
        print("its an american sports car made by chevrolet")
    if guess6.strip() == car6:
        print("you got it right")
        break
else:
    print(f"you got it wrong it was {car6}")

#q7
car7="BMW I8"
for attempt in range(3):
    guess7=input(f" This BMW is known for its butterfly doors and its supercharged 3 cylinder engine. (try {attempt+1}/3) ")
    hint7=input("do you want a hint?(yes/no)")
    if hint7=="yes":
        print("its mentioned in the hit playboicarti song shawty inlove")
    if guess7.strip() == car7:
        print("you got it right")
        break
else:
    print(f"you got it wrong it was {car7}")
# Questions=[guess,guess2,guess3,guess4,guess5,guess6,guess7]
# print(random.choice(Questions))
# print(random.choice(guess,guess2,guess3,guess4,guess5,guess6,guess7))
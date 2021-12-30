print("Welcome to Golf")
import random
distance = 100
print("The hole is",distance,"yards away")
print("Enter 'w' for a wood club (1-100 yards)")
print("enter 'h' for a hybrid club (1-70 yards)")
print("enter 'i' for an iron club (1-30 yards)")
print("enter 'e' for a wedge club (1-15 yards)")
shotNum = 0
while True:
    w = random.randint(1,100)
    h = random.randint(1,70)
    i = random.randint(1,30)
    e = random.randint(1,15)
    enter = input("Enter a club or press enter to shoot or q to quit: ")
    if enter.lower() == "w" or enter.lower() == "":
        shotNum += 1
        shot = w
        print("Shot: You got", shot, "yards")
        print("Distance Remaining:", abs(distance) - shot,"yards")
        distance = abs(distance) - shot
    if enter.lower() == "h":
        shotNum += 1
        shot = h
        print("Shot: You got", shot, "yards")
        print("Distance Remaining:", abs(distance) - shot,"yards")
        distance = abs(distance) - shot
    if enter.lower() == "i":
        shotNum += 1
        shot = i
        print("Shot: You got", shot, "yards")
        print("Distance Remaining:", abs(distance) - shot,"yards")
        distance = abs(distance) - shot
    if enter.lower() == "e":
        shotNum += 1
        shot = e
        print("Shot: You got", shot, "yards")
        print("Distance Remaining:", abs(distance) - shot,"yards")
        distance = abs(distance) - shot
    if distance == 0:
        print("Game Over")
        print("It took you", shotNum, "shots")
        break
    elif enter.lower() == "q":
        break
    

        



import random
print("hello")
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
length = len(people)
count = 0
while count<length:
    if people[count]=="Waldo":
        print("je hebt waldo gevonden hij zit op nummer"+str(count))
    count +=1
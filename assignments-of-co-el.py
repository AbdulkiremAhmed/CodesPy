name = "Elzero"
print(f"Second Letter Is : {name[1]} \nThird Letter Is : {name[2]} \nLast letter Is : {name[-1]}")
print(name[1:4])
print(name[ : :2])
print(name[-2: :-2])

name = "#@#@Elzero#@#@"
print(name.strip("#@"))

num = "23"
print(num.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))


name_one = "OSamA"
name_two = "osaMA"
print(name_one.upper())
print(name_two.lower())

name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

name = "Elzero"
print(name.index("z"))

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))

name = "Abdukllirem"
age = 20
country = "Sudan"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")


# الدرس 19 الي 20
print(f"Integer => {type(100)}")
print(f"Float => {type(100.0)}")
print(f"Complex => {type(100+100j)}")

complexNum = 1+2j
print(complexNum.imag)
print(complexNum.real)

num = 10
# print((float(num)).10f)
print("%.10f"%(float(num)))

num = 159.650
print(int(num))
print(type(int(num)))

# 100 ? 115 = -15   =>  -
# 50 ? 30 = 1500   =>  *
# 21 ? 4 = 1   =>  %
# 110 ? 11 = 10   =>  /
# 97 ? 20 = 4   =>  //


myFriends = ["Ahmed", "Naser","Alfateh","Nabil","Mohammed"]
print(myFriends[0])
print(myFriends.pop(0))
print(myFriends[-1])
print(myFriends.pop(-1))

print(myFriends[1: :2])
print(myFriends[ : :2])

print(myFriends[1:4])
print(myFriends[-2: ])

myFriends[-2: ] = ["Elzero"]
print(myFriends)

myFriends = ["Naser","Alfateh","Nabil"]
myFriends.append("Abdukllirem")
myFriends.insert(0,"Aya")
print(myFriends)

myFriends = ["Ahmed", "Naser","Alfateh","Nabil","Mohammed"]
myFriends[-2: ] = []
print(myFriends)
myFriends[-1: ] = []
print(myFriends)

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
print(friends+employees+school)

myFriends = ["Ahmed", "Naser","Alfateh","Nabil","Mohammed"]
myFriends.sort(reverse = False)
print(myFriends)
myFriends.sort(reverse = True)
print(myFriends)

print(len(myFriends))

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])

myTuple = "Abdukllirem",
print(myTuple)
print(type(myTuple))

myTuple = ("Osama", "Naser", "alryh")
myList = list(myTuple)
myList[0] = "Elzero"
# tuple(myTuple)
print(myList)


nums = (1, 2, 3)
letters = ("A", "B", "C")
newTuple = nums + letters
print(newTuple)
print(type(newTuple))

myValue = ("Abdukllirem", 20, "Male", "Student")
n ,a ,s ,e = myValue
print(n)
print(a)
print(s)

myList = [1, 5, 4, 3, 3, 2, 1]
myList.sort()
unique_list = myList.copy()
print(unique_list)
print(type(unique_list))
print(unique_list[ :-1])


mySetOne  = {1, 2, 3}
mySetTwo = {"A", "B", "C"}
print(mySetOne.union(mySetTwo))
mySetOne.update(mySetTwo)
print(mySetOne)
# mySetOne  = {1, 2, 3}
mySetOne.add("A")
mySetOne.add("B")
mySetOne.add("C")
print(mySetOne)

mySetOne  = {1, 2, 3}
print(mySetOne)
mySetOne.clear()
print(mySetOne)
mySetOne.update("A", "B")
print(mySetOne)
# mySetOne.remove("C")
mySetOne.discard("C")

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# print(set_one.issuperset(set_two))
print(set_one.issubset(set_two))

myDic = {
    "one" : {
        "Name" : "HTML",
        "Progress" : "90%",
    },
    "two" : {
        "Name" : "CSS",
        "Progress" : "80%",
    },
    "three" : {
        "Name" : "Js",
        "Progress" : "87%",
    }
}
# print(f"{myDic.get('one','Name')} Progress Is {myDic.get('one','Progress')}")

print(f"{myDic['one']['Name']}   Progress Is {myDic['one']['Progress']}")
print(f"{myDic['two']['Name']}   Progress Is {myDic['two']['Progress']}")
print(f"{myDic['three']['Name']} Progress Is {myDic['three']['Progress']}")
myDic.update({"four" : {"Name" : "Python","Progress" : "95%"}})
print(f"{myDic['four']['Name']}   Progress Is {myDic['four']['Progress']}")


print(bool("Abdulkirem"))
print(bool(9))
print(bool(9.9))
print(bool({1,2,3}))

print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool({}))

html = "80%"
css = "86%"
js = "75%"
print(html>"50%" and css>"50%" and js>"50%")

num_one = 10
num_two = 20
num = 20
print(num>num_one or num>num_two)
print(num>num_one and num>num_two)

num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result = result ** 3
print(result)
result = result % 26000
print(result)
result = result / 5
print(result)
print(type(result))
result = str(result)
print(type(result))


name = input("Enter Your Name : ").strip().capitalize()
print(f"Hello {name} , How Are You ")

age = int(input("Enter Your Age : "))
print(type(age))
if age < 16:
    print(f"Hello Your Age Is Under {age}, Some Articles Is Not Suitable For You")
if age >= 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

first_name = input("Enter Your First Name : ").strip().capitalize()
second_name = input("Enter Your Second Name : ").strip().capitalize()
print(f"Hello {first_name} {second_name:.1s}.")

email = input("Enter Your Email : ").strip().lower()
name = email[:email.index("@")].capitalize()
print(name)
web = email[email.index("@")+1:email.index(".")]
print(web)
domain = email[email.index(".")+1:]
print(domain)

# 40 >>> 46

num1 = int(input("Enter A Fisrt Number : ").strip())
num2 = int(input("Enter A Second Number : ").strip())
operation = input("What\'s A Operation : ").strip()
print(type(num1),type(num1))
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} =>> {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} =>> {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} =>> {result}")

elif operation == "/":
    result = num1 / num2
    print(f"{num1} / {num2} =>> {result}")

elif operation == "%":
    result = num1 % num2
    print(f"{num1} % {num2} =>> {result}")

elif operation == "//":
    result = num1 // num2
    print(f"{num1} // {num2} =>> {result}")

else:
    print("It\'s Wrong")


hisAge = 17
print("App Is Suitable For You" if hisAge == 17 else "App Is Not Suitable For You")

age = int(input("Enter Your Age : ").strip())
print(type(age))
ageMonthes = age * 12
ageWeeks = age * 4
ageDays = age * 365
ageHours = age * 24
ageMunets = age * 60
ageSeconds = age * 60

if age > 10 and age < 100:
    print(f"{ageMonthes:,} Monthes")
    print(f"{ageWeeks:,} Weeks")
    print(f"{ageDays:,} Days")
    print(f"{ageHours:,} Hours")
    print(f"{ageMunets:,} Munets")
    print(f"{ageSeconds:,} Seconds")

else:
    print("It\'s Wrong")


# 47 >>> 55

num = int(input("Enter Your Number : ").strip())
count = 0
if type(num) == int and num > 0:
    print("pass")
    num -= 1
    while num >= 1:
        if num == 6:
            num -= 1
            pass

        print(f"{num} \nIt\'s Done" if num == 1 else num)
        num -= 1
        count += 1
    print(f"It\'s Numbers Is Done Successfull : {count}")
else:
    print("You Con\'t Enter A Number Is Integer")


myFriends = ["Ahmed", "Naser","alfateh","Nabil","mohammed"]
count = 0
paas = 0
while count != len(myFriends):
    if myFriends[count][0] == myFriends[count][0].upper():
        print(f"Friend Num {count + 1}:Is Name\'s  {myFriends[count]}")
        count += 1
    # elif myFriends[count][0] != myFriends[count][0].upper():
    #     print(myFriends[count])
    #     count += 1
    else:
        count += 1
        paas += 1
        pass

print(f"Friends Printed And Ignored Names Count Is {paas}")

# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
#
# while skills:
#     print(f"{skill for skill skills }")


myFriends = []
top = 4
addFriend = input("Added A Friend : ").strip()
while top != 0:
    if addFriend == addFriend.upper():
        print("Invalid Name")
        addFriend = input("Added A Friend : ").strip()
        print(f"You Con Add {top} Friends")
    elif addFriend == addFriend.capitalize():

        myFriends.append(addFriend)
        print(f"Friend {addFriend} Added => 1st Is A Capital")
        print(f"Names Left in List Is {top}")
        addFriend = input("Added A Friend : ").strip()
        top -= 1
    elif addFriend == addFriend.lower():

        myFriends.append(addFriend)
        print(f"Friend {addFriend} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {top}")
        addFriend = input("Added A Friend : ").strip()
        top -= 1
print(f"You Con\'t add A Friend , Becouse Of Your List Is Full")
print(f"Those Are Your Friends ", myFriends)



listNum = [2, 4, 5, 1, 5, 9, 0, 30, 12]
listNum.sort(reverse=True)
for num in listNum:
    if num % 5 == 0:

        print(f"{num}")

print("All Numbers Printed")

for num in range(1,21):
    if num < 10:
        if  num in [6, 8 ,12]:
            print(f"{num}")
        print(f"{str(num).zfill(1)}")
    else:
        print(f"{num}")
print("Loop Is Done")



my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
a = 100
b = 80
c = 40
result = 0
for rank, point in my_ranks.items():
    print(f"My Rank in {rank} Is {my_ranks[rank]} ",end="")
    if my_ranks[rank] == "A":
        result += a
        print(f"And This Equal {a} Points")

    elif my_ranks[rank] == "B":
        result += b
        print(f"And This Equal {b} Points")
    # elif my_ranks[rank] == "C":
    #     print(f"And This Equal {c} Points")
    else:
        result += c
        print(f"And This Equal {c} Points")

print(f"Total Points Is {result}")


students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
a = 100
b = 80
c = 40
d = 20


for student in students:
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    result = 0
    for sabject,rank in students[student].items():
        if rank == "A":
            print(f"- {sabject} => {a} Points")
            result += 100
        elif rank == "B":
            print(f"- {sabject} => {b} Points")
            result += 80
        elif rank == "C":
            print(f"- {sabject} => {c} Points")
        else:
            result += 40
            print(f"- {sabject} => {d} Points")
            result += 20
    print(f"Total Points Is {result}")

number_one = int(input("Enter First Number :").strip())
number_Two = int(input("Enter Second Number :").strip())
apoti = input("Enter As Aption : ").strip()
def calculate(num1 ,num2 ,apotion):

    if apotion == "+" or apotion.startswith("A") == True or apotion.startswith("a") == True or apotion == " " or apotion == "":
        return num1 + num2
    elif apotion == "-" or apotion.startswith("S") == True or apotion.startswith("s") == True or apotion == "s":
        return num1 - num2
    elif apotion == "/" or apotion == "multiply" or apotion.startswith("M") == True  or apotion.startswith("m") == True :
        return num1 / num2
    else:
        return "Wrong"
print(calculate(number_one,number_Two,apoti))


def addition(*number):
    a = 0
    for num in number:
        if num == 10:
            continue
        elif num == 5:
            a -= 5
        else:
            a += num
    return a
print(addition(10,3,10,5,1,7,8))




def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")

    else:
        print(f"Hello {name} Your Skills Is")
        for skill in skills:
            print(f"- {skill}")

show_skills("Abdulkirem", "HTML", "CSS", "JS", "Python")


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
print(say_hello("Abdulkirem",10,"add"))

def get_score(**sabject):
    for sab, score in sabject.items():
        print(f"{sab} => {score}")

get_score(Math=90, Science=80, Language=70)


def get_people_scores(name="Unknown", **sabject):
    if name == "Unknown":
        for sab, score in sabject.items():
            print(f"{sab} => {score}")
    else:
        if sabject == True:
            print(f"Hello {name} This Is Your Score Table:")
            for sab, score in sabject.items():
                print(f"{sab} => {score}")
        else:
            print(f"Hello {name} You Have No Scores To Show")

get_people_scores("Abdulkirem", Math=90, Science=80, Language=70)

#  65  >>> 68

import os

for i in range(1,51):
    if i == 25:
        myFile = open(f"python\special-text{i}.py","a")
        myFile.write(f"Elzero Web School => {i}")


        myFile.close()
    else:
        myFile = open(f"python\text{i}.py","a")
        myFile.write(f"Elzero Web School => {i}")
        myFile.close()
    # os.remove(f"python\text{i}.py")
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(len(os.path.dirname(os.path.abspath(__file__))))

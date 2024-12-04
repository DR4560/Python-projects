""" CALCULATOR """

#def 1 main and 4 subfunctions
#print options for user
#ask for values input - included
#call the function
#while loop to continue the program until the user wants to exit


def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")
def sub(a,b):
    answer =  a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))
def mul(a,b):
    answer =  a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))
def div(a,b):
    answer =  a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

while True:
    print("A.Addition")
    print("B.Substraction")
    print("C.MultiplicATION")
    print("D.Division")
    print("E.Exit")

    choice = input("input your choice pls(ABDCE) ")
    if choice == "a" or choice == "A":
        print("Addition")
        a = input("input first number: ")
        b = input("input  second number: ")
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int("input first number: ")
        b = int("input  second number: ")
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Muptiplication")
        a = int("input first number: ")
        b = int("input  second number: ")
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int("input first number: ")
        b = int("input  second number: ")
        div(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int("input first number: ")
        b = int("input  second number: ")
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exit...Program ended")
        quit()
import random
digit=5
name=input("enter a name")
print("WELcome",name)
print("WELCOME TO COW AND BULL GAME")
def Secretnum():
    number=list(range(10))
    random.shuffle(number)
    return number
def clues():
    numbers=Secretnum()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return(secret_num)
def check_guess():
    bull=[]
    cow=[]
    num=clues()
    print(num)
    i=0
    chances=10
    while chances>0:
        guess=int(input("enter your guess="))
        position=int(input("enter the position of your number="))
        print("-----------------")
        print("-----------------")
        if guess in num:
            index=num.index(guess)
            if index==position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("Bull",bull)
                else:
                    print("you alreday used this digit try any different digit")
            else:
                cow.append(guess)
                print("cow this number is in list you can reuse it",cow)
        if bull==num:
            print(name,"Congractulations you win the game")
            break
        chances-=1
        print(chances,"Turns are left")
    else:
        print("you run outyour tries,You losse the game")
    return bull   
check_guess()
def play_again():
    while True:
        again=input("If you Want to play again press y for yes or N of No=")
        if again=="y":
            check_guess()
        else:
            break
play_again()



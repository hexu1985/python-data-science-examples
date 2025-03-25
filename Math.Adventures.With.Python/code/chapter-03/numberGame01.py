from random import randint

def numberGame():
    # 随机选择一个1到100的数
    number = randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess? "))
    if number == guess:
        print("That's correct! The number was", number)
    elif number > guess:
        print("Nope. Higher.")
    else:
        print("Nope. Lower.")

numberGame()


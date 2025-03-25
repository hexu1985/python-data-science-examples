
def average(a,b):
    return (a + b)/2

def squareRoot(num,low,high):
    '''采用猜数游戏策略，通过在从low到high的范围内猜测，寻找num的平方根'''
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: #“猜小一点儿。”
            high = guess
        else: #“猜大一点儿。”
            low = guess
    print(guess)

squareRoot(60,7,8)

def collatz(number):
    a=int(number)
    if a%2 == 0:
        n=a//2
    else :
        n=a*3+1
    print(n)
    return n

print('Enter the starting number of collatz sequence:')
num=int(input())
print('The collatz sequnce is :')
print(num)

while num!=1:
    num=collatz(num)

print('The collatz conjecture remains unproved!!')

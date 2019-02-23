from random import *
print('Lets play stone, paper and scissors!!!')
print('Type st:stone pa:paper & sc:scissor, OK!')
print('Rules - The one who scores 5 point wins the game...!!')

a=0
b=0
while a<5 and b<5:
    cn=randint(1,4)
    print('Enter your choice:')
    ch=input()
    if ch=='st' or ch=='pa' or ch=='sc':
        if cn==1:
            print('Me : stone!')
            cch='stone'
        elif cn==2:
            print('Me : paper!')
            cch='paper'
        else :
            print('Me : scissor!')
            cch='scissor'

        if cch=='stone' and ch=='st' :
            print('Tie!')
            a=a+1
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='stone' and ch=='pa' :
            print('You win!')
            a=a+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='stone' and ch=='sc' :
            print('I win!')
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='paper' and ch=='pa' :
            print('Tie!')
            a=a+1
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='paper' and ch=='st' :
            print('I win!')
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='paper' and ch=='sc' :
            print('You win!')
            a=a+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='scissor' and ch=='sc' :
            print('Tie!')
            a=a+1
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='scissor' and ch=='pa' :
            print('I win!')
            b=b+1
            print('Score : You-'+str(a)+' Me-'+str(b))
        elif cch=='scissor' and ch=='st' :
            print('You win!')
            a=a+1
            print('Score : You-'+str(a)+' Me-'+str(b))

    else :
        print('WRONG INPUT!!')

if a > b:
    print('YOU WIN..!!!:)')
elif a<b :
    print('YOU LOSE..!!!:C')
elif a==b:
    print('ITS A TIE!!')

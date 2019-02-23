print('Enter no. to be converted into binary :');
num=input()
num=int(num)
no = num
bin=0
b=0
while num>0 :
    r=num%2
    bin=bin*10+r
    num=num//2

while bin>0:
    r=bin%10
    b=b*10+r
    bin=bin//10
print('Binary equivalent of ' + str(no) + ' is '+str(b))

import os,numpy

def narray(arr, m):
    narr=[]
    temp=[]
    for i in range(0,len(arr)-1):
        s = arr[i].split(' ',m)
        for j in range(0,m):
            temp.append(float(s[j]))
        narr.append(temp)
        temp=[]

    return narr

def sigmoid(X, T):
    z = numpy.dot(X,T)
    sig = 1/(1+numpy.exp(-z))
    return sig

def cost(X, Y, T, m):
    L1 = numpy.log(sigmoid(X,T))
    L2 = numpy.log(1-sigmoid(X,T))
    M1 = numpy.multiply(Y,L1)
    M2 = numpy.multiply((1-Y),L2)
    J = -1/m*numpy.sum(M1 + M2)
    return J


FILEX = open('C:\\Users\\Admin\\Python progs\\ML\\FileXLO.txt','r')
FILEY = open('C:\\Users\\Admin\\Python progs\\ML\\FileYLO.txt','r')

print('Enter no. of test examples :')
M=int(input())

sX = FILEX.readlines()
sY = FILEY.readlines()

FILEX.close()
FILEY.close()

nX = narray(sX, M)
nY = narray(sY, M)

arrX = numpy.array(nX)
arrY = numpy.array(nY)

arrX = arrX.T
arrY = arrY.T

theta = numpy.zeros(((len(sX)-1),1))
Th = numpy.array(theta)

a = 0.01
oC = cost(arrX, arrY, Th, M)
nC = 0
for i in range(10000):
    Th = Th - a*1/M*(numpy.dot((arrX.T),(sigmoid(arrX,Th) - arrY)))
    nC = cost(arrX, arrY, Th, M)
    if (oC-nC)<=0.00001:
        break
    oC=nC

print('Enter the no. of parameters :')
n = int(input())

X=[1,]

print('Enter the parameters :\n')
for i in range(n):
    X.append(float(input()))

X = numpy.array(X)
i = sigmoid(X,Th)
j = 1-sigmoid(X,Th)
print('Probability of Y=1 : ' + str((i[0])*100)+ '%')
print('Probability of Y=0 : ' + str((j[0])*100)+ '%')

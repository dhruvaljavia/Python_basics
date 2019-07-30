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

def cost(x, y, t, m):
    J = 1/(2*m)*numpy.dot((numpy.subtract(numpy.dot(x,t),y)).T,(numpy.subtract(numpy.dot(x,t),y)))
    return J

FILEX = open('C:\\Users\\Admin\\Python progs\\ML\\FileXLI.txt','r')
FILEY = open('C:\\Users\\Admin\\Python progs\\ML\\FileYLI.txt','r')

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
    Th = Th - a*1/M*(numpy.dot((arrX.T),(numpy.dot(arrX,Th) - arrY)))
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

print('Predicted value of Y : ' + str(numpy.dot(X,Th)))


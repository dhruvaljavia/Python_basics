import os,numpy,random

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

def rndmassign(c, p, n, m):
    for i in range(n):
        rndm = random.randint(1,m) - 1
        c[i][0] = p[rndm][0]
        c[i][1] = p[rndm][1]

def cost(c, i, p, m):
    A = numpy.zeros(m,1)
    for x in range(m):
        A[x][0] = (p[x][0] - c[i[x][0]-1][0])*(p[x][0] - c[i[x][0]-1][0]) + (p[x][1] - c[i[x][0]-1][1])*(p[x][1] - c[i[x][0]-1][1])
    J = 1/m*numpy.sum(A)

    return J

def cassign(c, p, n, m):
    for i in range(m):
        

    
FILEP = open('C:\\Users\\Admin\\Python progs\\ML\\FileP.txt','r')

print('Enter the no. of points :')
M=int(input())

sP = FILEP.readlines()
FILEP.close()

nP = narray(sP, M)

arrP = numpy.array(nP)

arrP = arrP.T

print('Enter the no. of clusters to be formed :')
n = int(input())

C = numpy.zeros(n,2)
I = numpy.zeros(M,1)



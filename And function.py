#And

import math

x1=[0,0,1,1]
x2=[0,1,0,1]

y=[0,0,0,1]


def Func(i):
	return w1*x1[i]+w2*x2[i]+w3

def Sigmoid(x):
	return 1/(1+math.exp(-x))

def DSigmoid(x):
	return Sigmoid(x)*(1-Sigmoid(x))

def F(i):
	return y[i]-Sigmoid(Func(i))

w1=0.3
w2=0.6
w3=0.3

itter=0

while itter <10000:
	for i in range(4):
		w1=w1+x1[i]*(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
		w2=w2+x2[i]*(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
		w3=w3+(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
	itter+=1

print(w1)
print(w2)
print(w3)

print(Sigmoid(Func(0)))
print(Sigmoid(Func(1)))
print(Sigmoid(Func(2)))
print(Sigmoid(Func(3)))

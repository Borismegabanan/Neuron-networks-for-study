#Xor

import math

x1=[0,0,1,1]
x2=[0,1,0,1]

y=[0,1,1,0]


def FuncAnd(i):
	return w1*x1[i]+w2*x2[i]+w5

def FuncOr(i):
	return w3*x1[i]+w4*x2[i]

def FuncXor(i):
	return w6*Sigmoid(FuncAnd(i))+w7*Sigmoid(FuncOr(i))

def Sigmoid(x):
	return 1/(1+math.exp(-x))

def DSigmoid(x):
	return Sigmoid(x)*(1-Sigmoid(x))

#def F(i,x):
#	return y[i]-Sigmoid(x)

w1=0.6
w2=0.6
w3=0.6
w4=0.6
w5=0.6
w6=0.6
w7=0.6

itter=0

while itter <100000:
	for i in range(4):
		w1=w1+x1[i]*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncAnd(i))
		w2=w2+x2[i]*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncAnd(i))
		w5=w5+(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncAnd(i))
		w3=w3+x1[i]*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncOr(i))
		w4=w4+x2[i]*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncOr(i))
		w6=w6+FuncAnd(i)*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncXor(i))
		w7=w7+FuncOr(i)*(y[i]-Sigmoid(FuncXor(i)))*DSigmoid(FuncXor(i))
	itter+=1



print("w1",w1)
print("w2",w2)
print("w3",w3)
print("w4",w4)
print("w5",w5)
print("w6",w6)
print("w7",w7)
print(Sigmoid(FuncXor(0)))
print(Sigmoid(FuncXor(1)))
print(Sigmoid(FuncXor(2)))
print(Sigmoid(FuncXor(3)))
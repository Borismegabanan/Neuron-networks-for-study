import math

x1=[0,1,1,0]
x2=[0,1,0,1]
x3=[1,1,1,1]

y=[0,1,1,0]


def Func(i):
	return w1*x1[i]+w2*x2[i]+w3*x3[i]

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

while itter <1000:
    for i in range(4):
        w1=w1+x1[i]*(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
        w2=w2+x2[i]*(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
        w3=w3+x3[i]*(y[i]-Sigmoid(Func(i)))*DSigmoid(Func(i))
    itter+=1
    print(itter)

print(w1)
print(w2)
print(w3)
print(Sigmoid(1*w1+0*w2+w3*0))
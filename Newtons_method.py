
print("-----------------------------------")
print("-----------------------------------")
print("This is Newton's method")
print("-----------------------------------")

#輸入方程式
def function_value(x):
    y=0.4*(x-3)**3
    #回傳函數值
    return y
#test
# y=function_value(5)
# print(y)

#輸入方程式的一階微分
def First_Differential_function(x):
    First_Differential=3*0.4*(x-3)**2
    return First_Differential
#test
# First_Differential=First_Differential_function(5)
# print(First_Differential)

#輸入方程式的二階微分
def Sec_Differential_function(x):
    Sec_Differential=2*3*0.4*(x-3)
    return Sec_Differential
#test
# Sec_Differential=Sec_Differential_function(5)
# print(Sec_Differential)

#計算移動方向
def moving_direction(x):
    d=- First_Differential_function(x)/Sec_Differential_function(x)
    return d
#test
# d=moving_direction(5)
# print(d)

#輸入起始猜測值
x0=4
#收斂到多小
epsilon=1e-6

iteration=0

print("x0=",x0)
print("-----------------------------------")
First_Differential=First_Differential_function(x0)
x=x0
while  First_Differential_function(x)>epsilon and iteration<100:
    iteration=iteration+1
    print("iteration:",iteration)
    d=moving_direction(x)
    x=x+d
    print("x%d =%f" %(iteration,x))
    # print(First_Differential_function(x),Sec_Differential_function(x))
    print("-----------------------------------")
root=x
print("root=",root)



print("-----------------------------------")
print("-----------------------------------")


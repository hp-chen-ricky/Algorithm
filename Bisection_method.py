
print("-----------------------------------")
print("-----------------------------------")
print("This is Bisection method")
print("-----------------------------------")

def function_value(x):
    #輸入方程式
    value=x**3-5*x**2+10*x-80
    #回傳函數值
    return value
#test 輸入2得出函數值
value=function_value(2)
# print(value)

#輸入範圍[LB,UB]
LB,UB=0,100

#收斂到多小
epsilon=1e-6

def Bisection_method(LB,UB,epsilon):
    #範圍中點 mp
    mp=(LB+UB)/2

    #求出函數值
    value_LB=function_value(LB)
    value_UB=function_value(UB)
    value_mp=function_value(mp)
    iteration=0
    #當中點函數值很靠近收斂值 和 疊代小於100次
    while abs(value_mp)>epsilon and iteration<100:
        iteration=iteration+1
        # print("iteration=",iteration)
        mp=(LB+UB)/2
        # print(LB,mp,UB)
        value_LB=function_value(LB)
        value_UB=function_value(UB)
        value_mp=function_value(mp)
        if value_UB*value_mp<0:
            LB=mp
        elif value_LB*value_mp<0:
            UB=mp
        # print("update ",LB,mp,UB)
        # print("-----------------------------------")
    root=(LB+UB)/2
    return iteration,root


#test
iteration,root=Bisection_method(LB,UB,epsilon)
print("iteration=",iteration)
print("root= %.8f" % root)
print("-----------------------------------")
print("-----------------------------------")
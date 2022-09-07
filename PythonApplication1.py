import random

def func_1():
    print('Value of Sin 0')
    ans=input()
    if ans == "0":
        print('Good Job \n')
    else: print("The correct answer was '0'")

def func_2():
    print('Value of Sin 30')
    ans=input()
    if ans == "1/2":
        print('Good Job \n')
    else: print("The correct answer was '1/2'")

def func_3():
    print('Value of Sin 45')
    ans=input()
    if ans == "sqrt(2)/2":
        print('Good Job \n')
    else: print("The correct answer was 'sqrt(2)/2'")

def func_4():
    print('Value of Sin 60')
    ans=input()
    if ans == "sqrt(3)/2":
        print('Good Job \n')
    else: print("The correct answer was 'sqrt(3)/2'")

def func_5():
    print('Value of Sin 90')
    ans=input()
    if ans == "1":
        print('Good Job \n')
    else: print("The correct answer was '1'")

def func_6():
    print('Value of Cos 0')
    ans=input()
    if ans == "1":
        print('Good Job \n')
    else: print("The correct answer was '1'")

def func_7():
    print('Value of Cos 30')
    ans=input()
    if ans == "sqrt(3)/2":
        print('Good Job \n')
    else: print("The correct answer was 'sqrt(3)/2'")

def func_8():
    print('Value of Cos 45')
    ans=input()
    if ans == "sqrt(2)/2":
        print('Good Job \n')
    else: print("The correct answer was 'sqrt(2)/2'")

def func_9():
    print('Value of Cos 60')
    ans=input()
    if ans == "1/2":
        print('Good Job \n')
    else: print("The correct answer was '1/2'")

def func_10():
    print('Value of Cos 90')
    ans=input()
    if ans == "0":
        print('Good Job \n')
    else: print("The correct answer was '0'")



def sel_choice(sel):
        if sel ==1:
            func_1()
        elif sel ==2:
            func_2()
        elif sel ==3:
            func_3()
        elif sel ==4:
            func_4()
        elif sel ==5:
            func_5()
        elif sel ==6:
            func_6()
        elif sel ==7:
            func_7()
        elif sel ==8:
            func_8()
        elif sel ==9:
            func_9()
        elif sel ==10:
            fun_10()
      

i = 0
for i in range(25):
    sel = random.randrange(1,11)
    sel_choice(sel)
    
    i+=1

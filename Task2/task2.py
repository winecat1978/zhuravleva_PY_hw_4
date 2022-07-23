# Задайте натуральное число N. 
# Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

def GetNumber(x): # Получает на вход значение и удостоверяется, что оно натуральное
    num = 0
    for i in range (x):
        smt = False
        while not smt:
            try:
                number = int(input("Введите натуральное число: "))
                num = number
                smt = True
                if number <= 0:
                    smt = False
                    print("Введите положительное число!")
            except ValueError:
                print("Вы ошиблись. Введите натуральное число!")
    return num

def DivList(NUM): #Выводит все делители числа без 1
    i = 1
    listA = [0]*NUM
    for i in range (1, NUM):
        if NUM%i == 0:
            listA[i] = i
    
    wrong1 = 0
    listA=list(filter((wrong1).__ne__, listA)) # Избавляется от нулей в списке
    wrong2 = 1
    listA=list(filter((wrong2).__ne__, listA))
    return listA
    
def SimpleDivCheck(divids, NUM):
    i = 0
    for k in divids:
        for j in range(2,k):
            if k%j == 0:
                i+=1
        
        if i != 0:
         divids=list(filter((k).__ne__, divids))
         i = 0
        
    
    return divids

NUM = GetNumber(1)
print(NUM)
divids = DivList(NUM)
print(divids)
result = SimpleDivCheck(divids,NUM)
print(result)
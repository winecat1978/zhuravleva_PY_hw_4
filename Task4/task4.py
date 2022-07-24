# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
import random
def GetNumber(x): # Получает на вход значение и удостоверяется, что оно натуральное
    num = 0
    for i in range (x):
        smt = False
        while not smt:
            try:
                number = int(input("Введите натуральную степень k: "))
                num = number
                smt = True
                if number <= 0:
                    smt = False
                    print("Введите положительное число!")
            except ValueError:
                print("Вы ошиблись. Введите натуральное число!")
    return num

def Coefficients (k):
    m = [0]*(k+1)
    count = 0
    while count <= k:
        a = random.randrange(0,101)
        m[count] = a
        count+=1
        
    return m

def Stepeni (k):
    n = [0]*(k+1)  
    b = k
    count = 0
    while count <= k:
        n[count] = b
        b-=1
        count+=1
    return n

def Printer(koefs,powers,k):
    o = 0
    while powers[o] !=1:
        print(f"{koefs[o]}x^{powers[o]}", end="+")
        o+=1
    if powers[o] == 1:
        print(f"{koefs[o]}x", end="+")
        o+=1
    if powers[o] ==0:
        print(f"{koefs[o]}=0",end="")

k = GetNumber(1)
koefs = Coefficients(k)
powers = Stepeni(k)
Printer(koefs,powers,k) #да, форма записи немного некрасивая... на большее моего мозга не хватило
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def GetNumber(x): 
    list = [0]*x
    for i in range (x):
        smt = False
        while not smt:
            try:
                number = int(input(f"Введите {i+1} элемент последовательности: "))
                list[i] = number
                smt = True
            except ValueError:
                print("Вы ошиблись. Введите число!")
    return list

Num = int(input("Сколько элементов будет в последовательности? Ответ: "))
sequence1 = GetNumber(Num)
print(sequence1)
seq2 = list(set(sequence1)) # я знаю, что порядок элементов теряется и он все выстраивает по возрастанию
print(seq2)                 # но в условии задачи это не уточняется
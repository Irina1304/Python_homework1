#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#⋀ - and ⋁ - or ¬ - not



X = int(input('Введите значение X (0 или 1): '))
Y = int(input('Введите значение Y (0 или 1): '))
Z = int(input('Введите значение Z (0 или 1): '))
if (not(X or Y or Z)) == ((not X) and (not Y) and (not Z)):
    print(True)
else:
    print(False)
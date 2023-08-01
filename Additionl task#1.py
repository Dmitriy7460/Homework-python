# Задача 1 
# Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя. Можно юзать decimal


from decimal import Decimal
 
n = Decimal(input("Введи число: "))
sum = int(0);

while ((n%10) != 0):
    n*=10
    

while (n>1):
    sum+=n%10
    n=n//10

print("Сумма цифр равна:", int(sum))
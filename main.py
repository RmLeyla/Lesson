#4. Вычислить сумму чисел в заданном диапазоне

start = int(input())
end = int(input())
sum = 0

for i in range(start, end):
    sum += i
print(sum)


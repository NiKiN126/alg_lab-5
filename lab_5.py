from random import randint
import time

N = 15000
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

start_time = time.time()

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

end_time = time.time()

execution_time = end_time - start_time
print("Отсортированный масив:", a)
print("Время выполнения :", execution_time, "секунд")

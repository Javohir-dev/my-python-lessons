import random as run

n = 100
numbers = list(range(1, n+1))
x = numbers.pop(run.randint(1, n+1))
print(f"To'g'ri son: {x}")

# * 1-yechim
numbers2 = list(range(1, n+1))
print(sum(numbers2)-sum(numbers))

# ? 2-O'zimni yechimim
# n = 1
# for i in numbers:
#     if i == n:
#         n += 1
#     else:
#         print(n)
#         break

# ! 3-yechim va eng aptimali ham shu
summa = n*(n+1)/2
print(summa - sum(numbers))

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in x:
  if num % 2 == 0:
    x[num] = num*2
  else:
    pass

print(x)

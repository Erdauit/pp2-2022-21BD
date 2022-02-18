def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

numbers = list(map(int, input().split()))
print(unique_list(numbers)) 
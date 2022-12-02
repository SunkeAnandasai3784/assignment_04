def square_num(n):
  return n * n
numbers = [4, 5, 2, 9]
print("Original List: ",numbers)
result = map(square_num, numbers)
print("Square the elements of the said list using map():")
print(list(result))


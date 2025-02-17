def find():
  N = int(input())
  info = input()
  values = {chr(65 + i): int(input()) for i in range(N)}
  stack = []
  
  for i in info:
    if i.isalpha():
      stack.append(values[i])
    else:
      a = stack.pop()
      b = stack.pop()
      if i == "+":
        stack.append(b+a)
      if i == "-":
        stack.append(b-a)
      if i == "/":
        stack.append(b/a)
      if i == "*":
        stack.append(b*a)

  print(f"{stack[0]:.2f}")

find()
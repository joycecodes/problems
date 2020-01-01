class stack:
  def __init__(self):
    self.array = []

  def push(self, n):
    self.array.append(n)

  def get(self):
    return self.array

  def pop(self):
    if self.array == []:
      return "nope!"
    else:
      return self.array.pop()

  def peek(self):
    return self.array[-1]

  def get_stack(self):
    return self.array

  def reverse_string(self):
      mid = len(self.array)//2
      y = mid
      for x in range(0, mid):
          self.array[x], self.array[y] = self.array[y], self.array[x]
          mid -= 1
      return self.array

def reverse_string(stak, str):
    str2 = ""
    for x in str:
        stak.push(x)

    for x in str:
        str2 += stak.pop()
    return str2

stack1 = stack()
stack1.push(5)
stack1.push(3)
stack1.push(4)

print(stack1.get())
print(stack1.pop())
print(stack1.peek())
print(stack1.get_stack())
print(stack1.reverse_string())

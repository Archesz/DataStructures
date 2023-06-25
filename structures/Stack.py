class Stack():

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.stack = []
    self.size = 0

  def push(self, elemento):
    if self.size < self.capacidade:
      self.stack.append(elemento)
      self.size += 1
  
  def pop(self):
    if self.is_empty() == False:
      elemento = self.stack.pop(self.size - 1)
      self.size -= 1
      return elemento

    return -1

  def len(self):
    return self.size
     
  def peek(self):
    return self.stack[self.size - 1]

  def is_empty(self):
    if self.size == 0:
      return True
    
    return False

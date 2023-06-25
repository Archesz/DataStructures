class Queue():
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = []
    self.size = 0

  def enqueue(self, element):
    if self.capacity != self.size:
      self.queue.append(element)
      self.size += 1
      return

    return -1

  def dequeue(self):
    if self.is_empty() == False:
      elemento = self.queue.pop(0)
      self.size -= 1
      return elemento
    
    return -1

  def is_empty(self):
    if self.size == 0:
      return True

    return False

  def peek(self):
    return self.queue[0]

  def __len__(self):
    return self.size

  def len(self):
    return self.size

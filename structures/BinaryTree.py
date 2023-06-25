class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree():

  def __init__(self, root):
    self.root = Node(root)
    self.size = 0

  # Inserir
  def insert(self, value):
    node = self.root
    new = Node(value)

    while True:
      if new.value >= node.value and node.right == None:
        node.right = new
        break
      elif new.value < node.value and node.left == None:
        node.left = new
        break
      
      elif new.value >= node.value and node.right != None:
        node = node.right

      elif new.value < node.value and node.left != None:
        node = node.left

    self.size += 1

  def verifyInOrder(self, node, result):
    if node is None:
      return

    self.verifyInOrder(node.left, result)
    result.append(node.value)
    self.verifyInOrder(node.right, result)

    return result

  def verifyPreOrder(self, node, result):
    if node is None:
      return

    result.append(node.value)
    self.verifyPreOrder(node.left, result)
    self.verifyPreOrder(node.right, result)

    return result

  def verifyPosOrder(self, node, result):
    if node is None:
      return

    self.verifyPosOrder(node.left, result)
    self.verifyPosOrder(node.right, result)
    result.append(node.value)

    return result

  # Percurso
  def traverse(self, type):
      result = []
      node = self.root

      if type == "InOrder":
        result = self.verifyInOrder(node, result)
      elif type == "PreOrder":
        result = self.verifyPreOrder(node, result)
      elif type == "PosOrder":
        result = self.verifyPosOrder(node, result)

      print(result)
      #return result

  def find(self, value, show):
    node = self.root
    path = []
    
    while True:
      if node == None:
        return False

      elif node.value == value:
        path.append(f"{node.value}")
        if show == True:
          print("".join(path))
 
        return True
      elif value > node.value:
        path.append(f"{node.value} -> ")
        node = node.right
      elif value < node.value:
        path.append(f"{node.value} -> ")
        node = node.left

  def remove(self, value):
      # Encontrar o nó a ser removido
      node = self.root
      temp = None

      while node is not None:
          if node.value == value:
              # Caso 1: Nó sem filhos
              if node.left is None and node.right is None:
                  if temp is None:
                      self.root = None
                  elif temp.left is node:
                      temp.left = None
                  else:
                      temp.right = None
              # Caso 2: Nó com filho único (esquerda)
              elif node.left is not None and node.right is None:
                  if temp is None:
                      self.root = node.left
                  elif temp.left is node:
                      temp.left = node.left
                  else:
                      temp.right = node.left
              # Caso 3: Nó com filho único (direita)
              elif node.left is None and node.right is not None:
                  if temp is None:
                      self.root = node.right
                  elif temp.left is node:
                      temp.left = node.right
                  else:
                      temp.right = node.right
              # Caso 4: Nó com dois filhos
              else:
                  successor_parent = node
                  successor = node.right

                  while successor.left is not None:
                      successor_parent = successor
                      successor = successor.left

                  if temp is None:
                      self.root = successor
                  elif temp.left is node:
                      temp.left = successor
                  else:
                      temp.right = successor

                  if successor_parent.left is successor:
                      successor_parent.left = successor.right
                  else:
                      successor_parent.right = successor.right

              return True

          elif value > node.value:
              temp = node
              node = node.right

          elif value < node.value:
              temp = node
              node = node.left

      return False

def bubbleSort(lista):

  while True:
    troca = False
    for i in range(0, len(lista)):
      if i < len(lista) - 1:
        if lista[i] > lista[i+1]:
          lista[i], lista[i+1] = lista[i+1], lista[i]
          troca = True

    if troca == True:
      troca = False
    else:
      break

  return lista    

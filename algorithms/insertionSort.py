def insertionSort(lista):
  print(f"Base: {lista}")
  if(lista[1] < lista[0]):
    lista[1], lista[0] = lista[0], lista[1]
  print(f"Primeira Inversão: {lista}")
  
  for i in range(2, len(lista)):
    j = i
    while lista[j-1] > lista[j]:
      lista[j-1], lista[j] = lista[j], lista[j-1]
      print(f"Trocados: -> {lista[j-1]} e {lista[j]}")

      if j == 0:
        break

      j -= 1

    print(lista)

  return lista

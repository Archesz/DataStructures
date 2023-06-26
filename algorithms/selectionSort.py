def selectionSort(lista):

  minor = lista[0]
  idx = 0
  j = 0

  while j != len(lista) - 1:
    # Encontrar o menor elemento
    for i in range(j, len(lista)):
      if lista[i] < minor:
        minor = lista[i]
        idx = i

    lista[j], lista[idx] = lista[idx], lista[j]

    print(f"{lista[j]} -> {lista[idx]}")
    print(lista)
    
    j += 1
    minor = lista[j]
    idx = j

  return lista

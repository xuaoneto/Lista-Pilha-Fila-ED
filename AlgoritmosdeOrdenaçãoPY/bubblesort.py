
def BubbleSort(array):
    for i in range(len(array)):
        troca = False
        for k in range(len(array)-1):
            if array[k] > array[k+1]:
                aux = array[k]
                array[k] = array[k+1] 
                array[k+1] = aux
                troca = True
        if not troca:
            break

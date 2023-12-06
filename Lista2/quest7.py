def merge(lista,inicio,meio,fim):
    esq = lista[inicio:meio]
    dire = lista[meio:fim]
    top_esq,top_dir = 0,0
    for i in range(inicio,fim):
        if top_esq >= len(esq):
            lista[i] = dire[top_dir]
            top_dir+=1
        elif top_dir >= len(dire):
            lista[i] = esq[top_esq]
            top_esq+=1
        elif esq[top_esq] < dire[top_dir]:
            lista[i] = esq[top_esq]
            top_esq+=1
        else:
            lista[i] = dire[top_dir]
            top_dir+=1

def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

nums = [-4,-1,0,3,10]
nums = [i**2 for i in nums]
mergesort(nums,0,len(nums))
print(nums)
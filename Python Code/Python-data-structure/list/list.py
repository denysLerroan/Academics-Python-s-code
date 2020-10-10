# Cálculo de média

def listValue():
    for i in range(1,5):
        list.append(int(input(f'Digite o valor da sua prova {i} ')))

def media():
    sum = 0
    for i in range(len(List)):
        sum += List[i]
    m = sum / 4
    return m

List = []

listValue()
m = media()

print(m)
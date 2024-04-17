
v = [45,-89,32,-12,33]
v1 = [41,72,39,4,35]
v2 = [0,0,0,0,0]


#1.Fazer uma Função que retorne o primeiro elemento do vetor.
def primeiro_elemento(v: list) -> int:
    return v[0]
#2.Fazer um procedimento que exiba somente os números negativos contidos no vetor.
def exibe_negativos(v: list) -> None:
    print(f"{v[1]} e {v[3]}")

#3.Fazer uma função que retorne a soma dos elementos do vetor
def somaV(v: list) -> int:
    soma = 0
    for i in range(5):
        soma += v[i]
    return soma
#4.Fazer uma função que retorne a media dos elementos do vetos
def media_elementos(v: list) -> int:
    media = somaV(v) / 5
    return media
#5.Fazer um procedimento que exiba na tela os numeros ímpares contidos no vetor 
def elementos_impares(v: list) -> None:
    for i in range(5):
        if v[i] % 2 != 0:
            print(v[i])
#6.fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor.
def exibe_extremos(v: list) -> None:
    print(f"{v[0]} e {v[4]}")

#7.Fazer um procedimento que exiba os elementos cujos índices sejam pares.
def exibe_indice_par(v: list) -> None:
    for i in range(0,5,2):
        print(f"{v[i]}")
#8.Fazer uma função que retorne True caso um valor passado por parâmetro exista no vetor, senão False.
def busca(v: list, n) -> bool:
    for i in range(5):
        if v[i] == n:
            conta = 1
    if conta != 1:
        return False
    else:
        return True
#9.Fazer um procedimento que ordene os elementos do vetor.
def ordena_vetor_nv1(v: list) -> None:
    for i in range(5):
        for j in range(5):
            if v[i] < v[j]:
                mente = v[i]
                v[i] = v[j]
                v[j] = mente
    
#10.Fazer um procedimento chamado 'copia_vetor(v1, v2)' que copie os elementos do vetor v1 em v2.
def copia_vetor(v1: list, v2: list):
    for i in range(5):
        v2[i] = v1[i]
    
#11.Fazer um procedimento chamado 'inverte_vetor(v1, v2)' que copie os elementos invertidos do vetor v1 em v2, ou seja, o primeiro elemento de v1 será o último de v2.
def inverte_vetor(v1: list, v2: list) -> None:
    j = 5
    for i in range(5):
        j = j - 1
        v2[j] = v1[i]
    
#12.Fazer um procedimento chamado 'ordena_vetor_crescente(v)' que ordene de forma crescente o vetor passado por parâmetro.
def ordena_vetor_crescente(v1: list, v2: list) -> None:
    for i in range(5):
        v2[i] = v1[i]
    for i in range(5):
        for j in range(5):
            if v2[i] < v2[j]:
                mente = v2[i]
                v2[i] = v2[j]
                v2[j] = mente
#13.Fazer um procedimento chamado 'ordena_vetor_decrescente(v)' que ordene  de forma decrescente o vetor passado por parâmetro. 
def ordena_vetor_decrescente(v1: list, v2: list) -> None:
    for i in range(5):
        v2[i] = v1[i]
    for i in range(5):
        for j in range(5):
            if v2[i] > v2[j]:
                mente = v2[i]
                v2[i] = v2[j]
                v2[j] = mente                
#14.Fazer um procedimento chamado 'ordena_vetor(v, forma)' que baseado na forma ('c' para crescente ou 'd' para decrescente) ordene na ordem solicitada.
def ordena_vetor(forma) -> None:
    if forma == 'c':
        ordena_vetor_crescente(v1, v2)
        print(f"{v2}")
    elif forma == 'd':
        ordena_vetor_decrescente(v1, v2)
        print(f"{v2}")
        



#15.Fazer um procedimento chamado 'separa_pares_impares(v1)' que coloque nas posições mais a esquerda os valores pares e mais a diretia os impares.
def separa_pares_impares(v1: list, v2: list) -> None:
    for i in range(5):
        if v1[i] % 2 == 0:
            v2[i] = v1[i]
    for i in range(5):
        if v1[i] % 2 != 0:
            v2[i] = v1[i]
    print(f"{v2}")



                
#16.Fazer uma função chamada 'conta_acima_media(v1) que retorne quantos elementos do vetor estão acima da média.
def conta_acima_media(v1: list) -> float:
    soma = 0
    media = 0
    number = 0

    for i in range(5):
        soma = soma + v1[i]
    media = soma / 5
    for i in range(5):
        if v1[i] > media:
            number = number + 1
    return number  
#17.Fazer uma função chamada 'maior_elemento(v1)' que retorne o elemento de maior valor do vetor.
def maior_elemento(v1: list) -> int:
    maior = v1[1]
    for i in range(5):
        if v1[i] >= maior:
            maior = v1[i]
    return maior  
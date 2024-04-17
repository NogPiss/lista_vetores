import subalgoritimos
import os 
os.system("cls")


print("-- Lista de Vetores --\n")


v = [45,-89,32,-12,33]
v1 = [41,72,39,4,35]
v2 = [0,0,0,0,0]


#def primeiro_elemento(v: list) -> int:

        
            

print(f"vetor mestre dos exercicios nível 1: v{v}\n")
print("-- nivel 1--\n")
print("1. Retorna primeiro valor")
print("2. Numeros negativos do vetor")
print("3. Soma doselementos do vetor")
print("4. Media dos elementos do vetor")
print("5. Numeros ímpares do vetor")
print("6. Exibe o primeiro e o ultimo elemento do vetor")
print("7. indices pares do vetor")
print("8. verifica se o número existe no vetor")
print("9. Ordena vetor crescente\n")
print("-- nivel 2--\n")
print(f"vetores mestres a partir do nível 2: v1{v1} e v2{v2}")
print("10. copia vetor")
print("11. copia e inverte vetor")
print("12. Ordena vetor crescente")
print("13. Ordena vetor decrescente\n")
print("-- nivel 3--\n")
print("14. Ordena vetor 'c' ou 'd'")
print("15. Separa os pares dos impares")
print("16. Quantos elementos estao acima da media ")
print("17. Elemento de maior valor")

print("0. Sair")

opcao = 1

while opcao != 0:
    
    opcao = int(input("insira aqui a sua opção: "))
    soma = 0

    match opcao:
        case 1:
            v = [45,-89,32,-12,33]
            print(f"O primeiro valor do vetor é: {subalgoritimos.primeiro_elemento(v)}")
            continue
        case 2:
            v = [45,-89,32,-12,33]
            print(f"Os números negativos do vetor são: ")
            subalgoritimos.exibe_negativos(v)
            continue
        case 3:
            v = [45,-89,32,-12,33]
            print(f"O valor da soma dos elementos do vetor é: {subalgoritimos.somaV(v)}")
            continue
        case 4:
            v = [45,-89,32,-12,33]
            print(f"A media dos elementos do vetor é: {subalgoritimos.media_elementos(v)}") 
            continue
        case 5:
            v = [45,-89,32,-12,33]
            print("Os números ímpares do vetor são: ")
            subalgoritimos.elementos_impares(v)
            continue
        case 6:
            v = [45,-89,32,-12,33]
            print("Os extremos do vetor são: ")
            subalgoritimos.exibe_extremos(v)
            continue
        case 7:
            v = [45,-89,32,-12,33]
            print("Os indices ímpares do vetor são: ")
            subalgoritimos.exibe_indice_par(v)
            continue
        case 8:
            v = [45,-89,32,-12,33]
            n = int(input("Insira o numero que deseja verificar dentro do vetor: "))
            subalgoritimos.busca(v, n)
            print(subalgoritimos.busca(v, n))
            continue
        case 9:
            v = [45,-89,32,-12,33]
            subalgoritimos.ordena_vetor_nv1(v)
            print(f"{v}")
            continue
        case 10:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            subalgoritimos.copia_vetor(v1, v2)
            print(f"O vetor 1 foi copiado para o vetor 2: {v2}")
            continue
        case 11:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            subalgoritimos.inverte_vetor(v1, v2)
            print(f"O vetor 1 foi copiado invertido para o vetor 2: {v2}")
            continue
        case 12:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            subalgoritimos.ordena_vetor_crescente(v1,v2)
            print(f"O vetor 1 organizado de maneira crescente foi copiado para  vetor 2: {v2}")
            continue
        case 13:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            subalgoritimos.ordena_vetor_decrescente(v1, v2)
            print(f"O vetor 1 organizado de maneira decrescente foi copiado para  vetor 2: {v2}")
            continue 
        case 14:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            forma = str(input("Digite 'c' para ordenar o vetor de maneira crescente ou 'd' para decrescente: "))
            subalgoritimos.ordena_vetor(forma)
            continue
        case 15:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]

            subalgoritimos.separa_pares_impares(v1,v2)
            continue
        case 16:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]
            print("Números acima da média: ")
            print(f"{subalgoritimos.conta_acima_media(v1)}")
            continue
        case 17:
            v1 = [41,72,39,4,35]
            v2 = [0,0,0,0,0]

            print("O maior número do vetor é: ")
            print(f"{subalgoritimos.maior_elemento(v1)}")
            continue
        case 0:
            break
        case _:
            print("--Opção inválida--")
            continue   
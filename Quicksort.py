import random
import time

# Função para troca de elementos e contagem de trocas
def trocar(vetor, i, j, contador):
    vetor[i], vetor[j] = vetor[j], vetor[i]
    contador['trocas'] += 1

# Escolha do particionador: Mediana de 3
def escolher_mediana3(vetor, inicio, fim, contador):
    meio = (inicio + fim) // 2
    # Identificando a mediana dos três valores e trocando com o primeiro elemento
    if vetor[inicio] > vetor[meio]:
        trocar(vetor, inicio, meio, contador)
    if vetor[inicio] > vetor[fim]:
        trocar(vetor, inicio, fim, contador)
    if vetor[meio] > vetor[fim]:
        trocar(vetor, meio, fim, contador)
    trocar(vetor, inicio, meio, contador)

# Escolha do particionador: Aleatório
def escolher_aleatorio(vetor, inicio, fim, contador):
    indice_aleatorio = random.randint(inicio, fim)
    trocar(vetor, inicio, indice_aleatorio, contador)

# Particionamento de Lomuto
def particionamento_lomuto(vetor, inicio, fim, contador):
    pivo = vetor[inicio]
    i = inicio
    for j in range(inicio + 1, fim + 1):
        if vetor[j] < pivo:
            i += 1
            trocar(vetor, i, j, contador)
    trocar(vetor, inicio, i, contador)
    return i

# Particionamento de Hoare
def particionamento_hoare(vetor, inicio, fim, contador):
    pivo = vetor[inicio]
    i = inicio - 1
    j = fim + 1
    while True:
        while True:
            i += 1
            if vetor[i] >= pivo:
                break
        while True:
            j -= 1
            if vetor[j] <= pivo:
                break
        if i >= j:
            return j
        trocar(vetor, i, j, contador)

# Função de Quicksort com contadores
def quicksort(vetor, inicio, fim, escolha_particionador, estrategia_particionamento, contador):
    if inicio < fim:
        contador['recursao'] += 1
        
        # Escolha do particionador
        if escolha_particionador == 'mediana3':
            escolher_mediana3(vetor, inicio, fim, contador)
        elif escolha_particionador == 'aleatorio':
            escolher_aleatorio(vetor, inicio, fim, contador)

        # Particionamento e chamadas recursivas
        if estrategia_particionamento == 'lomuto':
            pivo_index = particionamento_lomuto(vetor, inicio, fim, contador)
            quicksort(vetor, inicio, pivo_index - 1, escolha_particionador, estrategia_particionamento, contador)
            quicksort(vetor, pivo_index + 1, fim, escolha_particionador, estrategia_particionamento, contador)
        elif estrategia_particionamento == 'hoare':
            pivo_index = particionamento_hoare(vetor, inicio, fim, contador)
            quicksort(vetor, inicio, pivo_index, escolha_particionador, estrategia_particionamento, contador)
            quicksort(vetor, pivo_index + 1, fim, escolha_particionador, estrategia_particionamento, contador)

# Função para processar o arquivo de entrada e executar os testes
def processar_arquivo_entrada(arquivo_entrada, arquivo_saida):
    resultados = []
    with open(arquivo_entrada, 'r') as entrada:
        for linha in entrada:
            dados = list(map(int, linha.strip().split()))
            tamanho = dados[0]
            vetor_original = dados[1:]
            for escolha in ['aleatorio', 'mediana3']:
                for particionamento in ['lomuto', 'hoare']:
                    vetor = vetor_original[:]
                    contador = {'trocas': 0, 'recursao': 0}
                    inicio = 0
                    fim = len(vetor) - 1
                    
                    inicio_tempo = time.time()
                    quicksort(vetor, inicio, fim, escolha, particionamento, contador)
                    tempo_execucao = (time.time() - inicio_tempo) * 1000
                    
                    resultados.append(f"{tamanho},{escolha},{particionamento},{contador['trocas']},{contador['recursao']},{tempo_execucao:.3f}")
    
    with open(arquivo_saida, 'w') as saida:
        for resultado in resultados:
            saida.write(resultado + "\n")

# Chamando a função principal
processar_arquivo_entrada('entrada-quicksort.txt', 'resultados.txt')

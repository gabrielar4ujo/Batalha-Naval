import traceback  #### IMPORT PARA CASO OCORRA ALGUM PROBLEMA NA CRIAÇÃO DE COORDENADAS
import random  #### IMPORT QUE PERMITE GERAR VALORES ALEATÓRIOS

def dados ():
    lista = [1,2,3]
    palavra = ''
    while True:
        
        nome = input('Digite seu nome: ').split()
        if len(nome) == 1:
            nome = nome[0]

        elif len(nome) > 1:
            for n in range(len(nome)):
                if n + 1 == len(nome):
                    palavra+= nome[n]
                else:
                    palavra+= nome[n]+' ' 
        if nome == []:
            
            nome = input('\nDigite seu nome: ').split()

        
        else:

            break
        print()

    while True:
        try:
            lvl = int(input('Digite o nível que deseja jogar: '))
            if lvl in lista:
                print('\nO jogo irá iniciar no nível %d!'%lvl)
                break

            else:
                print('\nNível inválido.\n')
        except:
            print('\nValor digitado inválido.\n')

    
    return lvl,palavra
        

def ranking_sort( lista , arquivo ):
    aux = []
    for n in range(len(lista)):
        var = lista[n].split()
        aux.append(int(var[len(var)-1]))

    aux.sort()
    aux.reverse()
    cont = 0
    while len(lista) != 0:
        
        for n in range(len(lista)):
            auxiliar = lista[n].split()
            valor = auxiliar[len(auxiliar)-1]
            if aux[cont] == int(valor) :
                arquivo.write(lista[n])
                break
        aux.remove(aux[cont])
        lista.remove(lista[n])
       
def mostrar_arquivo ( manipular ):
    for linha in manipular:
        linha = linha.rstrip()
        print(linha)
    
    print()
    

def adicionar_coordenadas ( barco_2,barco_3,barco_4,barco_5,vezes,tamanho_barco):
    if barco_2 > vezes:
        
        if vezes + 1 == barco_2:
            tamanho_barco += 1
        

    elif barco_3 > abs(barco_2 - vezes):
        
        if abs(barco_2 - vezes) + 1 == barco_3:
            tamanho_barco += 1

    elif barco_4 > abs((barco_3 + barco_2) - vezes):
        
        if abs((barco_3 + barco_2) - vezes) + 1 == barco_4:
            tamanho_barco += 1
    
    return tamanho_barco

def coordenada_aleatoria ( pos,tamanho,tamanho_barco ):
    if pos == 'h':
        return random.randint(0, (tamanho - 1)),random.randint(0, tamanho - tamanho_barco)
        
    else:
        return random.randint(0, tamanho - tamanho_barco), random.randint(0, (tamanho - 1))


def letra_da_matriz ( tam , dic ):
    for elementos in dic.items():
        if tam in elementos:
            return elementos[0]

def analisar_coordenadas_do_jogador ( valor, tamanho):
    if (valor > tamanho or valor < 1):
        print('\nEntrada não está nos limites do jogo. Tente novamente.\n')
        desenhar_matriz(matriz,tamanho,score,vida,tiros_total)
        return False
    return True
    
def posicao_bombas(c_x, c_y, l_b,aux,lvl): 

    x = c_x
    y = c_y

    if [x, y] in aux: 
        return False

    for n in range(x - 1, x + lvl + 1):
        for i in range(y - 1, y + lvl + 1):
            if [n, i] in l_b:
                return False
    return True

def coordenadas_bombas(bombas, lista_bombas,tamanho,aux,lvl):  #### Função para criar as coordenadas das bombas ALEATORIAMENTE.

    if bombas == 0:
        return lista_bombas

    x = random.randint(0, tamanho - 1)
    y = random.randint(0, tamanho - 1)

    if posicao_bombas(x, y, lista_bombas,aux,lvl):
        lista_bombas.append([x, y])

    else:
        bombas += 1
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)

    return coordenadas_bombas(bombas - 1, lista_bombas,tamanho,aux,lvl)


def posicao_barcos_horizontal(var_x, var_y, lista,tam,tamanho):  #### Função, para barcos na horizontal, que é chamada pela outra função "gerar_coordenadas_barco" 
                                                         #### que retorna True ou False caso a coordenada criada seja válida ou não.
    a = var_x
    if var_x == 0:
        a += 1
    if var_y == 0:
        var_y += 1
        a = 2

    for i in range(a - 1, var_x + tam + 1):
        coord_x = var_x - 1

        coord_y = var_y - 1
        for n in range(coord_y, (coord_y + tam) + 2):
            if [coord_x, n] in lista:
                return False
        var_x += 1

    return True


def posicao_barcos_vertical(var_x, var_y, lista,tam,tamanho):  #### Função, para barcos na vertical, que é chamada pela outra função "gerar_coordenadas_barco" 
                                                       #### que retorna True ou False caso a coordenada criada seja válida ou não.
    if lista == []:
        return True

    complementar = var_y + 2

    if var_x == 0:
        var_x += 1
        tam -= 1

    if var_y == 0:
        var_y += 1

    if var_y + 1 == tamanho:
        complementar = var_y + 1

    for i in range(var_y - 1, complementar):
        coord_x = var_x - 1  

        coord_y = var_y - 1  
        for n in range(var_x - 1, var_x + 1 + tam):
            if [n, coord_y] in lista:
                return False
        var_y += 1

    return True


def gerar_matriz(size):  #### Função gerado da matriz do jogo.
    matriz = []
    for linha in range(size):
        matriz.append([])
        for coluna in range(size):
            matriz[linha].append('.')

    return matriz


def desenhar_matriz(matriz,tamanho,score,vida,tiros_total):  #### Função que unicamente desenhará a matriz para o jogador.
    contador = 1
    letras = 'A B C D E F G H I J K L M N O P'
    barra = ' -'
    print()
    print('   ',letras[0:tamanho*2])
    print('  ',barra*tamanho)
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if c == 0:
                if contador > 9:
                    print(contador,end='| ')
                else:
                    print(contador,end=' | ')
            if c ==  len(matriz) - 1 and l == 0:
                
                print(matriz[l][c], end='   SCORE ---> %d'%score)
            elif c ==  len(matriz) - 1 and l == 2:
                print(matriz[l][c], end='   VIDA(S) ---> %d'%vida)
            elif c ==  len(matriz) - 1 and l == 4:
                print(matriz[l][c], end='   TOTAL DE TIROS ---> %d'%tiros_total)
            else:
                print(matriz[l][c], end=' ')
        print()
        contador+=1
    print()

def gerar_coordenadas_barco(quant, lista, x, y,achou,aleatorio,aux,tamanho_barco,tamanho):  #### Função recursiva que gera coordenadas, que retorna uma lista com [X,Y]
                                                                  #### e a condição "aleatoria", 'h' para horizontal, 'v' para vertical.
    if quant <= 0:  #### Condição de parada de recursão.

        return lista

    if quant == tamanho_barco:

        if aleatorio == 'h':
            achou = posicao_barcos_horizontal(x, y, aux, quant,tamanho,)

        else:
            achou = posicao_barcos_vertical(x, y, aux, quant,tamanho)

    if achou:
        lista.append([x, y])
        if aleatorio == 'h':
            y += 1
        else:
            x+=1

    else:  #### Condição caso a coordenada seja inválida.
        quant += 1
        aleatorio = random.choice(['v', 'h'])
        x ,y = coordenada_aleatoria(aleatorio,tamanho,tamanho_barco)

    return gerar_coordenadas_barco(quant - 1, lista, x, y, achou,aleatorio,aux,tamanho_barco,tamanho)



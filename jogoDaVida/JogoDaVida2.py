import numpy as np

matrizquadrada = int(input("Definir o tamanho Matriz: "))
Geracoes = int(input("Definir quantas geracoes: "))


# Considerando 1 como celula viva e 0 como celula morta.
# Rodar o jogo no terminal
# A cada geração irá aplicar as condições do jogo, criando assim uma nova matriz atualizada. 

def atualizacao(localCelula,N):
    valorAtualizado = np.zeros([N,N],dtype = int) #Receberá o valor atualizado, conforme as condicoes
    for linha in range(matrizquadrada):
            for celula in range(matrizquadrada):
                somaVizinhos = 0
                if linha==0 and celula ==0:
                    #Não tem vizinhos acima nem à esquerda 
                    somaVizinhos = localCelula[linha][celula + 1] + localCelula[linha + 1][celula] + localCelula[linha + 1][celula + 1]
                elif linha==0 and celula <N-1:   #N-1 == ultimo elemento da lista
                    #Não tem vizinhos acima
                    somaVizinhos = localCelula[linha][celula - 1] + localCelula[linha][celula + 1] + localCelula[linha + 1][celula - 1] + localCelula[linha + 1][celula] + localCelula[linha+ 1][celula + 1]
                elif linha == 0 and celula == N-1: 
                    #Não tem vizinhos acima nem à direita
                    somaVizinhos = localCelula[linha][celula - 1] + localCelula[linha + 1][celula - 1] + localCelula[linha + 1][celula]
            
                elif  linha > 0 and linha < N-1 and celula == 0:
                    #Não tem vizinhos à esquerda
                    somaVizinhos = localCelula[linha - 1][celula] + localCelula[linha - 1][celula + 1] + localCelula[linha][celula + 1] + localCelula[linha + 1][celula] + localCelula[linha + 1][celula + 1]
                elif linha > 0 and linha < N-1 and celula > 0 and celula < N-1:
                    #Tem todos os vizinhos
                    somaVizinhos = localCelula[linha - 1][celula - 1] + localCelula[linha - 1][celula] + localCelula[linha - 1] [celula+ 1] + localCelula[linha][celula - 1] + localCelula[linha][celula + 1] + localCelula[linha + 1][celula - 1] + localCelula[linha + 1][celula] + localCelula[linha + 1][celula + 1]
                elif linha > 0 and linha < N-1 and celula == N-1:  
                    #Não tem vizinhos à direita
                    somaVizinhos = localCelula[linha - 1][celula - 1] + localCelula[linha - 1][celula] + localCelula[linha][celula - 1] + localCelula[linha + 1][celula - 1] + localCelula[linha + 1][celula]
            
            
                elif linha ==N-1 and celula == 0:
                    #Não tem vizinhos abaixo e á esquerda
                    somaVizinhos = localCelula[linha - 1][celula] + localCelula[linha - 1][celula + 1] + localCelula[linha][celula + 1]
                elif linha == N-1 and celula > 0 and celula < N-1:
                    #'Não tem vizinhos abaixo
                    somaVizinhos = localCelula[linha - 1][celula - 1] + localCelula[linha - 1][celula] + localCelula[linha - 1][celula + 1] + localCelula[linha][celula - 1] + localCelula[linha][celula + 1]
                elif linha == N -1 and celula == N-1:
                    #Não tem vizinhos abaixo e à direita
                    somaVizinhos = localCelula[linha - 1][celula - 1] + localCelula[linha - 1][celula]+ localCelula[linha][celula - 1]

                #Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
                if localCelula[linha][celula] == 1 and somaVizinhos < 2:
                    valorAtualizado [ linha][celula] = 0
         #Receberá o valor atualizado, conforme as condicoes        
                
                #Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
                if localCelula[linha][celula] == 1 and somaVizinhos > 3:
                    valorAtualizado [ linha][celula] = 0
         #Receberá o valor atualizado, conforme as condicoes    
                
                #Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
                if localCelula[linha][celula] == 0 and somaVizinhos == 3:
                    valorAtualizado [ linha][celula] = 1
         #Receberá o valor atualizado, conforme as condicoes            
                
                
                #Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
                if localCelula[linha][celula] ==1 and (somaVizinhos== 2 or somaVizinhos== 3):
                    valorAtualizado [ linha][celula] = 1
         #Receberá o valor atualizado, conforme as condicoes        

    return(valorAtualizado ) 
    
    

#Começar
localCelula = np.random.randint(0,2,[matrizquadrada,matrizquadrada])

contGeracao = 1
for geracao in range(Geracoes):     
    
    localCelula = atualizacao(localCelula,matrizquadrada)
    print("\n {} - Geracao \n".format(contGeracao) )
    print(localCelula)
    contGeracao +=1



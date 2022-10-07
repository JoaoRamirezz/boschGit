import random
    

def escolher(x):
    global numero
    selecionada = "".join(random.choice(cartas)+random.choice(naipes))
    if selecionada in x:
        pass
    else: 
        x.append(selecionada)
        numero += 1
        

def separar(x,naipe,num):    
    a = 0    
    for i in x:
        for j in i:
            a += 1
            if a%2 == 0:
                naipe.append(j)
            else:
                num.append(j)
    return naipe, num
    
    

    
naipesjogador = []
numerosjogador = []
trincas = 0
trinca = []
vezes = 0    
cartas = ['1','2','3','4','5','6','7','8','9']
naipes = ['♠','♣','♥','♦']
jogador = []
pc = []
numero = 0


while True:
    escolher(jogador)
    if numero == 9:
        break
    
    
        
numero = 0  
while True:
    computador = "".join(random.choice(cartas)+random.choice(naipes))
    if computador in jogador or computador in pc:
        pass
    else: 
        pc.append(computador)
        numero += 1
    
    if numero == 9:
        break 


    
    
        
while True:
    
    while True:
        morro = "".join(random.choice(cartas)+random.choice(naipes))
        if morro in jogador or morro in pc:
            pass
        else:
            break    
    while True:
        baralho = "".join(random.choice(cartas)+random.choice(naipes))
        if baralho in jogador or baralho in pc or baralho == morro:
            pass
        else:
            break
            
            
    print('Descarte: ',morro)
    print('Suas Cartas: ',jogador)
    escolha = int(input('Você deseja pegar o descarte, ou uma carta do baralho?\n1) - Pegar descarte\n2) - Pegar do baralho\nR: '))
    if escolha == 1:  
        descarte = int(input(f'Selecione uma posição para descartar a carta: {jogador}\nR: '))
        jogador[descarte-1] = morro
        
        
    elif escolha == 2:
        print('Carta retirada: ', baralho)
        descarte = int(input(f'Selecione uma posição para descartar a carta: {jogador}\nR: '))
        jogador[descarte-1] = baralho
    
    print('\n\n\n\n')
        
        
    separar(jogador,naipesjogador,numerosjogador)
    
    
    for i in range(len(numerosjogador) - 2):
        if int(numerosjogador[i]) + 1 == numerosjogador[i + 1] == int(numerosjogador[i + 2]) - 1:
            if naipesjogador[i] == naipesjogador[i + 1] == naipesjogador[i + 2]: 
                trincas += 1
                break
    
    
    for i in range(len(numerosjogador)):
        for j in range(len(numerosjogador)):
            
            if numerosjogador[j] in trinca:
                pass
            else:
                
                if numerosjogador[j] == numerosjogador[i]:
                    vezes += 1
                    
                if vezes == 9:
                    trincas += 1
                    trinca.append(numerosjogador[j])
                    vezes = 0
                    
                    
    if trincas == 3:
        print('Você ganhou!')
        break








            



    
                


                
                  
            
            
            
            
            
            
            
            
            
            
            
            
            
import random

naipes = ('Copas', 'Paus', 'Espadas', 'Ouros')
ranks = ('Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Rainha', 'Rei', 'Ás')
numeros = {'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13, 'Ás': 14}

class Carta:
    def __init__(self, naipe, rank):
        self.naipe = naipe
        self.rank = rank
        self.valor = numeros[rank]
        
    
    def __str__(self):
        return '{} de {}'.format(self.rank, self.naipe)
    
class Baralho:
    def __init__(self):
        self.todas_cartas = []
        
        for naipe in naipes:
            for rank in ranks:
                self.todas_cartas.append(Carta(naipe, rank))
    
    def embaralhar_cartas(self):
        random.shuffle(self.todas_cartas)         

    def retirar_carta(self):
        return self.todas_cartas.pop()
    
class Jogador:
    def __init__(self, name):
        self.name = name
        self.cartas = []
        
    def remover_carta(self):
        return self.cartas.pop(0)
    
    def adicionar_carta(self, nova_carta):
        if type(nova_carta) == type([]):
            self.cartas.extend(nova_carta)
        else:
            self.cartas.append(nova_carta)
            
    def __str__(self):
        return '{} tem {} cartas'.format(self.name, len(self.cartas))
    

# Jogo

player1 = Jogador('Danilo')
player2 = Jogador('Eduardo')

deck = Baralho()
deck.embaralhar_cartas()

for i in range(len(deck.todas_cartas)//2):
    player1.adicionar_carta(deck.retirar_carta())
    player2.adicionar_carta(deck.retirar_carta())

round = 0


game_on = True

while game_on:
    round += 1
    print(f'Round {round}')
    
    if round > 100000:
        print('Parece que não haverá um fim.')
        game_on = False
        break
    
    #checar vitória
    if len(player1.cartas) == 0:
        print('{} está sem cartas, {} venceu a partida!'.format(player1.name, player2.name))
        game_on = False
        break
    elif len(player2.cartas) == 0:
        print('{} está sem cartas, {} venceu a partida!'.format(player2.name, player1.name))
        game_on = False
        break
        
    #jogadas
    player1_hand = []
    player1_hand.append(player1.remover_carta())
    
    player2_hand = []
    player2_hand.append(player2.remover_carta())
    
    while True:
        if player1_hand[-1].valor > player2_hand[-1].valor:
            player2.adicionar_carta(player1_hand)
            player2.adicionar_carta(player2_hand)
            break
        elif player1_hand[-1].valor < player2_hand[-1].valor:
            player1.adicionar_carta(player1_hand)
            player1.adicionar_carta(player2_hand)
            break
        else:
            print('GUERRA!')
            if len(player1.cartas) < 5:
                print('{} não tem cartas para uma guerra'.format(player1.name))
                print('{} Venceu!'.format(player2.name))
                game_on = False
                break
            elif len(player2.cartas) < 5:
                print('{} não tem cartas para uma guerra.'.format(player2.name))
                print('{} Venceu!'.format(player1.name))
                game_on = False
                break
            else:
                for i in range(5):
                    player1_hand.append(player1.remover_carta())
                    player2_hand.append(player2.remover_carta())
                    
                    
            
        
        
    
    
    
        

        

        
        
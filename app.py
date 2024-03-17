class AgenteSimples:
    def __init__(self, posicao_inicial):
        self.posicao_atual = posicao_inicial

    def mover_para_cima(self):
        self.posicao_atual = (self.posicao_atual[0] - 1, self.posicao_atual[1])

    def mover_para_baixo(self):
        self.posicao_atual = (self.posicao_atual[0] + 1, self.posicao_atual[1])

    def mover_para_esquerda(self):
        self.posicao_atual = (self.posicao_atual[0], self.posicao_atual[1] - 1)

    def mover_para_direita(self):
        self.posicao_atual = (self.posicao_atual[0], self.posicao_atual[1] + 1)

# Definição da posição inicial e do ponto de destino
posicao_inicial = (0, 0)
ponto_destino = (3, 6)

# Criando o agente
agente = AgenteSimples(posicao_inicial)

# Movendo o agente em direção ao ponto de destino
print("Posição inicial do agente:", agente.posicao_atual)
while agente.posicao_atual != ponto_destino:
    if agente.posicao_atual[0] < ponto_destino[0]:
        agente.mover_para_baixo()
        print("Movendo para baixo:", agente.posicao_atual)
    elif agente.posicao_atual[0] > ponto_destino[0]:
        agente.mover_para_cima()
        print("Movendo para cima:", agente.posicao_atual)

    if agente.posicao_atual[1] < ponto_destino[1]:
        agente.mover_para_direita()
        print("Movendo para a direita:", agente.posicao_atual)
    elif agente.posicao_atual[1] > ponto_destino[1]:
        agente.mover_para_esquerda()
        print("Movendo para a esquerda:", agente.posicao_atual)

print("Objetivo alcançado!")
print("Posição atual do agente:", agente.posicao_atual)
import random 

palavras = ['aviao', 'carro', 'sorvete', 'cachorro', 'gato', 
            'casa', 'computador', 'celular', 'livro', 'caneta', 'caderno', 'mesa', 'cadeira', 'cama', 'travesseiro', 
            'janela', 'porta', 'chave', 'cachecol', 'bone', 'chapeu', 'oculos', 'camisa', 'calca', 'sapato', 
            'meia', 'blusa', 'saia', 'vestido', 'anel', 'colar', 'pulseira', 'brinco', 
            'relogio', 'bolsa', 'mochila', 'carteira', 'dinheiro', 'cartao', 'chocolate', 'bolo', 'doce', 'salgado',
            'pizza', 'hamburguer', 'refrigerante', 'suco', 'agua', 'cerveja', 'vinho', 'whisky', 'vodka', 'tequila',
            'cigarro', 'charuto']

escolha = random.choice(palavras)
letras = [0]*len(escolha)
letrasCensuradas = [0]*len(escolha)
contador = len(escolha) + 5

for i in range(len(escolha)):
    letras[i] = escolha.split()[0][i]
    letrasCensuradas[i] = '_'

for j in range(contador):
    print(*f'''Você tem {contador} tentativas para acertar qual eh essa palavra: 
        {letrasCensuradas}.''')
    letra = input('Digite uma letra: ').lower()
    if letra in letras:
        for k in range(len(escolha)):
            if letra == letras[k]:
                letrasCensuradas[k] = letra
        print('''-------------------------------------------------------------
Voce acertou. Esta letra esta na palavra.''')
        contador -= 1
    else:
        print('''-------------------------------------------------------------
Voce errou. Esta letra não está na palavra.''')
        contador -= 1
    if contador == 0:
            print(f'''Você perdeu! A palavra era 
        {escolha}.''')
    elif letrasCensuradas == letras:
            print(f'Parabéns! Você acertou a palavra {escolha}!')
            break
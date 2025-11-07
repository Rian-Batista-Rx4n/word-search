from random import randint, choice

# Lista de palavras (Você pode adicionar Mais!)
words = ["PIE", "WOLF", "THING", "CODE", "PYTHON", "MATRIX"]
avaliable_words = []


# Tamanho da matriz (Você pode customizar o tamanho dela!)
matriz = 11

# Alfabeto
alpha = [chr(i) for i in range(65, 91)]

# Cria matriz vazia
game = [["" for _ in range(matriz)] for _ in range(matriz)]

# Direções possíveis: (linha, coluna)
directions = [
    (0, 1),   # direita
    (1, 0),   # para baixo
    (1, 1)    # diagonal
]

def can_place(word, row, col, dr, dc):
    """Verifica se a palavra pode ser colocada sem sair da matriz ou sobrepor"""
    for i in range(len(word)):
        r, c = row + dr * i, col + dc * i
        if r >= matriz or c >= matriz or (game[r][c] != "" and game[r][c] != word[i]):
            return False
    return True

def place_word(word):
    """Tenta colocar a palavra em uma posição e direção válidas"""
    placed = False
    tentativas = 0
    while not placed and tentativas < 100:
        tentativas += 1
        dr, dc = choice(directions)
        row = randint(0, matriz - 1)
        col = randint(0, matriz - 1)

        if can_place(word, row, col, dr, dc):
            for i in range(len(word)):
                game[row + dr * i][col + dc * i] = word[i]
            placed = True
    return placed

# Verificar se está posicionada a palavra
for w in words:
    if place_word(w):
        avaliable_words.append(w)

# Preencher espaços vazios com letras aleatórias
for r in range(matriz):
    for c in range(matriz):
        if game[r][c] == "":
            game[r][c] = alpha[randint(0, 25)]

# Mostrar caça-palavras
for r in range(matriz):
    print(" ".join(game[r]))

# Mostrar Palavras Validas
print("\nWords:", ", ".join(avaliable_words))

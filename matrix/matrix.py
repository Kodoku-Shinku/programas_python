import pygame
import random

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Matrix")

# Definir el tamaño y fuente de los símbolos
tamano_fuente = 20
fuente = pygame.font.Font("nsm-cjk-jp-regular/nsm-cjk-jp-regular.otf", tamano_fuente)

# Definir los colores para los símbolos
color_fuente = (0, 255, 0)  # Verde brillante
color_fondo = (0, 0, 0)     # Negro

# Definir la velocidad de caída mínima y máxima
velocidad_minima = 6
velocidad_maxima = 9

# Lista de símbolos japoneses
simbolos = [
    'あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん',
    'が', 'ぎ', 'ぐ', 'げ', 'ご',
    'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
    'だ', 'ぢ', 'づ', 'で', 'ど',
    'ば', 'び', 'ぶ', 'べ', 'ぼ',
    'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'
]

simbolos.extend([
    '人', '日', '月', '火', '水',
    '木', '金', '土', '山', '川',
    '田', '女', '男', '子', '学',
    '生', '先', '生', '会', '社',
    '時', '間', '食', '飲', '車',
    '自', '動', '音', '楽', '家',
    '族', '電', '話', '国', '語',
    '英', '語', '書', '道', '公'
])



# Lista de columnas
columnas = []
for x in range(0, ANCHO, tamano_fuente):
    tamano_columna = random.randint(1, ALTO // tamano_fuente)
    columna = {
        "x": x,
        "y": random.randint(-ALTO, 0),
        "symbol": [random.choice(simbolos) for _ in range(tamano_columna)],
        "velocidad": random.randint(velocidad_minima, velocidad_maxima)
    }
    columnas.append(columna)

# Bucle principal del juego
terminado = False
reloj = pygame.time.Clock()
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True

    # Actualizar la posición y el símbolo de las columnas
    for columna in columnas:
        columna["y"] += columna["velocidad"]

        # Si la columna se sale de la ventana, reiniciarla en la parte superior
        if columna["y"] > ALTO:
            columna["y"] = random.randint(-ALTO, 0)
            tamano_columna = random.randint(1, ALTO // tamano_fuente)
            columna["symbol"] = [random.choice(simbolos) for _ in range(tamano_columna)]
            columna["velocidad"] = random.randint(velocidad_minima, velocidad_maxima)
        else:
            # Cambiar aleatoriamente los símbolos en la columna
            for i in range(len(columna["symbol"])):
                if random.random() < 0.06:  # Probabilidad de cambio del símbolo (ajustable según se desee)
                    columna["symbol"][i] = random.choice(simbolos)

    # Limpiar la ventana
    ventana.fill(color_fondo)

    # Dibujar los símbolos en la ventana
    for columna in columnas:
        for i, symbol in enumerate(columna["symbol"]):
            texto = fuente.render(symbol, True, color_fuente)
            ventana.blit(texto, (columna["x"], columna["y"] + i * tamano_fuente))

    # Actualizar la ventana
    pygame.display.flip()
    reloj.tick(30)  # Limitar la velocidad de fotogramas a 30 FPS

# Salir del programa
pygame.quit()

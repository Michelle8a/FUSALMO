import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mover un círculo con las flechas")

# Color
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Posición inicial del círculo
x = ANCHO // 2
y = ALTO // 2
radio = 20
velocidad = 5

# Bucle principal
ejecutando = True
while ejecutando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.circle(ventana, ROJO, (x, y), radio)
    pygame.display.flip()

    # Controlar FPS
    pygame.time.Clock().tick(60)

pygame.quit()

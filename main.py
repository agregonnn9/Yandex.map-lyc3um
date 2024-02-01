import pygame
import requests

WIDTH, HEIGHT = 600, 450

latitude, longitude = 68.97917, 33.09251
zoom = 10

def show_yandex_map(latitude, longitude, zoom):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Яндекс Карты')

    running = True
    while running:
        response = requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&z={zoom}&l=map'
        )

        with open('map.png', 'wb') as f:
            f.write(response.content)

        map_image = pygame.image.load('map.png')

        screen.blit(map_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zoom += 1
                elif event.key == pygame.K_DOWN:
                    zoom -= 1
                elif event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

    pygame.quit()

show_yandex_map(latitude, longitude, zoom)

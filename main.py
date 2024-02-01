import pygame
import requests


WIDTH, HEIGHT = 600, 450


def show_yandex_map(latitude, longitude, zoom):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Яндекс Карты')

    response = requests.get(
        f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&z={zoom}&l=map'
    )

    with open('map.png', 'wb') as f:
        f.write(response.content)

    map_image = pygame.image.load('map.png')

    screen.blit(map_image, (0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


show_yandex_map(68.97917, 33.09251, 10)

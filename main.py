import random
import pygame
pygame.init()

clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY1 = (122, 122, 122)
GREY2 = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH = 800
HEIGHT = 360
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
FONT = pygame.font.Font('freesansbold.ttf', 20)

def generate_list():
    lst = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    random.shuffle(lst)
    return lst

def draw(arg):
    for i, ele in enumerate(arg[0]):
        rect = pygame.Rect(60 + i*8 + 1, 200, 8, ele*15)
        if i == arg[1]:
            pygame.draw.rect(SCREEN, RED, rect)
        elif i == arg[2]:
            pygame.draw.rect(SCREEN, GREEN, rect)
        elif i % 2 == 0:
            pygame.draw.rect(SCREEN, GREY2, rect)
        else:
            pygame.draw.rect(SCREEN, GREY1, rect)
    

def insertion_sort(lst):
    for i in range(0, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        yield lst, i, j

def print_text(word, x, y, color = BLACK):
    TEXT = FONT.render(word, True, color)
    text_rect = TEXT.get_rect()
    text_rect.center = (x, y)
    return SCREEN.blit(TEXT, text_rect)

lst = generate_list()
algo_name = 'insertion_sort'
sorting = False
count = 0

SCREEN.fill(WHITE)
generator = insertion_sort(lst)
output = ([], 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorting = not sorting
                count = 0
                SCREEN.fill(WHITE)
            elif event.key == pygame.K_r:
                sorting = False
                lst = generate_list()
                generator = insertion_sort(lst)

    if sorting:
        try:
            SCREEN.fill(WHITE)
            output = next(generator)
        except StopIteration:
            sorting = False

    SCREEN.fill(WHITE)
    draw(output)
    clock.tick(6)

    pygame.display.update()

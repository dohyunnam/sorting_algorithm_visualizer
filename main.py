import random
import pygame
pygame.init()

clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (122, 122, 122)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 360
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
FONT = pygame.font.Font('freesansbold.ttf', 20)

def generate_list():
    lst = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    random.shuffle(lst)
    return lst

def draw(lst, pos):
    pass
def insertion_sort(lst):
    for i in range(0, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        yield lst, i

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

while True:
    if sorting:
        try:
            pass
        except StopIteration:
                sorting = False

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
                try:
                    output = next(generator)
                except StopIteration:
                    sorting = False
                print_text(str(output), 100, 100)
            elif event.key == pygame.K_e:
                print_text(str(count), 100 + count * 20, 300)
                generator = insertion_sort(lst)

    clock.tick(100)
    pygame.display.update()
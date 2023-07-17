import pygame
import neat
import time
import os
import random #for randomly placing height of the tubes

# set the dimension of the screen
WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))
    ]

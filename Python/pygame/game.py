import pygame
from menu import MainMenu
from start import Start
from score import HighScore

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.SPACE_KEY = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 650, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = 'assets/fonts/menu.ttf'
        self.title_menu = pygame.image.load("assets/img/title.png")
        self.background_menu = pygame.image.load("assets/img/bg.png")
        #self.font_name = pygame.font.get_default_font()
        self.WHITE = (255, 255, 255)
        self.title = 'ARCADE RACING'
        self.music_menu = 'assets/audio/bgm/menu.wav'
        pygame.display.set_caption(self.title)
        self.curr_start = Start(self)
        self.curr_score = HighScore(self)
        self.curr_menu = MainMenu(self, self.curr_start, self.curr_score)
    
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            pygame.display.update()
            self.reset_keys()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                self.curr_start.mulai = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = False
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    def draw_text(self, text, size, font_type, surface, x, y):
        font = pygame.font.Font(font_type, size)
        textobj = font.render(text, True, self.WHITE)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)
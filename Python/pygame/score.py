import pygame
from menu import MainMenu

class HighScore():
    def __init__(self, game):
        self.game = game
        self.bg_score = pygame.image.load("assets/img/bg_highscore.png")
        self.score_mulai = False
    
    def display_score(self):
        self.score_mulai = True
        score = open("high_score.txt", "r").read().splitlines()
        score.sort()
        while self.score_mulai:
            self.game.window.blit(self.bg_score, (0, 0))
            for i in range(len(score)):
                self.game.draw_text(str(f"{i+1}. {score[i]}"), 40, self.game.font_name, self.game.window, 300, 250+(i*50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.score_mulai = False
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                    self.game.curr_start.mulai = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.score_mulai = False
                        self.game.curr_menu.run_display = True
                        self.game.curr_menu.display_menu()
            pygame.display.update()
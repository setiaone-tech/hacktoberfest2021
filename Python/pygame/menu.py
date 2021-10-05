import pygame

class Menu():
    def __init__(self, game, start, score):
        self.game = game
        self.start = start
        self.score = score
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, 250
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
    
    def draw_cursor(self):
        self.game.draw_text("<", 30, 'assets/fonts/pilih.otf', self.game.window, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        pygame.display.update()
        self.game.reset_keys()
        
class MainMenu(Menu):
    def __init__(self, game, start, score):
        Menu.__init__(self, game, start, score)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 50
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 80
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 110
        self.exitx, self.exity = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    
    def display_menu(self):
        pygame.mixer.music.load(self.game.music_menu)
        pygame.mixer.music.play(-1)
        self.run_display = True
        while self.run_display:
            self.game.window.blit(self.game.background_menu, (0,0))
            self.game.window.blit(self.game.title_menu, (200, 100))
            self.game.draw_text("Main Menu", 30, self.game.font_name, self.game.window, self.mid_w, self.mid_h)
            self.game.draw_text("Start", 18, self.game.font_name, self.game.window, self.startx, self.starty)
            self.game.draw_text("High Score", 18, self.game.font_name, self.game.window, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 18, self.game.font_name, self.game.window, self.creditsx, self.creditsy)
            self.game.draw_text("Exit", 18, self.game.font_name, self.game.window, self.exitx, self.exity)
            self.game.check_events()
            self.check_input()
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "High Score"
            elif self.state == "High Score":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "High Score":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "High Score"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.run_display = False
                self.start.mulai = True
                self.start.display_jalan()
            elif self.state == "High Score":
                self.run_display = False
                self.score.score_mulai = True
                self.score.display_score()
            elif self.state == "Credits":
                pass
            elif self.state == "Exit":
                self.game.running, self.game.playing = False, False
                self.run_display = False
            self.run_display = False
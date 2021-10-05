import pygame
from menu import MainMenu
import os, random
import math

class Player():
    def __init__(self, game):
        self.x = 313
        self.y = 530
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 0.3
        self.stepIndex = 0
        self.stepLooping = 22
        self.v = 1
        self.cars_explode = pygame.image.load("assets/img/cars_explode.png")
        self.exploison = [pygame.image.load(os.path.join("assets/img/exploison", "1.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "2.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "3.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "4.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "5.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "6.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "7.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "8.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "9.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "10.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "11.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "12.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "13.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "14.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "15.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "16.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "17.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "18.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "19.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "20.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "21.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "22.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "23.png")),
                          pygame.image.load(os.path.join("assets/img/exploison", "24.png"))]
    
    def update(self):
        if self.left_pressed:
            self.velX = -self.speed
            if self.x >= 379 or self.x <= 247:
                self.speed = 0
                open("high_score.txt", "a").write(f"{self.score}\n")
            self.x += self.velX
        if self.right_pressed:
            self.velX = self.speed
            if self.x >= 379 or self.x <= 247:
                self.speed = 0
                open("high_score.txt", "a").write(f"{self.score}\n")
            self.x += self.velX
        if self.up_pressed:
            if self.y == 550:
                self.speed = 0.3
                self.velY = -self.speed
                self.y += self.velY
            else:
                self.velY = -self.speed
                self.y += self.velY
        if self.down_pressed:
            if self.y == 0:
                self.speed = 0.3
                self.velY = self.speed
                self.y += self.velY
            else:
                self.velY = self.speed
                self.y += self.velY

class Enemies():
    def __init__(self, game):
        self.bg_enemies = [pygame.image.load(os.path.join("assets/img/", "enem1_fix.png")),
                           pygame.image.load(os.path.join("assets/img/", "enem2_fix.png")),
                           pygame.image.load(os.path.join("assets/img/", "enem3_fix.png"))]
        self.spawnX = 0
        self.spawnY = 0
        self.enemIndex = 0
        self.x_enem = 0
        self.y_enem = 0
        self.enem_on = True
        self.jumlah_enem = 5
        self.data_enem = []
    
    def update_enemies(self):
        if len(self.data_enem) <= self.jumlah_enem:
            self.spawn_enem()
        else:
            for i in range(len(self.data_enem)):
                self.game.window.blit(self.bg_enemies[self.data_enem[i-1][0]], (self.data_enem[i-1][1], self.data_enem[i-1][2]))
                if self.data_enem[i-1][2] >= 600:
                    self.data_enem.remove([self.data_enem[i-1][0], self.data_enem[i-1][1], self.data_enem[i-1][2]])
                    self.enem_on = False
                self.data_enem[i-1][2] += self.v
    
    def spawn_enem(self):
        self.enemIndex = random.randint(0, 2)
        self.x_enem = random.randint(248, 379)
        self.y_enem = random.randint(20, 600)
        self.y_enem = -self.y_enem
        self.data_enem.append([self.enemIndex, self.x_enem, self.y_enem])

class Score():
    def __init__(self, game):
        self.score = 0
        self.cetak_score = f"SCORE = {self.score}"
        self.broke = False
    def update_score(self):
        if not self.enem_on and not self.broke:
            self.score += 1
            self.cetak_score = f"SCORE = {self.score}"
            self.game.draw_text(str(self.cetak_score), 15, self.game.font_name, self.game.window, 550, 15)
            self.enem_on = True
            if self.score % 25 == 0:
                self.v += 0.2
        else:
            self.game.draw_text(str(self.cetak_score), 15, self.game.font_name, self.game.window, 550, 15)

class Paused():
    def __init__(self):
        self.pause = False
        self.bg_pause = pygame.image.load("assets/img/paused.png")
        self.pauseX = 340
        self.pauseY = 350
        self.posisi = "Continue"
        self.MULAI_KEY = False
        
        self.mainmenuX = 140
        self.continueX = 340
        self.restartX = 540
    
    def checkinput_pause(self):
        if self.MULAI_KEY:
            if self.posisi == "Continue":
                self.mulai = True
                self.display_jalan()
            elif self.posisi == "Main Menu":
                self.mulai = False
                self.game.curr_menu.run_display = True
                print("sini")
            elif self.posisi == "Restart":
                pass
    
    def display_pause(self):
        self.pause = True
        while self.pause:
            self.game.window.blit(self.bg_pause, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pauseX -= 200
                        if self.pauseX == self.continueX:
                            self.posisi = "Continue"
                        if self.pauseX == self.mainmenuX:
                            self.posisi = "Main Menu"
                        if self.pauseX == -60:
                            self.pauseX = 540
                            self.posisi = "Restart"
                    if event.key == pygame.K_RIGHT:
                        self.pauseX += 200
                        if self.pauseX == self.restartX:
                            self.posisi = "Restart"
                        if self.pauseX == self.continueX:
                            self.posisi = "Continue"
                        if self.pauseX == 740:
                            self.pauseX = 140
                            self.posisi = "Main Menu"
                    if event.key == pygame.K_RETURN:
                        self.MULAI_KEY = True
                        self.checkinput_pause()
                if event.type == pygame.QUIT:
                    self.mulai = False
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                    self.game.curr_start.mulai = False
            
            self.game.draw_text("Main Menu", 20, self.game.font_name, self.game.window, 140, 300)
            self.game.draw_text("Continue", 20, self.game.font_name, self.game.window, 340, 300)
            self.game.draw_text("Restart", 20, self.game.font_name, self.game.window, 540, 300)
            self.game.draw_text("*", 20, self.game.font_name, self.game.window, self.pauseX, self.pauseY)
            pygame.display.update()

class Start(Player, Enemies, Score, Paused):
    def __init__(self, game):
        Player.__init__(self, game)
        Enemies.__init__(self, game)
        Score.__init__(self, game)
        Paused.__init__(self)
        self.game = game
        self.jalan = pygame.image.load('assets/img/jalan_fix.png')
        self.cars = pygame.image.load('assets/img/cars.png')
        self.bg = pygame.transform.scale(self.jalan, (650, 600))
        self.music_start = 'assets/audio/bgm/start.mp3'
        self.mulai = False
        self.geser = 0
    
    def isCollison(self):
        for i in range(len(self.data_enem)):
            distanceX1 = math.sqrt(math.pow(self.data_enem[i-1][1]-self.x, 2) + math.pow(self.data_enem[i-1][2]-self.y, 2))
            if distanceX1 < 22:
                self.speed = 0
                open("high_score.txt", "a").write(f"{self.score}\n")
    
    def display_jalan(self):
        pygame.mixer.music.load(self.music_start)
        pygame.mixer.music.play(-1)
        while self.mulai:
            self.game.window.blit(self.bg, (0, self.geser))
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = False
                    if event.key == pygame.K_UP:
                        self.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = True
                        self.right_pressed = False
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = True
                        self.left_pressed = False
                    if event.key == pygame.K_UP:
                        self.up_pressed = True
                        self.down_pressed = False
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = True
                        self.up_pressed = False
                    if event.key == pygame.K_ESCAPE:
                        self.pause = True
                        self.display_pause()
                if event.type == pygame.QUIT:
                    self.mulai = False
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                    self.game.curr_start.mulai = False
            self.update()
            if self.geser > 600:
                self.game.window.blit(self.bg, (0, -600+self.geser))
                self.geser = 0
            if self.speed == 0:
                self.geser = 0
                self.broke = True
                if self.stepIndex >=24:
                    self.game.window.blit(self.cars_explode, (self.x, self.y))
                    self.game.window.blit(self.exploison[self.stepLooping], (self.x-35, self.y-20))
                    self.stepLooping += 1
                    if self.stepLooping > 23:
                        self.stepLooping = 22
                else:
                    self.game.window.blit(self.cars, (self.x, self.y))
                    self.game.window.blit(self.exploison[self.stepIndex], (self.x-35, self.y-20))
                    self.stepIndex += 1
            else:  
                self.game.window.blit(self.bg, (0, -600+self.geser))
                self.game.window.blit(self.cars, (self.x, self.y))
            
            self.update_score()
            self.update_enemies()
            self.isCollison()
            self.geser += self.v
            pygame.display.update()
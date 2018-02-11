import pygame
import Colors
import random
import Start
import End

WIDTH = 600
HEIGHT = 700

class Controller:
    def __init__(self):
        self.picker = []
        self.choice = []
        pygame.init()
        self.begin = True
        while self.begin:
            self.front = Start.Start()
            if self.front.choice():
                self.x = WIDTH / 2
                self.y = HEIGHT - 140
                self.score = 0
                self.box1 = Colors.Colors(50,20)
                self.box2 = Colors.Colors(180,20)
                self.box3 = Colors.Colors(310,20)
                self.box4 = Colors.Colors(440,20)
                self.box5 = Colors.Colors(50,150)
                self.box6 = Colors.Colors(180,150)
                self.box7 = Colors.Colors(310,150)
                self.box8 = Colors.Colors(440,150)
                self.box9 = Colors.Colors(50,280)
                self.box10 = Colors.Colors(180,280)
                self.box11 = Colors.Colors(310,280)
                self.box12 = Colors.Colors(440,280)
                self.box13 = Colors.Colors(50,410)
                self.box14 = Colors.Colors(180,410)
                self.box15 = Colors.Colors(310,410)
                self.box16 = Colors.Colors(440,410)
                self.box = [self.box1,self.box2,self.box3,self.box4, \
                            self.box5,self.box6,self.box7,self.box8, \
                            self.box9,self.box10,self.box11,self.box12, \
                            self.box13,self.box14,self.box15,self.box16]
                
                self.image = pygame.image.load('app.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (100,100))
                self.spritebox = pygame.sprite.Group(self.box)
                self.display = pygame.display.set_mode((WIDTH, HEIGHT))
                self.background = pygame.Surface(self.display.get_size()).convert()
                for i in self.box:
                    self.background.blit(self.image,(i.x,i.y))
                self.font = pygame.font.SysFont('bodoniblack',50)
                self.font2 = pygame.font.SysFont('bodoniblack',20)
                self.value = self.font.render('Score: '+ str(self.score),True,(0,0,255))
                self.text = self.font2.render('Click the images',True,(255,0,255))
                self.text2 = self.font2.render('in the order that',True,(255,0,255))
                self.text3 = self.font2.render('they change',True,(255,0,255))
                self.background.blit(self.text,(350,550))
                self.background.blit(self.text2,(350,580))
                self.background.blit(self.text3,(350,610))
                self.num = 4
                self.game = True
                while self.game:
                    for i in range(len(self.picker)):
                        self.picker[i].revert()
                    self.picker = []
                    self.choice = []
                    self.game = Controller.game(self)
                    self.num += 1
                self.end = End.End(self.score)
                self.begin = self.end.choice()
            else:
                self.begin = False
        pygame.quit()

    def game(self):
        self.good = True
        self.time = 3
        for i in range(3):
            self.font2 = pygame.font.SysFont('bodoniblack',300)
            self.countdown= self.font2.render(str(self.time),True,(0,0,255))
            if self.time != 1:
                self.time -= 1

            self.display.blit(self.background,(0,0))
            self.spritebox.draw(self.display)
            self.display.blit(self.countdown,(200,100))
            self.display.blit(self.value,(50,600))
            pygame.display.flip()
            pygame.time.delay(500)
            
        for num in range(self.num):
            self.pick = random.choice(self.box)
            self.picker.append(self.pick)
            self.pick.flash()
            self.display.blit(self.background,(0,0))
            self.spritebox.draw(self.display)
            self.display.blit(self.value,(50,600))
            pygame.display.flip()
            pygame.time.delay(500)
            self.pick.revert()
            
            self.display.blit(self.background,(0,0))
            self.spritebox.draw(self.display)
            self.display.blit(self.value,(50,600))
            pygame.display.flip()
            pygame.time.delay(500)
        pygame.event.clear()
        done = False
        while not done:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 50<self.mouse[0]<150 and 20<self.mouse[1]<120:
                        self.choice.append(self.box1)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 180<self.mouse[0]<280 and 20<self.mouse[1]<120:
                        self.choice.append(self.box2)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 310<self.mouse[0]<410 and 20<self.mouse[1]<120:
                        self.choice.append(self.box3)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 440<self.mouse[0]<540 and 20<self.mouse[1]<120:
                        self.choice.append(self.box4)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 50<self.mouse[0]<150 and 150<self.mouse[1]<250:
                        self.choice.append(self.box5)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 180<self.mouse[0]<280 and 150<self.mouse[1]<250:
                        self.choice.append(self.box6)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 310<self.mouse[0]<410 and 150<self.mouse[1]<250:
                        self.choice.append(self.box7)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 440<self.mouse[0]<540 and 150<self.mouse[1]<250:
                        self.choice.append(self.box8)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 50<self.mouse[0]<150 and 280<self.mouse[1]<380:
                        self.choice.append(self.box9)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 180<self.mouse[0]<280 and 280<self.mouse[1]<380:
                        self.choice.append(self.box10)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 310<self.mouse[0]<410 and 280<self.mouse[1]<380:
                        self.choice.append(self.box11)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 440<self.mouse[0]<540 and 280<self.mouse[1]<380:
                        self.choice.append(self.box12)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 50<self.mouse[0]<150 and 410<self.mouse[1]<510:
                        self.choice.append(self.box13)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 180<self.mouse[0]<280 and 410<self.mouse[1]<510:
                        self.choice.append(self.box14)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 310<self.mouse[0]<410 and 410<self.mouse[1]<510:
                        self.choice.append(self.box15)
                        self.good = Controller.correct(self)
                    elif pygame.mouse.get_pressed()[0] and 440<self.mouse[0]<540 and 410<self.mouse[1]<510:
                        self.choice.append(self.box16)
                        self.good = Controller.correct(self)
                            
                    if not self.good:
                        return False
                    elif len(self.choice) == len(self.picker):
                        self.score += 1
                        self.value = self.font.render('Score: '+ str(self.score),True,(0,0,255))
                        return True
                    else:
                        self.score += 1
                        self.value = self.font.render('Score: '+ str(self.score),True,(0,0,255))
                self.display.blit(self.background,(0,0))
                self.spritebox.draw(self.display)
                self.display.blit(self.value,(50,600))
                pygame.display.flip()

            

    def correct(self):
        right = True
        for i in range(len(self.choice)):
            if self.choice[i] == self.picker[i]:
                self.choice[len(self.choice)-1].right()
                self.display.blit(self.background,(0,0))
                self.spritebox.draw(self.display)
                self.display.blit(self.value,(50,600))
                pygame.display.flip()
                pygame.time.delay(150)
                self.choice[len(self.choice)-1].revert()
                self.display.blit(self.background,(0,0))
                self.spritebox.draw(self.display)
                self.display.blit(self.value,(50,600))
                pygame.display.flip()
                
            else:
                self.picker[i].wrong()
                self.display.blit(self.background,(0,0))
                self.spritebox.draw(self.display)
                pygame.display.flip()
                pygame.time.delay(1000)
                right = False
        return right
                        

Controller()

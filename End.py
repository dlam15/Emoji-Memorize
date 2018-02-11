import pygame

WIDTH = 600
HEIGHT = 700

class End:
    def __init__(self, num):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.font = pygame.font.SysFont('lucidaconsole',50)
        self.fonty = pygame.font.SysFont('comicsansms',25)
        self.score = self.fonty.render('Your Score: ' + str(num),True,(0,255,0))
        self.file = open('highscore.txt', 'r')
        self.happy = pygame.image.load('happyemoji.jpg')
        self.sad = pygame.image.load('sademoji.png').convert_alpha()
        self.sleep = pygame.image.load('sleepemoji.png').convert_alpha()
        self.angry = pygame.image.load('angryemoji.png').convert_alpha()
        self.tongue = pygame.image.load('tongueemoji.png').convert_alpha()
        self.happy = pygame.transform.scale(self.happy, (150,150))
        self.sad = pygame.transform.scale(self.sad, (150,150))
        self.sleep = pygame.transform.scale(self.sleep, (130,130))
        self.angry = pygame.transform.scale(self.angry, (130,130))
        self.tongue = pygame.transform.scale(self.tongue, (120,120))
        self.high = []
        for line in self.file:
            line = line.strip()
            self.high += [int(line)]
        for i in self.high:
            if num >= i:
                self.file.close()
                self.file = open('highscore.txt', 'w')
                self.file.write(str(num))
                self.file.close()
                self.highscore = self.fonty.render('New High Score: ' + str(num),True,(0,255,0))
            else:
                self.file = open('highscore.txt', 'r')
                self.highscore = self.fonty.render('High Score: ' + str(self.file.read()), True, (0,255,0))
                self.file.close()
        self.again = self.fonty.render('Try Again',True,(0,255,0))
        self.finish = self.fonty.render('Quit',True,(0,255,0))
        letter = 'Game Over'
        self.end = 100
        for c in letter:
            self.text = self.font.render(c,True,(255,0,0))
            pygame.time.delay(100)
            self.display.blit(self.text,(self.end,200))
            self.background.blit(self.display,(self.end,200))
            self.end += 50
            pygame.display.flip()
        self.display.blit(self.highscore,(170,300))
        self.display.blit(self.score,(200,350))
        self.display.blit(self.again,(160,500))
        self.display.blit(self.finish,(160,550))
        pygame.draw.rect(self.display, (0,0,0),(50,45,150,150))
        self.display.blit(self.sleep,(60,45))
        self.display.blit(self.angry,(240,45))
        self.display.blit(self.tongue,(420,50))
        pygame.display.flip()
        self.mouse = pygame.mouse.get_pos()

        
    def choice(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = pygame.mouse.get_pos()
                    if 160<self.mouse[0]<290 and 500<self.mouse[1]<540:
                        pygame.draw.rect(self.display, (255,255,255),(160,500,140,40))
                        self.display.blit(self.highscore,(170,300))
                        self.display.blit(self.score,(200,350))
                        self.display.blit(self.again,(160,500))
                        self.display.blit(self.finish,(160,550))
                        self.display.blit(self.happy,(350,500))
                        pygame.display.flip()

                    elif 155<self.mouse[0]<220 and 550<self.mouse[1]<590:
                        pygame.draw.rect(self.display,(255,255,255),(160,550,70,40))
                        self.display.blit(self.highscore,(170,300))
                        self.display.blit(self.score,(200,350))
                        self.display.blit(self.again,(160,500))
                        self.display.blit(self.finish,(160,550))
                        self.display.blit(self.sad,(350,500))
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(self.display, (0,0,0),(160,500,160,50))
                        pygame.draw.rect(self.display, (0,0,0),(160,550,70,50))
                        pygame.draw.rect(self.display, (0,0,0),(350,500,150,150))
                        self.display.blit(self.highscore,(170,300))
                        self.display.blit(self.score,(200,350))
                        self.display.blit(self.again,(160,500))
                        self.display.blit(self.finish,(160,550))
                        pygame.display.flip()
                                                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and 160<self.mouse[0]<290 and 500<self.mouse[1]<540:
                        return True
                    elif pygame.mouse.get_pressed()[0] and 160<self.mouse[0]<220 and 550<self.mouse[1]<590:
                        return False
            pygame.display.flip()

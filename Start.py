import pygame

WIDTH = 600
HEIGHT = 700

class Start:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.words = pygame.Surface(self.display.get_size()).convert()
        self.font = pygame.font.SysFont('comicsansms',30)
        self.fonty = pygame.font.SysFont('lucidaconsole',70)
        self.play = self.font.render('Play',True,(0,255,0))
        self.title = self.fonty.render('Memorize',True,(0,0,255))
        self.emoji = self.fonty.render('Emoji',True,(255,0,0))

        self.tape = pygame.image.load('tape.png').convert_alpha()
        self.smart = pygame.image.load('smartemoji.png').convert_alpha()
        self.tape = pygame.transform.scale(self.tape,(50,50))
        self.smart = pygame.transform.scale(self.smart,(150,150))
        
        self.mouse = pygame.mouse.get_pos()
        letter = 'Memorize'
        self.x = 150
        for c in letter:
            self.text = self.fonty.render(c,True,(0,0,255))
            pygame.time.delay(50)
            self.display.blit(self.text,(self.x,200))

            self.words.blit(self.display,(self.x,350))
            self.x += 40
            pygame.display.flip()
            pygame.time.delay(200)
            self.display.blit(self.background,(0,0))
            pygame.display.flip()
        self.display.blit(self.play,(400,500))
        pygame.draw.rect(self.display, (200,200,200),(110,100,230,80))
        self.display.blit(self.emoji,(120,100))
        self.display.blit(self.tape,(315,80))
        self.display.blit(self.tape,(95,145))
        self.display.blit(self.title,(150,200))
        self.display.blit(self.smart,(150,400))
        pygame.display.flip()

        
    def choice(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    return False
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = pygame.mouse.get_pos()

                    if 400<self.mouse[0]<470 and 500<self.mouse[1]<540:
                        pygame.draw.rect(self.display, (255,255,255),(400,500,70,45))
                        self.display.blit(self.play,(400,500))
                        pygame.display.flip()

                    else:
                        pygame.draw.rect(self.display, (0,0,0),(400,500,70,45))
                        self.display.blit(self.play,(400,500))
                        pygame.display.flip()
                                                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and 400<self.mouse[0]<470 and 500<self.mouse[1]<550:
                        return True
            
            pygame.display.flip()
        pygame.quit()

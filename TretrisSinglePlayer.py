import pygame, random

pygame.font.init()

blok_siz = 30
lin=1
l_play= (blok_siz+lin)*10
h_play=(blok_siz+lin)*20
l_tel= l_play+200
h_tel=h_play+100

x_top_e = (l_tel-l_play) // 2
y_top_e = (h_tel-h_play)-30

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

formsl = [S, Z, I, O, J, L, T]
coresl = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class piece:
    def __init__(self, s, x=0, y=0, r=0):
        self.x=x
        self.y=y
        self.rot=r
        self.clr=coresl[formsl.index(s)]

def grid_make():
    return([[(0,0,0) for i in range(10)] for j in range(20)])

def grid_update(solidic):
    gd=grid_make()
    for y in range(20):
        for x in range(10):
            if (y,x) in solidic:
                gd[y][x]=solidic[(y,x)]
    return(gd)

def draw_waiting(tela,wl):
    for i,s in enumerate(wl):
        pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e+(blok_siz//2+lin)*5*i+10*i),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
        for j in range(5):
            for k in range(5):
                if s[0][j][k]=='.':
                    pygame.draw.rect(tela, (0,0,0), ((x_top_e+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                else:
                    pygame.draw.rect(tela, coresl[formsl.index(s)], ((x_top_e+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                    
def draw_swap(tela,s=[['.....','.....','.....','.....','.....']]):
    pygame.draw.rect(tela, (100,100,100), ((x_top_e-10-(blok_siz//2)*5,y_top_e),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
    for j in range(5):
        for k in range(5):
            if s[0][j][k]=='.':
                pygame.draw.rect(tela, (0,0,0), ((x_top_e-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
            else:
                pygame.draw.rect(tela, coresl[formsl.index(s)], ((x_top_e-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
                    
            
def game():
    pygame.init()
    tela = pygame.display.set_mode((l_tel,h_tel))
    tela.fill((58,58,58))
    pygame.draw.rect(tela, (100,100,100), ((x_top_e,y_top_e),(l_play,h_play)))
    # pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e),((blok_siz/2+lin)*5,(blok_siz/2+lin)*5)))
    # pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e+(blok_siz/2+lin)*5+10),((blok_siz/2+lin)*5,(blok_siz/2+lin)*5)))
    # pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e+(blok_siz/2+lin)*5*2+20),((blok_siz/2+lin)*5,(blok_siz/2+lin)*5)))
    # pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e+(blok_siz/2+lin)*5*3+30),((blok_siz/2+lin)*5,(blok_siz/2+lin)*5)))
    grid=grid_make()
    waitl=[random.choice(formsl),random.choice(formsl),random.choice(formsl),random.choice(formsl)]
    draw_waiting(tela, waitl)
    draw_swap(tela)
    peça=piece(random.choice(formsl))
    while True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(tela, grid[i][j], ((x_top_e+j*(blok_siz+lin),y_top_e+i*(blok_siz+lin)),(blok_siz,blok_siz)))
        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    peça.x+=1
                if event.key == pygame.K_LEFT:
                    peça.x-=1
                if event.key == pygame.K_DOWN:
                    peça.y+=1
                if event.key == pygame.K_UP:
                    peça.rot+=1
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
game()
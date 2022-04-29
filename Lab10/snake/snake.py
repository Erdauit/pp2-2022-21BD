import pygame, psycopg2
import random
from config import config

def insert(sql):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def check(name):
    sql = f"SELECT name FROM snake WHERE name = '{name}'"
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    if result == None:
        return False
    else:
        return True



print("Enter your name:")
name = input()
if check(name) == False:
  sql = f"INSERT INTO snake VALUES('{name}', 0, 1)"
  insert(sql)

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Surface
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)
time = 0

BLOCK_SIZE = 20

clock = pygame.time.Clock()
FPS = 6

def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)
  

class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()
  
  def load_wall(self):
    with open(f'level1.txt', 'r') as f:
      wall_body = f.readlines()
    
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
  
  def draw(self): 
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

class Point:
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        
    def draw(self):
        point = self.location
        pygame.draw.rect(screen, RED, (point.x * BLOCK_SIZE, point.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        
    
class Food:
  def __init__(self):
      
      self.generate_random_pos()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  def respawn(self):
    self.generate_random_pos()
  
  def draw(self):
    pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10],]
      self.dx = 1
      self.dy = 0
  
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def collide_self(self):  # проверка столкновения с самим собой
        global running
        if self.body[0] in self.body[2:]:
          running = False
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy

    if self.body[0][0] * BLOCK_SIZE > WINDOW_WIDTH:
            self.body[0][0] = 0
        
    if self.body[0][1] * BLOCK_SIZE > WINDOW_HEIGHT:
          self.body[0][1] = 0

    if self.body[0][0]< 0:
        self.body[0][0] = WINDOW_WIDTH / BLOCK_SIZE
    
    if self.body[0][1] < 0:
        self.body[0][1] =WINDOW_HEIGHT/ BLOCK_SIZE
  

snake = Snake()
food = Food()
wall = Wall()
block = Block(0, 0)
level = 1
score = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        snake.dx = 1
        snake.dy = 0
      if event.key == pygame.K_LEFT:
        snake.dx = -1
        snake.dy = 0
      if event.key == pygame.K_UP:
        snake.dx = 0
        snake.dy = -1
      if event.key == pygame.K_DOWN:
        snake.dx = 0
        snake.dy = 1
      # if event.key == pygame.K_SPACE:
      #   p

  wallsCoor = open(f"level1.txt", 'r').readlines()
  walls = []
  for i, line in enumerate(wallsCoor):
      for j, each in enumerate(line):
          if each == "#":
            walls.append(Block(j, i))  

  for block in walls:
    block.draw()
    if food.x == block.x and food.y == block.y:
      food.respawn()
    if snake.body[0][0] == block.x and snake.body[0][1] == block.y:
      saved_score = score
      sql = f"UPDATE snake SET score = {saved_score}, level = {level} WHERE name = '{name}'"
      insert(sql)
      running = False    
  
  snake.move()    
    
  screen.fill(WHITE)
  
  draw_grid()
  snake.draw()
  food.draw()
  wall.draw()
  snake.collide_self()


  # if food.x == block.x and food.y == block.y:
  #   food.respawn()
  
  if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
    snake.body.append([0, 0])
    food.generate_random_pos()
    score += random.randint(1, 3)
    if score%5==0 and score!=0:
      FPS +=4
      level+=1

  time += FPS % 4
  # print(time)
  if time % 100 == 0 and time != 0:
    food.respawn()


  font = pygame.font.Font(None, 30)
  text = font.render(f'Score: {score}', True, (255, 0, 0))
  # font_l = pygame.font.SysFont("Verdana", 20)
  font_l = pygame.font.Font(None, 30)
  levell = font_l.render("LEVEL:"+str(level), True, (BLACK))
  screen.blit(levell, (300,20))
  screen.blit(text, (20, 20))
  
  pygame.display.update()
  clock.tick(FPS)
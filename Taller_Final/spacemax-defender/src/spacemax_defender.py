
import pygame
import random
import os
import sys
import math

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceMax Defender - Enhanced Edition")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configuración de rutas
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
img_path = os.path.join(assets_path, 'images')
sound_path = os.path.join(assets_path, 'sounds')

# Función para cargar imágenes con manejo de errores
def load_image(path, default_size=(64, 64)):
    try:
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, default_size)
    except pygame.error:
        # Crear imagen de respaldo si no se encuentra el archivo
        surf = pygame.Surface(default_size, pygame.SRCALPHA)
        pygame.draw.rect(surf, WHITE, surf.get_rect(), 2)
        return surf

# Función para cargar sonidos con manejo de errores
def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except pygame.error:
        # Crear sonido silencioso si no se encuentra
        return pygame.mixer.Sound(buffer=b'\x00' * 1024)

# Cargar recursos
try:
    # Jugador
    player_img = load_image(os.path.join(img_path, 'player.png'), (60, 40))
    
    # Enemigos
    enemy_imgs = [
        load_image(os.path.join(img_path, 'enemy1.png'), (40, 30)),
        load_image(os.path.join(img_path, 'enemy2.png'), (45, 35)),
        load_image(os.path.join(img_path, 'enemy3.png'), (50, 40))
    ]
    
    # Bala
    bullet_img = load_image(os.path.join(img_path, 'bullet.png'), (8, 15))
    
    # Fondo
    try:
        background = pygame.image.load(os.path.join(img_path, 'background.jpg')).convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    except pygame.error:
        # Fondo de respaldo - gradiente espacial
        background = pygame.Surface((WIDTH, HEIGHT))
        for y in range(HEIGHT):
            color_val = int(255 * (y / HEIGHT) * 0.1)
            pygame.draw.line(background, (color_val, 0, color_val * 2), (0, y), (WIDTH, y))
    
    # Sonidos
    laser_sound = load_sound(os.path.join(sound_path, 'laser.mp3'))
    explosion_sound = load_sound(os.path.join(sound_path, 'explosion.mp3'))
    
except Exception as e:
    print(f"Error cargando recursos: {e}")

class Particle(pygame.sprite.Sprite):
    """Partícula para efectos visuales"""
    def __init__(self, x, y, color=WHITE):
        super().__init__()
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (2, 2), 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = random.randint(-5, 5)
        self.vel_y = random.randint(-5, 5)
        self.life = 30
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.life -= 1
        if self.life <= 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 8
        self.lives = 3
        self.score = 0
        self.last_shot = 0
        self.shoot_delay = 250  # milisegundos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > HEIGHT // 2:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 5:
            self.rect.y += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            return Bullet(self.rect.centerx, self.rect.top, -12)
        return None

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.image = enemy_imgs[enemy_type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)
        self.direction = 1
        self.enemy_type = enemy_type
        self.last_shot = 0
        self.shoot_delay = random.randint(1000, 3000)

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 30
            
        # Los enemigos pueden disparar ocasionalmente
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay and random.random() < 0.001:
            self.last_shot = now
            return EnemyBullet(self.rect.centerx, self.rect.bottom)
        return None

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 12), pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (0, 0, 6, 12))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class GameState:
    def __init__(self):
        self.level = 1
        self.wave = 1
        self.game_over = False
        self.victory = False
        self.paused = False

def create_enemies(level):
    """Crear enemigos según el nivel"""
    enemies_group = pygame.sprite.Group()
    enemy_count = min(24 + level * 4, 40)
    rows = min(3 + level // 2, 6)
    cols = enemy_count // rows
    
    for row in range(rows):
        for col in range(cols):
            enemy_type = min(row, 2)  # Máximo 3 tipos
            x = 50 + col * 80
            y = 50 + row * 60
            enemy = Enemy(x, y, enemy_type)
            enemies_group.add(enemy)
    
    return enemies_group

def draw_ui(screen, player, game_state):
    """Dibujar interfaz de usuario"""
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    # Puntuación y vidas
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
    level_text = small_font.render(f"Level: {game_state.level}", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(level_text, (WIDTH - 100, 10))
    
    # Barra de vida visual
    pygame.draw.rect(screen, RED, (10, 90, 100, 10))
    pygame.draw.rect(screen, GREEN, (10, 90, (player.lives / 3) * 100, 10))

def main():
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    particles = pygame.sprite.Group()

    # Crear jugador
    player = Player()
    all_sprites.add(player)

    # Estado del juego
    game_state = GameState()

    # Crear enemigos iniciales
    enemies = create_enemies(game_state.level)
    all_sprites.add(enemies)

    # Bucle principal
    clock = pygame.time.Clock()
    running = True
    
    while running:
        dt = clock.tick(60)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    if bullet:
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        laser_sound.play()
                elif event.key == pygame.K_p:
                    game_state.paused = not game_state.paused
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if not game_state.paused and not game_state.game_over:
            # Actualizar sprites
            all_sprites.update()
            particles.update()

            # Enemigos disparan
            for enemy in enemies:
                enemy_bullet = enemy.update()
                if enemy_bullet:
                    all_sprites.add(enemy_bullet)
                    enemy_bullets.add(enemy_bullet)

            # Colisiones balas del jugador con enemigos
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                explosion_sound.play()
                player.score += (hit.enemy_type + 1) * 50
                
                # Crear partículas de explosión
                for _ in range(10):
                    particle = Particle(hit.rect.centerx, hit.rect.centery, 
                                       (255, random.randint(100, 255), 0))
                    particles.add(particle)

            # Colisiones balas enemigas con jugador
            player_hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
            if player_hits:
                player.lives -= 1
                # Efecto de daño
                for _ in range(15):
                    particle = Particle(player.rect.centerx, player.rect.centery, RED)
                    particles.add(particle)

            # Colisiones directas jugador-enemigos
            if pygame.sprite.spritecollide(player, enemies, True):
                player.lives -= 1
                explosion_sound.play()

            # Verificar condiciones de juego
            if player.lives <= 0:
                game_state.game_over = True
            
            if len(enemies) == 0:
                game_state.level += 1
                enemies = create_enemies(game_state.level)
                all_sprites.add(enemies)

        # Dibujar todo
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        particles.draw(screen)
        
        # UI
        draw_ui(screen, player, game_state)
        
        # Mensajes de estado
        font = pygame.font.Font(None, 48)
        if game_state.paused:
            pause_text = font.render("PAUSED - Press P to continue", True, YELLOW)
            screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2))
        elif game_state.game_over:
            game_over_text = font.render("GAME OVER - Press ESC to exit", True, RED)
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
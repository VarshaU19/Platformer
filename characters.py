import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.idle_sheet = pygame.image.load("assets/characters/Soldier-Idle.png").convert_alpha()

        frame_width =  250
        frame_height = 250
        num_frames = 6

        self.idle_frames = self.load_frames(self.idle_sheet, frame_width, frame_height, num_frames)
        self.idle_frames = [pygame.transform.scale(frame, (230, 230)) for frame in self.idle_frames]

        self.animation_index = 0
        self.animation_speed = 0.2

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def load_frames(self, sheet, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames
        
    def update(self, keys):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.idle_frames):
            self.animation_index = 0
        self.image = self.idle_frames[int(self.animation_index)]
        
        #movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
    

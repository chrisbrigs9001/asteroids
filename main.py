import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    #initialize pygame
    pygame.init()
    #initialize game clock and time delta
    game_clock=pygame.time.Clock()
    dt = 0
    
    #instantiate player
    my_player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    
    #set screen size
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    go = True
    while go:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            
        screen.fill("black")
        my_player.update(dt)
        my_player.draw(screen)
        dt = game_clock.tick(60)
        dt = dt/1000
        
        #debug print, removed
        #print (dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()

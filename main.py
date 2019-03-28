import pygame

class Game():
    """docstring for ClassName"""
    def __init__(self):
        self.width = 500
        self.height = 500
        self.running = False

    def run(self):
        pygame.init()
        self.running = True
     
        pygame.display.set_mode((self.width, self.height ) )

        while (self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        

if __name__ == "__main__":
    game = Game()
    game.run()
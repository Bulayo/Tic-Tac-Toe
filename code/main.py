from settings import *

class Game:

    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tic-Tac-Toe")
        self.running = True

    def run(self):

        while self.running:
            self.clock.tick(24)
            self.WINDOW.fill((50, 50, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
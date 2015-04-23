import sys
import pygame

WIDTH = 640
HEIGHT = 480


class Color:
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 128, 0)
    WHITE = (255, 255, 255)


class SequenceGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

    def start(self):

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

            self.write_header()
            problem = SequenceProblem(1)
            self.write_problem(problem)

            pygame.display.flip()
            self.clock.tick(60)

    def write_header(self):
        font = pygame.font.SysFont(None, 48)
        self.screen.fill(Color.WHITE)
        text = font.render("Sequences Game", True, Color.DARK_GREEN)
        top_center = ((self.screen.get_width() // 2) - text.get_width() // 2, 5)
        self.screen.blit(text, top_center)

    def write_problem(self, problem):
        font = pygame.font.SysFont(None, 32)
        if problem.is_find_equation():
            # Print equation
            equation_text = font.render(problem.get_equation(), True, Color.DARK_GREEN)
            middle = ((self.screen.get_width() // 2) - equation_text.get_width() // 2,
                      (self.screen.get_height() // 2) - equation_text.get_height() // 2)
            self.screen.blit(equation_text, middle)

            # Print Sequence
            sequence_text = font.render(problem.get_sequence(), True, Color.DARK_GREEN)
            below_middle = ((self.screen.get_width() // 2) - sequence_text.get_width() // 2,
                            middle[1] + equation_text.get_height() + 20)
            self.screen.blit(sequence_text, below_middle)

        else:
            equation_text = font.render(problem.get_equation(), True, Color.DARK_GREEN)
            middle = ((self.screen.get_width() // 2) - equation_text.get_width() // 2,
                      (self.screen.get_height() // 2) - equation_text.get_height() // 2)
            self.screen.blit(equation_text, middle)

            # Print Sequence
            sequence_text = font.render(problem.get_sequence(), True, Color.DARK_GREEN)
            below_middle = ((self.screen.get_width() // 2) - sequence_text.get_width() // 2,
                            middle[1] + equation_text.get_height() + 20)
            self.screen.blit(sequence_text, below_middle)


class SequenceProblem:
    def __init__(self, difficulty):
        # Generate problem here, hardcoded for now
        self.equation = "n + ?"
        self.sequence = "2, 3, 4, 5"
        self.solution = "1"

    def get_sequence(self):
        return self.sequence

    def get_equation(self):
        return self.equation

    def is_find_equation(self):
        return True

    def is_find_sequence(self):
        return False

    def is_correct(self, answer):
        return answer == self.solution


def main():
    pygame.display.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game = SequenceGame(screen, clock)
    game.start()

main()
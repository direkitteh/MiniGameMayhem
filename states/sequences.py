import random
import time
import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480


class Colors:
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 128, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


class SequenceGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.problem = None
        self.answer_input = None
        self.time_limit = 10

    def start(self):
        self.generate_new()

        done = False
        self.start_time = time.time()
        while not done:
            self.screen.fill(Colors.WHITE)
            # Events
            events = pygame.event.get()

            for event in events:
                if event.type == QUIT:
                    done = True
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                if event.type == KEYDOWN and (event.key == K_RETURN or event.key == K_KP_ENTER):
                    correct = self.problem.is_correct(self.answer_input.get_value())
                    self.reset(correct)
                    continue

            self.answer_input.update(events)

            if (time.time() - self.start_time) >= self.time_limit:
                self.reset(2)

            # Draws
            self.write_header()
            self.write_problem()
            self.draw_answer_input()
            self.write_timer()

            pygame.display.flip()
            self.clock.tick(60)

    def reset(self, correct):
        self.write_header()
        self.draw_response(correct)
        self.generate_new()
        pygame.display.flip()
        self.clock.tick(60)
        start_time = time.time()
        while (time.time() - start_time) < 1:
            self.screen.fill(Colors.WHITE)
            self.write_header()
            self.draw_response(correct)
            pygame.display.flip()
            self.clock.tick(60)
        self.start_time = time.time()

    def write_header(self):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Sequences Game", True, Colors.DARK_GREEN)
        top_center = ((self.screen.get_width() // 2) - text.get_width() // 2, 5)
        self.screen.blit(text, top_center)

    def write_problem(self):
        font = pygame.font.SysFont(None, 32)
        # Print equation
        equation_text = font.render(self.problem.get_equation(), True, Colors.DARK_GREEN)
        middle = ((self.screen.get_width() // 2) - equation_text.get_width() // 2,
                  (self.screen.get_height() // 2) - equation_text.get_height() // 2)
        self.screen.blit(equation_text, middle)

        # Print Sequence
        sequence_text = font.render(self.problem.get_sequence(), True, Colors.DARK_GREEN)
        below_middle = ((self.screen.get_width() // 2) - sequence_text.get_width() // 2,
                        middle[1] + equation_text.get_height() + 20)
        self.screen.blit(sequence_text, below_middle)

    def write_timer(self):
        time_left = int(round(self.time_limit - (time.time() - self.start_time), 0))
        font = pygame.font.SysFont(None, 32)
        percent = (self.time_limit - (time.time() - self.start_time)) / self.time_limit
        if percent > 0.6666:
            color = Colors.GREEN
        elif percent < 0.3333:
            color = Colors.RED
        else:
            color = Colors.YELLOW
        timer_text = font.render(str(time_left), True, color)
        text_position = ((self.screen.get_width() - timer_text.get_width()) - 10, 10)
        self.screen.blit(timer_text, text_position)

    def draw_answer_input(self):
        font = pygame.font.SysFont(None, 32)
        answer_text = font.render("Answer: ", True, Colors.DARK_GREEN)
        text_position = ((self.screen.get_width() // 2) - (answer_text.get_width() + self.answer_input.get_width()) // 2,
                         self.screen.get_height() - (answer_text.get_height() * 2))
        input_position = (text_position[0] + answer_text.get_width(), text_position[1])
        self.answer_input.set_pos(input_position[0], input_position[1])
        self.screen.blit(answer_text, text_position)
        self.answer_input.draw(self.screen)

    def draw_response(self, correct):
        font = pygame.font.SysFont(None, 32)
        if correct == True:
            text = font.render("Correct!", True, Colors.GREEN)
        elif correct == 2:
            text = font.render("Time's Up!", True, Colors.RED)
        else:
            text = font.render("Incorrect", True, Colors.RED)
        text_position = ((self.screen.get_width() // 2) - text.get_width() // 2,
                         self.screen.get_height() - (text.get_height() * 2))
        self.screen.blit(text, text_position)

    def generate_new(self):
        self.problem = SequenceProblem(1)
        self.answer_input = TextInput(True, self.problem.get_solution_length() + 1, pygame.font.SysFont(None, 32), Colors.DARK_GREEN)


class SequenceProblem:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        difficulty_mapping = {
            1: "+",
            2: "-",
            3: "*",
            4: "/"
        }
        operator = difficulty_mapping[self.translate_difficulty()]
        self.gen_simple(random.randint(0, 1), operator)

    def gen_simple(self, eqn_given, operator):
        increment = random.randint(1, 9)
        generate_equation = "x" + operator + str(increment)
        self.sequence = ""
        x = random.randint(1, 9)
        for i in range(0, 4):
            self.sequence += str(x) + ", "
            x = eval(generate_equation)
        if eqn_given:
            self.equation = "x " + operator + " " + str(increment)
            self.sequence = self.sequence + "?"
            self.solution = str(x)
        else:
            self.equation = "x " + operator + " ?"
            self.sequence = self.sequence[0:-2]
            self.solution = str(increment)

    def translate_difficulty(self):
        if self.difficulty < 6:
            return 1
        elif self.difficulty >= 6 or self.difficulty < 11:
            return 2
        elif self.difficulty >= 11 or self.difficulty < 16:
            return 3
        elif self.difficulty >= 16:
            return 4

    def get_sequence(self):
        return self.sequence

    def get_equation(self):
        return self.equation

    def is_correct(self, answer):
        return answer == self.solution

    def get_solution_length(self):
        return len(self.solution)


class TextInput:
    def __init__(self, only_numbers, max_length, font, text_color):
        self.only_numbers = only_numbers
        self.max_length = max_length
        self.font = font
        size = font.size("5" * max_length)
        self.width = size[0]
        self.height = size[1]
        self.x = 0
        self.y = 0
        self.color = text_color
        self.value = ""

    def update(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.value = self.value[:-1]
                if event.key == K_0: self.value += "0"
                elif event.key == K_1 or event.key == K_KP0: self.value += "1"
                elif event.key == K_2 or event.key == K_KP1: self.value += "2"
                elif event.key == K_3 or event.key == K_KP2: self.value += "3"
                elif event.key == K_4 or event.key == K_KP4: self.value += "4"
                elif event.key == K_5 or event.key == K_KP5: self.value += "5"
                elif event.key == K_6 or event.key == K_KP6: self.value += "6"
                elif event.key == K_7 or event.key == K_KP7: self.value += "7"
                elif event.key == K_8 or event.key == K_KP8: self.value += "8"
                elif event.key == K_9 or event.key == K_KP9: self.value += "9"
        if len(self.value) > self.max_length and self.max_length >= 0:
            self.value = self.value[:-1]

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_color(self, text_color):
        self.color = text_color

    def draw(self, surface):
        text = self.font.render(self.value, True, self.color)
        surface.blit(text, (self.x, self.y))

    def get_value(self):
        return self.value


def main():
    pygame.display.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game = SequenceGame(screen, clock)
    game.start()

main()
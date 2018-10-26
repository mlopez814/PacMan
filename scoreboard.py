import pygame.font
from pygame.sprite import Group

from player import Player


# noinspection SpellCheckingInspection,PyAttributeOutsideInit
class Scoreboard:
    def __init__(self, settings, screen, stats, maze, play_button):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = settings
        self.maze = maze
        self.stats = stats

        self.button = play_button

        self.scores = []

        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.get_scores()

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives(self.settings, self.screen, self.stats, self.maze)

    def prep_score(self):
        score_str = "Score: {:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

    def prep_high_score(self):
        high_score_str = "High score: {:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        current_level = self.stats.level
        current_level_str = "Level: {:,}".format(current_level)
        self.level_image = self.font.render(current_level_str, True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_lives(self, settings, screen, stats, maze):
        self.lives = Group()

        for lives_number in range(stats.pacman_lives):
            life = Player(settings, screen, stats, self, maze)
            life.rect.centerx = (self.screen_rect.left + 45) + (lives_number * 45)
            life.rect.centery = self.screen_rect.bottom - 100
            self.lives.add(life)

    def get_scores(self):
        with open('images/highscores.txt', 'r+') as f:
            self.rows = f.readlines()
        self.fill()
        self.stats.high_score = int(self.scores[0])

    def fill(self):
        for nrow in range(len(self.rows)):
            temp_score = self.rows[nrow]
            self.scores.append(temp_score)

    def prep_list(self):
        self.title_image = self.font.render("High Scores", True, self.text_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - 175

        self.one_image = self.font.render("1. {:s}".format(self.scores[0]), True, self.text_color)
        self.one_image_rect = self.one_image.get_rect()
        self.one_image_rect.centerx = self.screen_rect.centerx
        self.one_image_rect.centery = self.screen_rect.centery - 125

        self.two_image = self.font.render("2. {:s}".format(self.scores[1]), True, self.text_color)
        self.two_image_rect = self.two_image.get_rect()
        self.two_image_rect.centerx = self.screen_rect.centerx
        self.two_image_rect.centery = self.screen_rect.centery - 75

        self.three_image = self.font.render("3. {:s}".format(self.scores[2]), True, self.text_color)
        self.three_image_rect = self.three_image.get_rect()
        self.three_image_rect.centerx = self.screen_rect.centerx
        self.three_image_rect.centery = self.screen_rect.centery - 25

        self.four_image = self.font.render("4. {:s}".format(self.scores[3]), True, self.text_color)
        self.four_image_rect = self.four_image.get_rect()
        self.four_image_rect.centerx = self.screen_rect.centerx
        self.four_image_rect.centery = self.screen_rect.centery + 25

        self.five_image = self.font.render("5. {:s}".format(self.scores[4]), True, self.text_color)
        self.five_image_rect = self.five_image.get_rect()
        self.five_image_rect.centerx = self.screen_rect.centerx
        self.five_image_rect.centery = self.screen_rect.centery + 75

        self.button.draw_button()

    def display_list(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.one_image, self.one_image_rect)
        self.screen.blit(self.two_image, self.two_image_rect)
        self.screen.blit(self.three_image, self.three_image_rect)
        self.screen.blit(self.four_image, self.four_image_rect)
        self.screen.blit(self.five_image, self.five_image_rect)

    def check_leaderboard(self):
        for gstats in range(5):
            if self.stats.score > int(self.scores[gstats]):
                self.scores[gstats] = str(self.stats.score)

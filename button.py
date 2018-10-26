import pygame.font


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Button:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx - 100
        self.rect.centery = self.screen_rect.centery + 200

        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2.centerx = self.screen_rect.centerx + 100
        self.rect2.centery = self.screen_rect.centery + 200

        self.prep_msg("play", "highscores")

    def prep_msg(self, msg, msg2):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.msg_image2 = self.font.render(msg2, True, self.text_color)
        self.msg_image2_rect = self.msg_image2.get_rect()
        self.msg_image2_rect.center = self.rect2.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.fill(self.button_color, self.rect2)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)

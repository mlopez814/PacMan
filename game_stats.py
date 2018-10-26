class Stats:

    def __init__(self, settings):
        self.reset_stats(settings)

        self.game_active = False
        self.HS_active = False

        self.high_score = 0

        self.dots_clear = False
        self.DOTS_CLEAR = False

        self.BEAST_MODE = False

    # noinspection PyAttributeOutsideInit
    def reset_stats(self, settings):
        self.pacman_lives = settings.lives
        self.score = 0
        self.level = 1

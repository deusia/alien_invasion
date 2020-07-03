class GameStats():
    """记录Alien Invasion统计数据的类"""

    def __init__(self, ai_settings):
        """初始化游戏静态设置"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏进入启动
        self.game_active = False

        # 最高分数不能被重置
        self.high_score = 0

    def reset_stats(self):
        """"初始化能在游戏中改变的静态设置"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

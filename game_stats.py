class GameStats():
	"""Отслеживание статистики для игры Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Инициализирует статистику."""
		self.ai_settings = ai_settings
		# Рекорд не должен сбрасываться.
		with open('history_record.txt') as f_obj:
			hc = f_obj.read()
		self.high_score = int(hc)
		self.reset_stats()
		# Игра Alien Invasion запускается в неактивном состоянии.
		self.game_active = False
				
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

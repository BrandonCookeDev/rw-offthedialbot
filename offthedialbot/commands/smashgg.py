from smashggpy import Tournament

class smashgg_commands(object)
	
	@staticmethod
	def get_tournament(slug: str) -> Tournament:
		tourney = Tournament.get(slug)
		return tourney

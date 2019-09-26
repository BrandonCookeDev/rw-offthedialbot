import discord

from commands.smashgg import smashgg_commands


class Bot(object):

	# this is a singleton instance. Only one instance of your bot should exist at a time
	# this static variable will hold the bot
	__instance = None


	@staticmethod
	def init_singleton(api_key: str) -> None:
		# if our singleton instance isn't set, initialize it and set
		if Bot.__instance is None:

			# make connection to discord 
			bot = discord.make_connection(api_key)

			# set the singleton instance 
			Bot.__instance = bot


	@staticmethod
	def get_singleton():
		if Bot.__instance is not None:
			return Bot.__instance
		else 
			raise Exception('bot singleton not initialized')


	@staticmethod
	def parse(incoming_message: object) -> None:

		# check if the message is a bot command
		if incoming_message[0] is '!':

			# seperate the command from any parameters given
			split = incoming_message[1:].split(' ')
			command = split[0]
			params = split[1:]


			# process the tournament command if present
			if command is 'tournament':

				# validate the user gave us a slug
				if len(params) <= 0:
					raise Exception('!tournament command must have a slug included!')

				# call the static method to get a tournament with slug
				the_slug = params[0]
				the_tournament = smashgg_commands.get_tournament(the_slug)

				# return data to your user by replying to them as the bot instance
				Bot.get_instance().reply(str(the_tournament))


if __name__ == '__main__':

	# initialize the singleton
	my_bot = Bot.init_singleton('your api key')

	# register parse as the function to run on a new message
	my_bot.on_message(Bot.parse)

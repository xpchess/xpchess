from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep
import random


class NetClientChannel(Channel):

	def __init__(self, *args, **kwargs):
		Channel.__init__(self, *args, **kwargs)
		self.game = None

	def Network(self, data):
		pass

	def Close(self):
		print("Client disconnected")

	def Error(self, error):
		print("Error:", error)

	def Network_klik(self, data):
		x, y = data['x'], data['y']
		self.game.klik(x, y)



class NetServer(Server):

	channelClass = NetClientChannel

	def __init__(self, game, *args, **kwargs):
		Server.__init__(self, *args, **kwargs)
		self.game = game
		self.client = None
		self.my_color = ['White', 'Black'][random.randint(0, 1)]
		self.game_started = False
		print('Server launched')

	def Connected(self, channel, addr):
		if self.client != None:
			channel.close()
			print('New connection closed (too many clients connected)')
			return
		self.client = channel
		self.client.game = self.game
		print('New connection:', addr)
		self.client.Send({'action': 'game_started', 'color': 'White' if self.my_color == 'Black' else 'Black'})
		self.game_started = True

	def update(self):
		self.Pump()

	def send_klik(self, x, y):
		self.client.Send({'action': 'klik', 'x': x, 'y': y})


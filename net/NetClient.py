from PodSixNet.Connection import connection, ConnectionListener
from time import sleep


class NetClient(ConnectionListener):
	def __init__(self, game, localaddr):
		self.game = game
		self.game_started = False
		self.Connect(localaddr)
		# connection.Send({'action': 'pohni',
						 # 'c1': (0,1),
						 # 'c2': (0,2)})

	def Network_connected(self, data):
		print('You are now connected to the server')
	
	def Network_error(self, error):
		print("error:", error)
		connection.Close()

	def Network_disconnected(self, data):
		print('Server disconnected')
		print(data)
		exit()

	def update(self):
		connection.Pump()
		self.Pump()

	def Network_game_started(self, data):
		self.my_color = data['color']
		self.game_started = True

	def Network_klik(self, data):
		x, y = data['x'], data['y']
		self.game.klik(x, y)

	def send_klik(self, x, y):
		connection.Send({'action': 'klik', 'x': x, 'y': y})



# connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)
# connection.DoConnect()
# connection.Send({"action": "myaction", "blah": 123, "things": [3, 4, 3, 4, 7]})
# while True:
# 	connection.Pump()

# client = NetClient()
# while True:
# 	client.update()

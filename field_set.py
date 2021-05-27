from random import random

from piper import Piper

# Initialize before launching Rocket League
class FieldSet():
	def __init__(self):
		self.piper = Piper()
		print('Waiting for pipe connection...')
		self.piper.open_pipe()
		print('Pipe connected.')

	def set_ball_state(self, position=[0, 0, 0], velocity=[0, 0, 0]):
		ball_state = position + velocity
		str_ball_state = " ".join(ball_state)
		self.piper.write_pipe(str_ball_state)

	def randomize_ball_state(self):
		position = [str(random() * 8000 - 4000) for _ in range(3)]
		velocity = [str(random() * 8000 - 4000) for _ in range(3)]
		self.set_ball_state(position, velocity)

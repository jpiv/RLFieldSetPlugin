import time

from field_set import FieldSet

if __name__ == '__main__':
	field_set = FieldSet()
	while True:
		field_set.randomize_ball_state()
		time.sleep(3)
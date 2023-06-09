class Baterry():
	def __init__(self, battery_size=70):
		self.battery_size = baterry_size
	
	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + 'Kwh battery.')
	
	def atualiza_bateria(self):
		if self.battery_size != 85:
			self.baterry_size = 85
	
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 80:
			range = 270
			
		message = 'This car can go approximately ' + str(range) + 'miles on a full charge'
		print(message)

tesla = Battery()

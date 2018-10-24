"""

CAR LOOKUP SERVICE - Separated into separate retrieve requests for synchronization


"""
makesList = ["Toyota"]

class Model:
	model = "N/A"
	def __init__(self, model):
		self.model = model
	"""add API stuff here"""

class Year:
	year = 0 
	"""tester condition"""
	def __init__(self, year):
		self.year = year
	"""add API stuff here"""

class Make:
	make = "N/A"
	def __init__(self, make):
		self.make = make
	"""add API stuff here"""

class Car:
	def __init__(self, make, model, year):
		Make(make)
		Model(model)
		Year(year)
		self.year = year
		self.model = model
		self.make = make
		self.info = [year, make, model]

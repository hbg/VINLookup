"""

CAR LOOKUP SERVICE - Separated into separate retrieve requests for synchronization


"""
import datetime

makesList = [ "AMC", "Acura", "Alfa Romeo", "Anadol", "Aston Martin", "Audi", "Avanti", "BMW", "Bentley", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dacia", "Daewoo", "Daihatsu", "Datsun", "DeLorean", "Dodge", "Eagle", "FIAT", "Ferrari", "Fisker", "Ford", "Freightliner", "GMC", "Geely", "Geo", "HUMMER", "Honda", "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Jeep", "Kia", "Lamborghini", "Lancia", "Land Rover", "Lexus", "Lincoln", "Lotus", "MG", "MINI", "Maserati", "Maybach", "Mazda", "McLaren", "Mercedes-Benz", "Mercury", "Merkur", "Mitsubishi", "Nissan", "Oldsmobile", "Opel", "Peugeot", "Plymouth", "Pontiac", "Porsche", "Proton", "RAM", "Renault", "Rolls-Royce", "Rover", "SRT", "Saab", "Saturn", "Scion", "Skoda", "Sterling", "Subaru", "Suzuki", "Tesla", "Tofaş", "Toyota", "Triumph", "Volkswagen", "Volvo", "Yugo", "smart",];

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
		self.info = {}
		self.info["year"] = year
		self.info["model"] = model
		self.info["make"] = make
		self.info["dateSnap"] = datetime.datetime.utcnow()


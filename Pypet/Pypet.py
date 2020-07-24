class Pypet:
	def __init__(self, name, age, weight, photo):
		self.hungry = True
		self.bored = True
		self.name = name
		self.age = age
		self.weight = weight
		self.photo = photo

	def speak(self):
		print("Hello, my name is " + self.name + " and I look like this: " + self.photo)
		if self.hungry:
			print("I am hungry")
		if self.bored:
			print("I am bored")
		if not self.hungry and not self.bored:
			print("I am happy")

	def feed(self):
		self.hungry = False
		self.weight += 0.1

	def play(self):
		self.bored = False

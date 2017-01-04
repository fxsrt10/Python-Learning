from random import randint

def roll():
	print("Rolling Dice")
	print(randint(1,6))

print("Welcome to the roller 5000")
char = input("Wanna roll? Type r for yes ")

while(char == 'r'):
	roll()
	char = input("Wanna (r)oll again?")

sys.exit("Exited")



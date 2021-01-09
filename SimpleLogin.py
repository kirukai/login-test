user = ()

def screen():
	prompt = input("Are you registered? Y/N\n")
	if prompt == 'n':
		prompt2 = input("Do you want to make an account? Y/N\n")
		if prompt2 == 'y':
			register()
		elif prompt2 == 'n':
			screen()
	elif prompt == 'y':
		login()
	elif prompt == 'm':
		call_the_list()

def login():
	username = input("Enter username: ")
	password = input("Enter password: ")
	if username and password in user:
		print("Congratulations in logging in...")
		screen()
	else:
		print("Are you sure you are registered?")
		screen()

def register():
	username = user.append(input("Enter username: "))
	password = user.append(input("Enter password: "))
	if username and password in user:
		print("The given input is IN the database")
		register()
	else:
		print("Creation of account is successful")
		screen()

def call_the_list():
	print(user)

screen()
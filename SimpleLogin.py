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
	p6 = input("Enter username: ")
	p7 = input("Enter password: ")
	if p6 and p7 in user:
		print("Congratulations in logging in...")
		screen()
	else:
		print("Are you sure you are registered?")
		screen()

def register():
	p3 = user.append(input("Enter username: "))
	p4 = user.append(input("Enter password: "))
	if p3 and p4 in user:
		print("The given input is IN the database")
		register()
	else:
		print("Creation of account is successful")
		screen()

def call_the_list():
	print(user)

screen()
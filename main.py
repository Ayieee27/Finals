from utils.user_manager import UserManager
usermanager = UserManager()

def start():
	while True:
		choice = int(input("\nWelcome to Dice Roll Game!\n1.Register\n2.Login\n3.Exit\nEnter here: "))
		if choice == 1:
			usermanager.register()
		elif choice == 2:
			if usermanager.count_of_account == 0:
				print("Please register first.")
			else:
				usermanager.login()
		elif choice == 3:
			print("Thank you!")
			exit()
		else:
			print("Invalid choice. Please try again.")

start()
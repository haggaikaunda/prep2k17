version = "1.0"

from cdma import *

CODE_LENGTH = 8

codes = hadamard(CODE_LENGTH).tolist()

def main():
	print(f"welcome to CDMA version {version}\n")
	action = get_input("Hello there, would you like to encrypt a message or decrypt one? [d/e]")
	if action == "d":
		do_decryption()
	elif action == "e":
		do_encryption()
	elif action == "q":
		print("quitting cdma, thanks for visiting!.")
		return 
	else:
		print(f"{action} is not a valid option.\nEnter e to encrypt a message and d to decrypt a message.\n\nLets start over.")
	main()
	

	# FIXME
	return


def do_encryption():

	name = get_input("\nwho would you like to send a message to?")
	msg = get_input("\nenter the message you would like to send")

	# code = codes[0].tolist

	receiver = Person(name, message = msg)

	print(f"your message to {receiver.name} says : {receiver.message}\n")

	print(f"encrypting the message to {receiver.name}\n")
	receiver.code = codes[1]


	encrypted_msg = encrypt(receiver.get_message(), receiver.get_code())
	encrypted_msg.append(len(receiver.get_message()))

	with open('out.txt', 'w') as out:
		out.write(str(encrypted_msg))
	
	print(f"the encrypted message to {receiver.name} is {encrypted_msg}")

	main()


def do_decryption():

	encrypted_msg = ""
	sender = get_input("\nWho are you receiving the message from?")

	if get_input("\nIs the encrypted message in out.txt? [y/n]") == "y":
		with open('out.txt', 'r') as input_file:
			encrypted_msg = input_file.read()

			print(f"The encrypted msg is: \n{encrypted_msg}\n")
	else: 
		encrypted_msg = get_input("\nEnter the encrypted message you received")

	encrypted_msg_list = encrypted_msgtolist(encrypted_msg)



	print(f"decoding message from {sender}\n")

	decrypted_msg = decrypt(encrypted_msg_list, codes[1])

	print(f"your decrypted message from {sender} says: {decrypted_msg}\n")

	main()
	# FIXME
    # decrypt a message from the user.


def get_input(screen_message):
	return input(f"{screen_message} : ")

if __name__ == "__main__":
	main()

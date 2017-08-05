from util import *
from scipy.linalg import hadamard

version = "1.0"

#your name goes here. 
myName = "Athina"

members = ["Haggai", "Athina", "Aliki", "Leticia", "Dimitris", "Eleni", "Iraklis"]
codes = dict()

def main():
    
    action = get_input("Note: enter quit to exit the cdma.\nWould you like to encrypt/decrypt a message? [e/d]").lower()

    if action == "quit":
        print("Good bye, thanks for visiting. ")

    elif action == "e":
        do_encrypt()
    elif action == "d":
        do_decrypt()
    else:
        print(f"{action} is not a valid option.\nThe valid options are:\nquit => to exit cdma\ne => to encrypt a message\nd => to decrypt a message\n\nLets start over.")
        main()
    return

def do_encrypt():
    messages = dict()
    longest_msg = 0

    def get_messages(num):
            msg = get_input("Enter the message you would like to send")
    def update_lngst_msg(n):
       nonlocal longest_msg
       longest_msg = n
        
    num_msgs = int(get_input("How many messages would you like to send"))
    

    counter = 1
    while counter <= num_msgs:

        flag = True

        while flag:
            name = get_input(f"Message # {counter}.\nWho would you like to send this message to?")

            if not name in members:
                print(f"I don't have {name} registered in my members list. Please enter one of the following names\n{members}\n")
            else:
                flag = False


            msg = get_input("\nEnter the message you would like to send")

            messages[name] = msg

            if len(msg) > longest_msg:
                update_lngst_msg(len(msg))
            
            counter += 1

    print("Encrypting your messages. Hold on tight.\n")

    #add "r"*diff[msg] to each message to make them the same length.
    aggregated_msgs = []

    for name in messages.keys():
        msg = messages[name]
        diff = longest_msg - len(msg) 

        #add ";"*diff[msg] to each message to make them the same length.
        msg += " "*diff

        encrypted_msg = encrypt(msg, codes[name])

        #len of orignal message is used in decode_message function.
        encrypted_msg.append(longest_msg)

        #diff will be used to know how many carracters to remove from a message during decryption.
        #encrypted_msg.append(diff)
        
        aggregated_msgs = add_lists(encrypted_msg, aggregated_msgs)

    with open('out.txt', 'w') as out:
        out.write(str(aggregated_msgs))

    print("Your encrypted message has been written to out.txt\n")
    print(f"But here it is for your viewing pleasure : \n{aggregated_msgs}\n")

    main()


def do_decrypt():

    encrypted_msg, name = "", ""

    #get the name of the sender. Sender must be in members. 
    flag = True
    while flag:
            sender = get_input(f"\nWho are you receiving your message from?")

            if not sender in members:
                print(f"I don't have {name} registered in my members list. Please enter one of the following names\n{members}\n")
            else:
                flag = False

    #ask where to find encrypted msg.
    if get_input("\nIs the encrypted message in out.txt? [y/n]") == "y":
        with open('out.txt', 'r') as input_file:
            encrypted_msg = input_file.read()

            #print(f"The encrypted msg is: \n{encrypted_msg}\n")
    else: 
        encrypted_msg = get_input("\nEnter the encrypted message you received")

    encrypted_msg_list = encrypted_msgtolist(encrypted_msg) 

    #get extra carracters to original message.
    #extra = int(encrypted_msg_list.pop())



    print(f"decoding message from {sender}\n")

    decrypted_msg = decrypt(encrypted_msg_list, codes[sender])

    
    original_msg = decrypted_msg.rstrip()

    print(f"your decrypted message from {sender} says: {original_msg}\n")

    main()
    return





def get_input(screen_message):
    return input(f"{screen_message} : ")

def initialize_cdma(n = len(members)):

    from scipy.linalg import hadamard

    code_list = hadamard(n) if is_power_of_two(n) else hadamard(closest_power_of_two(n))
    code_list = code_list.tolist()

    for index, name in enumerate(members):
        codes[name] = code_list[index]







class Person:
    def __init__(self, name, code=None, message=None):
        self.name = name
        self.code = code
        self.message = message

    def get_code(self):
        return self.code if self.code is not None else self.name + " has " \
            "no code yet."

    def get_message(self):
        return self.message if self.message is not None else self.name \
                + " has no message yet."









if __name__ == "__main__":
    print(f"\nHello {myName}, welcome to Code Division Multiple Access (CDMA) version {version}.\n")
    initialize_cdma(len(members))
    main()
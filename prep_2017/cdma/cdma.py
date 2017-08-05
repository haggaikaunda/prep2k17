from util import *
from scipy.linalg import hadamard

version = "1.0"

#your name goes here. 
myName = "Athina"

members = ["Haggai", "Athina", "Aliki", "Leticia", "Dimitris", "Eleni", "Iraklis"]
codes = dict()

def main():
    
    action = get_input("Note: enter quit to exit the cdma.\nWould you like to "
     + "encrypt/decrypt a message? [e/d]").lower()

    if action == "quit":
        print("\nGood bye, thanks for visiting.\n")

    elif action == "e":
        do_encrypt()
    elif action == "d":
        do_decrypt()
    else:
        print(f"{action} is not a valid option.\nThe valid options are:\nquit => to "
            + "exit cdma\ne => to encrypt a message\nd => to decrypt a message\n\nLets start over.")
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
        
    num_msgs = int(get_input("\nHow many messages would you like to send"))
    

    counter = 1
    while counter <= num_msgs:

        name = get_name(f"\nMessage # {counter}.\nWho would you like to send"
             + " this message to?")

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
        
        aggregated_msgs = add_lists(encrypted_msg, aggregated_msgs)

    with open('encoded.txt', 'w') as out:
        out.write(str(aggregated_msgs))

    print("Your encrypted message has been written to encoded.txt\n")

    main()


def do_decrypt():

    encrypted_msg = ""

    #get the name of the sender. Sender must be in members.
    name = get_name(f"\nWho are you receiving your message from?") 

    #ask where to find encrypted msg.
    if get_input("\nIs the encrypted message in encoded.txt? [y/n]") == "y":
        with open('encoded.txt', 'r') as encoded_file:
            encrypted_msg = encoded_file.read()

            #print(f"The encrypted msg is: \n{encrypted_msg}\n")
    else: 
        encrypted_msg = get_input("\nEnter the encrypted message you received")

    encrypted_msg_list = encrypted_msgtolist(encrypted_msg) 

    print(f"decoding message from {name}\n")

    #Change this to [name] to decrypt messages from anyone.
    decrypted_msg = decrypt(encrypted_msg_list, codes[myName])

    
    original_msg = decrypted_msg.rstrip()

    with open('decoded.txt', 'w') as decoded_msg:
        decoded_msg.write(str(original_msg))

    print(f"your decrypted message from {name} has been written to decoded.txt.\n")

    main()
    return


def get_name(screen_msg):
    """get name."""
    flag = True
    while flag:
            name = get_input(screen_msg)

            if not name in members:
                print(f"I don't have {name} registered in my members list."
                    + " Please enter one of the following names\n{members}\n")
            else:
                flag = False

    return name

def get_input(screen_message):
    """Present SCREEN_MESSAGE to the user and wait for input."""
    return input(f"{screen_message} : ")

def initialize_cdma(n = len(members)):
    """Initialize_cdma program and assign codes to each name in members."""

    from scipy.linalg import hadamard

    code_list = hadamard(n) if is_power_of_two(n) else hadamard(closest_power_of_two(n))
    code_list = code_list.tolist()

    for index, name in enumerate(members):
        codes[name] = code_list[index]


if __name__ == "__main__":
    print(f"\nHello {myName}, welcome to Code Division Multiple Access (CDMA) version {version}.\n")
    initialize_cdma(len(members))
    main()
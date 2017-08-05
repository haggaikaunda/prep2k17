#Utility functions used by cdma to encrypt and decrypt Messages.
#@author: Haggai Kaunda


def upsample(message, n):
    """Return a new list that has each element of MESSAGE repeated N times."""

    result = []

    #begin Question 2

    #Your code goes here.

    #end question 2
    return result



def extend_code(code, msg_length):
    """Return a new list that has the elements of CODE repeated N times, while
    preserving order."""

    n = msg_length

    result = []
    for _ in range(n):
        result = result + code
    return result


def multiply_lists(lst1, lst2):
    """multipy two lists and return the result."""
    pairs = zip(lst1, lst2)
    return [x * y for x, y in pairs]

def add_lists(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1

    pairs = zip(lst1, lst2)
    return [x + y for x, y in pairs]


def encode_message(message, code):
    sampled_msg = upsample(message, len(code))
    extended_code = extend_code(code, len(message))

    encoded_msg = multiply_lists(sampled_msg, extended_code)

    return encoded_msg


def decode_message(received_msg, code, code_length):

    #get message length so you know how long to extend the code. 
    msg_length = received_msg.pop()

    recovery_code = extend_code(code, msg_length)

    code_len = code_length
    demod = multiply_lists(received_msg, recovery_code)
    result, length = [], len(demod)

    while length > 0:
        temp = demod[length - code_len:length]
        result.insert(0, sum(temp)/len(temp))
        length -= code_len
    return result


def msg_tostring(recovered_message):
    true_msg = ""
    for num in recovered_message:
        true_msg += chr(int(num))

    return true_msg


def msg_tolist(string_msg):
    return [ord(letter) for letter in string_msg]

def encrypt(message, code):
    """
    :param message: list of numbers
    :param code: type = list
    :return: list of an encrypted message.
    """
    msg = msg_tolist(message)
    return encode_message(msg, code)


def decrypt(message, code):
    msg = decode_message(message, code, len(code))
    return msg_tostring(msg)


def encrypted_msgtolist(encrypted_msg):
    assert encrypted_msg.startswith("[")
    assert encrypted_msg.endswith("]")

    encrypted_msg = encrypted_msg.replace(" ", "").replace("[", "").replace("]", "")

    encrypted_lst = encrypted_msg.split(",")

    return [int(elem) for elem in encrypted_lst]

def is_power_of_two(num):
    return num > 0 and not (num & (num - 1))

def closest_power_of_two(num):
    power = 1
    while power < num:
        power *= 2
    return power

if __name__ == "__main__":
    msg = str([x for x in range(10)])
    x = encrypted_msgtolist(msg)
    print(x)
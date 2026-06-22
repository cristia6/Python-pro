import random

def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def caraoucoroa():
    return random.choice(["cara", "coroa"])

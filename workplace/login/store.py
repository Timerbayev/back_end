import random

lst = [i for i in 'abcdefghijklmnopqrstuvwxyz1234567890']


def generate_long_random_key():
    password = [random.choice(lst) for _ in range(10)]
    return ''.join(password)


if __name__ == "__main__":
    generate_long_random_key()

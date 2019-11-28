MINIMUM_LENGTH = 1


def main():
    """Get a password of valid size and print asterisks."""
    password = input("Enter password of at least {} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ")

    print(password[1::2])


main()


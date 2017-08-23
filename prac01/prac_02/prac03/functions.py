def main():

    get_name()


def get_name():
    name = input("please enter you're name: ")
    while not name:
        name = input("please enter you're name: ")
    print_name(name)


def print_name(name):
    print(name[::2])


main()


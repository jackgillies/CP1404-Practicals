outFile = open("name.txt", "w")
name = input("What is your name?: ")
outFile.write(name)
outFile.close()

name_read_file = open("name.txt", 'r')
name = name_read_file.read()
print("you're name is: ", name)
name_read_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

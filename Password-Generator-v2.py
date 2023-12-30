import itertools

alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "%", "\\", "|", "=", "[", "]", "<", ">", "{", "}", "@", "#", "$", "_", "&", "-", "+", "(", ")", "*", '"', "'", ":", ";", "!", "?", ",", ".", "-", "~", "^"]

def generate_passwords(length):
    print(len(alphaList) ** length)
    file_name = input("Enter name of file to be created (without extension): ") + ".txt"
    
    with open(file_name, "w") as f:
        for combination in itertools.product(alphaList, repeat=length):
            password = "".join(combination)
            f.write(password + "\n")

if __name__ == "__main__":
    try:
        length = int(input("Enter the number of characters passwords must be (maximum - 20): "))
        if 1 <= length <= 20:
            generate_passwords(length)
        else:
            print("Invalid Input...\nLength should be between 1 and 20.")
    except ValueError:
        print("Invalid Input...\nLength should be a valid integer.")

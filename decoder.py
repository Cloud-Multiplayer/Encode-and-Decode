# Elijah De Guzman
# encodes data to each number being +3
def encode(data):
    out = ""
    for char in data:
        out += str(int(char) + 3)
    return out
if __name__ == "__main__":
    while(True):
        # menu
        print("0. Exit\n1. Encode\n2. Decode\n")
        menu = input("Enter your choice: ")
        if menu == "0":
            break
        elif menu == "1":
            data = input("Enter data to encode: ")
            print(encode(data))
        elif menu == "2":
            data = input("Enter data to decode: ")
            # print(decode(data))
        else:
            print("Invalid input")
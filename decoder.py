# Elijah De Guzman
# encodes data to each number being +3
def encode(data):
    out = ""
    for char in data:
        if(int(char) > 6):
            out += str(3 - (10-int(char)))
        else:
            out += str(int(char) + 3)
    return out


#Tom Bemben decode function
def decode(data):
    result = ''
    temp_array = []

    for i in range(len(data)): #splits string into integers subtracts 3
        temp_array.append(int(data[i]))


    for j in range(len(temp_array)): #creates string character following rollover digit rules
        if (temp_array[j] - 3) < 0:
            result += str(temp_array[j] + 7)
        else:
            result += str(temp_array[j] - 3)

    return result

if __name__ == "__main__":
    while(True):
        # menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu = input("Please enter an option: ")
        if menu == "3":
            break
        elif menu == "1":
            data = input("Please enter your password to encode: ")
            encrypted = encode(data)
            print("Your password has been encoded and stored!")
        elif menu == "2":
            decrypted = decode(encrypted)
            print(f"The encoded password is {encrypted}, and the original password is {decrypted}.")
        else:
            print("Invalid input")
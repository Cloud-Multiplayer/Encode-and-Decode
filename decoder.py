# Elijah De Guzman
# encodes data to each number being +3
def encode(data):
    out = ""
    for char in data:
        out += str(int(char) + 3)
    return out


#Tom Bemben decode function
def decode(data):
    result = ''
    temp_array = []

    for i in range(len(data)): #splits string into integers subtracts 3
        temp_array.append(int(data[i] - 3))


    for j in range(len(temp_array)): #creates string character following rollover digit rules
        if temp_array[j] < 0:
            result += str(temp_array[j] + 10)
        else:
            result += str(temp_array[j])



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

def mutate_string():

    string = input()
    data = input().split()

    position = int(data[0])
    character = data[1]

    string_list = list(string)
    string_list[position] = character

    modified_string = ""

    for ch in string_list:
        modified_string = modified_string + ch

    return modified_string

if __name__ == "__main__":

    result = mutate_string()

    print(result)
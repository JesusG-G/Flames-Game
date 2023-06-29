def total_of_character(list_1, list_2):
    total = len(list_1) + len(list_2)
    return total 

def remove_match_character(name_1_list,name_2_list):

    name_1_set =set(name_1_list)
    name_2_set =set(name_2_list)
    intersection_of_sets = name_1_set.intersection(name_2_set)
    new_list_1 = [character for character in name_1_list if character not in intersection_of_sets]
    new_list_2 = [character for character in name_2_list if character not in intersection_of_sets]
    total_of_character(new_list_1)
    print(new_list_1)
    print(new_list_2)
    print(intersection_of_sets)

if __name__ == "__main__":
    procced = True
    print("FLAMES GAME")
    print("Please introduce your name")
    name_1 = input("First player introduce your name: ").lower()
    name_2 = input("Second player introduce your name: ").lower()
    name_1_list = [character for character in name_1]
    name_2_list = [character for character in name_2]

    remove_match_character(name_1_list, name_2_list)
    """ while procced:

        result = remove_match_character(name_1_list,name_2_list)
        concatenate_list = result[0]
        procced = result[1]
        start_index = concatenate_list.index("*")
        name_1_list = concatenate_list[:start_index]
        name_2_list = concatenate_list[start_index+1:]

    print(name_1_list)
    print(name_2_list)
    print(result) """
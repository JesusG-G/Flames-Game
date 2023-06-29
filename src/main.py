def total_of_character(list_1, list_2):
    total = len(list_1) + len(list_2)
    return total 

def remove_match_character(name_1_list,name_2_list):
    name_1_set =set(name_1_list)
    name_2_set =set(name_2_list)
    intersection_of_sets = name_1_set.intersection(name_2_set)
    
    new_list_1 = [character for character in name_1_list if character not in intersection_of_sets]
    new_list_2 = [character for character in name_2_list if character not in intersection_of_sets]
    return new_list_1, new_list_2

if __name__ == "__main__":
    procced = True
    print("FLAMES GAME")
    print("""
    FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. 
    This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.
    """)
    print("*"*20)
    print("Please introduce your name")
    name_1 = input("First player introduce your name: ").lower()
    name_2 = input("Second player introduce your name: ").lower()
    
    name_1_list = [character for character in name_1]
    name_2_list = [character for character in name_2]

    new_list_1, new_list_2 = remove_match_character(name_1_list,name_2_list)
    total_character = total_of_character(new_list_1,new_list_2)

    list_flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(list_flames) > 1:
        split_index = (total_character % len(list_flames) - 1)
        if split_index >= 0:
            right = list_flames[split_index + 1:]
            left = list_flames[: split_index]
            list_flames = right + left
        else:
            list_flames = list_flames[: len(list_flames) - 1]
    print("*"*20)
    print(f"Relationship status: {list_flames[0]}")
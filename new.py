user_string = "dog and cat"

def capitalizer(string):
    #need empty place for char in string until we hit a space. resets when hit space.
    temp_string = ""
    #empty list for each word, no spaces.
    temp_string_list = []
    for char in string:
        if char == " ":
            #add temp string to lists
            temp_string_list.append(temp_string)
            #zero out temp string
            temp_string = ""
        
        else:
            temp_string += char
    temp_string_list.append(temp_string)
    print(temp_string_list)

capitalizer(user_string)




from player import Player

print("Creating first player")
player_one = Player(100)
print(player_one.cash)
player_one.set_name()


print("Creating player two")
player_two = Player(300)
player_two.name = "Jim"
print(player_two.name)



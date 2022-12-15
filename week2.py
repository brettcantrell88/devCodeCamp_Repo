def add_two_numbers(number_one, number_two):
     result_1 = number_one + number_two
     return result_1

result_1 = add_two_numbers(10, 10)
print(result_1)

print()

first_name = "Brett "
last_name = "Cantrell"

full_name = first_name + last_name
print(full_name)

print()

soccer_team = "Junior"

for char in soccer_team:
    print(char)
    
print()

string_1 = input("Give me a word. ")

def len(string_1):
    counter = 0
    for i in string_1:
        counter += 1
    return counter    
if len(string_1)>=3:
    print("Thank you. ")
elif len(string_1)<=3:
    print("Give me a different word. ")




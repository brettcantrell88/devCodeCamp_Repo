word = ""

def reverser(word):
    reversed_word = ""
    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]
    return reversed_word

print(f"Hello backwards is: {reverser('Hello')}")

new_string = input(" ")
def cap_letters(my_string):
    result = ""
    previous_letter = " "
    for letter in my_string:
        if previous_letter == " ":
            result += letter.capitalize()
            previous_letter = letter
        else:
            previous_letter = letter
            result += letter
    print(result)
cap_letters(new_string)

string = input(" ")

def compress_string(my_string):
    results = ""
    count = 0
    previous_letter = my_string[0]
    for letter in my_string:
        if previous_letter == letter:
            count += 1
        else:
            results += previous_letter + str(count)
            previous_letter = letter
            count = 1
    results += previous_letter + str(count)
    print(results)

def new_compress_string(my_string):
    new_string = ""
    count = 0
    for i in range(len(my_string)-1):
        if my_string[i] == my_string[i+1]:
            count = count +1
        else:
            new_string = new_string + my_string[i+1] + str(count)
            count = 1
    new_string = new_string + my_string[i+1] + str(count)
    print(new_string)
        
compress_string(string)
new_compress_string(string)

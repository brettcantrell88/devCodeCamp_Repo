#As a developer, I want to make at least three commits with descriptive messages.

#As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

#As a user, I want a destination to be randomly selected for my day trip.

#As a user, I want a restaurant to be randomly selected for my day trip.

#As a user, I want a mode of transportation to be randomly selected for my day trip.

#As a user, I want a form of entertainment to be randomly selected for my day trip.

#As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#As a user, I want to display my completed trip in the console.

import random

print("Thank you for choosing us to help plan your upcoming trip.")

trip_destinations = ["Oklahoma City", "New York", "Miami"]
restaurant_type_for_trip = ["Italian", "Mexican", "Indian"]
transportation_for_trip = ["Bus", "Uber","Car Rental"]
entertainment_for_trip = ["Bar", "Movies", "Nght Club"]

def choice_generator(list):
    user_eval = True
    while user_eval == True:
        random_selection = random.choice(list)
        user_input = input(f"Do you like the choice of {random_selection}? Y/N ").lower()
        if user_input == "y":
            print(f"{random_selection} confirmed!")
            return random_selection
        elif user_input == "n":
            print("Sorry, we will choose another selection!")
user_chosen_destination = choice_generator(trip_destinations)
user_chosen_restaurant = choice_generator(restaurant_type_for_trip)
user_chosen_transportation = choice_generator(transportation_for_trip)
user_chosen_entertainment = choice_generator(entertainment_for_trip)
print(f"For your trip we have chosen {user_chosen_destination} for your city, {user_chosen_restaurant} for the type of restaurant for your trip, {user_chosen_transportation} for a way to get around the city and {user_chosen_entertainment} for something to do while you are in town. Have fun!")


# destination = random.choice(trip_destinations)
# restaurant = random.choice(restaurant_type_for_trip)
# transportation = random.choice(transportation_for_trip)
# entertainment = random.choice(entertainment_for_trip)

# day_trip = (f"For your trip, we have selected {destination} for your destination, {restaurant} as the best type of restaurant to eat at, {transportation} as the best way to travel around town, and {entertainment} as an activity for the day. Do you like our choices? ")

# print(day_trip)

# confirm_choice = input("Please enter yes/no to confirm these travel options. ")

# def new_dest(confirm_choice):  
#     while confirm_choice == "no":
#         destination = random.choice(trip_destinations)
#         confirm_choice = input(f"We are sorry that the previous option did not work for you. We have selected {destination} as another place to go. Does this work for you?")
#         if input == "yes":
#             trip_destinations.remove(destination)
#         else:
#             print(f"You have selected {destination} as the destination for your trip. ")
#     return trip_destinations
# new_dest(confirm_choice)

# def new_restaurant(confirm_choice):  
#     while confirm_choice == "no":
#         restaurant = random.choice(restaurant_type_for_trip)
#         confirm_choice = input(f"We are sorry that the previous option did not work for your. We have seleceted {restaurant} as another place to eat. Does this work for you? ")
#         if input == "yes":
#             restaurant.remove(restaurant_type_for_trip)
#         else:
#             print(f"You have selected {restaurant} as the best place to eat during your trip. ")
#     return restaurant_type_for_trip
# new_restaurant(confirm_choice)

# def new_trans(confirm_choice):  
#     while confirm_choice == "no":
#         transportation = random.choice(transportation_for_trip)
#         confirm_choice = input(f"We are sorry that the previous option did not work for your. We have seleceted {transportation} as the best way to travel. Does this work for you? ")
#         if input == "yes":
#             transportation.remove(transportation_for_trip)
#         else:
#             print(f"You have selected {transportation} as a way to get around. ")
#     return transportation_for_trip
# new_trans(confirm_choice)

# def new_entertainment(confirm_choice):  
#     while confirm_choice == "no":
#         entertainment = random.choice(entertainment_for_trip)
#         confirm_choice = input(f"We are sorry that the previous option did not work for your. We have seleceted {entertainment} as a fun activity to do. Does this work for you? ") 
#         if input == "yes":
#             entertainment.remove(entertainment_for_trip)
#         else:
#             print(f"You have selected {entertainment} as a fun activity for you to do while on your trip. ")
#     return entertainment_for_trip
# new_entertainment(confirm_choice)

# ending_message = (f"For your trip we have confirmed that you are going to travel to {destination}, the type of food you want to eat will be {restaurant}, you will have {transportation} and your nightly activity will be {entertainment}. Thank you.")
# print(ending_message)

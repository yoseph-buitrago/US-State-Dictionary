import random
states = {
    "California": [ 39000000, "Sacramento", "Los Angeles", "The Golden State" ],
    "New York": [ 8000000, "Albany", "New York City", "The Empire State" ],
    "Florida": [ 21000000, "Tallahassee", "Maiami", "The Sunshine State" ],
    "Alaska": [ 739795, "Juneau", "Anchorage", "The Last Frontier" ],
    "Hawaii": [ 1000000, "Honolulu", "Honolulu", "The Aloha State" ],
    "Tennessee": [ 7000000, "Nashville", "Nashville", "The Volunteer State" ],
    "Kentucky": [ 4000000, "Frankfort", "Louisville", "Bluegrass State" ],
    "Louisiana": [ 5000000, "Baton Rouge", "New Orleans", "Child of the Mississippi, Creole State, Bayou State, Sugar State, Sportsman's Paradise, and Pelican State" ],
    "Delaware": [ 961939, "Dover", "Wilmington", "The First State, The Diamond State, The Small Wonder, and Blue Hen State" ], 
    "Wyoming": [ 579315, "Cheyenne", "Cheyenne", "Equality State, Cowboy State, and Big Wyoming" ],
    "South Dakota": [ 869666, "Pierre", "Sioux Falls", "The Mount Rushmore State" ],
    "West Virginia": [ 2000000, "Charleston", "Charleston", "Mountain State" ],
    "Maryland": [ 6000000, "Annapolis", "Baltimore", "Old Line State, Free State, and Little America" ],
    "Wisconsin": [ 6000000, "Madison", "Milwaukee", "America's Dairyland and Badger State" ],
    "New Mexico": [ 2000000, "Santa Fe", "Albuquerque", "Land of Enchantment" ],
    "Maine": [ 1000000, "Augusta", "Portland", "The Pine Tree State" ], 
    "Iowa": [ 3000000, "Des Moines", "Des Moines", "The Hawkeye State" ],
    "Ohio": [ 12000000, "Colombus", "Colombus", "The Mother of Presidents, The Heart of it All, The Buckeye State, and Birthplace of Aviation" ],
    "New Jersey": [ 9000000, "Trenton", "Newark", "The Garden State" ],
    "Washington": [ 7000000,"Olympia", "Seattle", "The Evergreen State" ],
    "Georgia": [ 1000000, "Atlanta", "Atlanta", "Peach State and Empire State of the South" ],
    "Missouri": [ 6000000, "Jefferson City", "Saint Louis", "The Show-Me State" ],
    "Mississippi": [ 3000000, "Jackson", "Jackson", "The Magnolia State and the Hospitality State" ]

    }


def display_menu():
    print("Menu: \n",
          "1. Get US State Population (Rounded Up) \n",
          "2. Get US State Capitol \n",
          "3. Get What US State most populated city \n",
          "4. Get US State Nickname(s) \n",
          "5. Get All the Information of a Random State \n",
          "6. Get US Population" )

          
def user_choice():
    user_choice = int(input("Choose What Information List Do You Want To Learn About: "))
    while user_choice < 1 or user_choice > 6:
        user_choice = int(input("Choose What Information List You Want To Learn About: "))

    return user_choice

def get_state_population():

    state = str(input("Enter a US State to get the population: "))

    for key in states:
        if key == state:
            print("The population in", state, "is:", states[key][0])


def get_state_capitol():

    state = str(input("Enter a US State to get the State Capitol: "))

    for key in states:
        if key == state:
            print("The Capitol of",state,"is:",states[key][1])
  
def get_state_populated_city():

    state = str(input("Enter a US State to get its Most Populated City: "))

    for key in states: 
        if key == state:
            print("The Most Populated City in",state,"is:",states[key][2])
            

def get_state_nickname():

    state = str(input("Enter a US State to get its State Nickname(s): "))

    for key in states:
        if key == state:
            print("The State Nickname(s) of",state,"is/are:",states[key][3])

def get_random_info():
    print(random.choice(list(states.values())))
    

def get_us_pop():

    us_population = 0

    for i in states:

        us_population += states[i][0]

    print("The US Population Is About:",us_population)
    

def quit_continue():

    start = str(input("Press 'c' to continue or 'q' to quit: "))

    while start != "c" and start != "q":
        start = str(input("Press 'c' to continue or 'q' to quit: "))

    while algien == True:
        if start == "c":
            main()
        elif start == "q":
            algien = False
    
def main():

    display_menu()
    choice = user_choice()

    if choice == 1:
        get_state_population()

    elif choice == 2:
        get_state_capitol()

    elif choice == 3:
        get_state_populated_city()

    elif choice == 4:
        get_state_nickname()

    elif choice == 5:
        get_random_info()

    elif choice == 6:
        get_us_pop()

    start = str(input("Press 'c' to continue or 'q' to quit: "))

    while start != "c" and start != "q":
        start = str(input("Press 'c' to continue or 'q' to quit: "))

    while algien == True:
        if start == "c":
            main()
        elif start == "q":
            algien = False

main()


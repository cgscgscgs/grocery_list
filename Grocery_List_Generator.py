# Date              Developer                   Changes
#
# 10/16/2025        celina schlecht             Initial creation
#
#
#
#
#

# This console application calculates a grocery list based on specified meals and snacks for the week.
# Designed for Celina Schlecht and T.B., by Celina Schlecht.
# Meal ingredients quantities are hard-coded and not interactive. 

# Print display main menu.
print(
"------------------------------------------------------------"  
"\n (: ---->  Welcome to the grocery list generator!  <---- :) "
"\n------------------------------------------------------------"
"\nChoose an option:")
print(
"\n[1] Create new grocery list"
"\n[2] View all ingredients"
"\n[3] View all recipes"
"\n[4] Exit\n")



# all ingredients
all_ingredients = {
    "lbs chicken": 0,
    "lbs beef": 0,
    "bell pepper" : 0,
    "poblano pepper" : 0,
    "jalapeno": 0,
    "onion": 0,
    "cups chopped carrot": 0,
    "minced garlic cloves": 0,
    "bunch cilantro": 0,
    "cans black bean": 0,
    "tbsp sriracha": 0,
    "tbsp chili powder": 0,
    "tbsp paprika": 0,
    "tbsp chipotle": 0,
    "heads lettuce": 0,
    "bags tortilla chips": 0,
    "cups shredded cheese": 0,
    "cups greek yogurt": 0,
    "15 oz can tomato sauce": 0,
    "28 oz can crushed tomato": 0,
    "6 oz tomato paste": 0,
    "cups broth": 0,
    "tbsp butter": 0,
    "tbsp sugar": 0,
    "tbsp basil": 0,
    "tbsp oregano": 0,
    "tsp parsley": 0,
    "oz protein pasta": 0,
    "cups rice": 0,
    "10 oz can rotel": 0,
    "cans corn": 0,
    "tbsp taco seasoning": 0,
    "cups broccoli floret": 0,
    "tsp minced ginger": 0,
    "tbsp cornstarch": 0,
    "tbsp soy sauce": 0,
    "cups honey": 0,
    "tbsp sesame oil": 0,
    "tsp red pepper flakes": 0,
    "tbsp olive oil": 0,
    "cups almond milk": 0,
    "scoops protein powder": 0,
    "tbsp peanut butter": 0,
    "bananas": 0,
    "eggs": 0,
    "cups spinach": 0,
    "slices bread": 0,
    "cups oats": 0,
    "tbsp jelly": 0,
    "box cereal": 0,
    "bags salad mix": 0,
    "cans kidney bean": 0,
    "container medjool dates": 0,
    "bags mixed nuts": 0
}

# function adding taco salad ingredients
def add_taco_salad():
    all_ingredients["bell pepper"] += 2
    all_ingredients["poblano pepper"] += 1
    all_ingredients["jalapeno"] += 1
    all_ingredients["onion"] += 1
    all_ingredients["cups chopped carrot"] += 0.5
    all_ingredients["minced garlic cloves"] += 6
    all_ingredients["bunch cilantro"] += 0.25
    all_ingredients["cans black bean"] += 2
    all_ingredients["tbsp sriracha"] += 4
    all_ingredients["tbsp chili powder"] += 1
    all_ingredients["tbsp paprika"] += 0.5
    all_ingredients["tbsp chipotle"] += 1
    all_ingredients["heads lettuce"] += 3
    all_ingredients["bags tortilla chips"] += 1
    all_ingredients["cups shredded cheese"] += 1
    all_ingredients["cups greek yogurt"] += 1

# function adding protein pasta ingredients
def add_protein_pasta():
    all_ingredients["onion"] += 1
    all_ingredients["minced garlic cloves"] += 4
    all_ingredients["15 oz can tomato sauce"] += 1
    all_ingredients["28 oz can crushed tomato"] += 1
    all_ingredients["6 oz tomato paste"] += 1
    all_ingredients["cups broth"] += 0.5
    all_ingredients["tbsp butter"] += 1
    all_ingredients["tbsp sugar"] += 1
    all_ingredients["tbsp basil"] += 1
    all_ingredients["tbsp oregano"] += 1
    all_ingredients["tsp parsley"] += 1
    all_ingredients["oz protein pasta"] += 8

# function for adding rice noodles ingredients
def add_rice_noodles():
    all_ingredients["cups broccoli floret"] += 2
    all_ingredients["bell pepper"] += 1
    all_ingredients["cups chopped carrot"] += 0.75
    all_ingredients["minced garlic cloves"] += 2
    all_ingredients["tsp minced ginger"] += 2
    all_ingredients["tbsp cornstarch"] += 1
    all_ingredients["cups broth"] += 0.25
    all_ingredients["tbsp soy sauce"] += 3
    all_ingredients["cups honey"] += 0.75
    all_ingredients["tbsp sesame oil"] += 1
    all_ingredients["tsp red pepper flakes"] += 1
    all_ingredients["tbsp olive oil"] += 2


# function for adding spanish rice ingredients
def add_spanish_rice():
    all_ingredients["bell pepper"] += 2
    all_ingredients["onion"] += 1
    all_ingredients["minced garlic cloves"] += 2
    all_ingredients["bunch cilantro"] += 0.75
    all_ingredients["cups rice"] += 2
    all_ingredients["10 oz can rotel"] += 2
    all_ingredients["15 oz can tomato sauce"] += 1
    all_ingredients["cups broth"] += 4
    all_ingredients["cans corn"] += 1
    all_ingredients["tbsp taco seasoning"] += 2


##### working on this part #####
# variable holding master grocery list ingredients
def master_grocery_list()
    for ingredient, quantity in all_ingredients.items():
        if all_ingredients.values() > 0
            print("\n" +)


# variable for reading user input of main menu selection.
main_menu_selection = input("")

# function for choosing chicken or beef on meal items
def chicken_or_beef(meal_chicken_or_beef):
    chicken_beef_choice = input("Chicken or beef for the " + meal_chicken_or_beef + "?  ")
    if chicken_beef_choice.startswith("c") | chicken_beef_choice.startswith("C"):
        chicken_lbs += 1.5
        print("Chicken " + meal_chicken_or_beef + " added to list!")
    elif chicken_beef_choice.startswith("b") | chicken_beef_choice.startswith("B"):
        beef_lbs += 1.5
        print("Beef " + meal_chicken_or_beef + " added to list!")
    else:
        print("Choose chicken or beef.\n")

# function for adding snacks after meals are chosen
def add_snacks():
    print("snacks added")
    #snack_counter = 0
    #while(snack_counter < 10):

# function for adding any other additional items after meals and snacks are chosen
def add_more_items():
    print("more items added")

# function for user selects main menu option 1, create grocery list
def create_grocery_list():

    # clear all_ingredient values to zero to start new blank grocery list
    for key in all_ingredients.keys():
        all_ingredients[key] = 0
    
    # ask for meals want to eat this week
    print("\nWhat are the meals you want to eat for dinner this week? Enter one by one.")
    print("     Taco salad")
    print("     Rice noodles")
    print("     Protein pasta")
    print("     Spanish rice\n")

    meal_counter = 0
    while (meal_counter < 2):
        meal = input("Meal " + str(meal_counter+1) + ":   ")

        # user selects taco salad
        if meal.startswith("t") | meal.startswith("T"):
            meal_counter+=1
            chicken_or_beef("taco salad")
            add_taco_salad()

        # user selects rice noodles
        elif meal.startswith("r") | meal.startswith("R"):
            meal_counter+=1
            add_rice_noodles()
            chicken_or_beef("rice noodles")

        # user selects protein pasta
        elif meal.startswith("p") | meal.startswith("P"):
            meal_counter+=1
            add_protein_pasta()
            chicken_or_beef("protein pasta")

        # user selects spanish rice
        elif meal.startswith("s") | meal.startswith("S"):
            meal_counter+=1
            add_spanish_rice()
            chicken_or_beef("spanish rice")

        else:
            print("Select a different meal.\n")
     
    print("Great! Those ingredients have been added to your grocery list.")



    # ask for snacks want to eat this week
    add_snacks_input = input("\nAdd snacks? Yes/No:  ")
    if add_snacks_input.startswith("y") | add_snacks_input.startswith("Y"):
        # add snacks
        add_snacks()
        print("Snacks added.")
    elif add_snacks_input.startswith("n") | add_snacks_input.startswith("N"):
        print("No snacks.")
    
        
   
    # ask for any additional items
    add_items_input = input("\nAnything else? Yes/No:   ")
    if add_items_input.startswith("y") | add_items_input.startswith("Y"):
        # add more items
        add_more_items()
    elif add_items_input.startswith("n") | add_items_input.startswith("N"):
        print("Okay! Printing your grocery list!")




# logic for user presses [1] grocery list 
if main_menu_selection == "1":
    create_grocery_list()
    # print display for user presses [1] grocery 

# logic for user presses [2] view ingredients
elif main_menu_selection == "2":
    # print display for user presses [2] view ingredients 
    print("2")

# logic for user presses [3] view recipes 
elif main_menu_selection == "3":
    print("3")
    # print display for user presses [3] view recipes
 
# logic for user presses [4] exit
elif main_menu_selection == "4": 
    print("Good-bye!")
    exit()

# logic for user presses a different key on main menu
else:
    print("Please press 1 - 4.\n")








        
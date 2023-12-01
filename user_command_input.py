import initial_user_housekeeping
import overall_country_queries
import database_queries

entity_list = ['capital city', 'capital_city', 'public transportation', 'transportation', 'public_transportation',
               'national cuisine', 'cuisine', 'national_cuisine', 'food', 'Economy', 'econ', 'climate', 'weather',
               'tourist attractions', 'tourism', 'attractions', 'tourist_attractions', 'national security',
               'security', 'national_security']

def print_command_list():
    print(f"\n\n\t\t\033[1m'{initial_user_housekeeping.get_user_id()}'\033[0m, here is a list of commands you can type and what each command does:\n")
    print(f"\t\t\033[1mReminder NOTHING is Case Sensitive but it is Spelling Sensitive\033[0m\n")
    print("\t\033[1mEnter 'E' or 'e'\033[0m" +
          "\n\t\t- Escapes the command sequence and leaves the travel guide")
    print("\t\033[1mEnter 'Help', 'help', 'H', or 'h'\033[0m"+
          "\n\t\t- Prints this command list again at any time!")
    print("\t\033[1mEnter '1 or countries'\033[0m" +
          "\n\t\t- Receive a list of countries covered in guide")
    print("\t\033[1mEnter '2'\033[0m" +
          "\n\t\t- Receive a list of information we offer about each country")
    print("\t\033[1mEnter '[country name]'\033[0m" +
          "\n\t\t- to view specific information regarding a country" +
          "\n\t\t- Example: 'Denmark'")
    print("\t\033[1mEnter '[country name] [country specific info]'\033[0m" +
          "\n\t\t- to view information in a specific sector of that country be" + 
          "\n\t\t  it climate, economy, food, etc" +
          "\n\t\t- Example: 'Denmark Economy'")
    print("\t\033[1mEnter '[country name] all'\033[0m" +
          "\n\t\t- To view everything regarding a country" +
          "\n\t\t- Example 'Denmark all'\n")

def print_country_list(country_list):
    midpoint1 = len(country_list) // 3
    midpoint2 = 2 * len(country_list) // 3

    max_index_digits = len(str(len(country_list)))

    # Print in three columns
    print("\nList of Countries:\n")
    for i, (country1, country2, country3) in enumerate(zip(country_list[:midpoint1], country_list[midpoint1:midpoint2], country_list[midpoint2:]), start=1):
        index_str1 = f"{i}.".ljust(max_index_digits + 1)
        index_str2 = f"{i + midpoint1}.".ljust(max_index_digits + 1)
        index_str3 = f"{i + midpoint2}.".ljust(max_index_digits + 1)
        print(f"{index_str1} {country1.ljust(25)} {index_str2} {country2.ljust(25)} {index_str3} {country3}")

def print_entity_list():
    print("\n\t\tEach country has the following country specific information offered about it:"+
        "\n\t\tYou can simply type the \033[1m'Country_name any_of_the_following'\033[0m to get specific info."
        "\n\t\t\t- Country" +
        "\n\t\t\t- Capital City or capital_city" +
        "\n\t\t\t- Public Transportation or transportation or public_transportation" +
        "\n\t\t\t- National Cuisine or cuisine or national_cuisine or food" +
        "\n\t\t\t- Economy or econ" +
        "\n\t\t\t- Climate or weather" +
        "\n\t\t\t- Tourist Attractions or tourism or attractions or tourist_attractions" +
        "\n\t\t\t- National Security or security or national_security" +
        "\n\t\t\t- Example: \033[1m'Italy Economy'\033[0m or \033[1m'norway Climate'\033[0m or \033[1m'russia econ'\033[0m")

def print_country_specific_info(user_input):
    country, specific_table = user_input.split()[0].title(), user_input.split()[1]
    if specific_table in ['capital city', 'capital_city']:
        print("\n\t\tcapital city attributes:\n")
        for key, value in database_queries.query_capital_city_attributes(country).items():
            print(f"\t\t{key:25}{value}")
    elif specific_table in ['public transportation', 'transportation', 'public_transportation']:
        print("\n\t\tpublic transportation attributes:\n")
        for key, value in database_queries.query_public_transportation_attributes(country).items():
            print(f"\t\t{key:35}{value}")
    elif specific_table in ['national cuisine', 'cuisine', 'national_cuisine', 'food']:
        print("\n\t\tnational cuisine attributes:\n")
        for key, value in database_queries.query_national_cuisine_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:45}{value}")
    elif specific_table in ['Economy', 'econ']:
        print("\n\t\tEconomy attributes:\n")
        for key, value in database_queries.query_economy_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:55}{value}")
    elif specific_table in ['climate', 'weather']:
        print("\n\t\tClimate:\n")
        for key, value in database_queries.query_climate_attributes(country).items():
            print(f"\t\t{key:35}{value}")
    elif specific_table in ['tourist attractions', 'tourism', 'attractions', 'tourist_attractions']:
        print("\n\t\tTourist Attractions:\n")
        for key, value in database_queries.query_tourist_attractions_attributes(initial_user_housekeeping.get_user_id(), country).items():
            print(f"\t\t{key:40}{value}")
    else:
        print("\n\nNational Security:\n")
        for key, value in database_queries.query_national_security_attributes(country).items():
            print(f"{key:40}{value}")

def user_command_loop():
    country_list = overall_country_queries.query_country_names()
    print_command_list()
    while True:        
        user_input = input("\n\t\tPlease enter your next command, type \033[1m'h'\033[0m for the list of commands:\n\t")
        user_input.lower()

        if user_input in ['e', 'exit']:
            break
        elif user_input in ['h', 'help']:
            print_command_list()
        elif user_input in ['1', 'countries']:
            print_country_list(country_list)
        elif user_input == "2":
            print_entity_list()
        elif user_input.title() in country_list:
            print("\n\nCountry Attributes:")
            for key, value in database_queries.query_country_attributes(user_input.title()).items():
                print(f"{key:25}{value:}")
        elif user_input.split()[0].title() in country_list and user_input.split()[1] in entity_list:
            print_country_specific_info(user_input)
        elif user_input.split()[0].title() in country_list and user_input.split()[1] == 'all':
            print("\n\t\tCountry Overview:\n")
            for key, value in overall_country_queries.query_country_overview(user_input.split()[0].title()).items():
                print(f"\t\t{key:40}{value}")
        else:
            print("Your command did not match any of the acceptable ones...")
            print("You may have mispelled a country or request.")
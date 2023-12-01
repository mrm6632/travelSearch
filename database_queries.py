import sqlite3

def format_country_name(user_inputted_country_name):
    return user_inputted_country_name.lower().title()

def query_country_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        name AS country_name,
                        government_struct AS government_structure,
                        most_common_religion,
                        time_zone,
                        official_language
                    FROM Country
                    WHERE name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Government Structure": result[1].title(),
                    "Most Common Religion": result[2],
                    "Time Zone": result[3],
                    "Official Language/s": result[4]
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_capital_city_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        country AS country_name,
                        capital_city,
                        capital_city_region,
                        population
                    FROM Capital_City
                    WHERE country = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Capital City": result[1],
                    "Capital City Region": result[2].title(),
                    "City Population": '{:,}'.format(result[3]),
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_public_transportation_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        country_name,
                        types_available AS public_transportation_options,
                        owned_by,
                        most_used AS most_used,
                        avg_price_of_ticket
                    FROM Public_Transportation
                    WHERE country_name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Public Transportation Options": result[1].title(),
                    "Operating Company": result[2],
                    "Most Used Public Transportation": result[3],
                    "Average Price of Ticket": result[4]
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_national_cuisine_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        country_name,
                        dish_name AS national_dish,
                        food_classification,
                        most_exported_food
                    FROM National_Cuisine
                    WHERE country_name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "National Dish": result[1].title(),
                    "Food Classification": result[2],
                    "Most Exported Food": result[3],
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_economy_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        country_name,
                        economic_world_ranking,
                        gdp AS gross_domestic_product,
                        type AS type_of_economy,
                        currency,
                        largest_industry
                    FROM Economy
                    WHERE country_name = ?;
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": result[0],
                    "Economic World Ranking": result[1],
                    "Total Gross Domestic Product, GDP": '${:,}'.format(result[2]),
                    "Type of Economy": result[3].title(),
                    "Currency": result[4],
                    "Country's Largest Industry": result[5].title()
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_national_security_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        global_peace_index,
                        homicide_rate,
                        avg_larceny AS average_larceny,
                        police_force AS police_force_type
                    FROM National_Security
                    WHERE economic_world_ranking = (
                        SELECT economic_world_ranking
                        FROM Economy
                        WHERE country_name = ?
                    );
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": country_name,
                    "Global Peace Index, gpi": result[0],
                    "Homicide Rate (per 100,000 people)": result[1],
                    "Average Larceny (per 100,000 people)": result[2],
                    "Police Force Type": result[3].title(),
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_tourist_attractions_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        city_name AS city_tourist_attractions_located_in,
                        top_visited AS top_visited_attraction,
                        tourist_attraction_region,
                        most_popular_nightlife_area
                    FROM Tourist_Attractions
                    WHERE city_name = (
                        SELECT capital_city
                        FROM Capital_City
                        WHERE country = ?
                    );
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": country_name,
                    "City": result[0].title(),
                    "Most Visited Tourist Attraction": result[1].title(),
                    "Tourist Attraction Region": result[2].title(),
                    "Most Popular Nightlife Area": result[3].title(),
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def query_climate_attributes(user_inputted_country_name):
    connection = sqlite3.connect('travelSearch.db')
    cursor = connection.cursor()

    country_name = format_country_name(user_inputted_country_name)

    select_query = """SELECT
                        city_name,
                        region_of_climate,
                        climate_type,
                        avg_days_of_sun,
                        season_to_travel
                    FROM Climate
                    WHERE city_name = (
                        SELECT capital_city
                        FROM Capital_City
                        WHERE country = ?
                    );
                    """
    cursor.execute(select_query, (country_name,))

    result = cursor.fetchone()
    
    if result:
        user_output = {"Country Name": country_name,
                    "City": result[0].title(),
                    "Region of Climate": result[1].title(),
                    "Climate Type": result[2].title(),
                    "Average Days of Sun in the Year": f"{result[3]} days",
                    "Season to Travel": result[4].title()
                    }
    else:
        user_output = {"Country Name": "Invalid country name. Country was either mispelled or is not in Europe, (not case sensitive)"}
    
    connection.close()

    return user_output

def main():
    print("\n\nCountry Attributes:")
    for key, value in query_country_attributes("hungary").items():
        print(f"{key:25}{value:}")

    print("\n\ncapital city attributes:\n")
    for key, value in query_capital_city_attributes("romania").items():
        print(f"{key:25}{value}")
    
    print("\n\npublic transportation attributes:\n")
    for key, value in query_public_transportation_attributes("united kingdom").items():
        print(f"{key:35}{value}")

    print("\n\nnational cuisine attributes:\n")
    for key, value in query_national_cuisine_attributes("germany").items():
        print(f"{key:25}{value}")

    print("\n\nEconomy attributes:\n")
    for key, value in query_economy_attributes("denmark").items():
        print(f"{key:38}{value}")

    print("\n\nNational Security:\n")
    for key, value in query_national_security_attributes("spain").items():
        print(f"{key:40}{value}")

    print("\n\nTourist Attractions:\n")
    for key, value in query_tourist_attractions_attributes("italy").items():
        print(f"{key:40}{value}")

    print("\n\nClimate:\n")
    for key, value in query_climate_attributes("switzerland").items():
        print(f"{key:35}{value}")

if __name__ == "__main__":
    main()
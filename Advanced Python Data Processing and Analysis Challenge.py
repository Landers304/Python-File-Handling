#Task 1:


import re

def analyze_sentiment():
    try:
        # Provided dataset example
        blogs = """
        Travel Blog Entries:
        "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
        "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
        "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
        "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
        "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
        "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
        "The food on our trip was excellent. We sampled delicious local cuisine at every stop."
        "The historical tour was enlightening. We learned so much about the culture and heritage of the region."
        "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
        """

        # Define positive and negative word lists
        positive_words = ["amazing", "enjoy", "wonderful", "memorable", "fantastic", "unforgettable", "excellent"]
        negative_words = ["disappointing", "poor", "lackluster", "scarce"]

        # Blog entries and count positive and negative words
        positive_count = 0
        negative_count = 0
        for blog in re.findall(r'"(.*?)"', blogs):
            words = re.findall(r'\b\w+\b', blog.lower())
            for word in words:
                if word in positive_words:
                    positive_count += 1
                elif word in negative_words:
                    negative_count += 1

        # Sentiment analysis summary
        print("Sentiment Analysis Summary:")
        print("Positive words count:", positive_count)
        print("Negative words count:", negative_count)

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied to access file.")

# Perform sentiment analysis
analyze_sentiment()




#Task 2:


import os

def analyze_weather_data(directory):
    try:
        # Initialize dictionary to store average temperatures for each year
        average_temperatures = {}

        # Iterate files in the directory
        for filename in os.listdir(directory):
            if filename.startswith("weather_") and filename.endswith(".txt"):
                year = filename.split("_")[1].split(".")[0]
                temperatures = []
                with open(os.path.join(directory, filename), 'r') as file:
                    for line in file:
                        # Extract temperature values from each line
                        temps = line.strip().split(",")[1:]
                        for temp in temps:
                            temperature = int(temp.split("°")[0])
                            temperatures.append(temperature)
                
                # Average temperature for the year
                average_temperature = sum(temperatures) / len(temperatures)
                average_temperatures[year] = average_temperature

        # Highest average temperature
        max_year = max(average_temperatures, key=average_temperatures.get)
        max_temperature = average_temperatures[max_year]

        # Average temperatures for each year
        print("Average temperatures for each year:")
        for year, temperature in average_temperatures.items():
            print(f"{year}: {temperature}°C")

        # Highest average temperature year
        print(f"\nThe year with the highest average temperature is {max_year} with {max_temperature}°C.")

    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied to access directory.")
    except Exception as e:
        print("An error occurred:", str(e))

# Analyze weather data in specified directory
analyze_weather_data("path/to/weather/data/directory")

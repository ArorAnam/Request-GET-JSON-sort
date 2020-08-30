import json
import requests

# best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

# best_food_chains_string = json.dumps(best_food_chains)
# # We've successfully converted our list to a string.
# print(type(best_food_chains_string))

# print(best_food_chains_string)

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Get the response data as a python object. Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
# 9 people are currently in space.
print(data["number"])
print(data)

print(help(response))
import json

# serializing JSON

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file_.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
json_string_2 = json.dumps(data)

# deserializing JSON

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

blackjack_hand == decoded_hand

blackjack_hand == tuple(decoded_hand)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

json_string3 = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgusian",
        "relatives": [
            {
                "name": "Xaapacsc asfsm".
                "species": "baerfef"
            }
        ]
    }
}
"""
data = json.loads(json_string3)
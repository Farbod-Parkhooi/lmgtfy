from json import load
def create_url(query):
    with open("log/data.json", "r") as file:
        url = load(file)["normal-url"]
        out_query = """"""
        for letter in query:
            if letter == " ": out_query += "+"
            else: out_query += letter
        return url + out_query

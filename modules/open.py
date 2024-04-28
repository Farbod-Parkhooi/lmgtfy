from json import load
def write_history(url):
    with open("log/history.txt", "r") as file: text = "".join(file.readlines())
    out = """"""
    out += text
    out += "\n"
    out += url
    with open("log/history.txt", "w") as file:
        file.write(out)
def create_url(query):
    with open("log/data.json", "r") as file:
        url = load(file)["normal-url"]
        out_query = """"""
        for letter in query:
            if letter == " ": out_query += "+"
            else: out_query += letter
        out = url + out_query
        write_history(out)
        return out

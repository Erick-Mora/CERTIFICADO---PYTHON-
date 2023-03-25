import json

def main():
    print("Ejercicio 15")
    print("---JSON Dictionary---")
    data = '''
    {
        "name": "Erick",
        "phone": {
            "type": "intl",
            "number": "333999"
        },
        "email": {
            "hide": "yes"
        }
    }
    '''
    info = json.loads(data)
    print("Name:",info["name"])
    print("Hide:",info["email"]["hide"])
    print("---JSON List---")
    data = '''
    [
        {"id":"001",
        "x": "3",
        "name":"Erick"},
        {"id":"003",
        "x":"7",
        "name":"another"}
    ]
    '''
    info = json.loads(data)
    print("User count:",len(info))
    for r in info:
        print("Name:",r["name"])
        print("Id:",r["id"])
        print("Value:",r["x"])
if __name__ == "__main__":
    main()
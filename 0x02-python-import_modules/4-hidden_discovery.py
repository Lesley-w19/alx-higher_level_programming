#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for names in dir(hidden_4):
        if names[0] != "_" and names[1] != "_":
            print(names)

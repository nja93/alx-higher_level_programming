#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for file_name in sorted(dir(hidden_4)):
        if file_name[:2] != "__":
            print("{}".format(file_name))

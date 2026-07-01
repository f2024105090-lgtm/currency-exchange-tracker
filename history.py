def get_history(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except:
        return []
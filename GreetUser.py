def name_concat(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


def greet_user(first_name, last_name):
    print(f"Welcome home, {name_concat(first_name, last_name)}!")

def say_hello(name, city, state):
    if isinstance(name, list):
        name = ' '.join(name)
    return "Hello, {}! Welcome to {}, {}!".format(name, city, state)
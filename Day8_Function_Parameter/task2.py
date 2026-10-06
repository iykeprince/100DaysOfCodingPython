def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Positional argument
greet_with("Jack Bauer", "Norway")
greet_with("Norway", "Jack Bauer")

# Keyword argument
greet_with(name="Jack Bauer", location="Nofolk")
greet_with(location="Norway", name="Jack Bauer")
# len(): Returns the length (number of characters) of a string
text = "Hello"
length = len(text) #5

# upper() and lower(): Convert a string to uppercase or lowercase
message = "Python is Fun"
upper_message = message.upper() # "PYTHON IS FUN"
lower_message = message.lower() # "python is fun"

# strip(): Removes leading and trailing whitespace or specified characters
sentence = "   Welcome!   "
stripped_sentence = sentence.strip()  # "Welcome!"

# replace(): Replaces a specified substring with another substring
text = "Hello, world!"
new_text = text.replace("world", "Python")  # "Hello, Python!"

# find() and index(): Search for a substring and return its index or position
sentence = "Python is powerful."
position = sentence.find("is") # 7

# count(): Counts the occurrences of a substring in a string
text = "Programming is fun and programming is cool."
count_is = text.count("is") # 2

# startswith() and endswith(): Check if a string starts or ends with a specified substring
title = "Mr. John Doe"
starts_with_mr = title.startswith("Mr.") # True
ends_with_doe = title.endswith("Doe")     # True

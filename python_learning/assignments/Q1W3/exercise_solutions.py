#1. Simple Message
message: str ='Hi How are You'
print(message)

#2. Simple Messages
message1: str = 'Change string is working'
print(message1)

#3. Personal Message
person_name: str ='Eric'
person_message: str = f"Hello {person_name}, would you like to learn some Python today?"
print(person_message)

#4. Name Cases
#Lower
person_message_lower: str = f"Hello {person_name.lower()}, would you like to learn some Python today?"
print(person_message_lower)
#Upper
person_message_upper: str = f"Hello {person_name.upper()}, would you like to learn some Python today?"
print(person_message_upper)
#Title
person_message_title: str = f"Hello {person_name.title()}, would you like to learn some Python today?"
print(person_message_title)

#5. Famous Quote
quot: str = """Albert Einstein once said, “A person who never/n made a mistake never
tried anything new.”"""
print(quot)

#6. Famous Quote 2
famous_person: str = "Faraz"
message2: str = f"{famous_person} once said, 'The ultimate aim of the ego is not to see something, but to be something.'"
print(message2)

#7. Stripping Names
name: str = "\t\n   Allama Iqbal   \n\t"
print(name)

print("Leading whitespace removed:")
print(name.lstrip())
print("Trailing whitespace removed:")
print(name.rstrip())
print("All whitespace removed:")
print(name.strip())

#8. Variable Sum
x: int= 5
y: int= 10
z: int= 15
print(f"Sum of x,y,z: {x+y+z}")

#9. Variable Swap
a: int = 5
b: int = 10
print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")
#Swap
a, b = b, a
print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")

#10. Favorite Color
my_color: str = "Blue"
print("Favorite color:", my_color)
color_new: str = my_color
print("Color with new variable:", color_new)

#11. Changing Pet Name
pet_name:str = "Buddy"
pet_name = "Max"
print(pet_name)

#12. Observing Name Error
my_variable: str = "Sunshine"
print(my_variable)
#print(sunshine)

#13. Reassigning Score
score: int = 100
print(score)
score = 50
print(score)

#14. City Name
city: str 
city = 'Lahore'
print(city)

#15. Title Case Text
text:str = "pYthoN ProgrAmminG"
print(text)
#16. Lowercase Conversion
print(text.lower())
#17. Uppercase Conversion)
print(text.upper())

#18. Current Temperature
temperature: int = 25
print(f"The current temperature is {temperature} degrees.")

#19. Printing a Poem
poem: str = """\
Python’s grace, a coder’s delight,
With syntax clear and logic tight,
From simple tasks to complex feats,
Python makes our work complete."""
print(poem)

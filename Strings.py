String Literals
Strings are any sequence of characters (letters, numberals, ~($/}  # ,etc.) enclosed in single or double quotes.abs(x)

print("this is a sample string")

Concatenating Strings and Variables with the print function
There are multiple ways that we can print a string containing data from variables.

The first is by adding a comma after the string, followed by the variable. Note that the comma is outside the closing quotation mark of the string. The print() function inserts a space between elements separated by a comma.

name="Zen"
print("My name is", name)

The second is by concatenating the contents into a new string, with the help of + .

name="Zen"
print("My name is " + name)

Type Casting or Explicit Type Conversion
We may find ourselves wanting to change a value's data type from one type to another.  Python doesn't know how to add a string and a number, but it can add two strings together, so if we can cast the number as a string, then we will be able to "add" the two values together, like so:

print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

Another example may be receiving a string input from a user that we want to treat as a number:
total=35
user_val="26"  # this is string
total=total + user_val		# output: TypeError
total=total + int(user_val)		# total will be 61

String Interpolation
we can also inject variables into our strings, which is known as string interpolation. there are a few different ways this can be done.

# F-Strings(Literal String INterpolation) *** will mostly use
Python 3.6 introduced f-strings for string interpolation. To construct a f-string, place an f right before the opening quotation. The within the string, place any variables within curly brackets.

first_name="Zen"
last_name="Coder"
age=27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name="Michael"
last_name="Lay"
age=31
print(f"My name is {first_name} {last_name} and I am {age} years old.")
print(f"My name is {first_name} {last_name} and I am {age} years old.")

example

def list_of_things(int, str, bool):
    print(int)
    print(str)
    print(bool)

    total_string =f"here is my list of things: {int}, {str}, {bool}."

# ..............................................................................

String format()
Prior to f-strings, string interpolation was accomplished with the .format() method. if you're searching online, you will likely to find code snippets using this method. To use it type out the full string, replaceing ay words that will get their values from variables with {}. Then call the format method on the string, passing in arguments in the order in which they should fill the {} placeholders. Here's an examples.

first_name="Michael"
last_name="Lay"
age=31
print("My name is {} {} and I am {} years olds.".format(
    first_name, last_name, age))
print("My name is {} {} and I am {} years olds".format(
    age, last_name, first_name))

% -formatting
There is an even older method of string interpolation that you may come across when troubleshooting or researching, so you should know about it. Rather than curly braces, the % symbol is used to indicate a placeholder, a % s for a string a % d for a number. After the string, a single % separates the string to be interpolated from the values to be inserted into the string, like so:

hw="Hello %s" % "world" 	# with literal values
py="I love Python %d" % 3
print(hw, py)
# output: Hello world I love Python 3

moto="I am not %s" % "failed"
sp="I just have not found %d solutions" % 9
print(moto, sp)

name="Zen"
age=27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

name="zen"
age=27
print("My name is %s and I am %d" % (name, age))

Built-In String methods

We've seen the format method, but there are several more methods that we can run on a string. Here's how to use them:

x="hello world"
print(x.title())



The following is a list of commonly used string methods:
string.upper(): returns a copy of the string with all the characters in uppercase.
string.lower(): returns a copy of the string with all the characters in lowercase.
string.count(substring): returns number of occurrences of substring in string.
string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
string.find(substring): returns the index of the start of the first occurrence of substring within string.
string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

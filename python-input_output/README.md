File Handling and JSON in Python
This guide covers various file handling operations in Python and introduces JSON, serialization, deserialization, and command line parameter handling.

Opening a File
To open a file in Python, you can use the open() function. It takes the file path and the mode ('r' for reading, 'w' for writing, 'a' for appending, and more) as arguments.

python
Copy code
file = open("filename.txt", "r")
Writing Text in a File
To write text to a file, you can use the write() method of the file object.

python
Copy code
file.write("Hello, world!\n")
Reading Full Content of a File
You can use the read() method to read the full content of a file.

python
Copy code
content = file.read()
Reading a File Line by Line
To read a file line by line, you can iterate over the file object.

python
Copy code
for line in file:
    print(line)
Moving the Cursor in a File
You can use the seek() method to move the cursor to a specific position in the file.

python
Copy code
file.seek(0)  # Moves cursor to the beginning of the file
Closing a File
It's essential to close a file after using it to release system resources. You can use the close() method.

python
Copy code
file.close()
Using the with Statement
The with statement ensures that the file is properly closed after usage, even if an exception occurs.

python
Copy code
with open("filename.txt", "r") as file:
    content = file.read()
    # file automatically closed after this block
JSON
JSON (JavaScript Object Notation) is a lightweight data interchange format. It's easy for humans to read and write and easy for machines to parse and generate.

Serialization
Serialization is the process of converting a data structure or object into a format that can be stored or transmitted.

Deserialization
Deserialization is the process of converting a serialized format back into its original data structure or object.

Converting a Python Data Structure to a JSON String
You can use the json.dumps() function to convert a Python data structure to a JSON string.

python
Copy code
import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
Converting a JSON String to a Python Data Structure
You can use the json.loads() function to convert a JSON string to a Python data structure.

python
Copy code
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
Accessing Command Line Parameters in a Python Script
You can access command line parameters using the sys.argv list from the sys module.

python
Copy code
import sys

# Command line arguments are stored in sys.argv
arg1 = sys.argv[1]
arg2 = sys.argv[2]
Remember to handle cases where command line arguments are missing or incorrect to avoid errors.
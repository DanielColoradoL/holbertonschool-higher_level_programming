Object-Oriented Programming Concepts
Superclass, Baseclass, or Parentclass
In object-oriented programming, a superclass, baseclass, or parentclass is a class from which other classes, known as subclasses, inherit attributes and methods.

Subclass
A subclass is a class that inherits attributes and methods from a superclass. It can also have its own unique attributes and methods.

Listing Attributes and Methods of a Class or Instance
To list all attributes and methods of a class or instance, you can use the dir() function in Python.

python
Copy code
print(dir(ClassName))
print(dir(instance))
Instances with New Attributes
An instance can have new attributes added to it at any time during runtime by simply assigning values to new attribute names.

python
Copy code
instance.new_attribute = value
Inheriting Class from Another
To inherit a class from another, specify the superclass in parentheses after the subclass name in the class definition.

python
Copy code
class SubclassName(SuperclassName):
    # subclass methods and attributes
    pass
Defining a Class with Multiple Base Classes
To define a class with multiple base classes, separate the superclass names with commas inside parentheses.

python
Copy code
class SubclassName(BaseClass1, BaseClass2):
    # subclass methods and attributes
    pass
Default Class Every Class Inherits From
The default class every class inherits from in Python is the object class.

Overriding Inherited Methods or Attributes
To override a method or attribute inherited from the base class, simply redefine it in the subclass with the desired implementation.

Inherited Attributes and Methods for Subclasses
Subclasses inherit all attributes and methods from their superclass(es) unless overridden.

Purpose of Inheritance
The purpose of inheritance in object-oriented programming is to create a hierarchy of classes that share common attributes and methods, promoting code reuse and abstraction.

Built-in Functions for Class and Type Checking
isinstance(obj, class_or_tuple): Checks if an object is an instance of a class or any of its subclasses.
issubclass(subclass, superclass_or_tuple): Checks if a class is a subclass of another class.
type(obj): Returns the type of an object.
super(): Returns a proxy object that allows you to access methods of the superclass. It is commonly used to call methods of the superclass from the subclass.
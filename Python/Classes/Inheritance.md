Inheritance allows one class, called the "child" to inherit the properties and methods of another "parent" class.

``` python
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
```

The super method allows for calling methods and the constructor from the parent class:

``` python
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self, num_udders):
        # call the parent constructor to give the cow some legs
        super().__init__(4)

        # set cow specific properties
        self.num_udders = num_udders
```


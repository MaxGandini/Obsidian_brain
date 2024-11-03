Examples:
- [[download_dataset.py]]
from [[Python]]'s documents: 
```
The type system aims to provide a standard syntax for type annotations, opening up Python code to easier static analysis and refactoring, potential runtime type checking, and (perhaps, in some contexts) code generation utilizing type information.

Of these goals, static analysis is the most important. This includes support for off-line type checkers such as mypy, as well as providing a standard notation that can be used by IDEs for code completion and refactoring.

Purpose
This specification aims to provide a full description of the Python type system. For type checker authors, it provides a complete description of expected semantics. For library authors, it provides guarantees to rely on when working with multiple type checkers.

The type system was originally specified in a series of PEPs, starting with PEP 484. This document is intended to replace those PEPs, and was initially created by merging the specification sections of the various PEPs. However, the PEPs are uneven in depth and do not fully cover all aspects of the type system. Addressing these issues is an ongoing project.
```

There's a very illustrative example:

```
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
```

The function surface_area_of_cube takes an argument expected to be an instance of float, as indicated by the type hint edge_length: float. The function is expected to return an instance of str, as indicated by the -> str hint.

Another very interesting example is defining a type like :
```
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

So now the vector type is defined as a list of floats.

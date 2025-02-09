# PlaneCoordinates
Utility to create 2D Coordinate Object types and perform some operations

To install the package use the following command in your terminal:
```
pip3 install https://github.com/rontech22/PlaneCoordinates/releases/download/v0.1.1/PlaneCoordinates-0.1.1-py3-none-any.whl
```

To use this package in one of your proyects, use this command to import the packge into your .py file:
```python
from PlaneCoordinate import coordinate
```

## Operations:

### Initiate a Coordinate object type:
```python
p1 = coordinate(1,2)
print(p1)
>> <1,2>
```
### Calculate the distance between two coordinates:
```python
coordinate.distance(p1, p2)
```
### Calculate the module of a 2D vector (from origin to coordinate)
```python
coordinate.module(p1)
```
### Sum and substract two coordinates (as vectors)
```python
p1 = coordinate(1,2)
p2 = coordinate(3,4)
print("p1+p2 =", p1+p2)
print("p2-p1 =", p2-p1)
>> p1+p2 = <4,6>
>> p2-p1 = <2,2>
```

More features in future releases...

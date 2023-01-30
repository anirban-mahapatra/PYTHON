"""""Problem:- Write a python program which accepts the radius of a circle from the user and
compute the Area and perimeter of a Circle."""

r=float(input("Enter the radius of the circle:-"))
pi=3.141592653589793238

area=(pi*r*r)
par=2*pi*r
print(f"Radius={r}\nArea={area:.2f}\nParimeter={par:.2f}")
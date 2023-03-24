Lab9: Methods and Special Methods

Problem Statement:
1.  Locate the Sun, Planet, and SolarSystem classes in the provided code. List constructor(s), accessors, mutators for each of them. 1%

2. Special method __repr__(self) returns a string (human-readable) representation of an object (it's also known as the representation function of a class which captures the essential content of an object). The __repr__ method should return a string of the form: "Name:Mercury,Mass:1000,Distance:0.25, Radius:19.5". Create a planet and print it before and after adding __repr__(self) to Planet class. What is the difference? Also create a list of planets and print the list before and after adding __repr__.  What is the difference?   0.5%

3. Special method __lt__(self, other) is used by the sort function of a list. Add __lt__(self, other) to Planet which compares two planets (self and other) by mass. Sort a list of planets with and without adding __lt__ and describe the difference. 0.5%

4. Run createSSandAnimate(). Modify the mass of Sun and describe the effects of both a larger mass and a smaller mass of Sun on how a planet orbits. Modify the vY of each planet and describe how it interacts with Sun's mass to influence how it orbits. 1%

5. Modify the sun and the planets to better reflect their relative sizes. By default, the radius of the turtle is 20 pixels. In the following method call on a turtle object, the first two arguments below represents how many units 20 pixels the Turtle's width and height are, and the last 1 represents the width of the Turtle's outline. Set them to 5 for sun, and to __radius/100 for all planets. 1%

turtle.shapesize(x, y, 1)

Special methods are covered in 10.3.4 of the book.

Modify the attached code. Write your answer to the above questions in a separate file. Include screenshots for 2, 3, 4, and 5. Upload both the modified code and the answer file to Moodle for grading.

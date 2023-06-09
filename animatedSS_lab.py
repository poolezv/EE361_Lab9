import turtle
import math


class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width / 2.0, -height / 2.0,
                                            width / 2.0, height / 2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()

            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.__theSun.getMass() * rX / r ** 3
            accY = G * self.__theSun.getMass() * rY / r ** 3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

    def freeze(self):
        self.__ssScreen.exitonclick()


class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0

        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getMass(self):
        return self.__mass

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def __lt__(self, other):
        return self.__mass < other.__mass

    def __str__(self):
        return self.__name + str(self.__mass)

    def shapesize(self):
        x = self.__radius / 100.0
        y = self.__radius / 100.0
        w = 1
        if isinstance(self, Sun):
            x = 5
            y = 5
        self.__sTurtle.shapesize(x, y, w)


class Planet:
    __name: object

    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy

    def __repr__(self):
        return f"Name:{self.__name},Mass:{self.__mass},Distance:{self.__distance},Radius:{self.__radius}"

    def __lt__(self, other):
        return self.__mass < other.__mass

    def shapesize(self):
        x = self.__radius / 100.0
        y = self.__radius / 100.0
        w = 1
        if isinstance(self, Sun):
            x = 5
            y = 5
        self.__pTurtle.shapesize(x, y, w)


def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("Sun", 5000, 10, 5800)
    sun.shapesize()
    ss.addSun(sun)

    m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
    m.shapesize()
    ss.addPlanet(m)

    m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
    m.shapesize()
    ss.addPlanet(m)

    m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
    m.shapesize()
    ss.addPlanet(m)

    m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
    m.shapesize()
    ss.addPlanet(m)

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()


# ------------------ For Q2 - Q4 ------------------------
# p = Planet("Pluto", 7.3, 777, .13, 0, 1.7, "blue")
# print(p)
#
# j = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
# m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
# e = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
# mer = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
# lPlanet = [j, m, e, mer]
#
# lPlanet.sort()
#
# print(lPlanet)

createSSandAnimate()

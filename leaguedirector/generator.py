from leaguedirector.sequencer import *
import math


class CameraCircleAround:
    def __init__(self):
        self.center = (5000, 100, 5000)
        self.height = self.center[1]
        self.radius = 100
        self.numPoints = 5
        self.startAngle = 0
        self.length = 5
        self.points = []

    def calculatePoints(self):
        return [(math.cos(2*math.pi/self.numPoints*i)*self.radius, 
                self.height, 
                math.sin(2*math.pi/self.numPoints*i)*self.radius) for i in range(0, self.numPoints+1)]

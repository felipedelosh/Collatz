"""
FelipedelosH

"""
from Graph import *

class Controller:
    def __init__(self) -> None:
        self.graph = Graph()
        self.number = None
        self.limitInfinite = 1000
        self._steps = [] # Save in vector f(x) mouves
        self.LOGS = ""
        self.output = "TEST"
        self.defaultColor = {'bg':"black", 'fg':"red", 'visible':"green", 'axes':"blue"}


    def setNumber(self, number):
        self.number = int(number)


    def ejecuteAlgorithm(self):
        self._steps = []
        count = 0
        while count < self.limitInfinite:
            self._steps.append(self.number)
            if self.number == 1:
                # How to add previus ?
                self.output = f"Proccess is over > Steps: {count} Nodes: {len(self.graph.nodes)} Edges: {len(self.graph.edges)} Vector control: {len(self._steps)}"
                break
            elif self.number % 2 == 0:
                newNumber = self.number / 2
                self.graph.addEdge(self.number, newNumber, 1)
                self.number = newNumber
            else:
                newNumber = (self.number*3) + 1
                self.graph.addEdge(self.number, newNumber, 1)
                self.number = newNumber

            self.graph.addNode(self.number)
            count = count + 1


    def paintRoute(self, type, canvas):
        """
        Enter a Tkinter canvas and paint via type:
        types examples: "point"
        """
        if type == "point":
            self._paintPointRoute(canvas)


    def _paintPointRoute(self, canvas):
        """
        Enter a canvas and create XY point graphics
        """
        canvas.delete("point")
        _h = int(canvas['height'])
        _w = int(canvas['width'])

        # Get the max number of axes y
        maxY = 0
        for i in self._steps:
            if i > maxY:
                maxY = i

    
        # Paint Axis
        # Y
        _kdy = _h*0.1
        canvas.create_line(_w*0.05, _kdy, _w*0.05, _h*0.9, fill=self.defaultColor['axes'], tags="point")
        # Put labels min-middle-max
        canvas.create_text(_w*0.03, _h*0.88, text="0", fill=self.defaultColor['axes'], tags="point")
        canvas.create_text(_w*0.03, _h*0.44, text=str(maxY/2), fill=self.defaultColor['axes'], tags="point")
        canvas.create_text(_w*0.03, _kdy, text=str(maxY), fill=self.defaultColor['axes'], tags="point")
    

        # X
        _k = _w*0.05
        canvas.create_line(_k, _h*0.9, _w*0.94, _h*0.9, fill=self.defaultColor['axes'], tags="point")

        # Total Aixis Y
        _totalY = _h - (_kdy) - (_h*0.1)

        # Total Axis X 
        counterSteps = len(self._steps)
        if counterSteps > 0:
            _totalX = _w - (_k) - (_w*0.08) # How long is X axis?
            _dx = _totalX / len(self._steps) # X0 and X1 equal distance for all points
            # Paint Points
            counter = 0
            for i in self._steps:
                x0 = _k + (_dx*counter)
                y0 = _kdy + (_totalY - (_totalY*(i/maxY))) 
                x1 = x0 + 4
                y1 = y0 + 4
                canvas.create_oval(x0, y0, x1, y1, fill=self.defaultColor['axes'], tags="point")
                counter = counter + 1

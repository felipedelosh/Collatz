"""
FelipedelosH

Controller of graphics

"""
from Graph import *

class Controller:
    def __init__(self) -> None:
        self.graph = Graph()
        self.number = None
        self.limitInfinite = 1000
        self._steps = [] # Save in vector f(x) mouves
        self._pairs = {'pair':[], 'unpair':[]} # Counter if pair or unpair {}
        self.LOGS = ""
        self._typesOfGraphics = ['point', 'line', 'continue', 'pairs']
        self.output = "Welcome to 3x+1 plz insert value of x (eN)"
        self.defaultColor = {'bg':"black", 'fg':"red", 'visible':"green", 'axes':"blue", 'text':"yellow", 'pair': "yellow", 'unpair':"red"}


    def setNumber(self, number):
        self.number = int(number)


    def ejecuteAlgorithm(self):
        self._steps = []
        self._pairs = {'pair':[], 'unpair':[]}
        count = 0
        while count < self.limitInfinite:
            self._steps.append(self.number)
            if self.number == 1:
                self._pairs['unpair'].append(self.number)
                self.graph.addEdge(self.number, self._steps[-1], 1)
                self.output = f"Proccess is over > Steps: {count} Nodes: {len(self.graph.nodes)} Edges: {len(self.graph.edges)} Vector control: {len(self._steps)}"
                break
            elif self.number % 2 == 0:
                self._pairs['pair'].append(self.number)
                newNumber = self.number / 2
                self.graph.addEdge(self.number, newNumber, 1)
                self.number = newNumber
            else:
                self._pairs['unpair'].append(self.number)
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
        self.deletePreviousGraphics(canvas)
        if type == "point":
            self._paintPointRoute(canvas)
        elif type == "line":
            self._paintLineRoute(canvas)
        elif type == "continue":
            self._paintInCountinueMode(canvas)
        elif type == "pairs":
            self._paintPairs(canvas)

        

    def _paintPointRoute(self, canvas):
        """
        Enter a canvas and create XY point graphics
        """
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
                if len(self._steps) < 20:
                    canvas.create_text(x0, y0-5, text=str(i), fill=self.defaultColor['text'], tags="point")
                canvas.create_oval(x0, y0, x1, y1, fill=self.defaultColor['axes'], tags="point")
                counter = counter + 1


    def _paintLineRoute(self, canvas):
        """
        Enter a canvas and create XY line graphics
        """
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
        canvas.create_line(_w*0.05, _kdy, _w*0.05, _h*0.9, fill=self.defaultColor['axes'], tags="line")
        # Put labels min-middle-max
        canvas.create_text(_w*0.03, _h*0.88, text="0", fill=self.defaultColor['axes'], tags="line")
        canvas.create_text(_w*0.03, _h*0.44, text=str(maxY/2), fill=self.defaultColor['axes'], tags="line")
        canvas.create_text(_w*0.03, _kdy, text=str(maxY), fill=self.defaultColor['axes'], tags="line")
    

        # X
        _k = _w*0.05
        canvas.create_line(_k, _h*0.9, _w*0.94, _h*0.9, fill=self.defaultColor['axes'], tags="line")

        # Total Aixis Y
        _totalY = _h - (_kdy) - (_h*0.1)

        # Total Axis X 
        counterSteps = len(self._steps)
        if counterSteps > 0:
            _totalX = _w - (_k) - (_w*0.08) # How long is X axis?
            _dx = _totalX / len(self._steps) # X0 and X1 equal distance for all points
            # Paint Points
            counter = 0
            for i in range(0, counterSteps):
                try:
                    x0 = _k + (_dx*counter)
                    y0 = _kdy + (_totalY - (_totalY*(self._steps[i]/maxY)))
                    x1 =  _k + (_dx*(counter+1))
                    y1 = _kdy + (_totalY - (_totalY*(self._steps[i+1]/maxY)))
                    canvas.create_line(x0, y0, x1, y1, fill=self.defaultColor['axes'], tags="line")
                    if len(self._steps) < 20:
                        canvas.create_text(x0, y0-5, text=str(self._steps[i]), fill=self.defaultColor['text'], tags="point")
                except:
                    pass
                counter = counter + 1

    def _paintInCountinueMode(self, canvas):
        """
        Enter a canvas and show in mode one to one (+1)
        """
        _h = int(canvas['height'])
        _w = int(canvas['width'])


        # Paint Axis
        # Y
        _kdy = _h*0.1
        canvas.create_line(_w*0.05, _kdy, _w*0.05, _h*0.9, fill=self.defaultColor['axes'], tags="continue")
        # Put labels min-middle-max
        #canvas.create_text(_w*0.03, _h*0.88, text="0", fill=self.defaultColor['axes'], tags="point")
        #canvas.create_text(_w*0.03, _h*0.44, text=str(maxY/2), fill=self.defaultColor['axes'], tags="point")
        #canvas.create_text(_w*0.03, _kdy, text=str(maxY), fill=self.defaultColor['axes'], tags="point")
    

        # X
        _k = _w*0.05
        canvas.create_line(_k, _h*0.9, _w*0.94, _h*0.9, fill=self.defaultColor['axes'], tags="continue")

        # Total Aixis Y
        _totalY = _h - (_kdy) - (_h*0.1)
        # Someday i continue

    def _paintPairs(self, canvas):
        """
        
        """
        _h = int(canvas['height'])
        _w = int(canvas['width'])

        # Paint Axis
        # Y
        _kdy = _h*0.1
        canvas.create_line(_w*0.05, _kdy, _w*0.05, _h*0.9, fill=self.defaultColor['axes'], tags="pairs")
        # Put labels 
        canvas.create_text(_w*0.03, _h*0.70, text="pairs", fill=self.defaultColor['pair'], tags="pairs")
        canvas.create_text(_w*0.03, _h*0.35, text="unpairs", fill=self.defaultColor['unpair'], tags="pairs")
    
        # X
        _k = _w*0.05
        canvas.create_line(_k, _h*0.9, _w*0.94, _h*0.9, fill=self.defaultColor['axes'], tags="pairs")
        # Total Aixis X
        _totalX = _w - (_k) - (_h*0.1)

        _totalPairs = len(self._pairs['pair'])
        _totalUnpairs = len(self._pairs['unpair'])

        
        _E = (_totalPairs+_totalUnpairs)

        #paint pairs
        if _totalPairs > 0:
            x0 = _k
            y0 = _h*0.70
            x1 = _totalX * (_totalPairs/_E)
            y1 = _h*0.71
            canvas.create_rectangle(x0, y0, x1, y1, fill=self.defaultColor['pair'], tags="pairs")


        #paint unpairs
        if _totalUnpairs > 0:
            x0 = _k
            y0 = _h*0.35
            x1 = _totalX * (_totalUnpairs/_E)
            y1 = _h*0.36
            canvas.create_rectangle(x0, y0, x1, y1, fill=self.defaultColor['unpair'], tags="pairs")




    def deletePreviousGraphics(self, canvas):
        for i in self._typesOfGraphics:
            canvas.delete(i)

    
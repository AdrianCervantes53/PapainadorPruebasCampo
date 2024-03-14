from PyQt6.QtGui import QFont
import pyqtgraph as pg

class GraphClass():
    estandares = ['Suprema', 'Primera', 'Segunda', 'Tercera', 'Cuarta']
    def __init__(self, graphObject):
        self.graphObject = graphObject
        self.graphObject.setBackground((216, 216, 216))
        self.graphObject.showGrid(x=False, y=True, alpha=0.2)
        
        self.x = list(range(1,len(self.estandares)+1))

        ticks=[]
        for i, item in enumerate(self.estandares):
            ticks.append( (self.x[i], item) )
        self.ticks = [ticks]
        self.colors = [(76,165,34), (114,196,44), (255,215,26), (255,151,42), (255,86,46)]
        
        styles = {"color": "black", "font-size": "25"}
        self.graphObject.setLabel("left", "Cantidad", **styles)
        self.graphObject.setLabel("bottom", "Categoria", **styles)

        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        font.setBold(True)

        axX = self.graphObject.getAxis('bottom')
        axY = self.graphObject.getAxis('left')

        axX.label.setFont(font)
        font.setPointSize(20)
        axY.label.setFont(font)

        pen = pg.mkPen(color=(46, 47, 58))
        axX.setTextPen(pen)
        axY.setTextPen(pen)

        axX.setTickFont(QFont('Ubuntu', 16))
        axY.setTickFont(QFont('Ubuntu', 12))

        axX.setTicks(self.ticks)

        self.graphObject.hideButtons()
        
        self.graphObject.setMouseEnabled(x=False, y=False)

    def clearGraph(self):
        self.graphObject.clear()
    
    def graph(self, data):
        self.clearGraph()
        y = [data.Suprema, data.Primera, data.Segunda, data.Tercera, data.Cuarta]

        bargraph = pg.BarGraphItem(x = self.x, height = y, width = 0.5, pens=self.colors, brushes=self.colors)
        self.graphObject.setRange(rect=None, xRange=(1,5), yRange=(0, int(max(y) + max(y)*0.08)), padding=0.05, update=True, disableAutoRange=True)
        self.graphObject.addItem(bargraph)






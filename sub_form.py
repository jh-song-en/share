import os
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import pyqtSlot
import pandas as pd
import plotly.express as px
import plotly


class sub_form(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi(os.path.abspath('plot.ui'), self)
        self.ui.show()
        self.a = 0
    @pyqtSlot()
    def plot(self):
        self.a += 1
        df = pd.DataFrame([[self.a+1,2],[self.a * self.a,4]], columns=["x","y"])
        fig = px.line(df, x="x", y="x")
        fig.update_layout(
            template='plotly_white'
        )
        config = {'doubleClick': 'reset', 'displaylogo': False, 'scrollZoom': True}
        html = '<html><head><meta charset="utf-8"/><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn', config=config)
        html += '</body></html>'
        self.widget.setHtml(html)


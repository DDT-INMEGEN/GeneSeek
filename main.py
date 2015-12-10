from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

import xml.etree.ElementTree as ET

from fakedf import genes

class GeneSeek(Widget):

    def seek_summary(self):
        gene_symbol = self.ids.textinput.text


        summary = u"""
=============
**{gene_symbol}**
=============

""".format(gene_symbol=gene_symbol)

        summary = genes.get(gene_symbol, 'not found')
        
        self.ids.ficha.text = summary


class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

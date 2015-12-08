from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

import xml.etree.ElementTree as ET
import eutils.client


class GeneSeek(Widget):

    def seek_summary(self):
        gene_symbol = self.ids.textinput.text


        summary = u"""
=============
**{gene_symbol}**
=============

""".format(gene_symbol=gene_symbol)

        
        found = False

        ec = eutils.client.Client(cache_path=False)
        esr = ec.esearch(db='gene',term=gene_symbol)

        if len(esr.ids)>0:
            egs = ec.efetch(db='gene', id=esr.ids[0])        
            summary += egs.summary
            found = True
        

        if not found:
            summary += "not found!"
            
        self.ids.ficha.text = summary


class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

import xml.etree.ElementTree as ET
from Bio_Eutils import Entrez



class GeneSeek(Widget):

    def seek_summary(self):
        gene_symbol = self.ids.textinput.text
        Entrez.email = 'A.N.Other@example.com'
        pub_search = Entrez.read(Entrez.esearch(db="gene", retmax=100, term=gene_symbol + "[sym]"))
        encoded = Entrez.efetch(db='gene',  id=pub_search['IdList'], retmax=20, rettype="xml").read()
        root = ET.fromstring(encoded)

        summary = """
{gene_symbol}
=============

""".format(gene_symbol=gene_symbol)
        found = False
        
        for i in root:
            for j in i:
                if j.tag == 'Entrezgene_summary':
                    found = True
                    summary += j.text

        if not found:
            summary += "not found!"
            
        self.ids.ficha.text = summary


class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

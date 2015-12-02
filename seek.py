from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

import xml.etree.ElementTree as ET
from Bio_Eutils import Entrez



class GeneSeek(Widget):

    def do_action(self):
        Entrez.email = 'A.N.Other@example.com'
        handle = Entrez.esearch(db="gene", retmax=100, term=self.ids.textinput.text + "[sym]")
        pub_search = Entrez.read(handle)
        handle = Entrez.efetch(db='gene',  id=pub_search['IdList'], retmax=20, rettype="xml")
        encoded = handle.read()
        root = ET.fromstring(encoded)

        summary = ""
        for i in root:
            for j in i:
                if j.tag == 'Entrezgene_summary':
                    summary += j.text

        self.ids.ficha.text = summary


class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

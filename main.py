from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
import pickle

genes = pickle.load(open('fakedb.pickle','rb'))


class GeneSeek(Widget):

    def seek_summary(self):
        gene_symbol = self.ids.textinput.text


        summary = u"""
=============
**{gene_symbol}**
=============

""".format(gene_symbol=gene_symbol)

        text = ""
        for summary in genes.get(gene_symbol, 'not found'):
            if summary == 'not found':
                text = 'not found'
            else:
                text += """
                
{title}
----------------
{desc}
                
""".format(title=summary['title'],
           desc =summary['desc'])
        self.ids.ficha.text = text
            
class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
import pickle
from fakedb import genes



class GeneSeek(Widget):

    def seek_summary(self):
        gene_symbol = self.ids.textinput.text.decode(encoding='UTF-8')


        summary = u"""
=============
**{gene_symbol}**
=============

""".format(gene_symbol=gene_symbol)

        summaries = genes.get(gene_symbol, False)
        if summaries:
            text = u""
            for summary in summaries:
                text += u"""
{title}
----------------
{desc}
                
""".format(title=summary['title'],
           desc =summary['desc'])
            self.ids.ficha.text = text                
        else:
            self.ids.ficha.text = "not found"
            
class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()

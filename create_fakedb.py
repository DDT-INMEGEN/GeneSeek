from metapub import MedGenFetcher
import pickle
from time import sleep

symbols = open('hsapiens_genes_uniq.txt').readlines()
#symbols = open('aguas').readlines()

f = MedGenFetcher()

db = {}

for symbol in symbols:
    for uid in f.uids_by_term(symbol.strip()):
        c = f.concept_by_uid(uid)
        if c.definition:
            if symbol in db:
                db[symbol].append({'title': c.title,
                                   'definition': c.definition})
            else:
                db[symbol] = [{'title': c.title,
                                   'definition': c.definition},]
            sleep(1)
                
pickle.dump( db, open('hsapiens_genes_uniq.pickle', 'wb') )

#from pprint import pprint
#pprint(db)

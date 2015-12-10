from metapub import MedGenFetcher
#import pickle
from time import sleep

symbols = open('hsapiens_genes_uniq.txt').readlines()
#symbols = open('aguas').readlines()

f = MedGenFetcher()


for symbol in symbols:
    try:
        for uid in f.uids_by_term(symbol.strip()):
            c = f.concept_by_uid(uid)
            if c.definition:
                print "%s|||%s|||%s" % (symbol.strip(), c.title, c.definition)
                sleep(1)
    except:
        pass
                
#pickle.dump( db, open('hsapiens_genes_uniq.pickle', 'wb') )

#from pprint import pprint
#pprint(db)

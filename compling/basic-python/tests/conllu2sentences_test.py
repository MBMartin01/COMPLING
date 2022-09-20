import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import conllu2sentences

def testEasy():

    fname = 'fr_easy.conllu'

    sents = conllu2sentences.conllu2sents(fname)
    assert sents == ['Les nouvelles dépenses sont alimentées par le compte en banque imposant de Clinton', 
                    'Elle a parlé de son expérience à CCN Style']

def testHard():
    fname = 'fr_hard.conllu'
    sents = conllu2sentences.conllu2sents(fname)

    assert sents == ["« Alors que la plus grande partie de la transition numérique est sans précédent aux États-Unis, la transition sereine du pouvoir, elle, ne l'est pas,» a publié Kori Schulman, assistante spéciale d'Obama, dans un blog ce lundi."]


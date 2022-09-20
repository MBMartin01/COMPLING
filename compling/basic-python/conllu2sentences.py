
def conllu2sents(fname: str) -> list:
    """
    Args: 
        fname: A variable holding the name of file to read

    Returns:
        A list of sentences from the conllu file. For example, 

        With a conllu file containing, 

            # sent_id = weblog-blogspot.com_marketview_20050511222700_ENG_20050511_222700-0003
            1	Google	Google	PROPN	NNP	Number=Sing	6	nsubj	6:nsubj	_
            2	is	be	AUX	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	6	cop	6:cop	_
            3	a	a	DET	DT	Definite=Ind|PronType=Art	6	det	6:det	_
            4	nice	nice	ADJ	JJ	Degree=Pos	6	amod	6:amod	_
            5	search	search	NOUN	NN	Number=Sing	6	compound	6:compound	_
            6	engine	engine	NOUN	NN	Number=Sing	0	root	0:root	SpaceAfter=No

            # sent_id = weblog-blogspot.com_marketview_20050511222700_ENG_20050511_222700-0006
            1	Is	be	AUX	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	5	cop	5:cop	_
            2	that	that	PRON	DT	Number=Sing|PronType=Dem	5	nsubj	5:nsubj	_
            3	a	a	DET	DT	Definite=Ind|PronType=Art	5	det	5:det	_
            4	money	money	NOUN	NN	Number=Sing	5	compound	5:compound	_
            5	maker	maker	NOUN	NN	Number=Sing	0	root	0:root	SpaceAfter=No

        The function should return:
            ['Google is a nice search engine', 'Is that a money maker']

    Hints:

        Notice the new line between entries (which contain sentences). 
        Notice the use of # as marking comments.
        Notice that the column(s) you need to consider.

        In the hard cases, you will see punctuation. For example, 

            # sent_id = weblog-blogspot.com_marketview_20050511222700_ENG_20050511_222700-0006
            1	Is	be	AUX	VBZ	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	5	cop	5:cop	_
            2	that	that	PRON	DT	Number=Sing|PronType=Dem	5	nsubj	5:nsubj	_
            3	a	a	DET	DT	Definite=Ind|PronType=Art	5	det	5:det	_
            4	money	money	NOUN	NN	Number=Sing	5	compound	5:compound	_
            5	maker	maker	NOUN	NN	Number=Sing	0	root	0:root	SpaceAfter=No
            6	?	?	PUNCT	.	_	5	punct	5:punct	_

        You should return: 
            ['Is that a money maker?']
        Notice that there is no space between maker and ?. Is this marked in the columns somewhere?

    """
    pass


if __name__ == '__main__':

    fname = 'fr_easy.conllu'
    sents = conllu2sents(fname)
    print(sents)

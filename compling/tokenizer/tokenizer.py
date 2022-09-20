import re #Python regular expressions (may be useful)
import string
from typing_extensions import Self
from xml.dom.expatbuilder import theDOMImplementation #Python string library
import torch #pytorch
from typing import Union, Dict, List, Tuple

from tokeniclearzer import Tokenizer

import torch



class Tokenizer:
    """
    A class for tokenzing text for input to a model. 

    Attributes:
        word2idx (dict): A dictionary mapping tokens (string) to id.
        idx2word (dict): A list which associates ids with tokens 
                         (e.g., idx2word[9] returns token with id 9). 
        maxSequenceLength (int): Maximum length of text. Default is 1024.
        unk_token (str): Token for unknown tokens. Default is <unk>.
        unk_token_id (int): Token id for unknown tokens.
        eos_token (str): Start or end of sequence token. Default is <eos>.
        eos_token_id (int): Token id for eos token.
        mask_token (str): Mask token (for masked language models). 
                          Default is <mask>. 
        mask_token_id (int): Token id for mask token.
        pad_token (str): Token for padding. Default is <pad>.
        pad_token_id (int): Token id for mask token.
        add_special_tokens (bool): Whether to add eos tokens to start 
                                   and end of sequence when __call__. 
                                   Default is True.
        lower (bool): Whether to lowercase text
        padding (bool): Whether to pad (when applicable) when __call__.
                        Default is True.
        truncate (bool): Whether to right truncate when sequence length
                         is greater than maxSequenceLength when __call__.
                         Default is True.
        return_tensors (str): Return type of encoding when __call__ 
                              (either "pt" for torch.Tensor or None for list). 
                              Default is "pt".

    """

    def __init__(self,
        maxSequenceLength = 1024,
        unk_token="<unk>", 
        eos_token='<eos>', 
        mask_token='<mask>', 
        pad_token = '<pad>', 
        add_special_tokens = True, 
        lower = True,
        padding = True, 
        truncate = True, 
        return_tensors = 'pt'):

        self.word2idx = dict()
        self.idx2word = []
        self.unk_token = unk_token
        self.eos_token = eos_token
        self.mask_token = mask_token
        self.pad_token = pad_token
        self.maxSequenceLength = maxSequenceLength

        self.add_special_tokens = add_special_tokens
        self.lower = lower
        self.padding = padding
        self.truncate = truncate
        self.return_tensors = return_tensors


    def __len__(self):
        """
        Sets len operator for the class to number of tokens in vocab.
        """
        return len(self.idx2word)


    def __call__(self, 
            text: Union[str, List[str]]) -> Union[int, List[int], torch.Tensor]:
        """
        Sets call operator for the class to be encode. Thus, 
        tokenizer(text, ...) is equivalent to tokenizer.encode(text, ...)
        """
    

        return self.encode(text,
            add_special_tokens = self.add_special_tokens, 
            padding = self.padding, 
            truncate = self.truncate, 
            return_tensors = self.return_tensors)

    @property
    def unk_token_id(self):
        """
        Fixes self.unk_token_id
        """
        if self.unk_token not in self.word2idx:
            return None
        return self.word2idx[self.unk_token]

    @property
    def eos_token_id(self):
        """
        Fixes self.eos_token_id
        """
        if self.eos_token not in self.word2idx:
            return None
        return self.word2idx[self.eos_token]

    @property
    def mask_token_id(self):
        """
        Fixes self.mask_token_id
        """
        if self.mask_token not in self.word2idx:
            return None
        return self.word2idx[self.mask_token]

    @property
    def pad_token_id(self):
        """
        Fixes self.pad_token_id
        """
        if self.pad_token not in self.word2idx:
            return None
        return self.word2idx[self.pad_token]

    #TODO
    def save_tokenizer(self, outname: str):
        """
        Save the tokenizer to a plain txt file named outname. 
        Format the file such that each line has one token and 
        the line number corresponds to the index of that token.

        For example, 
            assuming we have self.idx2word = ['the', 'cat']
            outname should contain:
            the
            cat
        """
        #TODO: Your code goes here 

        def save_tokenizer(self, outname: str):
            'the'
            'cat'
        return self.word2idx[save_tokenizer]



        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def load_tokenizer(self, vocabfname: str):
        """
        Load a tokenizer from a plain txt file name vocabfname
        (i.e. the output of save_tokenizer). 
        That is, we assume the format is such 
        that each line has one token with the line in the file 
        the index of the token in the vocabulary (counting from 0). 
        You should update both word2idx and idx2word!

        For example, 
            >>> from tokenizer import Tokenizer
            >>> tokenizer = Tokenizer()
            >>> tokenizer.load_tokenizer('ToyVocab.txt')
            >>> tokenizer.word2idx
            >>> {'the': 0, 'a': 1, 'cat': 2, 'loves': 3, 'eats': 4, 'food': 5, 
            ...      '.': 6, '!': 7, '<unk>': 8, 
            ...      '<eos>': 9, '<pad>': 10, '<mask>': 11}

            >>> tokenizer.idx2word
            >>> ['the', 'a', 'cat', 'loves', 'eats', 'food', '.', '!', '7', 
            ... '<unk>', '<eos>', '<pad>', '<mask>']

        """
        #TODO: Your code goes here 
def load_tokenizer(self, vocabfname: str): 
        'the'
        'cat'
        return Self.word2idx[load_tokenizer]


from tokenizer import Tokenizer
tokenizer = Tokenizer()
tokenizer.load_tokenizer

        #Delete the following line when implementing your function
        #raise NotImplementedError

    #TODO
   # def preprocess(self, text: str) -> str:
        """
        Preprocess the text for use by tokenizer. It should 
        separate punctuation (!"#$%&'()*+,-./\\:;=?@[]^_`{|}~) 
        from words, lowercase the input (if specified with 
        self.lower), and remove any newline 
        characters, trailing spaces, or extra spaces. 
        Take care that the punctuation does not include < or >, 
        so that the special tokens (e.g., <unk>)
        are not modified.

        Args:
            text (str): Text to be input to the tokenizer.

        Returns:
            str: Preprocessed text

        For example, 
            >>> from tokenizer import Tokenizer
            >>> tokenizer = Tokenizer()
            >>> tokenizer.preprocess(" the man, who is tall, is happy!\n")
            >>> "the man , who is tall , is happy !"
            >>> tokenizer.preprocess(" The <unk> cat loves to buy food; I love him? \n\n")
            >>> "the <unk> cat loves to buy food ; i love him ?"

        Hints: 
            For handling punctuation, you may consider using 
            regular expressions using pythons re package or
            the string functions translate and maketrans. 
            Consider, for example, wanting to replace B with ABC: 
            >>> text = 'CD B EF'
            >>> re.sub('B', r'ABC', text)
            >>> 'CD ABC EF'
            ...
            >>> text = 'CD B EF'
            >>> table = {'B': "ABC"}
            >>> text.translate(str.maketrans(table))
            >>> 'CD ABC EF'
        """
        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def tokenize(self, text: str) -> List[int]:
        """
        Takes a string a returns a list of tokens. Tokens are defined
        as space delineated characters. 

        Args: 
           text (str): text to be input to tokenizer.

        Returns:
            List[str]: A list of strings (words).

        For example, 
            >>> from tokenizer import Tokenizer
            >>> tokenizer = Tokenizer()
            >>> tokenizer.tokenize("the man , who is tall , is happy !")
            >>> ["the", "man", ",", "who", "is", "tall", ",", "is", "happy", "!"]
        """

        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def convert_tokens_to_ids(self, 
            tokens: Union[str, List[str]]) -> Union[int, List[int]]:
        """
        Takes a string (a token) or a list of strings 
        (tokens; output of tokenize) and returns the id(s) of the token(s). 
        If the token is not in the vocabulary return the unk token id.

        Args:
            tokens (str, List[str]): Token or list of tokens to be converted to ids. 

        Returns:
            int | List[int]: The id of the token or a list of the ids of the tokens.  

        For example, 
            assuming that self.word2idx = {'the': 0, 'cat': 1, '<unk>': 2}
            >>> tokenizer.convert_tokens_to_ids("the")
            >>> 0
            >>> tokenizer.convert_tokens_to_ids(["the", "cat"])
            >>> [0, 1]
            >>> tokenizer.convert_tokens_to_ids(["the", "cat", "sleeps"])
            >>> [0, 1, 2]

        Hint: 
            Consider using the built-in function type
            Use word2idx

        """
        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def encode(self, text: Union[str, List[str]], 
            add_special_tokens: bool = False, 
            padding:bool = False, 
            truncate:bool = False, 
            return_tensors: str = None) -> Union[List[int], List[List[int]], torch.Tensor]:
        """
        Take input text, preprocess it, tokenize it, add special 
        tokens (if specified), pad to the maximum length in the batch 
        (if a batch and specified), truncate if longer than maximum length
        (if specified), and return the ids in the tokenizer. 
        Padding will be crucial for returning pytorch tensor. 

        Args:
            text (str, List[str]): Input text or batch of texts. 
            add_special_tokens (bool): Whether to add <eos> to 
                                       beginning and end of text.
                                       Default is False
            padding (bool): Whether to pad to the maximum length 
                            in the batch. Default is False.
            truncate (bool): Whether to truncate input if it exceeds 
                             maxSequenceLength (truncate from the right). 
                             Default is False.
            return_tensors (str): Type of return. None returns a int 
                                  or List of ints. "pt" returns a 
                                  pytorch Tensor of shape: 
                                  (batch_size, seq length) or
                                  just (sequence length,) if not a batch. 
                                  Note: Padding will be critical for 
                                  uneven batches! Default is None.

        Returns:
            List[int] | List[List[int]] | torch.Tensor: The encoding of the text or 
                                            batch of texts by the tokenizer.

        For example, 
            assuming word2idx = {'the':0, 'cat':1, 'eats':2, '<pad>':3, '<eos>':4}
            and maxSequenceLength = 5

            >>> text = "the"
            >>> tokenizer.encode(text)
            >>> [0]
            >>> text = "the cat"
            >>> tokenizer.encode(text)
            >>> [0, 1]
            >>> tokenizer.encode(text, add_special_tokens=True)
            >>> [4, 0, 1, 4]
            >>> text = ['the cat', 'the cat eats']
            >>> tokenizer.encode(text)
            >>> [[0, 1], [0, 1, 2]]
            >>> tokenizer.encode(text, padding=True, return_tensors='pt')
            >>> tensor([[0, 1, 4], [0, 1, 2]])
            >>> text = 'the cat eats the cat'
            >>> tokenizer.encode(text, truncate=True, add_special_tokens=True)
            >>> [4, 0, 1, 2, 4]
        """

        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def convert_ids_to_tokens(self, 
            ids: Union[int, List[int]]) -> Union[str, List[str]]:
        """
        Takes an id or a list of ids and returns the token(s) 
        corresponding to those ids. 

        Args:
            ids (int, List[int]): id or list of ids

        Returns:
            str | List[str]: The token or list of tokens corresponding to the ids.

        For example, 
            assuming that self.word2idx = {'the': 0, 'cat': 1, '<unk>': 2}
            >>> tokenizer.convert_ids_to_tokens(0)
            >>> "the"
            >>> tokenizer.convert_ids_to_tokens([0, 1])
            >>> ["the", "cat"]
            >>> tokenizer.convert_ids_to_tokens([0, 1, 2])
            >>> ["the", "cat", "<unk>"]

        Hint: 
            Use idx2word
        """
        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def decode(self, 
            ids: Union[List[int], List[List[int]], torch.Tensor]) -> Union[List[str], List[List[str]]]:
        """
        Takes ids (a list of ids or a batch of ids) and returns 
        the tokens corresponding to those ids (as a list of a batch). 

        Args:
            ids (List[int] | List[List[int]] | torch.Tensor): The ids as a list, batch, or tensor.

        Returns:
            List[str] | List[List[str]]: The tokens or batch of tokens. 

        For example, 
            assuming word2idx = {'the':0, 'cat':1, 'eats':2, '<pad>':3, '<eos>':4}

            >>> ids = [0, 1]
            >>> tokenizer.decode(ids)
            >>> ['the', 'cat']
            >>> ids = torch.tensor([[0, 1, 2], [0, 0, 0]])
            >>> tokenizer.decode(ids)
            >>> [['the', 'cat', 'eats'], ['the', 'the', 'the']]

        """
        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError

    #TODO
    def create_vocab(self, fname: str, 
            freqThreshold: int = 30, 
            addSpecialTokens: bool = True): 
        """
        Create a vocabulary for the tokenizer from a file name 
        (called fname). Only keep words that occur more than 
        freqThreshold and, if specified, add special tokens 
        (<unk>, <pad>, <mask>, <eos>). Make sure you use 
        the same preprocessing and tokenization scheme
        (e.g., how should you treat "this?"). Words
        should be added both to word2idx and idx2word.  

        Args:
            fname (str): Name of file to build vocabulary from.
            freqThreshold (int): Threshold of frequency for 
                                 inclusion in vocabulary. 
                                 Default is 30.
            addSpecialTokens (bool): Whether to add special tokens to 
                                     the vocabulary. Default is True.

        For example, suppose we have a file, called "cat.txt",
        with the following text (the specific ids can vary depending 
        on how you do this):

        The cat jumps over the other cat. The other cat was
        unhappy, and as we know, an unhappy cat is one 
        that never jumps over anything again.

        >>> tokenizer = Tokenizer()
        >>> tokenizer.create_vocab("cat.txt", freqThreshold=1, addSpecialTokens=False)
        >>> tokenizer.word2idx
        >>> {'the': 0, "cat": 1, "jumps": 2, "over": 3, 
        ...     "other": 4, ".": 5, "unhappy": 6, ",": 7}

        """
        #Reset (do not remove this)
        self.word2idx = {}
        self.idx2word = []

        #TODO: Your code goes here 

        #Delete the following line when implementing your function
        raise NotImplementedError


if __name__ == "__main__":

    tokenizer = Tokenizer(maxSequenceLength=5)
    ##Try out your tokenizer below


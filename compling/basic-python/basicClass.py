class Word:
    """
    A class word manipulating words.

    Attributes:
        vowels (set): (class attribute) A set of all vowels
        text (str): Text of the word 
    """

    #A variable shared by all instances of the class
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    def __init__(self, text):
        #self identifies the instance of class and can be used
        #to reference the variables of a specific instance of 
        #a class. So for an instance W of Word, W.text will 
        #return the text of that W. Within the class methods
        #self.text can be used to pick out the text of the instance.
        self.text = text

    def whereAreTheVowels(self):
        """
        A function that returns the position of the vowels in the word.

        Returns:
            list: A list of the positions of the vowels in the word.

        """
        where = []
        #enumerate is a built in function which yields the 
        #index of the element in a list and also the element
        #E.g., enumerate([a, b, c]) -> [(0, a), (1, b), (2, c)]
        #A cavet is enumerate is a generator so its return type
        #isn't exactly a list. We ignore this for now.
        #Here we loop through each character in self.text
        for position, letter in enumerate(self.text):
            #Checks if the letter is contained in the set 
            #vowels, if so, we append the position to where
            if letter in Word.vowels:
                where.append(position)
        #retun this list
        return where

"""
Below you should make a class called Linguist which has two attributes: 
    name: the name of the linguist
    advisor: the name of their advisor

Additional the class should have one function, addUniversity which takes 
a string and adds to the class (via self) a variable uni which contains 
this string. 

For example, consider the following expected behavior:

    >>> name = 'Forrest'
    >>> advisor = 'Marten'
    >>> davis = Linguist(name, advisor)
    >>> davis.name
    >>> "Forrest"
    >>> gradSchool = 'Cornell'
    >>> davis.addUniversity(gradSchool)
    >>> davis.uni
    >>> "Cornell"

"""

if __name__ == '__main__':
    text = 'strawberry'
    word = Word(text)
    print(word.text)
    vowelPos = word.whereAreTheVowels()
    print(vowelPos)

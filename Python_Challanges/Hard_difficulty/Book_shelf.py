class Book:
    #constructor
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
    #methods
    def getTitle(self):
        return 'Title: {}'.format(self.__title)
    def getAuthor(self):
        return 'Author: {}'.format(self.__author)


#create Book objects
PP = Book('Pride and Prejudice','Jane Austen')
H = Book('Hamlet','William Shakespeare')
WP = Book('War and peace','Leo Tolstoy')

#Test
print(PP.getTitle(),' -- ',PP.getAuthor())
print(H.getTitle(),' -- ',H.getAuthor())
print(WP.getTitle(),' -- ',WP.getAuthor())
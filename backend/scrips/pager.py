class Pager: 
    def __init__(self, initialsoup):
        self._soup               = initialsoup
        self._nextpageidentifier = self.nextpageidentifier()
        
    @property
    def soup(self):
        return self._soup   
     
    @soup.setter
    def soup(self, soup):
        self.soup = soup
        
    
    def nextpageidentifier(self, builder):
        
        #Solo properati
        
        soup = self.soup
        listelempagination = soup.find_all('a', class_='pagination__link')
        elempagination     = listelempagination[-1]
        
        print(elempagination)
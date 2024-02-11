
class WebsiteData:
    
    def __init__(self, swid, title, desc, price, exchange, img, location, linktowebsite, category, residence):
        self._swid          = swid
        self._title         = title
        self._desc          = desc
        self._price         = price
        self._exchange      = exchange
        self._img           = img
        self._location      = location
        self._linktowebsite = linktowebsite
        self._category      = category
        self._residence     = residence
        
    def toJson(self):
        
        json = {
            "swid"  : self._swid,
            "titulo": self._title,
            "descripcion": self._desc,
            "precio": self._price,
            "cambio": self._exchange,
            "img": self._img,
            "ubicacion": self._location,
            "link": self._linktowebsite,
            "categoria": self._category,
            "residencia": self._residence
        }
        
        return json
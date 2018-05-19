import xml.sax

class RainHandler( xml.sax.ContentHandler ) :
    def __int__(self):
        self.CurrentData = ""
        self.lat = ""
        self.lon = ""
        self.locationName = ""
        self.stationId = ""
    
    #element start event processing
    def startElement(self, tag, attributes) :
        self.CurrentData = tag
        if tag == "location":
            print ("*********location*******")
    
    #element end event processing
    def endElement(self, tag):
        if self.CurrentData == "lat":
            print ("Lat:", self.lat)
        elif self.CurrentData == "lon":
            print ("Lot", self.lon)
        elif self.CurrentData == "locationName":
            print ("LocationName:", self.locationName)
        elif self.CurrentData == "stationId":
            print ("stationId: ", self.stationId)
        self.CurrentData = ""
    
    #content event processing
    def characters( self, content):
        if self.CurrentData == "lat":
            self.lat = content
        elif self.CurrentData == "lon":
            self.lon = content
        elif self.CurrentData == "locationName":
            self.locationName = content
        elif self.CurrentData == "stationId":
            self.stationId = content
        
if( __name__ == "__main__"):

    #創建一個 XMLReader
    parser = xml.sax.make_parser()

    #turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    #重寫ContextHandler
    Handler = RainHandler()
    parser.setContentHandler( Handler )

    parser.parse("rain_data.xml")



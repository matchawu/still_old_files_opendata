import requests
import Loca

r = requests.get("http://opendata2.epa.gov.tw/AQI.json")

# print(r.json())

class  Loca( object ):
    def  __init__( self ,SiteName,County,AQI):
        self .SiteName =  SiteName
        self .County =  County
        self .AQI = AQI
    def  __repr__( self ):
        return  'Loca Object SiteName : %s , County : %s , AQI: %d' % ( self .SiteName, self .County,  self .AQI)
if  __name__   ==  '__main__' :
    p =  Loca( 'Peter' , 22 )
    print(p)
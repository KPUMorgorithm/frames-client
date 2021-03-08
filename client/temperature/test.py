from ctypes import cdll
 
class Temperature(object):
 
    def __init__( self ):
 
        self.lib = cdll.LoadLibrary('./temperature.dll')
        self.obj = self.lib.Temperature_new()
 
    def check( self ):
 
        self.lib.Temperature_check( self.obj )
 
if __name__ == '__main__':
 
    f = Temperature()
    f.check()


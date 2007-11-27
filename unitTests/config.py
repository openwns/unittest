# import the openWNS module. Contains all sub-classes needed for
# configuration of openWNS
import openwns.OpenWNS

# create an instance of the openWNS configuration
# The variable must be called WNS!!!!
WNS = openwns.OpenWNS.OpenWNS()

WNS.masterLogger.enabled = False

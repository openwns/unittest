# import the openWNS module. Contains all sub-classes needed for
# configuration of openWNS
moduleList = ["constanze", "simpleTL", "dll", "rise", "ofdmaphy", "wifimac", "ip", "wimac", "tcp", "copper", "glue"]

import openwns

for module in moduleList:
    try:
	__import__(module)
    except ImportError:
	print "C++ Unit Test Warning: Module " + module + " is not available\n"
	

simulator = openwns.Simulator()

simulator.environment.masterLogger.enabled = False

simulator.outputStrategy = openwns.simulator.OutputStrategy.DELETE
simulator.masterLogger.enabled = False

openwns.setSimulator(simulator)

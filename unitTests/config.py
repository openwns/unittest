# import the openWNS module. Contains all sub-classes needed for
# configuration of openWNS
import openwns

simulator = openwns.Simulator()

simulator.environment.masterLogger.enabled = False

openwns.setSimulator(simulator)

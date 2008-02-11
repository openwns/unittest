# import the openWNS module. Contains all sub-classes needed for
# configuration of openWNS
import openwns
# this is a project which shows how to write a loadable module to extend openWNS
import projname

simulator = openwns.Simulator()

simulator.environment.masterLogger.enabled = False

openwns.setSimulator(simulator)

from mininet.topo import Topo

class OFTEIN(Topo):
    "OF@TEIN Testbed Topology"

    def __init__(self):
        "Create OF@TEIN Testbed Topology"

        # Initialize topology
        Topo.__init__(self)

        # TODO: Add controller

        # Create switches
        switchMY = self.addSwitch("SW_MY_1")
        switchKR = self.addSwitch("SW_KR_1")
        switchTW = self.addSwitch("SW_TW_1")

        # Create hosts
        # TODO: Define custom IP addresses

        hostMY = []
        hostMY.append(self.addHost("MY1"))
        hostMY.append(self.addHost("MY2"))

        hostKR = []
        hostKR.append(self.addHost("KR1"))
        hostKR.append(self.addHost("KR2"))

        hostTW = []
        hostTW.append(self.addHost("TW1"))
        hostTW.append(self.addHost("TW2"))

        # Create host links
        for h in hostMY:
            self.addLink(switchMY, h)

        for h in hostKR:
            self.addLink(switchKR, h)

        for h in hostTW:
            self.addLink(switchTW, h)

        # Create switch links (Broadcast Storm Alert)
        self.addLink(switchMY, switchKR)
        self.addLink(switchKR, switchTW)
        self.addLink(switchTW, switchMY)

topos = { 'oftein' : OFTEIN }
from mininet.topo import Topo

class TENANTS(Topo):
    "OF@TEIN Testbed Topology with 3 Tenants (A, B, C)"

    def __init__(self):
        "Create OF@TEIN Testbed Topology with 3 Tenants(A, B, C)"

        # Initialize topology
        Topo.__init__(self)

        # TODO: Add controller

        # Create switches
        switchMY = self.addSwitch("SW_MY_1")
        switchKR = self.addSwitch("SW_KR_1")
        switchTW = self.addSwitch("SW_TW_1")

        # Create hosts

        hostMY = []
        hostMY.append(self.addHost("A1", ip='10.0.0.1/8', mac="00:00:00:00:00:01"))
        hostMY.append(self.addHost("B1", ip='10.0.0.1/8', mac="00:00:00:00:00:01"))
        hostMY.append(self.addHost("C1", ip='192.168.1.1/24', mac="00:00:00:00:00:01"))

        hostKR = []
        hostKR.append(self.addHost("A2", ip='10.0.0.2/8', mac="00:00:00:00:00:02"))
        hostKR.append(self.addHost("B2", ip='10.0.0.2/8', mac="00:00:00:00:00:02"))

        hostTW = []
        hostTW.append(self.addHost("A3", ip='10.0.0.3/8', mac="00:00:00:00:00:03"))
        hostTW.append(self.addHost("C2", ip='192.168.1.2/24', mac="00:00:00:00:00:02"))

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

topos = { 'tenants' : TENANTS }
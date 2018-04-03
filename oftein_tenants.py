from mininet.topo import Topo

class TENANTS(Topo):
    "OF@TEIN Testbed Topology with 3 Tenants (A, B, C)"

    def __init__(self, **opts):
        "Create OF@TEIN Testbed Topology with 3 Tenants(A, B, C)"

        # Initialize topology
        Topo.__init__(self, **opts)

        # TODO: Add controller

        # Create switches
        switches = []
        switches.append(self.addSwitch("SW_MY_1", dpid="1122334455667701", protocols="OpenFlow13"))
        switches.append(self.addSwitch("SW_KR_1", dpid="1122334455667702", protocols="OpenFlow13"))
        switches.append(self.addSwitch("SW_TW_1", dpid="1122334455667703", protocols="OpenFlow13"))

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
            self.addLink(switches[0], h)

        for h in hostKR:
            self.addLink(switches[1], h)

        for h in hostTW:
            self.addLink(switches[2], h)

        # Create switch links (Broadcast Storm Alert)
        self.addLink(switches[0], switches[1])
        self.addLink(switches[1], switches[2])
        self.addLink(switches[2], switches[0])

topos = { 'tenants' : TENANTS }

# sudo mn --custom oftein_tenants.py --topo tenants --controller remote,ip=<IP Address>
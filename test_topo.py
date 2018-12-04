from mininet.topo import Topo

class TEST(Topo):

    def __init__(self, **opts):

        # Initialize topology
        Topo.__init__(self, **opts)

        # TODO: Add controller

        # Create switches
        switches = []
        switches.append(self.addSwitch("S1", dpid="1122334455667701", protocols="OpenFlow13"))
        switches.append(self.addSwitch("S2", dpid="1122334455667702", protocols="OpenFlow13"))
        switches.append(self.addSwitch("S3", dpid="1122334455667703", protocols="OpenFlow13"))
        switches.append(self.addSwitch("S4", dpid="1122334455667704", protocols="OpenFlow13"))

        # Create hosts
        hostS1 = []
        hostS1.append(self.addHost("A1", ip='10.0.0.1/8', mac="0A:00:00:00:00:01"))
        hostS1.append(self.addHost("B1", ip='10.0.0.1/8', mac="0B:00:00:00:00:01"))
        hostS1.append(self.addHost("A2", ip='192.168.1.1/24', mac="0A:00:00:00:0A:01"))
        hostS1.append(self.addHost("B2", ip='172.16.31.1/24', mac="0B:00:00:00:0A:01"))

        hostS4 = []
        hostS4.append(self.addHost("A3", ip='10.0.0.2/8', mac="0A:00:00:00:00:02"))
        hostS4.append(self.addHost("B3", ip='10.0.0.2/8', mac="0B:00:00:00:00:02"))
        hostS4.append(self.addHost("A4", ip='192.168.1.2/24', mac="0A:00:00:00:0A:02"))
        hostS4.append(self.addHost("B4", ip='172.16.31.2/24', mac="0B:00:00:00:0A:02"))

        # Create host links
        for h in hostS1:
            self.addLink(switches[0], h)

        for h in hostS4:
            self.addLink(switches[3], h)

        # Create switch links (Broadcast Storm Alert)
        self.addLink(switches[0], switches[1])
        self.addLink(switches[0], switches[2])
        self.addLink(switches[1], switches[3])
        self.addLink(switches[2], switches[3])

topos = { 'test' : TEST}

# sudo mn --custom oftein_tenants.py --topo test --controller remote,ip=<IP Address>
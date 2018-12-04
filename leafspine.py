from mininet.topo import Topo

class LEAFSPINE(Topo):

    def __init__(self, **opts):

        # Initialize topology
        Topo.__init__(self, **opts)

        # Create switches
        switches = []
        switches.append(self.addSwitch("S1", dpid="1122334455667701", protocols="OpenFlow13"))
        switches.append(self.addSwitch("S2", dpid="1122334455667702", protocols="OpenFlow13"))
        switches.append(self.addSwitch("L1", dpid="1122334455667711", protocols="OpenFlow13"))
        switches.append(self.addSwitch("L2", dpid="1122334455667722", protocols="OpenFlow13"))
        switches.append(self.addSwitch("L3", dpid="1122334455667733", protocols="OpenFlow13"))
        switches.append(self.addSwitch("L4", dpid="1122334455667744", protocols="OpenFlow13"))

        # Create hosts
        hostsL1 = []
        hostsL1.append(self.addHost("A1", ip='10.0.0.1/8', mac="0A:00:00:00:01:01", defaultRoute = "via 10.0.0.254"))
        hostsL1.append(self.addHost("A2", ip='192.168.1.1/24', mac="0A:00:00:00:02:01", defaultRoute = "via 192.168.1.254"))
        hostsL1.append(self.addHost("B1", ip='10.0.0.1/8', mac="0B:00:00:00:01:01", defaultRoute="via 10.0.0.254"))

        hostsL2 = []
        hostsL2.append(self.addHost("A3", ip='10.0.0.2/8', mac="0A:00:00:00:01:02", defaultRoute="via 10.0.0.254"))
        hostsL2.append(self.addHost("B2", ip='192.168.1.1/24', mac="0B:00:00:00:02:01", defaultRoute="via 192.168.1.254"))
        hostsL2.append(self.addHost("B3", ip='172.16.0.1/16', mac="0B:00:00:00:03:01", defaultRoute="via 172.16.0.254"))

        hostsL3 = []
        hostsL3.append(self.addHost("A4", ip='192.168.1.2/24', mac="0A:00:00:00:02:02", defaultRoute="via 192.168.1.254"))
        hostsL3.append(self.addHost("B4", ip='10.0.0.2/8', mac="0B:00:00:00:01:02", defaultRoute="via 10.0.0.254"))
        hostsL3.append(self.addHost("B5", ip='192.168.1.2/24', mac="0B:00:00:00:02:02", defaultRoute="via 192.168.1.254"))

        hostsL4 = []
        hostsL4.append(self.addHost("A5", ip='10.0.0.3/8', mac="0A:00:00:00:01:03", defaultRoute="via 10.0.0.254"))
        hostsL4.append(self.addHost("A6", ip='192.168.1.3/24', mac="0A:00:00:00:02:03", defaultRoute="via 192.168.1.254"))
        hostsL4.append(self.addHost("B6", ip='172.16.0.2/16', mac="0B:00:00:00:03:02", defaultRoute="via 172.16.0.254"))

        # Create host links
        for h in hostsL1:   self.addLink(switches[2], h)
        for h in hostsL2:   self.addLink(switches[3], h)
        for h in hostsL3:   self.addLink(switches[4], h)
        for h in hostsL4:   self.addLink(switches[5], h)

        # Create switch links
        self.addLink(switches[0], switches[1])  # S1 - S2
        self.addLink(switches[0], switches[2])  # S1 - L1
        self.addLink(switches[0], switches[3])  # S1 - L2
        self.addLink(switches[0], switches[4])  # S1 - L3
        self.addLink(switches[0], switches[5])  # S1 - L4
        self.addLink(switches[1], switches[2])  # S2 - L1
        self.addLink(switches[1], switches[3])  # S2 - L2
        self.addLink(switches[1], switches[4])  # S2 - L3
        self.addLink(switches[1], switches[5])  # S2 - L4

topos = { 'leafspine' : LEAFSPINE }

# sudo mn --custom leafspine.py --topo leafspine --controller remote,ip=127.0.0.1
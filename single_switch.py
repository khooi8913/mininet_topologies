from mininet.topo import Topo

class SingleSwitch(Topo):
    "Single switch topology with k hosts"

    def __init__(self, k=2):
        "Create custom topology"

        # Initialize topology
        Topo.__init__(self)

        # Add switch
        switch = self.addSwitch("s1")

        # Add hosts
        hosts = [self.addHost("h%d" % i) for i in range(1, k + 1)]

        # Add links
        for h in hosts:
            self.addLink(switch, h)

topos = { 'single_switch': SingleSwitch }

import os
import subprocess

list_of_networks = []
working = True
class Router:
    def __init__(self, router_name, MAC_address, security):
        self.name = router_name
        self.MAC = MAC_address
        self.security = security

while working == True:


    option = raw_input("1. Scan nearby networks. \n2. Print networks. \n3. Scan, join, and login to router of unprotected networks. \n4. Quit\n")
    if int(option) == 1:
        output  = os.popen('airport scan').readlines()
        for line in output[1:]:
            network_attributes = line.split()
            security_on_router = network_attributes[-1]
            MAC_address = network_attributes[-6]
            router_name = " ".join(network_attributes[0:-6])
            router = Router(router_name, MAC_address, security_on_router)
            list_of_networks.append(router)
        print "Networks scanned"


    if int(option) == 2:
        for router in list_of_networks:
            print router.name + " | " + router.MAC + " | " + router.security


    if int(option) == 3:
        test = subprocess.Popen(["networksetup" , "-setairportnetwork", "en1", "test"], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        joined_network = False
        if output != "Could not find network test.\n":
            joined_network = True

    if int(option) == 4:
        working = False

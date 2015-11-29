import os
import subprocess

#initalizing a list for us to store the routers we find
list_of_networks = []
running = True

#A class that contains the structure for the information we can pull from the routers using Airport
class Router:
    def __init__(self, router_name, MAC_address, security):
        self.name = router_name
        self.MAC = MAC_address
        self.security = security

#Keep looping until user wants to quit
while running == True:
    #inital option prompt
    option = raw_input("1. Scan nearby networks. \n2. Print networks. \n3. Scan, join, and login to router of unprotected networks. \n4. Quit\n")
    #Scans network and stores router info
    if int(option) == 1:
        #Calls on airport
        #Requires a symbolic link to Airport
        output  = os.popen('airport scan').readlines()
        for line in output[1:]: #ignoring header line
            network_attributes = line.split()
            security_on_router = network_attributes[-1]
            MAC_address = network_attributes[-6]
            router_name = " ".join(network_attributes[0:-6]) #joins together network names with spaces
            router = Router(router_name, MAC_address, security_on_router)
            list_of_networks.append(router)
        print "Networks scanned"

    #Displays router info
    #Would like to do pretty formatting with headers in the future
    if int(option) == 2:
        for router in list_of_networks:
            print router.name + " | " + router.MAC + " | " + router.security

    #Joins unsecured networks
    if int(option) == 3:
        test = subprocess.Popen(["networksetup" , "-setairportnetwork", "en1", "test"], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        joined_network = False
        if output != "Could not find network test.\n":
            joined_network = True

    #Quits program
    if int(option) == 4:
        running = False

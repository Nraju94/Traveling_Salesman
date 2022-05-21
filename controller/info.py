"""
@author: Raj Gouravelli
Student index : OD51572
"""

import csv
from model.notification import Notification
from model.locations import Location
from model.packets import Packet
from model.path import Path
from controller.ht import HT



class Info:
    """
    A utility class that handles importing files and making it available to the program
    """


    def __init__(self):
        """
        Initializes the Info class, calls the 'read' methods
        """
        self.locs, self.packets, self.paths, self.notifications = HT(), HT(), HT(), HT()

        self.locs_count, self.packets_count, self.notification_count = 0, 0, 0

        self.access_locs()
        self.access_packets()
        self.access_paths()
        self.access_notifications()


    def access_locs(self):
        """
        Creates a Location object for each location in the imported csv file,
        then stores the Location objects in a hash table. Each Location object
        includes an adjacency list containing length to each other location
        :return:
        :rtype:
        """
        with open('files/locations.csv') as loccsv:
            file_read = csv.reader(loccsv, delimiter='\t')

            for r in file_read:
                index = int(r[0])
                location_detail = r[1]
                length = [float(r[col]) for col in range(2, 29)]

                location = Location(index=index, location_detail=location_detail, length=length)
                self.locs.push(int(index), location)
                self.locs_count += 1

            # print('Locations')
            # for i in range(0, self.number_of_locations):
            #     l = self.locations.get(i)
            #     print(l.get_index(), l.get_location_detail(), last=' ')
            #     for d in l.get_distances():
            #         print(d, last=' ')
            #     print()


    def get_locations(self):
        """
        Gets the hash table of Location objects
        :return:
        :rtype:
        """
        return self.locs


    def get_number_of_locations(self):
        """
        Gets the number of Location objects
        :return:
        :rtype:
        """
        return self.locs_count


    def access_packets(self):
        """
        Creates a Packet object for each packet in the imported csv file,
        then stores the Packet objects in a hash table
        :return:
        :rtype:
        """
        with open('files//packets.csv') as packets_csv:
            file_read = csv.reader(packets_csv, delimiter='\t')

            for r in file_read:
                index = int(r[0])
                location = 0
                location_detail = r[1]
                final_time = r[5]
                town = r[2] + ', ' + r[3]
                pincode = r[4]
                weight = r[6]

                for i in range(0, self.locs_count):
                    loc = self.locs.pop(i)
                    if location_detail + ', ' + town + ' ' + pincode == loc.get_location_detail():
                        location = loc.get_index()
                        break

                packet = Packet(index=index, location=location, location_detail=location_detail, final_time=final_time, town=town, pincode=pincode, weight=weight)
                self.packets.push(int(index), packet)
                self.packets_count += 1

            # print('Packets')
            # for i in range(1, self.number_of_packets + 1):
            #     p = self.packets.get(i)
            #     print(p.get_index(), p.get_location(), p.get_location_detail())


    def get_packets(self):
        """
        Gets the hash table of Packet objects
        :return:
        :rtype:
        """
        return self.packets


    def get_number_of_packets(self):
        """
        Gets the number of Packet objects
        :return:
        :rtype:
        """
        return self.packets_count


    def access_paths(self):
        """
        Creates a Path object for each path in the imported csv file,
        then stores the Path objects in a hash table
        :return:
        :rtype:
        """
        with open('files//path.csv') as routes_csv:
            file_read = csv.reader(routes_csv, delimiter='\t')

            for r in file_read:
                index = int(r[0])
                vehicle_ = r[1]
                tour = r[2]
                packets = [int(x) for x in r[3].split(',')]

                path = Path(index=index, vehicle_=vehicle_, tour=tour, packets=packets)
                self.paths.push(int(index), path)

            # print('Routes')
            # for i in range(1, 5):
            #     r = self.paths.get(i)
            #     print(r.get_index(), r.get_vehicle(), r.get_tour(), r.get_packets())


    def retrieve_paths(self):
        """
        Gets the hash table of Path objects
        :return:
        :rtype:
        """
        return self.paths


    def access_notifications(self):
        """
        Creates an Notification object for each notification in the imported csv file,
        then stores the Notification objects in a hash table
        :return:
        :rtype:
        """
        with open('files//notification.csv') as alerts_csv:
            file_read = csv.reader(alerts_csv, delimiter='\t')

            for r in file_read:
                index = int(r[0])
                path = int(r[1])
                type = r[2]
                notification = r[3]
                packet = 0
                status = ''
                location = 0
                location_detail = ''
                town = ''
                pincode = ''
                hour = 0
                minute = 0

                if type == 'location_detail' or type == 'update':
                    packet = int(r[4])
                    status = r[5]

                if type == 'update':
                    location = int(r[6])
                    location_detail = r[7]
                    town = r[8]
                    pincode = r[9]
                    hour = int(r[10])
                    minute = int(r[11])

                a = Notification(index=index, path=path, type=type, notification=notification, packet=packet, status=status, location=location, location_detail=location_detail, town=town, pincode=pincode, hour=hour, minute=minute)
                self.notifications.push(int(index), a)
                self.notification_count += 1

            # print('Alerts')
            # for i in range(self.notification_count):
            #     a = self.notifications.get(i)
            #     print(a.get_index(), a.get_type(), a.get_notification(), a.get_packet(), a.get_status(), a.get_location())


    def retrieve_notifications(self):
        """
        Gets the hash table of Notification objects
        :return:
        :rtype:
        """
        return self.notifications


    def retrieve_notifications_count(self):
        """
        Gets the number of Notification objects
        :return:
        :rtype:
        """
        return self.notification_count

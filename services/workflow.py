"""
@author: Raj Gouravelli
Student Id : OD51572
"""
import pandas as pd
from tabulate import tabulate


from services.transport import Transport
from controller.info import Info
from controller.instance import Instance
from services.color import Color

class Workflow:
    """
    A class that manages packet transport by selecting the order of "transports" using a closest neighbour approach.
    """

    def __init__(self):
        """
        """
        self.info = Info()
        self.instance = Instance()
        self.repeat = True

    def display_choices(self):
        """
        :return:
        :rtype:
        """
        while self.repeat is True:
            print(f'{Color.BOLD}########## Packet Transport System ##########{Color.END}')
            print('a. Packet Workflow\nb. Packets final Gist\nc. Pop Packet Travel details\nd. Terminate')
            self.read_choice()

    def read_choice(self):
        """
        :return:
        :rtype:
        """
        self.info = Info()
        self.instance = Instance()

        option = input('Make a choice: ')
        if option == 'a':
            self.start_workflow(True)
        elif option == 'b':
            self.final_gist()
        elif option == 'c':
            self.pop_packet()
        elif option == 'd':
            self.terminate_workflow()
        else:
            print(f'{Color.DARKCYAN }Kindly retry{Color.END }')
            self.read_choice()

    def start_workflow(self, view):
        """
        :param view:
        :type view:
        :return:
        :rtype:
        """
        if view is True:
            print(f'\n{Color.BOLD}########## Packet Workflow ##########{Color.END}\n')

        transport = Transport(view)

        # Vehicle 1, Routes 1 & 2
        if self.instance.now < self.instance.last:
            truck1 = self.info.retrieve_paths().pop(1)
            transport.transport_packets(self.info, self.instance, truck1)
            total_miles = truck1.get_miles()

        if self.instance.now < self.instance.last:
            truck1 = self.info.retrieve_paths().pop(2)
            transport.transport_packets(self.info, self.instance, truck1)
            total_miles += truck1.get_miles()

        self.instance.refresh()

        # Vehicle 2, Routes 1 & 2
        if self.instance.now < self.instance.last:
            truck2 = self.info.retrieve_paths().pop(3)
            transport.transport_packets(self.info, self.instance, truck2)
            total_miles += truck2.get_miles()

        if self.instance.now < self.instance.last:
            truck2 = self.info.retrieve_paths().pop(4)
            transport.transport_packets(self.info, self.instance, truck2)
            total_miles += truck2.get_miles()

        if view is True:
            print(f'{Color.BOLD}{Color.GREEN}Total Mileage: %.1f miles {Color.END}{Color.END}\n' % total_miles )

    def final_gist(self):
        """
        :return:
        :rtype:
        """
        print(f'\n{Color.BOLD}########### Packets final Gist ###########{Color.END}')

        for i in range(1, self.info.get_number_of_packets() + 1):
            self.info.get_packets().pop(i).set_status('At Warehouse')

        hours = self.read_user_feed('Enter hour (0-23): ', 0, 24)
        minutes = self.read_user_feed('Enter minutes (0-59): ', 0, 60)
        instance = self.instance.convert_time(hours=hours, minutes=minutes, seconds=0)

        self.instance.last = instance
        self.start_workflow(False)
        self.instance.now = instance

        print(f'\n{Color.UNDERLINE}Current Instance:', self.instance.view_time(), f'{Color.END}\n')
        list_of_packets = []
        for i in range(1, self.info.get_number_of_packets() + 1):
            p = self.info.get_packets().pop(i)
            list_of_packets.append([p.get_index(), p.get_location_detail(),
                                    p.get_final_time(), p.get_town(), p.get_pincode(),
                                    p.get_weight(), p.get_status()])
        dataframe_of_packets = pd.DataFrame(list_of_packets,
                                            columns=['Packet ID', 'Address', 'Deadline', 'City', 'Zip Code', 'Weight',
                                                     'Status'])
        print(tabulate(dataframe_of_packets, headers='keys', tablefmt='pretty', showindex=False))
        print()

    def pop_packet(self):
        """
        :return:
        :rtype:
        """
        print(f'\n{Color.BOLD}############## Pop Packet Travel details ##############{Color.END}')

        i = self.read_user_feed('Enter a Packet ID (1-40): ', 1, 41)
        p = self.info.get_packets().pop(i)
        self.info.get_packets().pop(i).set_status('At Warehouse')

        hours = self.read_user_feed('Enter hour (0-23): ', 0, 24)
        minutes = self.read_user_feed('Enter minutes (0-59): ', 0, 60)
        instance = self.instance.convert_time(hours=hours, minutes=minutes, seconds=0)

        self.instance.last = instance
        self.start_workflow(False)
        self.instance.now = instance
        df = pd.DataFrame([[p.get_index(), p.get_location_detail(),
                            p.get_final_time(), p.get_town(),
                            p.get_pincode(), p.get_weight(),
                            p.get_status()]],
                          columns=['Packet ID','Address','Deadline','Town','Pincode','Weight',f'Status at {self.instance.view_time()}'])

        print(tabulate(df.T, tablefmt='grid', showindex=True))

    def read_user_feed(self, string, low, high):
        """
        :param string:
        :type string:
        :param low:
        :type low:
        :param high:
        :type high:
        :return:
        :rtype:
        """
        i = input(string)
        if i in [str(i) for i in range(low, high)] or i in ['0' + str(i) for i in range(low, high)]:
            return int(i)
        else:
            print(f'{Color.DARKCYAN }Kindly retry{Color.END }')
            return self.read_user_feed(string, low, high)

    def terminate_workflow(self):
        """
        :return:
        :rtype:
        """
        print(f"{Color.BOLD}{Color.RED}Program is terminated!!!{Color.END}{Color.END}")
        self.repeat = False

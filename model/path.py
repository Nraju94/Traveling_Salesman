"""
@author: Raj Gouravelli
Student Id : OD51572
"""


class Path:
    """
    A "class of Path" object that represents the truck routes.
    """


    def __init__(self, index=0, vehicle_=0, tour=0, miles=0.0, packets=None):
        """
        :param index:
        :type index:
        :param vehicle_:
        :type vehicle_:
        :param tour:
        :type tour:
        :param miles:
        :type miles:
        :param packets:
        :type packets:
        """
        self.index = index
        self.vehicle = vehicle_
        self._trip = tour
        self._miles = miles
        self.packets = packets


    def get_index(self):
        """
        :return:
        :rtype:
        """
        return self.index



    def set_index(self, index):
        """
        :param index:
        :type index:
        :return:
        :rtype:
        """
        self.index = index


    def get_vehicle(self):
        """
        :return:
        :rtype:
        """
        return self.vehicle


    def set_vehicle(self, vehicle_):
        """
        :param vehicle_:
        :type vehicle_:
        :return:
        :rtype:
        """
        self.vehicle = vehicle_


    def get_tour(self):
        """
        :return:
        :rtype:
        """
        return self._trip


    def set_tour(self, tour):
        """
        :param tour:
        :type tour:
        :return:
        :rtype:
        """
        self._trip = tour


    def get_miles(self):
        """
        :return:
        :rtype:
        """
        return self._miles


    def set_miles(self, miles):
        """
        :param miles:
        :type miles:
        :return:
        :rtype:
        """
        self._miles = miles


    def get_packets(self):
        """
        :return:
        :rtype:
        """
        return self.packets


    def set_packets(self, packets):
        """
        :param packets:
        :type packets:
        :return:
        :rtype:
        """
        self.packets = packets

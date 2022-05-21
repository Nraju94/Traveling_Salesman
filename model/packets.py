"""
@author: Raj Gouravelli
Student Id : OD51572
"""

class Packet:
    """
    Objects that represent packets in a "class of Packet"
    """


    def __init__(self, index=0, location=0, location_detail='', final_time='', town='', pincode='', weight='', status='At Warehouse'):
        """
        :param index:
        :type index:
        :param location:
        :type location:
        :param location_detail:
        :type location_detail:
        :param final_time:
        :type final_time:
        :param town:
        :type town:
        :param pincode:
        :type pincode:
        :param weight:
        :type weight:
        :param status:
        :type status:
        """
        self._index = index
        self._location = location
        self._location_detail = location_detail
        self._final_time = final_time
        self._town = town
        self._pincode = pincode
        self._weight = weight
        self._status = status


    def get_index(self):
        """
        :return:
        :rtype:
        """
        return self._index


    def set_index(self, index):
        """
        :param index:
        :type index:
        :return:
        :rtype:
        """
        self._index = index


    def get_location(self):
        """
        :return:
        :rtype:
        """
        return self._location


    def set_location(self, location):
        """
        :param location:
        :type location:
        :return:
        :rtype:
        """
        self._location = location


    def get_location_detail(self):
        """
        :return:
        :rtype:
        """
        return self._location_detail


    def set_location_detail(self, location_detail):
        """
        :param location_detail:
        :type location_detail:
        :return:
        :rtype:
        """
        self._location_detail = location_detail


    def get_final_time(self):
        """
        :return:
        :rtype:
        """
        return self._final_time


    def set_final_time(self, final_time):
        """
        :param final_time:
        :type final_time:
        :return:
        :rtype:
        """
        self._final_time = final_time


    def get_town(self):
        """
        :return:
        :rtype:
        """
        return self._town


    def set_town(self, town):
        """
        :param town:
        :type town:
        :return:
        :rtype:
        """
        self._town = town


    def get_pincode(self):
        """
        :return:
        :rtype:
        """
        return self._pincode


    def set_pincode(self, pincode):
        """
        :param pincode:
        :type pincode:
        :return:
        :rtype:
        """
        self._pincode = pincode


    def get_weight(self):
        """
        :return:
        :rtype:
        """
        return self._weight


    def set_weight(self, weight):
        """
        :param weight:
        :type weight:
        :return:
        :rtype:
        """
        self._weight = weight


    def get_status(self):
        """
        :return:
        :rtype:
        """
        return self._status


    def set_status(self, status):
        """
        :param status:
        :type status:
        :return:
        :rtype:
        """
        self._status = status

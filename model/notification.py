"""
@author: Raj Gouravelli
Student Id : OD51572
"""

class Notification:
    """
    Transport, packet, and location detail alerts are represented by this class of "Notification" objects.
    """

    def __init__(self, index=0, path=0, type='', notification='', packet=0, status='', location=0, location_detail='', town='', pincode='', hour=0, minute=0):
        """
        :param index:
        :type index:
        :param path:
        :type path:
        :param type:
        :type type:
        :param notification:
        :type notification:
        :param packet:
        :type packet:
        :param status:
        :type status:
        :param location:
        :type location:
        :param location_detail:
        :type location_detail:
        :param town:
        :type town:
        :param pincode:
        :type pincode:
        :param hour:
        :type hour:
        :param minute:
        :type minute:
        """
        self.index = index
        self._path = path
        self._type = type
        self._notification = notification
        self._packet = packet
        self._status = status
        self._location = location
        self._location_detail = location_detail
        self._town = town
        self._pincode = pincode
        self._hour = hour
        self._minute = minute


    def get_index(self):
        """
        :return:
        :rtype:
        """
        return self.index

    def get_path(self):
        """
        :return:
        :rtype:
        """
        return self._path

    def set_path(self, path):
        """
        :param path:
        :type path:
        :return:
        :rtype:
        """
        self._path = path


    def get_type(self):
        """
        :return:
        :rtype:
        """
        return self._type


    def get_notification(self):
        """
        :return:
        :rtype:
        """
        return self._notification


    def get_packet(self):
        """
        :return:
        :rtype:
        """
        return self._packet


    def get_status(self):
        """
        :return:
        :rtype:
        """
        return self._status


    def get_location(self):
        """
        :return:
        :rtype:
        """
        return self._location


    def get_location_detail(self):
        """
        :return:
        :rtype:
        """
        return self._location_detail


    def get_town(self):
        """
        :return:
        :rtype:
        """
        return self._town


    def get_pincode(self):
        """
        :return:
        :rtype:
        """
        return self._pincode


    def get_hr(self):
        """
        :return:
        :rtype:
        """
        return self._hour


    def get_min(self):
        """
        :return:
        :rtype:
        """
        return self._minute

"""
@author: Raj Gouravelli
Student Id : OD51572
"""


class Location:
    """
    A collection of "Location" objects that represent different modes of transportation.
    """


    def __init__(self, index=0, location_detail='', length=None):
        """
        :param index:
        :type index:
        :param location_detail:
        :type location_detail:
        :param length:
        :type length:
        """
        self._index = index
        self._location_detail = location_detail
        self._length = length


    def get_index(self):
        """
        :return:
        :rtype:
        """
        return self._index


    def get_location_detail(self):
        """
        :return:
        :rtype:
        """
        return self._location_detail


    def get_distances(self):
        """
        :return:
        :rtype:
        """
        return self._length

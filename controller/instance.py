"""
@author: Raj Gouravelli
Student Id : OD51572
"""

from datetime import timedelta


class Instance:
    """
    A utility class for tracking "instances," conversions, and view time.
    """

    def __init__(self, now=timedelta(hours=8), last=timedelta(hours=24)):
        """
        :param now:
        :type now:
        :param last:
        :type last:
        """
        self.now = now
        self.last = last


    @staticmethod
    def convert_time(miles=1, hours=0, minutes=3, seconds=20):
        return timedelta(hours=hours, minutes=minutes, seconds=seconds) * miles


    def refresh(self):
        """
        :return:
        :rtype:
        """
        self.now = timedelta(hours=8)


    def view_time(self):
        """
        :return:
        :rtype:
        """
        if self.now < timedelta(hours=12):
            return str(self.now) + ' AM'
        elif self.now >= timedelta(hours=13):
            return str(self.now - timedelta(hours=12)) + ' PM'
        else:
            return str(self.now) + ' PM'

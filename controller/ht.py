"""
@author: Raj Gouravelli
Student Id : OD51572
"""


class HT:
    """
    A file structure "class" that uses a "hash table" to store and retrieve files.
    """


    def __init__(self, len=101):
        """
        :param len:
        :type len:
        """
        self._t = [None] * len
        self._len = len


    def push(self, k, val):
        """
        :param k:
        :type k:
        :param val:
        :type val:
        :return:
        :rtype:
        """
        id = self._h(k)
        k_v_comb = [k, val]


        if self._t[id] is None:
            """
            """
            self._t[id] = list([k_v_comb])
            return


        for combination in self._t[id]:
            """
            """
            if combination[0] == k:
                combination[1] = val
                return


        self._t[id].append(k_v_comb)
        """
        """


    def pop(self, k):
        """
        :param k:
        :type k:
        :return:
        :rtype:
        """
        id = self._h(k)


        if self._t[id] is None:
            """
            """
            return None


        for combination in self._t[id]:
            """
            """
            if combination[0] == k:
                return combination[1]

        """
        """
        return None



    def _h(self, k):
        """
        :param k:
        :type k:
        :return:
        :rtype:
        """

        hash = 0
        for char in str(k):
            hash += ord(char)
        return hash % self._len


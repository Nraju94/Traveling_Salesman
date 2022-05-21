"""
@author: Raj Gouravelli
Student Id : OD51572
"""

from services.color import Color

class Transport:
    """
    A class that manages packet transport by selecting the order of "transports" using a closest neighbour approach.
    """

    def __init__(self, display):
        """
        :param display:
        :type display:
        """
        self.show = display
        self.vehicle = None
        self.now_value = None
        self.dist = None

    def transport_packets(self, info, instance, vehicle_):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :param vehicle_:
        :type vehicle_:
        :return:
        :rtype:
        """
        if self.terminate(instance):
            return

        self.fill_vehicle(info, instance, vehicle_)

        while len(vehicle_.get_packets()) > 0:
            self.request_loc(info, instance)
            if self.terminate(instance):
                return

            self.execute_transports(info, instance)
            if self.terminate(instance):
                return

        self.from_begin(info, instance)

    def fill_vehicle(self, info, instance, vehicle_):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :param vehicle_:
        :type vehicle_:
        :return:
        :rtype:
        """
        self.vehicle = vehicle_
        self.now_value = info.get_locations().pop(0)

        for i in self.vehicle.get_packets():
            p = info.get_packets().pop(i)
            p.set_status('On Vehicle ' + str(self.vehicle.get_vehicle()))

        if self.show is True:
            print(f'{Color.BOLD}###### Transports: Vehicle', str(self.vehicle.get_vehicle()) + ', Tour', str(self.vehicle.get_tour()),
                  f'######{Color.END}\n')
            print('Begin at', self.now_value.get_location_detail(), '\n')

        self.notify(info, instance, 'load')

    def request_loc(self, info, instance):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :return:
        :rtype:
        """
        self.dist = 9999999999
        next_location = 0

        for i in range(len(self.now_value.get_distances())):
            for p in self.vehicle.get_packets():
                if i == info.get_packets().pop(p).get_location() and self.dist > self.now_value.get_distances()[i]:
                    self.dist = self.now_value.get_distances()[i]
                    next_location = i

        self.now_value = info.get_locations().pop(next_location)

        self.vehicle.set_miles(self.vehicle.get_miles() + self.dist)
        instance.now += instance.convert_time(self.dist)

    def execute_transports(self, info, instance):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :return:
        :rtype:
        """
        self.notify(info, instance, 'update')

        if self.show is True:
            print('Move', self.dist, 'miles to', self.now_value.get_location_detail())

        delivered = [p for p in self.vehicle.get_packets() if
                     info.get_packets().pop(p).get_location() == self.now_value.get_index()]
        for p in delivered:
            if self.notify(info, instance, 'address', p) is False:
                info.get_packets().pop(p).set_status('Delivered at ' + instance.view_time())
                if self.show is True:
                    print('Packet', p, 'is delivered at', self.now_value.get_location_detail())

        if self.show is True:
            print(f'{Color.BLUE }Time Log:', instance.view_time() + ', Total length: %.1f miles' % self.vehicle.get_miles(), f'{Color.END }\n')

        self.vehicle.set_packets([p for p in self.vehicle.get_packets() if p not in delivered])

    def from_begin(self, info, instance):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :return:
        :rtype:
        """
        self.notify(info, instance, 'transport')

        self.dist = self.now_value.get_distances()[0]
        self.now_value = info.get_locations().pop(0)

        if self.show is True:
            print('Move', self.dist, 'miles to', self.now_value.get_location_detail())

        self.vehicle.set_miles(self.vehicle.get_miles() + self.dist)
        instance.now += instance.convert_time(self.dist)

        if self.show is True:
            print(f'{Color.BLUE}Time Log:', instance.view_time() + ', Total length: %.1f miles' % self.vehicle.get_miles(), f'{Color.END}\n')

    def notify(self, info, instance, event, p=None):
        """
        :param info:
        :type info:
        :param instance:
        :type instance:
        :param event:
        :type event:
        :param p:
        :type p:
        :return:
        :rtype:
        """
        for i in range(info.retrieve_notifications_count()):
            a = info.retrieve_notifications().pop(i)

            if event == 'address':
                if a.get_packet() == p and self.vehicle.get_index() == a.get_path():
                    info.get_packets().pop(p).set_status(a.get_status())
                    if self.show is True:
                        print(f'{Color.RED}*** Notification ***{Color.END}', a.get_notification())
                    return True

            elif event == a.get_type() == 'update':
                if self.vehicle.get_index() == a.get_path() and instance.now >= instance.convert_time(hours=a.get_hr(),
                                                                                               minutes=a.get_min()):
                    info.get_packets().pop(a.get_packet()).set_location(a.get_location())
                    info.get_packets().pop(a.get_packet()).set_location_detail(a.get_location_detail())
                    info.get_packets().pop(a.get_packet()).set_town(a.get_town())
                    info.get_packets().pop(a.get_packet()).set_pincode(a.get_pincode())
                    info.get_packets().pop(a.get_packet()).set_status(a.get_status())
                    if self.show is True:
                        print(f'{Color.RED}*** Notification ***', a.get_notification(), 'at', instance.view_time(), f'{Color.END}\n')
                    a.set_path(0)

            elif event == a.get_type() and self.vehicle.get_index() == a.get_path():
                if self.show is True:
                    print(f'{Color.RED}*** Notification ***', a.get_notification(), 'at', instance.view_time(), f'{Color.END}\n')

        return False

    def terminate(self, instance):
        """
        :param instance:
        :type instance:
        :return:
        :rtype:
        """
        if instance.now >= instance.last:
            instance.now = instance.last
            return True
        return False

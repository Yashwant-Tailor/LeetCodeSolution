class Solution:
    class BUS:
        def __init__(self,bus_num):
            self.bus_num = bus_num
            self.stops = []
            self.vis = False
        def get_bus_stops(self):
            return self.stops
        def add_stop(self,stop):
            self.stops.append(stop)
    class STOP:
        def __init__(self,stop_num):
            self.stop_num = stop_num
            self.buses = []
            self.req_bus = int(1e7)
        def add_bus(self,bus):
            self.buses.append(bus)
        def get_buses(self):
            return self.buses
    def get_next_buses(self,buses,stops,stops_q):
        next_buses = []
        req_bus = None
        while len(stops_q) > 0:
            stop = stops_q.popleft()
            req_bus = stops[stop].req_bus + 1
            for bus in stops[stop].get_buses():
                if not buses[bus].vis :
                    buses[bus].vis = True
                    next_buses.append(bus)
        return next_buses,req_bus
    def get_next_stops(self,buses,stops,next_buses,changed_bus,stops_q):
        for bus in next_buses:
            for stop in buses[bus].get_bus_stops():
                if stops[stop].req_bus > changed_bus:
                    stops[stop].req_bus = changed_bus
                    stops_q.append(stop)
        return
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = [self.BUS(idx) for idx in range(len(routes))]
        stops = [self.STOP(idx) for idx in range(int(1e6))]
        for bus,route in enumerate(routes):
            for stop in route:
                buses[bus].add_stop(stop)
                stops[stop].add_bus(bus)
        from collections import deque
        stops_q = deque()
        stops_q.append(source)
        stops[source].req_bus = 0
        while len(stops_q) > 0:
            next_buses,changed_bus = self.get_next_buses(buses,stops,stops_q)
            self.get_next_stops(buses,stops,next_buses,changed_bus,stops_q)
        if stops[target].req_bus == int(1e7):
            return -1
        return stops[target].req_bus

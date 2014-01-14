from lib.socketcollector import *


class HAProxy:
    def __init__(self):
        pass

    @staticmethod
    def collect():
        parameters = SocketCollectorParameters()
        parameters.socketFile = "/var/lib/haproxy/stats.sock"
        parameters.command = "show info\n"

        collector = SocketCollector(parameters)
        return collector.get()

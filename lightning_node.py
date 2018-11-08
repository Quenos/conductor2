import lndAL

class HomeNode(object):

    def __init__(self):
        info = lndAL.LndAL.get_info()
        self.name = info.alias

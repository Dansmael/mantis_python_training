from sys import maxsize

class Project:

    def __init__(self, id=None, name=None, description=None, status=None, inheritGlobal=None, viewState=None,):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.inheritGlobal = inheritGlobal
        self.viewState = viewState

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.name, self.description, self.status, self.inheritGlobal, self.viewState)

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
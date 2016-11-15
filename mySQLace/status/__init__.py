class status:
    def setFailed(self, message):
        self.code = 3
        self.verbose = "FAILED"
        self.message = message

    def setConnected(self):
        self.code = 2
        self.verbose = "CONNECTED"
        self.message = ""

    def setReady(self):
        self.code = 1
        self.verbose = "READY"
        self.message = ""

    def __init__(self):
        self.setReady()

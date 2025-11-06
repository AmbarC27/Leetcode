class Logger:

    def __init__(self):
        self.last_message_displayed_till = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_message_displayed_till:
            self.last_message_displayed_till[message] = timestamp + (10 - 1)
            return True

        ## case when message has been displayed before
        if timestamp > self.last_message_displayed_till[message]:
            self.last_message_displayed_till[message] = timestamp + (10 - 1)
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
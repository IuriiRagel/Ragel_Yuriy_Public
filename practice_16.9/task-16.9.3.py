class Client:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def client_info(self):
        # solution option 1:
        return "Client: {name}. Balance: {balance}".format(name=self.name,balance=self.balance)
        # solution option 2:
        # "Client:", str(self.name), "Balance:", str(self.balance)

Client1 = Client("John Smith",4000)
Client2 = Client("Martha Stuart", 350)
print(Client1.client_info())
print(Client2.client_info())
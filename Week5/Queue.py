class TicketQueue:
    def __init__(self):
        self.queue = []

    def add_customer(self, name):
        self.queue.append(name)

    def serve_customer(self):
        if not self.queue:
            return "No customers in line"
        return self.queue.pop(0)


# Example
tickets = TicketQueue()

tickets.add_customer("Rodrigo")
tickets.add_customer("Aylin")
tickets.add_customer("Dario")

print(tickets.serve_customer())
print(tickets.serve_customer())
print(tickets.serve_customer())
print(tickets.serve_customer())
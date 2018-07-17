'''
class Tickets:
    ticket_price = 100
    def holiday(self):
        self.ticket_price = self.ticket_price * 1.2
        return self.ticket_price
    def children(self):
        self.ticket_price = self.ticket_price / 2
        return self.ticket_price

adult = int(input('几个成人:'))
child = int(input('几个儿童:'))
holiday = input('是否为节假日(yes/no):')

ticket = Tickets()

if holiday.upper() == 'YES':
    ticket.holiday()
else:
    pass
ticket_adult = adult * ticket.ticket_price
ticket.children()
ticket_child = child * ticket.ticket_price
print('票价为:%d' % (ticket_adult + ticket_child))    

'''
class Ticket():
    def __init__(self, weekend=False, chile=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if chile:
            self.discount = 0.5
        else:
            self.discount = 1
    def calcPrice(self, num):
        return self.exp * self.inc * self.discount * num

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    reconstruct your trip from your mass of flight tickets
    source string represents the starting airport and
    destination string represents the next airport along our trip
    The ticket for your first flight has a destination with a source of NONE,
    and the ticket for your final flight has a source with a destination of NONE.
    """
    destination = None

    # Add Tickets to the HashTable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # Get First ticket
    destination = hash_table_retrieve(hashtable, "NONE")

    i = 0 # index

    # Loop thru until destination is NONE
    while not destination == "NONE":
        route[i] = destination
        destination = hash_table_retrieve(hashtable, destination)
        i += 1

    # Remove Last None element
    route.pop()

    return route
# Team: Jay Balaji, Jacob Ryan, Luke McCleery, Pierce McKelvey
# Inventory
# I (Jay) created this program to work in the command line to increase my understanding of how an inventory management system
# might be used in the professional world. This is a very basic method of using inventory management, and it does not
# write to any file either. It can however be continually developed to be applied to other databases using the same
# ideas. The simplicity of this program is what is desirable, as it adds to, removes from and shows the inventory. It
# can later on be used to check which userID added or removed items from the inventory. It can also implement a search
# for an item if the inventory is large. This is very basic and can be improved, but at its basic level, it was a
# good learning experience.

# I created the class Inv.
class Inv:
    # We are using a dictionary
    def __init__(self):
        self.ourInventory = {}

    # This can be used to see what the inventory looks like.
    def __str__(self):
        return str(self.ourInventory)

    # We create add which takes the item's name and how much of the item we want to add to the inventory.
    def add(self, thing, amount):
        # We check if the item already exists in the inventory, just in case. This is so we do not add multiples.
        if thing in self.ourInventory:
            self.ourInventory[thing] += amount
        # We just add to the dictionary. The order does not matter for this, in our case.
        else:
            self.ourInventory[thing] = amount
        # We return this string once the computation is finished.
        return '{} {} ADDED'.format(amount, thing)

    # We create remove which takes the item's name as well as the number of items we are removing.
    def remove(self, thing, amountRemoved):  # We could either remove all or just one.
        # We check if the amount we want to remove is the same as the amount of the item already in the inventory.
        # If it is, then we do not want it sitting in the inventory at 0 forever, so we just delete it,
        # and if the same item is added back later on, then great. This just makes the inventory much less cluttered.
        if amountRemoved == self.ourInventory[thing]:
            del self.ourInventory[thing]
        # Otherwise we just reduce the inventory by the amount we want to reduce it.
        else:
            self.ourInventory[thing] -= amountRemoved
        # We return a string at the end of the computation
        return '{} {} REMOVED'.format(amountRemoved, thing)





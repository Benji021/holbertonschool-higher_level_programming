#!/usr/bin/python3
"""Docstring extending the python list with notifications"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with {items_added} items.")
    
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


vlist = VerboseList([1, 2, 3])
print("Initial list:", vlist)

vlist.append(4)

vlist.extend([5, 6, 7])

vlist.remove(2)

vlist.pop()

vlist.pop(0)

try:
    vlist.remove(10)
except ValueError as e:
    print(f"Error: {e}")

print("Final list:", vlist)

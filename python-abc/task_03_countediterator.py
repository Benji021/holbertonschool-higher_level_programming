#!/usr/bin/python3
"""Docstring countediterator - keeping track of iteration"""


class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    counted_iterator = CountedIterator(numbers)
    
    for number in counted_iterator:
        print(f"Item: {number}")
        print(f"Count so far: {counted_iterator.get_count()}")
    
    counted_iterator_manual = CountedIterator(numbers)
    
    try:
        while True:
            item = next(counted_iterator_manual)
            print(f"Item: {item}")
            print(f"Count so far: {counted_iterator_manual.get_count()}")
    except StopIteration:
        print("All items have been iterated.")

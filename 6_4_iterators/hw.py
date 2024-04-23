#1 

class FlatIterator:

    def __init__(self, list_of_list):
        self.iter_of_list = iter(list_of_list)

    def __iter__(self):
        self.next_list = next(self.iter_of_list)
        self.iter_items = iter(self.next_list)
        self.next_list_len = len(self.next_list)
        return self

    def __next__(self):
        self.next_list_len -= 1
        
        if self.next_list_len < 0:
            self._get_list()
            if self.iter_items is None:
                raise StopIteration
            else:
              item = self._get_item()
        else:
            item = self._get_item()
          
        return item
    
    def _get_list(self):
        try:
            self.next_list = next(self.iter_of_list)
            self.iter_items = iter(self.next_list)
            self.next_list_len = len(self.next_list) - 1
        except StopIteration:
            self.iter_items = None
        
        return self
    
    def _get_item(self):
        try:
            item = next(self.iter_items)
        except StopIteration:
            item = None
        
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()



#2

import types

def flat_generator(list_of_lists):
    for next_list in list_of_lists:
        for item in next_list:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_counter = 0
        self.add_counter = -1

        return self

    def __next__(self):
        if len(self.list_of_list) <= self.main_counter:
            raise StopIteration
        
        self.add_counter += 1
        item = self.list_of_list[self.main_counter]
        if len(item) <= self.add_counter:
            self.add_counter = -1
            self.main_counter += 1
            return self.__next__()
        else:
            return item[self.add_counter]


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
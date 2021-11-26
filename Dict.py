class Dict:

    def __init__(self) -> None:
        super().__init__()
        self.test_count = None
        self.array_test = []
        self.clear_array_test = []
        self.set_arr = []

    def enter_test_count(self):
        self.test_count = input(int())

    def enter_test(self):
        if self.test_count != 0:
            for i in range(0, int(self.test_count)):
                test_dict = {}
                first_test = input()
                second_test = input()
                test_dict['first'] = first_test
                test_dict['second'] = second_test
                self.array_test.append(test_dict)

    def check(self):
        i = len(self.array_test)
        for element in self.array_test:
            if i == 0:
                break
            first_array_string = element['first'].split()
            second_array_string = element['second'].split()
            for el in first_array_string:
                for ele in second_array_string:
                    if el == ele:
                        first_array_string.remove(el)
                        second_array_string.remove(ele)
            element['first'] = first_array_string
            element['second'] = second_array_string

            self.clear_array_test.append(element)

    def check_group_synonym(self):
        for element in self.clear_array_test:
            first_array_string = element['first']
            second_array_string = element['second']
            set_dict = {}
            for i in range(0, len(first_array_string)):
                if first_array_string[i] != second_array_string[i]:
                    set_first = {first_array_string[i]}
                    set_second = {second_array_string[i]}
                    if set_dict.get(first_array_string[i]) is not None:
                        for elem in set_dict.get(first_array_string[i]):
                            set_dict[elem] = set_first | set_second | set_dict.get(first_array_string[i])
                        set_first = set_first | set_second | set_dict.get(first_array_string[i])
                        set_second = set_second | set_first | set_dict.get(first_array_string[i])
                        set_dict[second_array_string[i]] = set_second
                        set_dict[first_array_string[i]] = set_first
                    elif set_dict.get(second_array_string[i]) is not None:
                        for elem in set_dict.get(first_array_string[i]):
                            set_dict[elem] = set_first | set_second | set_dict.get(first_array_string[i])
                        set_second = set_first | set_second | set_dict.get(second_array_string[i])
                        set_first = set_first | set_second | set_dict.get(second_array_string[i])
                        set_dict[second_array_string[i]] = set_second
                        set_dict[first_array_string[i]] = set_first
                    else:
                        set_first = set_first | set_second
                        set_second = set_second | set_first
                        set_dict[second_array_string[i]] = set_second
                        set_dict[first_array_string[i]] = set_first

            for i in set_dict.keys():
                if set_dict.get(i) in set_dict.values():
                    if set_dict.get(i) not in self.set_arr:
                        self.set_arr.append(set_dict.get(i))
            self.print_set()

    def print_set(self):
        len_of_array = []
        for i in self.set_arr:
            len_of_array.append(len(i))
        len_of_array.sort()
        len_of_array.reverse()
        print(len(self.set_arr))
        print(*len_of_array)
        self.set_arr.clear()


dict = Dict()
dict.enter_test_count()
dict.enter_test()
dict.check()
dict.check_group_synonym()

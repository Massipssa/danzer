from dataclasses import asdict, dataclass


@dataclass
class MyClass:
    name: str

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def loop_dict(dict_items):
        return dict_items
        """
        toto = {
            key: value
            for key, value in dict_items
            if value % 2 == 0
        }
        return toto
        """


if __name__ == '__main__':
    my_class = MyClass("toto")
    print(asdict(my_class))

    test_items = {
        "two": 2,
        "three": 3,
        "four": 4,
    }
    rst = MyClass.loop_dict(test_items)
    print(rst)

# ���� ������� �������� �� ������� ������ ���� ���� ����� � 4 �������
# d = Dictionary4()
# d["sdfe] = 12
# d["uucernbe"] - crash
# d[34] = 12 - 34 is not string, and it's len != 4


class Dictionary4:
    """ �������������� �������

    ���� ������� �������� �� ������� ������ ���� ���� ����� � 4 �������
    ����� Dictionary4 - �������� ��������
    """
    def __init__(self):
        self.__my_dict = {}

    def __str__(self):
        """  ������������ �������� � �����

        :return: �����
        """
        return f"Dictionary4 {str(self.__my_dict)}"

    def __setitem__(self, key, value):
        "��������� ���� ���� ������ �������� [] ��� ��������� ��� ����� ��������"
        assert isinstance(key, str) and len(key) == 4
        self.__my_dict[key] = value

    def __len__(self):
        return len(self.__my_dict)

    def __contains__(self, key):
        return key in self.__my_dict

    def __getitem__(self, key):
        if key not in self.__my_dict:
            return None
        return self.__my_dict[key]
    def __delitem__(self, key):
        del self.__my_dict[key]




if __name__ == '__main__':
    d = Dictionary4()
    print(d)
    d["ghgh"] = 1234
    d["zxcv"] = 12
    print(d)
    print(len(d))
    print("12" in d)
    print("3432423" not in d)
    def d[1234]

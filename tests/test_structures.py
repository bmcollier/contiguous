import unittest

from contiguous.structures import DataSection, Group
from contiguous.types import String


class TestContiguous(unittest.TestCase):
    """ Test basic functionality with native Python types in schemas."""

    def test_lengths(self):
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        length = data.length
        self.assertEqual(length, 68)

    def test_get_member(self):
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        street = data.get_member("street")
        pass

    def test_set(self):
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        data.set("name", "Ben")
        data.set("surname", "Collier")
        self.assertEqual(data._data[0:3].decode(), "Ben")
        self.assertEqual(data._data[25:32].decode(), "Collier")

    def test_set_nested(self):
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        data.set("street", "Verney Close")
        pass

    def test_get_nested(self):
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        data.set("address", "14 Verney Close")
        house = data.get("house_number")
        self.assertEqual(int(house), 14)

    def test_basic_structure(self):
        """

        :return:
        """
        data = DataSection(
            String("name", 25),
            String("surname", 25),
            Group("address",
                  String("house_number", 3),
                  String("street", 15)
                  )
        )
        data.set("address", "14 Verney Close")
        self.assertEqual(data._data[50:65].decode(), "14 Verney Close")


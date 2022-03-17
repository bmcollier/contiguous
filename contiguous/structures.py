from contiguous.types import ContiguousType, String


class Group:

    def __init__(self, name, *args):
        self.name = name
        self.length = 0
        for arg in args:
            print(arg.length)
            self.length += int(arg.length)
        self._data = bytearray(b'\0' * self.length)
        self.members = args

    def get_offset(self, name):
        offset = 0
        if self.name == name:
            return 0
        for member in self.members:
            if isinstance(member, ContiguousType):
                if member.name == name:
                    return offset
            else:
                increment = member.get_offset(name)
                if increment is not False:
                    offset += increment
                    return offset
            offset += member.length
        return False

    def get_member(self, name):
        if self.name == name:
            return self
        for member in self.members:
            if isinstance(member, ContiguousType):
                if member.name == name:
                    return member
            else:
                return member.get_member(name)
        raise ValueError("Member name not found")


class DataSection(Group):

    def __init__(self, *args):
        super().__init__("root", *args)

    def set(self, name: str, value):
        offset = 0
        for member in self.members:
            if isinstance(member, ContiguousType):
                if member.name == name:
                    self._data[offset:offset + member.length] = bytes(str(value).ljust(member.length, ' '), "latin-1")
                    return
            else:
                increment = member.get_offset(name)
                if increment is not False:
                    offset += increment
                    self._data[offset:offset + member.length] = bytes(str(value).ljust(member.length, ' '), "latin-1")
                    return
            offset += member.length
        raise ValueError(f"Data member not found: {name}")


    def get(self, name):
        offset = 0
        for member in self.members:
            if isinstance(member, ContiguousType):
                if member.name == name:
                    return self._data[offset:offset + member.length].decode()
            else:
                increment = member.get_offset(name)
                if increment is not False:
                    offset += increment
                    return self._data[offset:offset + self.get_member(name).length].decode()
            offset += member.length
        raise ValueError(f"Data member not found: {name}")

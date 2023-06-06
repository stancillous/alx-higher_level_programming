#!/user/bin/python3
class LockedClass:
    """
    prevent object instantiation of any attr
    other thatn first_name"""
    __slots__ = ["first_name"]

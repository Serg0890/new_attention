from typing import List

users: List[str] = ["user1", "user2", "user30", "user3", "user100"]


def string_to_int(elem: str) -> int:
    return int(elem[4:])


# sorted_users = sorted(users, key=string_to_int)
sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
# print(sorted_users)

x = lambda a: a + 10
print(x(5))

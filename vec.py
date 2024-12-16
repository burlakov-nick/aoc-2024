from typing_extensions import Iterable


def sign(x: int) -> int:
    if x == 0:
        return 0
    return -1 if x < 0 else 1


class V:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other) -> "V":
        return V(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "V":
        return V(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> "V":
        return V(self.x * other, self.y * other)

    def __neg__(self) -> "V":
        return V(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, V)
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: object) -> bool:
        assert isinstance(other, V)
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def __repr__(self) -> str:
        return (self.x, self.y).__repr__()

    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0

    def dist_to(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def dist(self) -> int:
        return abs(self.x) + abs(self.y)

    def neighbors_8(self) -> Iterable["V"]:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    yield self + V(dx, dy)

    def neighbors_4(self) -> Iterable["V"]:
        yield self + V(0, -1)
        yield self + V(0, 1)
        yield self + V(1, 0)
        yield self + V(-1, 0)

    def neighbors_8_in_box(self, n: int, m: int) -> Iterable["V"]:
        for v in self.neighbors_8():
            if 0 <= v.x < n and 0 <= v.y < m:
                yield v

    def neighbors_4_in_box(self, n: int, m: int) -> Iterable["V"]:
        for v in self.neighbors_4():
            if 0 <= v.x < n and 0 <= v.y < m:
                yield v

    def dir(self) -> "V":
        return V(sign(self.x), sign(self.y))

    def in_box(self, n: int, m: int) -> bool:
        return 0 <= self.x < n and 0 <= self.y < m

    def clockwise(self) -> "V":
        return V(self.y, -self.x)

    def counter_clockwise(self) -> "V":
        return V(-self.y, self.x)


DIRECTIONS_4 = [V(0, -1), V(0, 1), V(-1, 0), V(1, 0)]


class V3:
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __add__(self, other: "V3") -> "V3":
        return V3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "V3") -> "V3":
        return V3(self.x - other.x, self.y - other.y, self.z + other.z)

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, V3)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return (self.x, self.y, self.z).__hash__()

    def __repr__(self) -> str:
        return (self.x, self.y, self.z).__repr__()

    def dist_to(self, other: "V3") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def neighbors_6(self) -> Iterable["V3"]:
        for d in [
            V3(-1, 0, 0),
            V3(1, 0, 0),
            V3(0, -1, 0),
            V3(0, 1, 0),
            V3(0, 0, -1),
            V3(0, 0, 1),
        ]:
            yield self + d

    def neighbors_6_in_box(
        self, lx: int, rx: int, ly: int, ry: int, lz: int, rz: int
    ) -> Iterable["V3"]:
        for d in [
            V3(-1, 0, 0),
            V3(1, 0, 0),
            V3(0, -1, 0),
            V3(0, 1, 0),
            V3(0, 0, -1),
            V3(0, 0, 1),
        ]:
            v = self + d
            if lx <= v.x < rx and ly <= v.y < ry and lz <= v.z < rz:
                yield self + d

    def dir(self) -> "V3":
        return V3(sign(self.x), sign(self.y), sign(self.z))

import unittest


def elmozdulas(utvonal: str) -> str:
    x = 0  # vízszintes elmozdulás (jobbra +, balra -)
    y = 0  # függőleges elmozdulás (fel +, le -)

    for lepes in utvonal:
        if lepes == "F":
            y += 1
        elif lepes == "L":
            y -= 1
        elif lepes == "J":
            x += 1
        elif lepes == "B":
            x -= 1

    if x == 0 and y == 0:
        return "Nem mentunk sehova"

    return f"Vizszintes: {x}, Fuggoleges: {y}"


class TestElmozdulas(unittest.TestCase):

    def test_pelda(self):
        self.assertEqual(
            elmozdulas("JBBFB"),
            "Vizszintes: -2, Fuggoleges: 1"
        )

    def test_visszateres(self):
        self.assertEqual(
            elmozdulas("JB"),
            "Nem mentunk sehova"
        )

    def test_csak_fuggoleges(self):
        self.assertEqual(
            elmozdulas("FFFL"),
            "Vizszintes: 0, Fuggoleges: 2"
        )

    def test_csak_vizszintes(self):
        self.assertEqual(
            elmozdulas("JJJBB"),
            "Vizszintes: 1, Fuggoleges: 0"
        )

    def test_ures_utvonal(self):
        self.assertEqual(
            elmozdulas(""),
            "Nem mentunk sehova"
        )


if __name__ == "__main__":
    unittest.main()

import unittest

def jelszo_erosseg(jelszo: str) -> int:
    if len(jelszo) == 0:
        return 0
    if "jelszo" in jelszo or "123" in jelszo:
        return 0
    erosseg = 1  

    if len(jelszo) >= 5:
        erosseg += 1
    if len(jelszo) >= 8:
        erosseg += 2

    for karakter in jelszo:
        if karakter in "_-.":
            erosseg += 2
    return erosseg

class TestJelszoErosseg(unittest.TestCase):

    def test_alap(self):
        self.assertEqual(jelszo_erosseg("abc"), 1)

    def test_hossz_noveles(self):
        self.assertEqual(jelszo_erosseg("abcde"), 2)
        self.assertEqual(jelszo_erosseg("abcdefgh"), 4)

    def test_specialis_karakterek(self):
        self.assertEqual(jelszo_erosseg("abc_de"), 4)
        self.assertEqual(jelszo_erosseg("abc-de."), 6)

    def test_tiltott_reszszoveg(self):
        self.assertEqual(jelszo_erosseg("jelszo123"), 0)
        self.assertEqual(jelszo_erosseg("titkos123"), 0)
        self.assertEqual(jelszo_erosseg("jelszo_erős"), 0)

    def test_ures_jelszo(self):
        self.assertEqual(jelszo_erosseg(""), 0)


if __name__ == "__main__":
    unittest.main()

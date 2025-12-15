import unittest


def maganhangzot_torol(szoveg: str) -> str:
    # Magyar és angol magánhangzók
    maganhangzok = "aeiouAEIOUáÁéÉíÍóÓöÖőŐúÚüÜűŰ"
    return "".join(karakter for karakter in szoveg if karakter not in maganhangzok)


class TestMaganhangzoTorol(unittest.TestCase):

    def test_alap(self):
        self.assertEqual(maganhangzot_torol("hello"), "hll")

    def test_nagybetuk(self):
        self.assertEqual(maganhangzot_torol("AEIOUaeiou"), "")

    def test_szokoz_es_irasjelek(self):
        self.assertEqual(
            maganhangzot_torol("Ez egy teszt mondat."),
            "z gy tszt mndt."
        )

    def test_szamok_es_egyeb(self):
        self.assertEqual(
            maganhangzot_torol("Twitter 280 karakter!"),
            "Twttr 280 krrktr!"
        )

    def test_ures_szoveg(self):
        self.assertEqual(maganhangzot_torol(""), "")


if __name__ == "__main__":
    unittest.main()

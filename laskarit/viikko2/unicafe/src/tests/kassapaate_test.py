import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1200)

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_jos_maksu_riittava_kassan_rahamaara_kasvaa_oikein_ja_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(vaihtoraha, 10)

    def test_kateisosto_maukas_jos_maksu_riittava_kassan_rahamaara_kasvaa_oikein_ja_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_edullinen_jos_maksu_riittava_myytyjen_lounaiden_maara_kasvaa(self):
        for x in range(3):
            self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_kateisosto_maukas_jos_maksu_riittava_myytyjen_lounaiden_maara_kasvaa(self):
        for x in range(3):
            self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_kateisosto_edullinen_jos_maksu_ei_riittava_ei_muutoksia(self):
        maksu = 239
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(vaihtoraha, maksu)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_jos_maksu_ei_riittava_ei_muutoksia(self):
        maksu = 399
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(vaihtoraha, maksu)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_jos_kortilla_tarpeeksi_rahaa_veloitus_kortilta_oikein_ja_palautuu_true(self):
        palautusarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.6)
        self.assertEqual(palautusarvo, True)

    def test_korttiosto_maukas_jos_kortilla_tarpeeksi_rahaa_veloitus_kortilta_oikein_ja_palautuu_true(self):
        palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 8)
        self.assertEqual(palautusarvo, True)

    def test_korttiosto_edullinen_jos_kortilla_tarpeeksi_rahaa_myytyjen_lounaiden_maara_kasvaa(self):
        for x in range(3):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_korttiosto_maukas_jos_kortilla_tarpeeksi_rahaa_myytyjen_lounaiden_maara_kasvaa(self):
        for x in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_korttiosto_edullinen_jos_kortilla_ei_tarpeeksi_rahaa_ei_muutoksia_ja_palautuu_false(self):
        maksukortti = Maksukortti(239)
        palautusarvo = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 2.39)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(palautusarvo, False)

    def test_korttiosto_maukas_jos_kortilla_ei_tarpeeksi_rahaa_ei_muutoksia_ja_palautuu_false(self):
        maksukortti = Maksukortti(399)
        palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 3.99)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(palautusarvo, False)

    def test_korttiosto_edullinen_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_maukas_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasvaa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 800)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1008)

    def test_kortille_ladattaessa_negatiivisella_summalla_kortin_saldo_ja_kassan_rahamaara_eivat_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -800)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

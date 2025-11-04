import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(240)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        maksukortti = Maksukortti(200)
        maksukortti.ota_rahaa(240)

        self.assertEqual(maksukortti.saldo_euroina(), 2.0)

    def test_rahan_ottaminen_palauttaa_true_jos_rahat_riittavat(self):
        palautusarvo = self.maksukortti.ota_rahaa(240)

        self.assertEqual(palautusarvo, True)

    def test_rahan_ottaminen_palauttaa_false_jos_rahat_eivat_riita(self):
        maksukortti = Maksukortti(200)
        palautusarvo = maksukortti.ota_rahaa(240)

        self.assertEqual(palautusarvo, False)

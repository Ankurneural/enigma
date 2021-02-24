import unittest
from enigma import *

pl = PlugLead("AB")
pb = Plugboard()
pb.add(pl)
class TestClass(unittest.TestCase):

    def test_PLencode(self):

        self.assertEqual(pl.encode("A"), "B")
        self.assertEqual(pl.encode("B"), "A")
        self.assertEqual(pl.encode("Z"), "Z")
        
    def test_PBencode(self):
        
        self.assertEqual(pb.encode("A"), "B")
        # self.assertEqual(pb.encode("D"), "D")
        

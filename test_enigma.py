import unittest
from enigma import *

pl = PlugLead("AB")

pb = Plugboard()
pb.add(PlugLead("SZ"))
pb.add(PlugLead("GT"))
pb.add(PlugLead("DV"))
pb.add(PlugLead("KU"))


rotor = Rotor("I")
rotorA = Rotor("A")



class TestClass(unittest.TestCase):

    def test_PLencode(self):

        self.assertEqual(pl.encode("A"), "B")
        self.assertEqual(pl.encode("B"), "A")
        self.assertEqual(pl.encode("Z"), "Z")
        
    def test_PBencode(self):
        
        self.assertEqual(pb.encode("D"), "V")
        self.assertEqual(pb.encode("K"), "U")
        self.assertEqual(pb.encode("A"), "A")
        
    def test_rotor(self):
        
        self.assertEqual(rotor.encode_right_to_left("A"), "E")
        self.assertEqual(rotor.encode_left_to_right("A"), "U")
        
        self.assertEqual(rotorA.encode_right_to_left("A"), "E")
        self.assertEqual(rotorA.encode_left_to_right("A"), "E")
        
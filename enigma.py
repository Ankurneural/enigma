
class PlugLead:
    """Requirements:
    1. Two character letter only allowed, Same character is not allowed.
    2. If not encoded in the pluglead, the character should return itself.
    3. Raise exceptions for all the invalid configurations.
    """
    def __init__(self, mapping):
        # Your code here
        self.mapping = mapping
        self.map_dic = self.map_dictionary()
    
    def map_dictionary(self):
        """Creates a dictionary of the inputs for mapping
        """
        try:
            assert(len(self.mapping)==2)
            assert(self.mapping[0] != self.mapping[1])

            map_d = {}
            map_d[self.mapping[0]] = self.mapping[1]
            map_d[self.mapping[1]] = self.mapping[0]
            
            return map_d

        except AssertionError as e:
            print("Mapping must be of Length 2 or \n Same character cannot be mapped with itself \n")
            raise Exception
        
        
    def encode(self, character):
        # Your code here
        if character in self.map_dic.keys():
            return self.map_dic[character]
        else:
            return character


class Plugboard:
    """Requirements:
    1. You cannot encode one character more than once.
    """
    # Your code here
    def __init__(self) -> None:
        self.dict = {}
        self.mappings = list()

    def add(self, pluglead):
        """
        Take a PlugLead object and add the encoding. 
        """
        if any(x in self.dict.keys() for x in list(pluglead.mapping)):
            print("One of the character is already mapped, Change mappings \n")
            raise Exception

        else:
            self.dict.update(pluglead.map_dic)
            self.mappings.append(pluglead.mapping)

    def encode(self, character):
        if character in self.dict.keys():
            return self.dict[character]
        else:
            return character

class Rotor:
    
    Label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping_dictionary = {
        "I" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II" : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III" : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV" : "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V" : "VZBRGITYUPSDNHLXAWMJQOFECK",
        "Beta" : "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "Gamma" : "FSOKANUERHMBTIYCWLQPZXVGJD",
        "A" : "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B" : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C" : "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }
    
    def __init__(self, rotor) -> None:
        self.rotor = rotor

    def encode_right_to_left(self, charr):
        ind = Rotor.Label.find(charr)
        return Rotor.mapping_dictionary[self.rotor][ind]

    def encode_left_to_right(self, charr):
        ind = Rotor.mapping_dictionary[self.rotor].find(charr)
        return Rotor.Label[ind]

class Rotor_simulator(Rotor):
    
    def __init__(self, rotors):
        # Rotor.__init__(self)
        self.rotors = rotors
        self.encode_counter = 0

    def encode(self, ch):
        """Takes plugboard input, 
        travels from left to right rotors,
        Reflects back,
        Travels right to left and back to the plugboards
        """
        ch_1 = ch
        for rtr in self.rotors[1:][::-1]:
            r = Rotor(rtr)
            ch_1 = r.encode_right_to_left(ch_1)
            # print(ch_1)

        r = Rotor(self.rotors[0])
        ch_1 = r.encode_left_to_right(ch_1)
        # print(ch_1)

        for rtr in self.rotors[1:]:
            r = Rotor(rtr)
            ch_1 = r.encode_left_to_right(ch_1)
            # print(ch_1)

        self.encode_counter += 1

        return ch_1

# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    rs = Rotor_simulator(["B", "I", "II", "III"])
    print(rs.encode("A"))
    

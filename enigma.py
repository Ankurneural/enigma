
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
    
    def __init__(self, rotors, initial_positions, ring_settings, reflector):
    
        self.rotors = rotors

        self.initial_pos = initial_positions
        self.ring_settings = ring_settings

        self.rotor_offset = self.cal_rotor_offset()

        self.reflector = reflector

    def cal_rotor_offset(self):
        """Finds how much the offset is for each rotor
           The offset is the position of the Character at the Label string 
        """
        try:
            assert(len(self.rotors) == len(self.initial_pos))
        except:
            raise AssertionError
        
        initial_pos_post_rs = list()
        for r_s, i_p in zip(self.ring_settings, self.initial_pos):
            if r_s == "1":
                initial_pos_post_rs.append(i_p)
            else:
                ind = Rotor.Label.find(i_p) - (int(r_s)-1)
                initial_pos_post_rs.append(Rotor.Label[ind])
        
        self.initial_pos = initial_pos_post_rs
        print(f"Post Ring Setting: Initial Positions {self.initial_pos}")

        ro = list()
        for rotor in self.initial_pos:
            ro.append(Rotor.Label.find(rotor))
        return ro

    def set_offset(self):
        """increase the offset, run before each encoding
        """
        self.rotor_offset[-1] += 1
        self.rotor_offset = [offset % 26 for offset in self.rotor_offset]
    
    def before_reset_char(self, rotor_object, charr, offset):
        """Based on the rotor, and offset, shift the character
        """
        if offset == 0:
            return charr
        else:
            ind = rotor_object.Label.find(charr) + offset
            char1 = rotor_object.Label[ind]
            print(f"The character is changed due to before offset{offset} from {charr} to {char1}")
            return char1
    
    def after_reset_char(self, rotor_object, charr, offset):
        """Based on the rotor, and offset, shift the character
        """
        if offset == 0:
            return charr
        else:
            ind = rotor_object.Label.find(charr) - offset
            char1 = rotor_object.Label[ind]
            print(f"The character is changed due to after offset{offset} from {charr} to {char1}")
            return char1

    def encode(self, ch):
        """Takes plugboard input, 
        travels from left to right rotors,
        Reflects back,
        Travels right to left and back to the plugboards
        """
        self.set_offset()
    
        ch_1 = ch
        for rtr, os in zip(self.rotors[::-1], self.rotor_offset[::-1]):
            r = Rotor(rtr)
            ch_1 = self.before_reset_char(r, ch_1, os)
            ch_1 = r.encode_right_to_left(ch_1)
            ch_1 = self.after_reset_char(r, ch_1, os)
            print(f"Right to Left with rotor {rtr} and offset {os} ")
            print(ch_1)

        r = Rotor(self.reflector)
        ch_1 = r.encode_left_to_right(ch_1)
        print(f"Transformation after the reflector")
        print(ch_1)

        for rtr, os in zip(self.rotors, self.rotor_offset):
            r = Rotor(rtr)
            ch_1 = self.before_reset_char(r, ch_1, os)
            ch_1 = r.encode_left_to_right(ch_1)
            ch_1 = self.after_reset_char(r,ch_1, os)
            print(f"Left to Right with rotor {rtr} and offset{os}")
            print(ch_1)

        print("--------------")

        return ch_1

# You will need to write more classes, which can be done here or in separate files, you choose.
if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    rs = Rotor_simulator(rotors=["I", "II", "III"], initial_positions=["A", "A", "A"],
                                    ring_settings=["1", "1", "1"], reflector="B")
    rs.encode("A")
    # rs.encode("F")
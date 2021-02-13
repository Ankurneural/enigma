
class PlugLead:
    def __init__(self, mapping):
        # Your code here
        self.mapping = mapping
        self.map_dic = self.map_dictionary()
    
    def map_dictionary(self):
        """Creates a dictionary of the inputs for mapping
        """
        try:
            assert(len(self.mapping)==2)
        except ValueError as e:
            print(e)
            print("Mapping must be of Length 2")
        
        map_d = {}
        map_d[self.mapping[0]] = self.mapping[1]
        map_d[self.mapping[1]] = self.mapping[0]
        return map_d
        
    def encode(self, character):
        # Your code here
        if character in self.map_dic.keys():
            return self.map_dic[character]
        else:
            return character


class Plugboard:
    # Your code here
    pass

# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    l = PlugLead("AB")
    print(l.encode("A"))
    print(l.encode("B"))
    print(l.encode("Z"))


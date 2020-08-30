import json

# encoding custom types
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"object of type '{type_name}' in not JSON' serializable")

'''
Encoding Custom Types:
- provide encoding function to the dump() method's default's parameter/
'''

def encode_complex(z):
    if isnstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

# The other common approach is to subclass the standard JSONEncoder nad override
# default() method:
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            raise super().default(z)

'''
Instead of raising the TypeError yourself, you can simply let the 
base class handle it. You can use this either directly in the dump() 
method via the cls parameter or by creating an instance of the 
encoder and calling its encode() method:
'''

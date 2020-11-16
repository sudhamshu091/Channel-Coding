import numpy as np
from scipy.ndimage.interpolation import shift

class ConvolutionalCodes:

    def __init__(self, poly):
        self.poly = poly

    def poly2regs(self):
        poly = self.poly
        L = poly[0] # Constrain length
        Gen = [] # List for generators
        for g in poly[1]:
            bin_str = bin(int(str(g), 8))[2:] # From octal to binary representation
            split_str = list(tuple(bin_str)) # Split the bits
            split_int = [int(i) for i in split_str] # Convert to from chars to integers
            Gen.append(split_int)
        return L, Gen

    def encoder(self, message):
        L, Gen = self.poly2regs()
        Gen = np.matrix(Gen)
        memory = np.zeros((L,))
        encoded = []
        for bit in message:
            memory = np.abs(shift(memory, 1, cval=np.NaN).round())
            memory[0] = bit
            y = np.array(np.dot(Gen, memory) % 2)
            [encoded.append(i) for i in y[0]]
        return encoded

convC = ConvolutionalCodes([7,[171, 133]])
convC.poly2regs()
convC.encoder([1, 0, 1, 0, 0, 1, 1])

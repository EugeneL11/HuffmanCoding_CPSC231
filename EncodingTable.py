# COURSE: CPSC 231 FALL 2021
# Name: Eugene Lee
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Zack Hassan - T04
# ID: 30137489
# Date: Dec.9th, 2021
# Description: This class will encode the text and create a table of characters using methods and recursion

import sys

class EncodingTable:
    """
    A class to represent an Encoding Table made from a Huffman Tree
    Attributes
    ----------
    encode : str
        The dictionary storing for each symbol "char" as binary bit string code "code"
    """

    def __init__(self, tree):
        """
        Constructs an EncodingTable using a HuffmanTree
        :param tree: The HuffmanTree to use to build the EncodingTable dictionary encode
        """
        # Create empty dictionary
        self.encode = {}
        # Launch recursive function to store values into self.encode dictionary
        self.recurse(tree, "")

    # PART 7 (recurse)
    def recurse(self, tree, code):
        """
        Uses recursion to continually assign numbers to their bits
        :param tree: The HuffmanTree tree to use to determine the codes
        :param code: the current string code created so far
        :return: None
        """
        # Every recursive call
        if tree.bit is not None:
            if tree.bit == True:
                code += "1"
            else:
                code += "0"
        # The base case
        if tree.left is None and tree.right is None:
            self.encode[tree.char] = code
        # The recursive case
        else:
            self.recurse(tree.left, code)
            self.recurse(tree.right, code)

    # PART 6 (string)
    def __str__(self):
        """
        Creates the visual of the encoding table
        :return: The string of the encoding table
        """
        empty_string = ""
        encoding_table_list = []
        # Creating a list of the information from the encode dictionary
        for key in self.encode:
            encoding_table_list.append(key)
            encoding_table_list.sort()
        # Creating the encoding table
        for char in encoding_table_list:
            empty_string += "{}:{}\n".format(repr(char), self.encode[char])
            # Gets rid of the new line at the end
            new_string = empty_string[0:-1]
        return new_string

    def encode_text(self, text):
        """
        Encodes the provided text using the internal encoding dictionary (turns each character symbol into a bit string)
        :param text: The string text to encode
        :return: A bit string "000100" based on the internal encode dictionary
        """
        output_text = ""
        # Loop through characters
        for char in text:
            # If one matches then encode into bitstring
            if char in self.encode:
                output_text += self.encode[char]
            else:
                sys.exit(f"Can't encode symbol {char} as it isn't in the encoding table:\n{self}")
        return output_text

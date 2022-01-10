# COURSE: CPSC 231 FALL 2021
# Name: Eugene Lee
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Zack Hassan - T04
# ID: 30137489
# Date: Dec.9th, 2021
# Description: This class will make the trees, sort and compare them, convert them to strings, and merge them

class HuffmanTree:
    """
    A class to represent an Huffman Tree
    Attributes
    ----------
    char : str
        The characters represented by this tree
    count : int
        The count of how many times char occurred in the text
    left : HuffmanTree/None
        The left HuffmanTree below this one
    right : HuffmanTree/None
        The right HuffmanTree below this one
    bit : bool
        The bit symbol used to reach this HuffmanTree (either True/False for 1/0)


    General Structure
                         HuffmanTree (char,count,bit)
                          /    \
                      left    right
                        /        \
                HuffmanTree      HuffmanTree

    Default Structure
                         HuffmanTree (char,count,None)
                          /    \
                      left    right
                        /        \
                     None         None
    """

    # PART1 (constructor)
    def __init__(self, char, count, left=None, right=None, bit=None):
        """
        Creating the constructor for the class
        All the parameters are already described at the top of the program
        :return: None
        """
        # Using the constructors for initialization
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit

    # PART2 (order)
    def __lt__(self, other):
        """
        This less than function will compare two trees
        :param other: Some other object that is being compared to self
        :return: A True or False value that will sort the trees
        """
        # Compare the count of each tree so that we can sort them properly
        if self.count > other.count:
            return True
        elif self.count < other.count:
            return False
        # If the count of each tree is identical to each other, compare the char to sort properly
        else:
            if self.char > other.char:
                return True
            else:
                return False

    # PART3 (string)
    def __str__(self):
        """
        Converts the text into readable string
        :return: The string sentence
        """
        # If left or right is None, use None
        if self.left is None:
            left = None
        else:
            left = repr(self.left.char)
        if self.right is None:
            right = None
        else:
            right = repr(self.right.char)
        # Setting the bit values for when they are True and False
        if self.bit == True:
            self.bit = 1
        if self.bit == False:
            self.bit = 0
        return "({},{},{},{},{})".format(repr(self.char), self.count, left, right, self.bit)

    # PART3 (representation)
    def __repr__(self):
        """
        Converts the text into the appropriate repr form
        :return: The string sentence
        """
        # This is for the verbose input, involving the detailed printing
        if self.bit == True:
            self.bit = True  # Should print True and False instead of 0 and 1
        if self.bit == False:
            self.bit = False
        return "HuffmanTree({},{},{},{},{})".format(repr(self.char), repr(self.count), repr(self.left), repr(self.right), repr(self.bit))

    # PART5 (equality)
    def __eq__(self, other):
        """
        Checks if two trees are identical to each other
        :param other: Another tree that is being compared to self
        :return: A True or False value on if the trees are the same or not
        """
        # Checking if the two input files are identical to each other
        if other is None:
            return False
        if self.char == other.char and self.left == other.left and self.right == other.right:
            return True
        else:
            return False

# PART1 (make_trees)
def make_trees(dictionary):
    """
    Loop through the dictionary in order to store the char and count in a list
    :param dictionary: The dictionary with char as its key and count as its value
    :return: The huffman list that contains the char and its associated count
    """
    #  The empty list to store the trees in
    huffman_list = []
    # Loop through the whole dictionary and store the necessary data into the list created above
    for key in dictionary:
        huffman_list.append(HuffmanTree(key, dictionary[key]))
    return huffman_list

# PART4 (merge)
def merge(t1, t2):
    """
    Merges two trees into one, sorted by its count and char
    :param t1: The first tree being compared
    :param t2: The second tree being compared
    :return: A bigger tree with t1 and t2 merged into one
    """
    # t1 has a smaller count so put it on the left side
    if t1.count < t2.count:
        left_tree = t1
        right_tree = t2
        t1.bit = 0
        t2.bit = 1
    # t2 has a smaller count so put it on the left side
    elif t2.count < t1.count:
        left_tree = t2
        right_tree = t1
        t2.bit = 0
        t1.bit = 1
    # If the count is identical, we further evaluate using the char value
    else:
        if t2.char < t1.char:
            left_tree = t2
            right_tree = t1
            t2.bit = 0
            t1.bit = 1
        else:
            left_tree = t1
            right_tree = t2
            t1.bit = 0
            t2.bit = 1
    merged_tree_char = t1.char + t2.char
    merged_tree_count = t1.count + t2.count
    new_bit = None
    return HuffmanTree(merged_tree_char, merged_tree_count, left_tree, right_tree, new_bit)

class ModulusHashing:
    # creation
    def __init__(self):
        self.table = [None] * 10

    # modulus hash function
    def H(self, key):
        # equal to key % size(10)
        return key % 10

    # insert
    def insert(self, data):
        # hash value
        hash_value = self.H(data)
        # insert to table
        self.table[hash_value] = data

    # retrieve
    def retrieve(self, key):
        hash_value = self.H(key)
        # return value if in table
        if hash_value < len(self.table):
            return self.table[hash_value]
        # else return None
        else:
            return None

    # display table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
# create a hash table with the given elements
elements = [1, 3, 5, 4, 7, 2, 9, 20]
hash_table = ModulusHashing()
for element in elements:
    hash_table.insert(element)

# display the hash table
hash_table.display()

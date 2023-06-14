# copy this complete cell to a text file and include it in your submission

# a relation subclass respecting key constraints:
class KeyRelation(Relation):
    # keys: names of the key attributes as a list
    def __init__(self, name, schema, keys):
        super().__init__(name, schema)

        # assert that the list of keys is subset-equal self-attributes:
        assert set(keys) <= set(self.attributes)
        # make sure that at least one key attribute is defined:
        assert len(keys) >= 1

        # add your code here!
        # ...
        # initialize data structures that are required
        # to check the key constraint for new tuples

        # get index of key attributes in schema
        indices = []
        for k in keys:
            for i, (key_name, key_type) in enumerate(schema):
                if k == key_name:
                    indices.append(i)
                    break
        self.indices = indices
        self.tuples_prim_keys = set()  # will be a set containing a tuple with each value at the indices position
        self.key_attributes = keys

    def add_tuple(self, tup):
        # add your code here!
        # ...
        # check if there is a tuple with the same key in the relation
        # only insert it using super().add_tuple(tup) if there is not.
        # raise a ValueError if the key is already present.
        # Make sure to perform your check in O(1) time!

        # get the important information
        key = tuple([tup[i] for i in self.indices])
        if key in self.tuples_prim_keys:
            raise ValueError()

        super().add_tuple(tup)
        self.tuples_prim_keys.add(key)

    def print_schema(self):
        super().print_schema()
        # add your code here!
        # ...
        # should also print the key attributes
        print("Keys:", self.key_attributes)
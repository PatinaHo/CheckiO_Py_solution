### Island: O'Reilly. Problem: Friends

class Friends:
    def __init__(self, connections):
        """ Create a Friends object.
        Args:
            connections: An iterable object(list or tuple) which includes multiple sets,
                         each set contains 2 vertices that connects together.
                         ex. ({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}), [{"1", "2"}, {"3", "1"}]
        Produce:
            self.network: A dictionary that includes vertices(keys) and their neighbors(values).
                          ex. {'b': {'c', 'a'}, 'c': {'b', 'a'}, 'a': {'b', 'c'}}
            vertices_set: A set that includes all vertices(int).

        """
        vertices_set = connections[0]
        for e in connections:
            vertices_set = vertices_set.union(e)
        self.network = dict.fromkeys(vertices_set, set())

        for e in connections:
            elem1 = e.pop()
            elem2 = e.pop()
            self.network[elem1] = self.network[elem1] | set([elem2])
            self.network[elem2] = self.network[elem2] | set([elem1])
        
    def add(self, connection):
        elem1 = connection.pop()
        elem2 = connection.pop()
        if(elem1 not in self.network.keys() or elem2 not in self.network.keys()):  # Doesn't exist, can be added
            if(elem1 not in self.network.keys()):
                self.network[elem1] = set([elem2])    
            if(elem2 not in self.network.keys()):            
                self.network[elem2] = set([elem1])
            self.network[elem2] = self.network[elem2] | set([elem1])
            self.network[elem1] = self.network[elem1] | set([elem2])
            return True
        elif(elem2 in self.network[elem1]):  # Exist already, cannot be added
            return False
        else:  # Doesn't exist, can be added
            self.network[elem1] = self.network[elem1] | set([elem2])
            self.network[elem2] = self.network[elem2] | set([elem1])
            return True

    def remove(self, connection):
        elem1 = connection.pop()
        elem2 = connection.pop()
        if(elem1 not in self.network.keys() or elem2 not in self.network.keys()):  # no such element in network
            return False
        elif(elem2 in self.network[elem1]):  # Exist, can be removed
            self.network[elem2] = self.network[elem2] - set([elem1])
            self.network[elem1] = self.network[elem1] - set([elem2])
            return True
        else:  # element key in network, but no connection
            return False

    def names(self):
        vertices_set = set(self.network.keys())
        for vertex in vertices_set:
            if (self.network[vertex] == set()):
                vertices_set = vertices_set - set([vertex])            
        return vertices_set

    def connected(self, name):
        if (name in self.names()):
            return self.network[name]
        else:
            return set()



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

### Island: O'Reilly. Problem: How to Find Friends

def check_connection(network, first, second):
    """
    Args:
        network: tuple of strings representing connections.
        first: string of the checking point1
        second: string of the checking point2
    Returns:
        boolean value(true/false) of whether the two check points are in the same graph
    Important side effect:
        setlist: list of sets. Each set representing a subgraph, without denoting the sequence of graph vertices.

    """
    setlist = []
    for connection in network:
        s = ab = set(connection.split('-'))    # unify all set related to a, b
        print("setlist =", setlist)
        print("ab =", ab)

        for t in setlist[:]:    # we need to use copy
            print("t =", t)
            if t & ab:    # check if t include a or b, include means they're in the same subgraph
                print("t include ab")
                s = s|t   # s became new subgraph include ab and old subgraph
                setlist.remove(t)    # remove old subgraph
                print("setlist, after removing t =", setlist)
        setlist.append(s)    # only s include a, b    # either replacing old subgraph or append a new subgraph
        print("setlist, after append s =", setlist)
        print("")
    return any(set([first, second]) <= s for s in setlist)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False

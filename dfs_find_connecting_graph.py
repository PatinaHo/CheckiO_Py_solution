graph = {'dr101': ['mr99', 'out00'], 'mr99': ['dr101', 'out00'], 'out00': ['mr99', 'dr101'], 
         'scout1': ['scout2', 'scout3', 'scout4'], 'scout2': ['scout1'], 'scout3': ['scout1'],
         'scout4': ['scout1', 'sscout'], 'sscout': ['scout4', 'super'], 'super': ['sscout']}

def dfs_recursive(graph, vertex, vertex_compo_pair, component_no, path=[]):
    """ Depth-first search a connected graph and give graph number.
    Args: 
        graph: A dictionary of vertices(keys: string) and their neighbors(value: list).
        vertex: starting vertex
        vertex_compo_pair: A dictionary of visited vertex(keys: string) and the graph number they were given(value: int).
        component_no: number that each graph were given
        path: List of visited vertices to be modify each time
    Returns: 
        path: A list of visited vertices.
    """
    path += [vertex]
    vertex_compo_pair[vertex] = component_no    # Prework for find_connecting_components
    for neighbor in graph[vertex]:
        if neighbor not in path:
            vertex_compo_pair[neighbor] = component_no    # Prework for find_connecting_components
            path = dfs_recursive(graph, neighbor, vertex_compo_pair, component_no, path)
    
    return path

def find_connecting_components(graph):
    """
    Args:
        graph: A dictionary of vertices(keys: string) and their neighbors(value: list).
    Returns:
        vertex_compo_pair: A dictionary of visited vertex(keys: string) and the graph number they were given(value: int).
    """
    vertex_compo_pair = {}
    component_no = 1
    for vertex in graph:
        if vertex not in vertex_compo_pair:
            dfs_recursive(graph, vertex, vertex_compo_pair, component_no)
            component_no += 1
            
    return vertex_compo_pair
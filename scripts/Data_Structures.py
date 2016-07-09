#!/usr/bin/env python
'''A ROSALIND bioinformatics script containing useful data structures.'''


class SuffixTree(object):
    '''Creates a suffix tree for the provided word.'''

    def __init__(self, word):
        '''Initializes the suffix tree.'''
        self.nodes = [self.Node(None, 0)]
        self.edges = dict()
        self.descendants_dict = dict()
        if type(word) == str:
            self.add_word(word)

    class Node(object):
        '''Suffix tree node class.'''
        def __init__(self, parent, number):
            self.parent = parent
            self.number = number
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def remove_child(self, child):
            self.children.remove(child)

        def update_parent(self, parent):
            self.parent = parent

    def add_word(self, word):
        '''Add a word to the suffix tree.'''
        # Check to make sure word ends in '$'.
        if word[-1] != '$':
            word += '$'
        self.word = word
        self.n = len(self.word)

        for i in xrange(self.n):
            parent_node, edge_start, overlap = self.insert_position(i, self.nodes[0])

            if overlap:
                p_edge_start, p_edge_end = self.edges[(parent_node.parent.number, parent_node.number)]

                # Get the edge to insert
                insert_len = 0
                while word[edge_start:edge_start + insert_len] == word[p_edge_start:p_edge_start + insert_len]:
                    insert_len += 1

                # Create a new node for insertion
                new_node = self.Node(parent_node.parent, len(self.nodes))
                new_node.add_child(parent_node)
                self.add_node(parent_node.parent, p_edge_start, p_edge_start + insert_len - 1, new_node)

                # Update the parent node since a new node is inserted above it
                del self.edges[(parent_node.parent.number, parent_node.number)]
                parent_node.parent.remove_child(parent_node)
                parent_node.update_parent(new_node)
                self.edges[(parent_node.parent.number, parent_node.number)] = [p_edge_start + insert_len - 1, p_edge_end]

                # Add new child node
                self.add_node(new_node, edge_start + insert_len - 1, self.n)

            else:
                # No insertion necessary, just append the new node.
                self.add_node(parent_node, edge_start, self.n)

    def insert_position(self, start_index, parent_node):
        '''Determine the location and method to insert a suffix into the suffix tree.'''
        for child_node in parent_node.children:
            edge_start, edge_end = self.edges[(parent_node.number, child_node.number)]
            if self.word[start_index:start_index + edge_end - edge_start] == self.word[edge_start:edge_end]:
                return self.insert_position(start_index + edge_end - edge_start, child_node)

            elif self.word[edge_start] == self.word[start_index]:
                return child_node, start_index,  True

        return parent_node, start_index, False

    def add_node(self, parent_node, edge_start, edge_end, child_node=None):
        '''Adds a node and the associated edge to the suffix tree.'''

        # Create child node, if necessary
        if child_node is None:
            child_node = self.Node(parent_node, len(self.nodes))

        # Add node to node list
        self.nodes.append(child_node)

        # Add child to parent
        parent_node.add_child(child_node)

        # Add edge to edge dict
        self.edges[(parent_node.number, child_node.number)] = [
            edge_start, edge_end]

    def print_edges(self):
        '''Returns the string representations of the edges.'''
        return [self.word[i:j] for i, j in self.edges.values()]

    def total_descendants(self, base_node):
        '''Returns the total number of descendants of a given node.'''
        if base_node not in self.descendants_dict:
            self.descendants_dict[base_node] = len(base_node.children) + sum([self.total_descendants(c) for c in base_node.children])

        return self.descendants_dict[base_node]

    def node_word(self, end_node):
        '''Returns the prefix of the suffix tree word up to a given node.'''
        current_word = ''
        while end_node.number != 0:
            temp_indices = self.edges[(end_node.parent.number, end_node.number)]
            current_word = self.word[temp_indices[0]:temp_indices[1]] + current_word
            end_node = end_node.parent

        return current_word.strip('$')


class Trie(object):
    '''Constructs a trie.'''

    def __init__(self, word=None):
        self.nodes = [[self.Node('', 1)]]
        self.edges = []
        if word is not None:
            self.add_word(word)

    class Node(object):
        '''Trie node class.'''
        def __init__(self, prefix, number):
            self.prefix = prefix
            self.number = number
            self.depth = len(prefix)

    class Edge(object):
        '''Trie edge class.'''
        def __init__(self, letter, par_node, chi_node):
            self.letter = letter
            self.parent_node = par_node
            self.child_node = chi_node

        def get_info(self):
            '''Return the edge information compactly.'''
            return ' '.join(map(str, [self.parent_node, self.child_node, self.letter]))

    def add_word(self, word):
        '''Adds a word to the trie.'''
        if type(word) == list:
            for w in word:
                self.add_word(w)
        else:
            parent = self.find_parent(word)
            for i in range(len(parent.prefix), len(word)):
                new_node = self.Node(word[:i + 1], self.node_count() + 1)
                self.edges.append(self.Edge(word[i], parent.number, self.node_count() + 1))
                self.insert_node(new_node)
                parent = new_node

    def insert_node(self, node):
        '''Determine the location to insert the current node.'''
        if node.depth > self.depth():
            self.nodes.append([node])
        else:
            self.nodes[node.depth].append(node)

    def depth(self):
        '''Returns the depth of the trie.'''
        return len(self.nodes) - 1

    def node_count(self):
        '''Returns the total number of nodes.'''
        count = 0
        for trie_depth in self.nodes:
            count += len(trie_depth)
        return count

    def find_parent(self, word):
        '''Return the parent node of the word to be inserted.'''
        for i in range(min(len(word), self.depth()), 0, -1):
            for node in self.nodes[i]:
                if word[:i] == node.prefix:
                    return node

        return self.nodes[0][0]

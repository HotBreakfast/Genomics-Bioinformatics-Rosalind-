#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing classes that converts a suffix array to a suffix tree.'''


class Node(object):
    """Node class to be used in the SuffixArrayToTree class."""
    def __init__(self, parent_num):
        """Initialize parameters."""
        self.parent = parent_num
        self.children = []

    def update_parent(self, new_parent_num):
        """Update the nodes parent."""
        self.parent = new_parent_num

    def add_child(self, node_num):
        """Add a child node to the node."""
        self.children.append(node_num)

    def remove_child(self, node_num):
        """Remove a child from the node."""
        self.children.remove(node_num)


class Edge(object):
    """Edge class to be used in the SuffixArrayToTree class."""
    def __init__(self, start_index, stop_index):
        """Initialize parameters."""
        self.start_index = start_index
        self.stop_index = stop_index


class SuffixArrayToTree(object):
    """Constucts a suffix tree for thefrom the given word, suffix array and lcp array."""
    def __init__(self, word, suffix_array, lcp_array):
        """Initialize parameters and build the tree with the given words."""

        # Initialize parameters.
        self.word = word + ['', '$'][word[-1] != '$']
        self.suffix_array = suffix_array
        self.lcp_array = lcp_array

        # Initialize nodes and edges.
        self.nodes = [Node(-1)]
        self.edges = {}

        # Add the words to the generalized suffix tree.
        self._add_word()

    def _add_word(self):
        """Adds a word to the generalized suffix tree."""

        # Add each suffix to the generalized suffix tree.
        for i, sa_elmt in enumerate(self.suffix_array):
            # Get the insertion point and associated suffix.
            insertion_parent, insertion_suffix = self._insert_node(self.word[sa_elmt:], self.lcp_array[i])

            # Create the new node, and add it as a child to its parent node.
            self.nodes.append(Node(insertion_parent))
            self.nodes[insertion_parent].add_child(len(self.nodes)-1)

            # Create the edge associated to with the new node.
            self.edges[insertion_parent, len(self.nodes)-1] = Edge(len(self.word)-len(insertion_suffix), len(self.word))

    def _insert_node(self, suffix, lcp_distance, current_node=0):
        """Traverses the tree to determine the insertion point of the given suffix."""

        # Done if we've hit zero lcp_distance.
        if lcp_distance == 0:
            return current_node, suffix

        # Distance to the next node is the length of the edge word associated with travelling to rightmost path.
        dist_to_next_node = len(self.edge_word(self.edges[current_node, self.nodes[current_node].children[-1]]))

        if dist_to_next_node <= lcp_distance:
            return self._insert_node(suffix[dist_to_next_node:], lcp_distance - dist_to_next_node, self.nodes[current_node].children[-1])
        else:
            return self._split_edge(current_node, self.nodes[current_node].children[-1], lcp_distance), suffix[lcp_distance:]

    def _split_edge(self, parent_num, child_num, split_pos):
        """
        Splits the edge between the given parent and child nodes at the given split position.
        Inserts a new node at the split position and returns the index of the new node.
        """

        # Create the new node.
        new_node = len(self.nodes)
        self.nodes.append(Node(parent_num))
        self.nodes[new_node].add_child(child_num)

        # Add new_node as a child of parent_num.  Remove child_num from children list.
        self.nodes[parent_num].add_child(new_node)
        self.nodes[parent_num].remove_child(child_num)

        # Update child_num's parent to new_node.
        self.nodes[child_num].update_parent(new_node)

        # Create the new edges.
        old_edge = self.edges[parent_num, child_num]
        self.edges[parent_num, new_node] = Edge(old_edge.start_index, old_edge.start_index + split_pos)
        self.edges[new_node, child_num] = Edge(old_edge.start_index + split_pos, old_edge.stop_index)

        # Remove the old edge.
        del self.edges[parent_num, child_num]

        return new_node

    def edge_word(self, e):
        """Returns the substring associated with a given edge."""
        return self.word[e.start_index:e.stop_index]

    def word_up_to_node(self, node_num):
        """Returns the substring associated with a traversal to the given node."""
        node_word = ''
        while self.nodes[node_num].parent != -1:
            # Prepend the substring associated with each edge until we hit the root of the generalized suffix tree.
            node_word = self.edge_word(self.edges[self.nodes[node_num].parent, node_num]) + node_word
            node_num = self.nodes[node_num].parent

        return node_word

    def node_depth(self, node_num):
        """
        Returns the length of the substring traversal up to the given node,
        discounting the out of alphabet character, and without constructing the entire word.
        """

        # Trivially have depth zero if at the root.
        if node_num == 0:
            return 0

        # The first edge (working backwards) is the only one that can have an out of alphabet character, so take extra precaution.
        first_edge = self.edge_word(self.edges[self.nodes[node_num].parent, node_num])
        depth = len(first_edge) if '$' not in first_edge else len(first_edge[:first_edge.index('$')])

        # Move to the parent node and add the length of the next edge until we hit the root.
        node_num = self.nodes[node_num].parent
        while self.nodes[node_num].parent != -1:
            # Prepend the substring associated with each edge until we hit the root of the generalized suffix tree.
            depth += len(self.edge_word(self.edges[self.nodes[node_num].parent, node_num]))
            node_num = self.nodes[node_num].parent

        return depth

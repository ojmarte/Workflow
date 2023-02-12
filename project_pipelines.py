"""
This module provides functions for performing various mathematical operations.
"""

import re

class Node:
    """
    This is a docstring that describes what the class does.
    """
    def __init__(self, func, inputs, outputs, name):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs if outputs is not None else []
        self.name = name

class Pipeline:
    """
    This is a docstring that describes what the class does.
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        """
        This is a docstring that describes what the function does.

        Parameters:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

        Returns:
        str: The result of the function.
        """
        node.inputs = [n.outputs for n in self.nodes]
        self.nodes.append(node)

    def node_dependencies(self):
        """
        This is a docstring that describes what the function does.

        Parameters:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

        Returns:
        str: The result of the function.
        """
        nodes_deps = []
        for node in self.nodes:
            deps = []
            for other_node in self.nodes:
                if node.name == other_node.name:
                    break
                deps.append(other_node.name)
            nodes_deps.append({'node': node.func.__name__, 'name': node.name, 'deps': deps})
        return nodes_deps

def create_pipeline(nodes):
    """
    This is a docstring that describes what the function does.

    Parameters:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

    Returns:
    str: The result of the function.
    """
    pipeline = Pipeline()
    for node in nodes:
        pipeline.add_node(node)
    return pipeline

def clean_name(name):
    """
    This is a docstring that describes what the function does.

    Parameters:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

    Returns:
    str: The result of the function.
    """
    return re.sub(r"[\W_]+", "-", name).strip("-")

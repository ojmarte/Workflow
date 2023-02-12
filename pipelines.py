"""
This module provides functions for performing various mathematical operations.
"""
from nodes import make_predictions, report_accuracy, split_data, project_data

from project_pipelines import create_pipeline, Node

def generate_pipeline():
    """
    This is a docstring that describes what the function does.

    Parameters:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

    Returns:
    str: The result of the function.
    """

    return create_pipeline([
        Node(
            make_predictions,
            ["example_iris_data", "parameters"],
            ["X_train", "X_test", "y_train", "y_test"],
            "make_predictions"),
        Node(
            report_accuracy,
            ["X_train", "X_test", "y_train"],
            ["y_pred"],
            "report_accuracy"),
        Node(
            split_data,
            ["y_pred", "y_test"],
            None,
            "split_data"),
        Node(
            project_data,
            ["y_pred", "y_test"],
            None,
            "project_data")
    ])

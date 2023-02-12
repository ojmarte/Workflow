"""
This module provides functions for performing various mathematical operations.
"""

from pathlib import Path
import click
from jinja2 import Environment, FileSystemLoader

from pipelines import generate_pipeline

TEMPLATE_FILE = "argo_spec.tmpl"
SEARCH_PATH = Path("templates")

@click.command()
@click.argument("image", required=True)
@click.option("-p", "--pipeline", "pipeline_name", default=None)
def generate_file_config(image, pipeline_name):
    """
    This is a docstring that describes what the function does.

    Parameters:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

    Returns:
    str: The result of the function.
    """
    loader = FileSystemLoader(searchpath=SEARCH_PATH)
    template_env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = template_env.get_template(TEMPLATE_FILE)

    package_name = "Workflow Template"

    pipeline_name = pipeline_name or "__default__"
    pipeline = generate_pipeline()
    tasks = pipeline.node_dependencies()

    output = template.render(image=image, package_name=package_name, tasks=tasks)

    (SEARCH_PATH / f"argo-{package_name}.yml").write_text(output)

if __name__ == "__main__":
    generate_file_config()

# Project Name
This project generates an Argo workflow configuration file based on your pipeline tasks.

## Requirements
- Python 3
- Jinja2
- Click
## Usage
To generate a workflow configuration file, run the following command:

```python
python3 build_spec.py <image_name> --pipeline <pipeline_name>
```
Where `<image_name>` is the name of the Docker image you want to use in the workflow, and `<pipeline_name>` is an optional argument that specifies the name of the pipeline. If no pipeline name is specified, a default name will be used.

Example usage:

css
Copy code
python3 build_spec.py my_image_name --pipeline pipeline_test
This will generate a workflow configuration file in the templates directory.

## Parameters
### Required
`<image_name>`: The name of the Docker image you want to use in the workflow.
### Optional
--pipeline `<pipeline_name>`: The name of the pipeline. If no pipeline name is specified, a default name will be used.
### Notes
The workflow configuration file is based on the `work_spec.tmpl` template file in the templates directory. You can customize this file as needed to generate a workflow that meets your needs.

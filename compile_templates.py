import os
from jinja2 import Environment, FileSystemLoader

# Define the templates directory
template_dir = './templates/'

# Define the output directory
output_dir = './static/'

# Create a Jinja2 environment with the FileSystemLoader
env = Environment(loader=FileSystemLoader(template_dir))

# Get a list of all template files in the templates directory
template_files = os.listdir(template_dir)

# For each template file
for template_file in template_files:
    if template_file != 'base.html':
        # Load the template
        template = env.get_template(template_file)

        # Render the template with no variables
        output = template.render()

        # Write the output to a file in the output directory
        with open(os.path.join(output_dir, template_file), 'w') as f:
            f.write(output)
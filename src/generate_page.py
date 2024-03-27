import os
import shutil
from block_markdown import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}to {dest_path} using {template_path}.")
    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path):
        from_contents = from_path.read()
    # Read the template file at template_path and store the contents in a variable.
    with open(template_path):
        template_contents = template_path.read()
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to HTML.
    from_contents_html = markdown_to_html_node(from_contents)
    #Use the extract_title function to grab the title of the page.
    from_title = extract_title(from_contents)
    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    template_contents.replace("\{\{ Title \}\}", from_title).replace("\{\{ Content \}\}", from_contents_html)
    # Write the new HTML to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    shutil.copy(template_contents, dest_path)



def extract_title(markdown):
    with open(markdown):
        contents = markdown.read()
    lines = contents.split('\n')
    for line in lines:
        if line.startswith("# "):
            text_only = line.lstrip("# ").rstrip('\n')
            return text_only
    raise Exception("No title found.")
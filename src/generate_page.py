import os
from pathlib import Path
from block_markdown import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content}, to {dest_dir_path} using {template_path}.")
    #iterate across the directory
    for item in os.listdir(dir_path_content):

        # Create path-like objects from our inputs
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        
        # if its a markdown file, add a .html file ending and call generate_page
        if os.path.isfile(from_path) and from_path.endswith('.md'):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)

        # Otherwise, its a directory, call this function on that directory
        else:
                generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path) as f:
        from_contents = f.read()
    # Read the template file at template_path and store the contents in a variable.
    with open(template_path) as f:
        template_contents = f.read()
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to HTML.
    node = markdown_to_html_node(from_contents)
    print(node)
    html = node.to_html()
    print(html)
    #Use the extract_title function to grab the title of the page.
    from_title = extract_title(from_contents)
    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    output_html = template_contents.replace("{{ Title }}", from_title).replace("{{ Content }}", html)
    # Write the new HTML to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output_html)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            text_only = line.lstrip("# ").rstrip('\n')
            return text_only
    raise Exception("No title found.")
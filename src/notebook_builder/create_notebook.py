import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import importlib.resources as pkg_resources


def get_image_base64(package, image_file_name):
    with pkg_resources.open_text(package, image_file_name) as img_file:
        return img_file.read()


def parse_py_to_notebook(args):
    base64_img = get_image_base64("notebook_builder", "python-logo-no-text.base64")

    image_html = f'<img src="data:image/png;base64,{base64_img}" style="display:block;margin:auto;width:10%"/>'
    additional_html = f"""
                        <br>
                        <div style="text-align:center; font-size:200%;">
                        <b>{args.topic}</b>
                        </div>
                        <br/>
                        <div style="text-align:center;">{args.author}</div>
                        <br/>
                        """
    header_html = image_html + additional_html

    with open(f"output/{args.name}" + ".py", "r") as file:
        lines = file.readlines()

    notebook = new_notebook()
    current_cell = []
    cell_type = None
    header_replaced = False

    for line in lines:
        # Replace the header section with the image and additional content
        if line.strip().startswith('""" Header cell """') and not header_replaced:
            if current_cell:
                add_cell_to_notebook(current_cell, cell_type, notebook)
            # Add the header as a markdown cell
            notebook.cells.append(new_markdown_cell(header_html))
            current_cell = []
            header_replaced = True
            continue

        # Ignore lines starting with """
        if line.strip().startswith('"""'):
            continue

        # Check for start of a markdown cell
        elif line.startswith("# %% [markdown]"):
            # Add previous cell to notebook if exists
            if current_cell:
                add_cell_to_notebook(current_cell, cell_type, notebook)
            current_cell = []
            cell_type = "markdown"

        # Check for start of a code cell
        elif line.startswith("# %%"):
            # Add previous cell to notebook if exists
            if current_cell:
                add_cell_to_notebook(current_cell, cell_type, notebook)
            current_cell = []
            cell_type = "code"

        # Add content to the current cell
        else:
            if cell_type == "markdown":
                # Remove leading '# ' from markdown lines
                formatted_line = line[2:] if line.startswith("# ") else line
                current_cell.append(formatted_line)
            elif cell_type == "code":
                # For code cells, add the line as it is, including blank lines
                current_cell.append(line)

    # Add the last cell to the notebook if exists
    if current_cell:
        add_cell_to_notebook(current_cell, cell_type, notebook)

    return notebook


def add_cell_to_notebook(cell_content, cell_type, notebook):
    if cell_type == "markdown":
        # For markdown cells, join the lines with a newline
        notebook.cells.append(new_markdown_cell("\n".join(cell_content)))
    elif cell_type == "code":
        # For code cells, join the lines as they are, but trim trailing blank lines
        code_content = "".join(cell_content).rstrip()
        notebook.cells.append(new_code_cell(code_content))

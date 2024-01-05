import streamlit as st
import nbformat
import nbconvert
import argparse
import os
import streamlit.components.v1 as components

from notebook_builder.generate import generate_py
from notebook_builder.create_notebook import parse_py_to_notebook


def main():
    st.title("Notebook Builder")

    # Initialize default_template
    default_template = ""

    # Reading the default template file
    try:
        with open("template.txt", "r") as file:
            default_template = file.read()
    except FileNotFoundError:
        st.error("Default template file not found.")
        return  # Stop further execution if the file is not found

    general_topic = st.text_input("General Topic", "Reinforcement Learning")
    topic = st.text_input("Specific Topic", "Markov Decision Processes")
    author = st.text_input("Author", "Anonymous")
    output_name = st.text_input("Output Notebook Name", "markov_decision_processes")

    # Editable text area for the template
    template_content = st.text_area(
        "Notebook Instructions", default_template, height=300
    )

    if st.button("Generate Notebook"):
        args = argparse.Namespace(
            general_topic=general_topic, topic=topic, author=author, name=output_name
        )

        generate_py(args, template_content)

        notebook = parse_py_to_notebook(args)

        with st.spinner("Generating Notebook..."):
            output_path = f"output/{output_name}.ipynb"
            nbformat.write(notebook, output_path)

            # Convert notebook to HTML
            html_exporter = nbconvert.HTMLExporter()
            html_exporter.template_name = (
                "classic"  # or use other templates like 'lab', 'base', etc.
            )
            body, _ = html_exporter.from_notebook_node(notebook)

            # Example HTML content
            body = "<div style='height:800px; overflow:auto;'>" + body + "</div>"

            # Use components.html to render the HTML
            components.html(body, height=800, scrolling=True)

            # Provide a download link for the notebook
            with open(output_path, "r") as file:
                st.download_button(
                    "Download Notebook", file, file_name=f"{output_name}.ipynb"
                )


if __name__ == "__main__":
    main()

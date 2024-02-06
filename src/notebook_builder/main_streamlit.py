import streamlit as st
import nbformat
import nbconvert
import argparse
import os
import streamlit.components.v1 as components

from notebook_builder.create_notebook import parse_py_to_notebook

import argparse
import nbformat

from notebook_builder.generate_with_html import (
    generate_from_data_science_handbook,
    generate_from_green_tea_press,
    generate_from_raw_code,
)


def main():
    st.title("Build Notebooks that help you learn better")

    # Add a field for entering a URL

    general_topic = st.text_input("General Topic", "What is the topic?")
    topic = st.text_input("Specific Topic", "What is the specific topic?")
    author = st.text_input("Author", "Your name")
    output_name = st.text_input("Output Notebook Name", "...")

    url = st.text_input("Enter the URL for the ressource", "https://example.com")

    if st.button("Generate Notebook"):
        args = argparse.Namespace(
            url=url,  # Include the URL in your arguments if needed
            general_topic=general_topic,
            topic=topic,
            author=author,
            name=output_name,
        )

        generate_from_raw_code(args)
        # generate_workshop(args)

        notebook = parse_py_to_notebook(args)

        # nbformat.write(notebook, f"output/{args.name}.ipynb")

        with st.spinner("Generating Notebook..."):
            output_path = f"output/{output_name}.ipynb"
            nbformat.write(notebook, output_path)

            # Convert notebook to HTML
            # html_exporter = nbconvert.HTMLExporter()
            # html_exporter.template_name = "classic"
            # body, _ = html_exporter.from_notebook_node(notebook)

            # Example HTML content
            # body = "<div style='height:800px; overflow:auto;'>" + body + "</div>"

            # Use components.html to render the HTML
            # components.html(body, height=800, scrolling=True)

            # Provide a download link for the notebook
            with open(output_path, "r") as file:
                st.download_button(
                    "Download Notebook", file, file_name=f"{output_name}.ipynb"
                )


if __name__ == "__main__":
    main()

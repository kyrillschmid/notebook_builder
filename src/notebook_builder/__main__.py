import argparse
import nbformat

from notebook_builder.generate import generate_py
from notebook_builder.create_notebook import parse_py_to_notebook


def main():
    parser = argparse.ArgumentParser(
        prog="notebook-builder",
        description="A tool to generate course material from a template notebook.",
        epilog="Have fun!",
    )
    parser.add_argument(
        "-general_topic",
        "--general_topic",
        default="Reinforcement Learning",
        help="What is the overall topic of the course?",
    )
    parser.add_argument(
        "-topic",
        "--topic",
        default="Markov Decision Processes",
        help="What is the specific topic of the course?",
    )
    parser.add_argument(
        "-author",
        "--author",
        default="Anonymous",
        help="What is your name?",
    )
    parser.add_argument(
        "-template",
        "--template",
        default="template_mdp.md",
        help="What is the name of the template?",
    )
    parser.add_argument(
        "-name",
        "--name",
        default="markov_decision_processes",
        help="What is the name of the output notebook?",
    )
    args = parser.parse_args()

    # generate .py
    generate_py(args)

    # generate .ipynb
    notebook = parse_py_to_notebook(args)

    # Saving the notebook
    nbformat.write(notebook, f"output/{args.name}.ipynb")


if __name__ == "__main__":
    main()
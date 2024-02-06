import argparse
import nbformat

from notebook_builder.generate_with_html import (
    generate_from_data_science_handbook,
    generate_from_green_tea_press,
    generate_from_raw_code,
)

from notebook_builder.translate import get_translation


def main():
    parser = argparse.ArgumentParser(
        prog="notebook-builder",
        description="A tool to generate course material from a template notebook.",
        epilog="Have fun!",
    )
    parser.add_argument(
        "-general_topic",
        "--general_topic",
        default="Python Data Sciece and Machine Learning",
        help="What is the overall topic of the course?",
    )
    parser.add_argument(
        "-topic",
        "--topic",
        default="Numpy Array Basics",
        help="What is the specific topic of the course?",
    )
    parser.add_argument(
        "-author",
        "--author",
        default="Dr. Kyrill Schmid",
        help="What is your name?",
    )
    parser.add_argument(
        "-name",
        "--name",
        default="Data Types in Python",
        help="What is the name of the output notebook?",
    )

    parser.add_argument(
        "-url",
        "--url",
        default="--",
        help="What is the url of the html file?",
    )
    args = parser.parse_args()

    print("Generating notebook...")

    # generate_from_data_science_handbook(args)
    # generate_from_green_tea_press(args)
    # generate_from_raw_code(args)

    # print(first_line + "\n" + section)

    get_translation(args)

    # notebook = parse_py_to_notebook(args)

    # nbformat.write(notebook, f"output/{args.name}.ipynb")


if __name__ == "__main__":
    main()

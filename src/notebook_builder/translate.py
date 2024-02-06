import re
from notebook_builder.prompt import get_prompt_translate_en_to_de
from notebook_builder.model import call_model

from notebook_builder.create_notebook import parse_py_to_notebook
from notebook_builder.write_notebook import write_translated_py


def split_file(args):
    with open(f"{args.name}" + ".py", "r") as file:
        content = file.read()  # Read the entire file content into a single string

    # Split the content at each occurrence of '# %%'
    sections = re.split("(# %%)", content)

    # Re-attach the delimiter to the parts it was split from, except for the first part if it doesn't start with the delimiter
    result = []
    if (
        sections[0] != "# %%"
    ):  # If the first part doesn't start with the delimiter, add it as is
        result.append(sections.pop(0))
    while sections:
        # Combine the delimiter with the following part
        result.append(sections.pop(0) + sections.pop(0) if sections else "")

    return result


def get_translation(args):

    sections = split_file(args)

    all_sections = [sections[0]]

    for section in sections[1:]:
        all_sections.append(section)

        translated_first_line = section.splitlines()[0].replace("en", "de")
        remainder = "\n".join(section.splitlines()[1:])

        if not is_code_cell(translated_first_line):
            prompt = get_prompt_translate_en_to_de(args, remainder)
            translated_remainder = call_model(prompt, model="gpt-3.5-turbo-0125")
            all_sections.append(
                translated_first_line + "\n" + translated_remainder + "\n\n"
            )

    write_translated_py(args, all_sections)


def is_code_cell(first_line):
    return not "lang" in first_line

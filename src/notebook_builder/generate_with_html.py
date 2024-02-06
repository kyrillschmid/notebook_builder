from notebook_builder.crawl_site import (
    get_data_science_handbook_html,
    get_green_tea_press_html,
    get_raw_py_file,
)
from notebook_builder.prompt import (
    get_prompt,
    get_workshop_prompt,
    get_prompt_for_raw_code,
    get_prompt_divide_raw_code,
)
from notebook_builder.model import call_model
from notebook_builder.write_notebook import (
    write_notebook_header,
    write_noteboo_body,
    write_workshop_to_file,
)


def generate_from_data_science_handbook(args):
    write_notebook_header(args)

    sections = get_data_science_handbook_html(args)

    for i, section in enumerate(sections):
        prompt = get_prompt(args, section)
        # print(prompt)
        response = call_model(prompt)
        write_noteboo_body(args, response)


def generate_from_green_tea_press(args):
    write_notebook_header(args)

    sections = get_green_tea_press_html(args)

    for i, section in enumerate(sections):
        # prompt = get_prompt(args, section)
        # print(prompt)
        # response = call_model(prompt, i, len(sections))
        # write_noteboo_body(args, response)

        prompt = get_workshop_prompt(args, section)
        print(prompt)
        response = call_model(prompt)
        write_workshop_to_file(args, response, i)


def generate_from_raw_code(args):
    write_notebook_header(args)

    code = get_raw_py_file(args)
    separate_code_prompt = get_prompt_divide_raw_code(args, code)
    separated_code = call_model(separate_code_prompt)
    # print(separated_code)
    sections = separated_code.split(">>>section")

    for i, section in enumerate(sections):
        prompt = get_prompt_for_raw_code(args, section)
        print(prompt)
        response = call_model(prompt)
        write_noteboo_body(args, response)

def write_notebook_header(args):
    file_header = f'# j2 from \'macros.j2\' import header\n# {{{{ header("{args.topic}", "{args.topic}") }}}}\n\n'
    with open(f"output/{args.name}.py", "a") as file:
        file.write(file_header)


def write_noteboo_body(args, response):
    with open(f"output/{args.name}.py", "a") as f:
        f.writelines(response)
        f.write("\n")


def write_workshop_to_file(args, response, section):
    with open(f"output/ws_10{section}_{str(args.topic).lower()}.py", "w") as f:
        f.writelines(response)
        f.write("\n")


def write_translated_py(args, sections):
    with open(f"{args.name}_translated.py", "w") as f:
        for section in sections:
            f.write(section)

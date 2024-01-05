from openai import OpenAI
from dotenv import load_dotenv
import importlib.resources as pkg_resources


def generate_py(args, template):
    load_dotenv()

    client = OpenAI()

    with pkg_resources.open_text("notebook_builder", "cell_templates.py") as file:
        cells = file.read()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f"""Please act as a {args.general_topic} expert and teacher! I want to create course material on {args.topic}.
                                            The ouput should be specified in a Python notebook for which I provide you a template with the cell types you can use as a reference.
                                            The template file shows the general format of this course material. Each line starting with $ is an instruction for you for a specific section. Follow these instructions to create the notebook. 
                                            Take a deep breath and go through each instruction in the template step by step!
                                            Template file: \n"""
                + template
                + """ Cell templates: \n"""
                + cells
                + """\n\n
                                            Output notebook:"
                                            """,
            },
        ],
    )

    with open(f"output/{args.name}.py", "w") as f:
        f.write(response.choices[0].message.content + "\n\n")

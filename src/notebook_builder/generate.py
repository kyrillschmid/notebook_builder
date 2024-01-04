from openai import OpenAI
from dotenv import load_dotenv
import importlib.resources as pkg_resources


def generate_py(templates):
    load_dotenv()

    client = OpenAI()
    template = templates.template

    with pkg_resources.open_text("notebook_builder", f"{template}") as file:
        notebook = file.read()

    with pkg_resources.open_text("notebook_builder", "cell_templates.py") as file:
        cells = file.read()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f"""Please act as a {templates.general_topic} expert and teacher! I want to create course material on {templates.topic}.
                                            The ouput should be specified in a Python notebook for which I provide you a template notebook as reference.
                                            The template notebook shows how this course should be built up. Also it contains instructions for each specific section.
                                            The notebook also contains meta commands, introduced with $ at the beginning of a line. Follow these instructions to create the notebook.
                                            I also provide you a description of the cells that you can use.
                                            The ouput format should be equal to the given input noteook. Remember to keep each cell small and concise. Make multiple to split up the content if helpful. Dont 
                                            Take a deep breath and go through it step by step!
                                            Template notebook: \n"""
                + notebook
                + """ Cell templates: \n"""
                + cells
                + """\n\n
                                            Output notebook:"
                                            """,
            },
        ],
    )

    with open(f"output/{templates.name}.py", "w") as f:
        f.write(response.choices[0].message.content + "\n\n")

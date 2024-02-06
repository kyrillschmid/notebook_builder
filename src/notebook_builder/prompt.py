def get_prompt(args, section):
    return (
        f"Please act as a {args.general_topic} expert focussed on creating high-quality {args.topic} training material!\n"
        f"Your task is to create a section of Jupyter notebook for the following topic: {args.topic}!\n"
        f"I will give you a section from a HTML file and your task is to transform the content into a sequence of jupyter notebook cells.\n"
        "The provided html consists of a heading (h1, h2, h3) and subsequent paragraphs with code snippets.\n"
        "To create the cells of the notebook use the following templates:\n"
        "-----Slide Cell Template-----\n"
        "For headings (h1, h2, h3) and following paragrpahs use the following slide cell template:\n"
        '# %% [markdown] lang="en" tags=["slide"]\n# ## $Heading$\n# - bulletpoint 1 \n# - bullet point 2 \n# - bullet point N \n'
        "Note that a slide should contain not more than 4 bulletpoints and each new line needs a # symbol. You can create multiple slide cells if the section contains multiple paragraphs. Also you should summarize and rephrase the contents of the paragraphes profundly to make neat bulletpoints.\n"
        "Here is an example of a slide cell:\n"
        '# %% [markdown] lang="en" tags=["slide"]\n'
        "# ## Data Indexing and Selection\n"
        "# - NumPy provides methods and tools to perform indexing, slicing, masking & fancy indexing\n"
        "#   - Examples are `arr[2, 1]`, `arr[:, 1:5]`, `arr[arr > 0]`, `arr[0, [1, 5]]`, `arr[:, [1, 5]]`\n"
        "# - In this section, we delve into ways to apply these operations on Pandas `Series` and `DataFrame` objects\n"
        "# - We will begin with simple one-dimensional `Series` object, then proceed to two-dimensional `DataFrame` objects\n"
        "-----Code Cell Template-----\n"
        "For html elements <code> use the following code cell template:\n"
        "# %%\ncode line 1\ncode line 2\ncode line three\n"
        "Here is an example of a code cell:\n"
        "# %%\n"
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "df = pd.DataFrame(np.random.randn(6, 4))\n"
        "----------\n"
        "Note that code examples should be dividded into multiple code cells to group code logically.\n"
        "Here is the html section to be processed:\n"
        f"{section}"
    )


def get_workshop_prompt(args, relevant_notebook):
    with open(f"src/notebook_builder/workshop_template_mini.py", "r") as file:
        workshop = file.read()

    return (
        f"Please act as a {args.general_topic} expert and lecturer!"
        f" Your task is to create an exercise (called Mini-Workshop) as Jupyter notebook cells for the following topic: {args.topic}!"
        f" I will give you:\n"
        "a) An example workshop as a reference with a different topic to show you roughly the length and structure of the workshop.\n"
        "b) The relevant content on which the new workshop should be based.\n"
        f" Make sure to use the same template cells as in the reference workshop.\n"
        f"Here is the  content for the workshop:\n"
        f"{relevant_notebook}"
        f" Here is the reference workshop :\n"
        f"{workshop}"
    )


def get_prompt_for_raw_code(args, section):
    return (
        f"Please act as a {args.general_topic} expert focussed on creating high-quality {args.topic} training material!\n"
        f"Your task is to create a Jupyter notebook for the following topic: {args.topic}!\n"
        f"I will give you a piece of a code file and your task is to annotate the content and transform it into a sequence of jupyter notebook cells.\n"
        "The resulting notebook should explain the provided code step by step and provide detailled explainations as slide cells and code as code cells.\n"
        "To create the cells of the notebook use the following templates:\n"
        "-----Slide Cell Template-----\n"
        "To explain a section use the following slide cell template:\n"
        '# %% [markdown] lang="en" tags=["slide"]\n# ## $Section Heading$\n# - bulletpoint 1 \n# - bullet point 2 \n# - bullet point N \n'
        "Note that a slide should contain 3-4 bulletpoints and each new line needs a # symbol.\n"
        "Here is an example of a slide cell:\n"
        '# %% [markdown] lang="en" tags=["slide"]\n'
        "# ## Q-Learning\n"
        "# - Q-Learning is a model-free reinforcement learning algorithm to learn quality of actions\n"
        "#   - It is used in combination with a policy which is used to select actions\n"
        "# - In this section, we delve into Deep Q-Learning\n"
        "# - We will use PyTorch to implement a Deep Q-Learning agent\n"
        "-----Code Cell Template-----\n"
        "To include code in the notebook use the following cell template:\n"
        "# %%\ncode line 1\ncode line 2\ncode line three\n"
        "Here is an example of a code cell:\n"
        "# %%\n"
        "import numpy as np\n"
        "import torch \n"
        "learning_rage = 0.0004\n"
        "----------\n"
        "Make sure to interleave slide cells as explanations with code examples to illustrate usage. Code should be divided into multiple cells to group code logically.\n"
        "Here is the raw code file to be processed:\n"
        f"{section}"
    )


def get_prompt_divide_raw_code(args, text):
    return (
        f"Please act as a {args.general_topic} expert focussed on creating high-quality {args.topic} training material!\n"
        f"Your task is split the following raw code into logical sections! for example classes or functions!\n"
        "At each logical break, insert the following sequence : >>>section\n"
        "Make sure to only return the code including the section markers and nothing else.\n"
        "Here is the raw code file to be processed:\n"
        f"{text}"
    )


def get_prompt_translate_en_to_de(args, text):
    return (
        f"Please act as a professional translator!\n"
        f"Your task is to translate exisiting Python training material from a Jupyter notebook from English to German\n"
        "Make sure to use keep the structure of the original material and translate only the content.\n"
        f"Rephrase the content if necessary to make it sound natural in German. Keep with technical terms in English.\n"
        "Make sure to keep the # symbols at the beginning of a newline if in the oringial text like in the example below!\n"
        f"Here is an translation example:\n Input:\n"
        "# ## 1.1 What is a program?\n"
        "# - A program is a sequence of instructions for computing.\n"
        "# - Computations can be mathematical (like solving systems of equations) or symbolic (such as text searching).\n"
        "# - Whether graphical processing or video playing, it all boils down into basic instructions which are common across languages.\n"
        "Output:\n"
        "# ## 1.1 Was ist ein Programm?\n"
        "# - Ein Programm ist eine Abfolge von Anweisungen zur Datenverarbeitung.\n"
        "# - Berechnungen können mathematisch sein (wie das Lösen von Gleichungssystemen) oder symbolisch (wie die Textsuche).\n"
        "# - Ob grafische Verarbeitung oder Videowiedergabe, letztendlich basiert alles auf grundlegenden Anweisungen, die sprachübergreifend gleich sind.\n"
        "Here is the content to be translated:\n"
        f"{text}"
    )


# %%

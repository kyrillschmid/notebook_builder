# Package Notebook builder

A python package that lets you build course material as notebooks

## Installation

Create virtual env:

```shell script
python -m venv notebookbuilder
```

Install dependencies:

```shell script
pip install -r requirements.txt
```

To build the project use

```shell script
python -m build
```

```shell script
pip install dist/simple_packaging-0.0.1-py3-none-any.whl
```

To install the package so that it can be used for development purposes
install it with

```shell script
pip install -e .
```

in the root directory.

## Usage

To create a notebook from file use:

```shell script
python notebookbuilder --general_topic "Reinforcement Learning" --topic "Markov Decision Processes" --author "Anonymous" --template "template_mdp.md" --name "markov_decision_processes"
```

Adjust the markdown template to your needs. The template should contain the following tags:

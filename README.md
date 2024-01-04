# Package Notebook builder

A python package that lets you build course material as notebooks

## Installation

Create and activate virtual env:

```shell script
python -m venv notebookbuilder
source notebookbuilder/bin/activate
```

Install dependencies:

```shell script
pip install -r requirements.txt
```

To build the project use

```shell script
python -m build
```

Install the package with

```shell script
pip install dist/notebook_builder-0.1.0-py3-none-any.whl
```

To install the package so that it can be used for development purposes
install it with

```shell script
pip install -e .
```

in the root directory.

Create a .env file in the root directory and add the following variables:

```shell script
API_KEY=...
```

## Usage

To create a notebook from file use:

```shell script
notebook-builder --general_topic "Reinforcement Learning" --topic "Markov Decision Processes" --author "Anonymous" --template "template_mdp.txt" --name "markov_decision_processes"
```

Adjust the txt template to your needs. The template should contain the following tags:

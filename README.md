# León Speedcams
![Version](https://img.shields.io/badge/Version-2.0.0-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.11-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

León Speedcams is a Python script that scrapes the location and speed limit of the speed cameras in the city of León, Spain, and optionally sends that information to a Telegram bot chat.

## Table of Contents
* [Features](#features)
* [Configuration](#configuration)
* [Installation with Poetry (recommended)](#installation-with-poetry-recommended)
* [Installation with pip](#installation-with-pip)
* [Development Setup](#development-setup)
* [Contributing](#contributing)
* [License](#license)

## Features
* Fetches the latest data about the speedcams in the city of León, Spain.
* Sends that information to a Telegram bot chat.

## Configuration
Before running the script, make sure to configure the necessary settings in the `config.yaml` file. You can use the provided `config.example.yaml` file as a template.

## Installation with Poetry (recommended)
To set up the project, follow these steps:
1. Make sure you have [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) installed in your system.
2. It is highly recommended to set this Poetry configuration parameter to avoid multiple issues:
    ```bash
    poetry config virtualenvs.in-project true
    poetry config virtualenvs.prefer-active-python true
    ```
3. Clone the repository:
    ```bash
    git clone https://github.com/dmarts05/leon-speedcams.git
    ```
4. Navigate to the project directory:
    ```bash
    cd leon-speedcams
    ```
5. Install the project dependencies using Poetry:
    ```bash
    poetry install
    ```
    You might need [pyenv](https://github.com/pyenv/pyenv) to install the Python version specified in the `pyproject.toml` file. If that's the case, run `pyenv install 3.11` before running the previous command. Also, check out the [Poetry documentation about pyenv](https://python-poetry.org/docs/managing-environments/) for more information.
6. Configure the script by updating the `config.yaml` file with your specific information (as mentioned in the previous section).
7. Run the script:
    ```bash
    poetry run leon-speedcams
    ```
    This will execute the script and start scraping and redeeming Amazon Gift Card codes from Microsoft Rewards emails.

## Installation with pip
This is an alternative installation method that uses pip instead of Poetry. It might not work as expected, so it is recommended to use the Poetry installation method instead. To set up the project, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/dmarts05/leon-speedcams.git
    ```
2. Navigate to the project directory:
    ```bash
    cd leon-speedcams
    ```
3. Install the project dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
    You might need [pyenv](https://github.com/pyenv/pyenv) to install the Python version specified in the `requirements.txt` file.
4. Configure the script by updating the `config.yaml` file with your specific information (as mentioned in the previous section).
5. Run the script:
    ```bash
    python -m leon_speedcams
    ```

## Development Setup
If you want to contribute to the project or run the development environment, follow these additional steps:
1. Install the project dependencies:
    ```bash
    poetry install
    ```
2. Install pre-commit hooks:
    ```bash
    poetry run pre-commit install
    ```
    This will install pre-commit hooks that will run every time you commit changes to the repository.
3. Format the code:
    ```bash
    poetry run ruff leon_speedcams
    ```
4. Run static type checking:
    ```bash
    poetry run mypy leon_speedcams
    ```
5. Run the tests:
    ```bash
    poetry run pytest tests
    ```
That's it! You now have the project set up and ready for development or execution.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). See the [LICENSE](LICENSE) file for details.
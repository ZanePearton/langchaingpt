# Langchaingpt

Langchaingpt is a Python library that provides functionalities of natural language processing, text embedding, document indexing, and information retrieval. It allows users to easily leverage powerful models like GPT-3 for various tasks. This project demonstrates how to implement a conversational retrieval model using the Langchaingpt library and OpenAI's GPT-3 model.

## Features

The key features of Langchaingpt include:

- **Loading Data**: Langchaingpt can load data from different sources, such as directories or individual text files.
  
- **Indexing Text Documents**: The library provides functionality to index text documents for efficient searching.
  
- **Persistent Storage**: Langchaingpt supports persistent storage of indexed data, which can improve performance for repeated queries.
  
- **GPT-3 Integration**: The library can leverage the GPT-3 model for natural language understanding.
  
- **Conversational Interface**: Langchaingpt provides a console-based chat interface for interaction.

## Requirements

- Python 3.7+
- OpenAI Python SDK
- langchain Python library
- Constants Python library

## File Structure
```bash
Langchaingpt/
│
├── data/
│   └─ .txt       # Text data files to be loaded and processed
├── main.py       # Main application script
└── constants.py  # Contains necessary constants such as the OpenAI API Key
```

## Installation

Clone this repository and install the required packages:

```bash
git clone https://github.com/yourgithubusername/Langchaingpt.git
cd Langchaingpt
pip install langchain
pip install constants
```

## Usage

The main application file `Langchaingpt.py` reads text documents from a directory, indexes them, and then provides a console-based chat interface. During a chat, it uses OpenAI's GPT-3 model to understand and respond to user queries.

The application accepts an optional argument which can be a question you want to start your conversation with:

```bash
python main.py "query data"
```

Or you can run the program without arguments and provide your prompts during the conversation:

```bash
python main.py
```

Type 'quit', 'q', or 'exit' to exit the program.

If the `PERSIST` variable is set to `True`, the application will use persistent storage for the document index to improve the performance of repeated queries.

## Setting Up OpenAI API Key

The program requires an OpenAI API Key to work with GPT-3. You need to put your key into `constants.py`:

```python
APIKEY = "your-openai-api-key"
```

Replace 'your-openai-api-key' with your actual OpenAI API Key. Please make sure not to commit this key to your repository or share it with others.

## Contact

If you have any questions or issues, please open an issue on the repository.

## License

This project is licensed under the terms of the MIT license.

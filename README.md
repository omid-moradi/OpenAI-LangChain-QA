# LangChain Chroma Retrieval

This project demonstrates how to use LangChain, Chroma, and OpenAI embeddings to create a retrieval-based question-answering system. The system is designed to retrieve relevant documents from a database and filter out redundant information using a custom retriever.

## Features

- **OpenAI Embeddings**: Leverages OpenAI's embeddings for semantic similarity.
- **Chroma Integration**: Uses Chroma for storing and retrieving document embeddings.
- **Custom Retriever**: Implements a custom retriever to filter redundant results.
- **Text Splitting**: Splits large text documents into manageable chunks for efficient processing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/langchain-chroma-retrieval.git
    cd langchain-chroma-retrieval
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables by creating a `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

### Running the Question-Answering System

1. Make sure you have the necessary environment variables set up by loading the `.env` file:
    ```bash
    source .env
    ```

2. Run the script to perform a query:
    ```bash
    python file1.py
    ```

   This script uses the `RetrievalQA` chain to find an interesting fact about the English language.

### Loading and Splitting Documents

1. Prepare your text documents (e.g., `facts.txt`) and ensure they are in the correct format.
2. Run the text loader script to split the text and store embeddings:
    ```bash
    python file2.py
    ```

### Custom Redundant Filter Retriever

- The custom retriever is implemented in `file3.py` as `RedundantFilterRetriver`. It filters out redundant information by using a relevance search with embeddings.

## Project Structure

- `prompt.py`: Main script for setting up the QA system using LangChain and Chroma.
- `main.py`: Script for loading and splitting text documents into chunks, then storing them in Chroma.
- `redundant_filter_retriver.py`: Contains the `RedundantFilterRetriver` class for custom document retrieval.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Chroma](https://chroma-langchain.com)
- [OpenAI](https://openai.com)


# AI Intern Assignment

## Overview

This repository contains the solution for the AI Intern Assignment. The task involves building a Python-based API using **FastAPI** that loads invoice data into a **Chromadb** collection, processes user queries, and utilizes an **AI model** (ChatGroq with Llama) to provide insights based on the data.

## Features

- **Data Ingestion**: Loads invoice data from a JSON file into a Chromadb collection.
- **Query API**: Allows users to send queries related to the invoice data and receive answers powered by a pre-trained Llama AI model.
- **AI Model Integration**: Uses ChatGroq with Llama 3-8b-8192 for analyzing the context and generating human-readable responses.
- **Error Handling & Validation**: Ensures proper exception handling and input validation to handle edge cases and incorrect questions.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- FastAPI
- Uvicorn (for running the API server)
- Other Python dependencies (listed in `requirements.txt`)

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/ai-intern-assignment.git
    cd ai-intern-assignment
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables. Make sure to add your `GROQ_API_KEY` in the `.env` file located in the project root.

    Example `.env` file:

    ```
    GROQ_API_KEY=your_api_key_here
    ```

### Running the API

To run the FastAPI server, use Uvicorn:

```bash
uvicorn main:app --reload

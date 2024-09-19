# Secure API Key Handling in Python Projects
A guide to properly managing API keys and environment variables in Python projects

## 📜 Introduction

When working with APIs in Python, you often need to use API keys or other sensitive credentials. It's crucial to **manage these keys securely** to avoid leaking sensitive information or accidentally committing them to your Git repository.

This repository demonstrates best practices for managing API keys and environment variables using `.env` files and the `python-dotenv` package.

## 🚀 Getting Started

Follow these steps to set up your project for secure API key handling:



### 1. Install Dependencies

You'll need the `python-dotenv` package to load environment variables from a `.env` file.

```bash
pip install python-dotenv
````



### 2. Set Up a `.env` File

Create a `.env` file in your project root, where you'll store your API key and other environment-specific variables:

```bash
# .env
API_KEY=your_api_key_here
```
**Important:** This .env file should never be committed to your repository. We’ll configure .gitignore to ensure that.



### 3. Add `.env` to `.gitignore`

Add the following line to your `.gitignore` file to ensure that `.env` doesn't get pushed to Git:

```plaintext
# .gitignore
.env
```


### 5. Provide a `.env.example` File

For other developers working on your project, include a `.env.example` file as a template:

```plaintext
# .env.example
API_KEY=your_api_key_here
```

This file will not contain sensitive data, but it gives an example of the variables required to run the project. Other developers can copy this file to .env and add their own credentials.

```bash
cp .env.example .env
```



## 🛑 Common Mistakes to Avoid

- **Hardcoding API Keys**: Never hardcode sensitive information directly in your Python code.
  
```python
# BAD EXAMPLE: Never do this
api_key = "hardcoded_api_key"
```

- **Committing .env files** : Ensure that .env is always included in .gitignore to avoid accidentally pushing it to version control.

- **Pushing Virtual Environments**: Always exclude virtual environments (like venv) from Git:

```plaintext
# .gitignore
venv/
``````

## 📚 Resources:

- [8 Tips for Securely Using API Keys](https://blog.streamlit.io/8-tips-for-securely-using-api-keys/)


## 🧑‍💻 Contributing
Contributions are welcome!
Feel free to open an issue or submit a pull request if you have suggestions for improvements or want to share additional best practices.


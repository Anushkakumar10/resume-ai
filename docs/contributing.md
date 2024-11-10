# Contributing to ResumeAI

We welcome contributions to ResumeAI! This document provides guidelines to ensure smooth collaboration and code quality.

## Code of Conduct

Please adhere to our [Code of Conduct](./code_of_conduct.md) to foster a welcoming and inclusive environment.

## Getting Started

1. **Fork the Repository**: Fork the repository to your GitHub account.
2. **Clone the Fork**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/ResumeAI.git
   cd ResumeAI
   ```
3. **Set Up Virtual Environment**: Set up a virtual environment and install dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**: Add any necessary environment variables in `app/config.py`.

## Making Changes

1. **Create a Feature Branch**  
   Create a new branch with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write Clear, Concise Code**  
   - Follow consistent naming conventions and file structure.
   - Ensure each function and module does a specific task.
   - Add comments and documentation as needed.

3. **Test Your Changes**  
   Run the application and test your changes thoroughly. Document any new dependencies or steps required for your code to run.

4. **Commit and Push**  
   Commit your changes with descriptive messages:
   ```bash
   git commit -m "Add feature X to improve Y"
   git push origin feature/your-feature-name
   ```

5. **Submit a Pull Request**  
   Go to the original repository on GitHub and submit a pull request from your feature branch. Provide a detailed description of your changes, including any new functionality or fixes.

## Code Style

- **PEP 8 Compliance**: Follow PEP 8 guidelines for Python code.
- **Docstrings**: Use docstrings for function descriptions, especially in complex functions.
- **Logging**: Use logging where applicable, especially in error handling.

## Reporting Issues

If you encounter bugs or have feature requests, please [open an issue](https://github.com/yourusername/ResumeAI/issues). Include a clear title and detailed description.

## License

By contributing, you agree that your contributions will be licensed under the same MIT License as this repository.

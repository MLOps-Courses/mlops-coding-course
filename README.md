# MLOps Coding Course

**Welcome to the [MLOps Coding Course](https://mlops-coding-course.fmind.dev/)!**

This course is designed to dive deep into the intersection of software development and data science, focusing on the practical applications of machine learning (ML) and artificial intelligence (AI) projects using Python.

Whether you are a beginner eager to explore or an experienced professional seeking to enhance your skill set, this course offers valuable insights and hands-on experience.

**Related Resources:**

- **[MLOps Python Package (Example)](https://github.com/fmind/mlops-python-package)**: Kickstart your MLOps initiative with a flexible, robust, and productive Python package.
- **[LLMOps Coding Package (Example)](https://github.com/callmesora/llmops-python-package/)**: Example with best practices and tools to support your LLMOps projects.
- **[Cookiecutter MLOps Package (Template)](https://github.com/fmind/cookiecutter-mlops-package)**: Start building and deploying Python packages and Docker images for MLOps tasks.
- **NEW: [Agent Skills](https://agentskills.io/home)**: Enhance your learning with the [MLOps Coding Skills](https://github.com/MLOps-Courses/mlops-coding-skills) repository. These "skills" are specialized instruction sets that you can add to your AI coding assistant to help it understand and execute the MLOps tasks in this course more effectively.

## Key Features

- **Hands-on Python Coding**: Learn to code with Python in a way that's directly applicable to real-world AI projects.
- **Project-Driven Learning**: Each chapter includes practical project instructions to help you apply what you've learned.
- **MLOps Techniques**: Gain insights into effective MLOps coding strategies that streamline the development and deployment of AI/ML models.
- **Open Source Tools**: Familiarize yourself with industry-standard tools like [uv](https://docs.astral.sh/uv/), [Ruff](https://docs.astral.sh/ruff/), [ty](https://github.com/astral-sh/ty), [pytest](https://docs.pytest.org/en/latest/), [MLflow](https://mlflow.org/), [mise](https://mise.jdx.dev/), [lefthook](https://lefthook.dev/), [GitHub](https://github.com/), and [VS Code](https://code.visualstudio.com/).
- **Mentoring sessions**: Boost your learning experience with personalized feedback and expert insights from the course authors.
  - Book [a one-on-one mentoring session](https://calendar.app.google/9KfEBkpCHQKwarLF8) to receive tailored guidance and support on the course.
  - Contact the [course creators](mailto:mlops-coding-course@fmind.dev) to request a personalized quote for group and organization training.
- **MLOps Coding Assistant**: Get help from the [MLOps Coding Assistant](https://mlops-coding-assistant.fmind.dev/), a premium tool that provides code snippets, explanations, and examples to help you learn and apply MLOps techniques.
  - Contact the [course creators](mailto:mlops-coding-course@fmind.dev) to access the assistant for $10 per month.

## Course Content

1. **Initializing**: Set up your development environment, manage Python versions, and handle external dependencies.
1. **Prototyping**: Use Jupyter notebooks for ML prototyping, explore dataset manipulation, and perform initial model assessments.
1. **Productionizing**: Transition from notebooks to clean Python packages, learn about modular coding, and understand different programming paradigms.
1. **Validating**: Focus on code quality with typing, linting, testing, and debugging to ensure your ML projects are robust and maintainable.
1. **Refining**: Dive into advanced MLOps techniques including CI/CD workflows, software containers, and model registries to streamline your operations.
1. **Sharing**: Learn how to effectively organize and document your MLOps projects to ensure they are accessible and collaborative.
1. **Observability**: Gain comprehensive insights into the behavior and performance of your deployed models and infrastructure.

## Installation

To start contributing, you will need to set up your development environment:

1. Clone the repository.
1. In the cloned repository directory, install dependencies and git hooks with [mise](https://mise.jdx.dev/) (which drives [uv](https://docs.astral.sh/uv/)):

   ```bash
   mise run install
   ```

1. Serve the documentation locally (from that directory) to see course material in your browser:

   ```bash
   mise run serve
   ```

You can then access the course at this URL from your computer: <http://localhost:8000/>

## Development

Every task goes through [mise](https://mise.jdx.dev/); run `mise tasks` for the full list.

| Command            | Purpose                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| `mise run install` | Sync Python dependencies (`uv`) and install the git hooks (`lefthook`).                                   |
| `mise run format`  | Format JSON, Markdown, TOML, and YAML with `dprint`.                                                      |
| `mise run check`   | Run every static check: workflows, strict site build, formatting, secrets, scanning, and vulnerabilities. |
| `mise run build`   | Build the static site into `site/`.                                                                       |
| `mise run serve`   | Serve the documentation locally with live reload.                                                         |
| `mise run all`     | The canonical gate — format, check, build — exactly what CI runs.                                         |

## Contributions

This course is [open source under the CC-BY 4.0 license](https://github.com/MLOps-Courses/mlops-coding-course/blob/main/LICENSE.txt), and we welcome contributions! Whether it's improving the documentation, adding new examples, or fixing bugs, your input is valuable. Check out the `docs` among other project files to see where you can contribute.

Feel free to [submit pull requests](https://github.com/MLOps-Courses/mlops-coding-course/pulls) or [open issues](https://github.com/MLOps-Courses/mlops-coding-course/issues) to discuss potential changes or additions to the course content.

**Join us in advancing the field of MLOps by sharing your expertise and learning from others!**

## Donations

If you find this course helpful and would like to support its creators, you can make a donation via [Stripe](https://donate.stripe.com/4gw8xT9oVbCc98s7ss).

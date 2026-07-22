# Quickstart

This guide is intended for developers who want to build and run CaveGenLabs from source.

If you're looking to use a prebuilt release instead, download the latest version from the [Homepage](index.md).

---

## Prerequisites

Before getting started, ensure the following is installed:

- Python 3.14 or newer
- Git

---

## Clone the Repository

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/hsal-o/cavegen-labs.git
cd cavegen-labs
```

---

## Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

=== "Windows"

    ```bat
    .venv\Scripts\activate
    ```

=== "Linux / macOS"

    ```bash
    source .venv/bin/activate
    ```

---

## Install Development Dependencies

Install the project and its development dependencies:

```bash
pip install -e ".[dev]"
```

---

## Launch the Application

Start CaveGenLabs by running:

```bash
python -m cavegenlabs
```

If everything is configured correctly, the application will launch and display the main window.

---

## Next Steps

Now that CaveGenLabs is running, you may want to explore the following sections:

- **[Documentation](documentation.md)** -- Learn about the project's architecture and how to add new algorithms
- **[Algorithms](algorithms.md)** -- Explore the implemented cave generation algorithms
- **[Contributing](contributing.md)** -- Learn how to contribute to the project


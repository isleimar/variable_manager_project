from setuptools import setup, find_packages

setup(
    name="variable-manager",
    version="1.0.0",
    author="Isleimar Oliveira",
    author_email="isleimar@gmail.com",
    description="A powerful Variable Manager for managing and importing variables from various sources.",
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/isleimar/variable_manager_project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "variable-manager=variable_manager.core:main",
        ],
    },
)

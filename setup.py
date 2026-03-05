setup
"""Setup configuration for python-accounting-xls."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-accounting-xls",
    version="1.0.0",
    author="Financial Consolidation Team",
    author_email="support@example.com",
    description="Excel-based financial consolidation tool using python-accounting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feifeijiang48/python-accounting-xls",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires=">=3.9",
    install_requires=[
        "python-accounting>=0.7.0",
        "pandas>=1.3.0",
        "openpyxl>=3.6.0",
        "SQLAlchemy>=1.4.0",
        "pydantic>=1.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.0",
            "flake8>=3.9.0",
        ],
    },
)
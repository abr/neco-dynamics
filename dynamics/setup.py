from setuptools import setup

setup(
    name="neco-dynamics",
    version="0.1",
    description="Software for NeCo paper",
    author="Applied Brain Research",
    author_email="info@appliedbrainresearch.com",

    install_requires=[
        "jupyter",
        "notebook",
        "seaborn",
        "nengo",
        "nengo-extras",
        "scikit-learn",
    ],
    zip_safe=False,
)

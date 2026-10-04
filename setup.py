from setuptools import setup, find_packages

setup(
    name="aadigod",
    version="27.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["python-telegram-bot>=20.0,<22.0"],
    entry_points={
        "console_scripts": [
            "aadigod = aadigod.cli:main",
            "aadi-god = aadigod.cli:main",
        ]
    },
    python_requires=">=3.9",
)

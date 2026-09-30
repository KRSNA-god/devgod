from setuptools import setup, find_packages

setup(
    name="devgod",
    version="27.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["python-telegram-bot>=20.0,<22.0"],
    entry_points={
        "console_scripts": [
            "devgod = devgod.cli:main",
            "dev-god = devgod.cli:main",
        ]
    },
    python_requires=">=3.9",
)

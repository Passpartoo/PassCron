import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PassCron",
    version="0.0.1",
    author="Passpartoo",
    author_email="",
    description="A package to automate the script launcher visualy (UX friendly)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Passpartoo/PassCron",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "xlrd==1.2.0",
        "XlsxWriter==1.2.6",
        "click==6.7",
        "python-dotenv==0.10.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

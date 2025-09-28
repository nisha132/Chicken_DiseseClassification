import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken_DiseseClassification"
AUTHOR_USER_NAME = "nisha132"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "nishpanchal132@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN Image Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)    
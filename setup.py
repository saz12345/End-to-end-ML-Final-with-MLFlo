import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-DVC-MLFlow"
AUTHOR_USER_NAME= "saz12345"
SRC_REPO= "mlProject"
AUTHOR_EMAIL="sasram1995@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version = _version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)

"""ojd_daps_skills."""
from pathlib import Path
from setuptools import find_packages
from setuptools import setup

import os
import subprocess
import platform	

tag_cmd = "git describe --tags --abbrev=0"	
tag_cmd = tag_cmd if platform.system() == "Windows" else f"echo $({tag_cmd})"

try:
    tag_version = (
        subprocess.check_output(tag_cmd, shell=False).decode("ascii").replace("\n", "")
    )
except:
    #an error occurred, potentially an issue with git cli
    tag_version = "v1.0.0"
    
print(f"Tag version: {tag_version}")

def read_lines(path):
    """Read lines of `path`."""
    with open(path) as f:
        return f.read().splitlines()


BASE_DIR = Path(__file__).parent


setup(
    name="ojd_daps_skills",
    long_description=open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=read_lines(os.path.join(BASE_DIR, "requirements.txt")),
    extras_require={"dev": read_lines(os.path.join(BASE_DIR, "requirements_dev.txt"))},
    packages=find_packages(
        exclude=["docs", "ojd_daps_skills/analysis", "ojd_daps_skills/app"]
    ),
    classifiers=['Development Status :: 5 - Production/Stable'],
    package_data={
        # If any package contains *.yaml files, include them:
        "": [
            "*.yaml",
        ],
    },
    version=tag_version,
    description="Extract skills from job ads and maps them onto a skills taxonomy of your choice.",
    url="https://github.com/nestauk/ojd_daps_skills",
    project_urls={
        "Documentation": "https://nestauk.github.io/ojd_daps_skills/build/html/about.html",
        "Source": "https://github.com/nestauk/ojd_daps_skills",
    },
    author="Nesta",
    author_email="dataanalytics@nesta.org.uk",
    maintainer="Nesta",
    maintainer_email="dataanalytics@nesta.org.uk",
    license="MIT",
)

from setuptools import setup, find_packages

setup(
    name="django-ui-forms",
    version="1.0",
    description="A Django reusable app to extend forms with Bootstrap and Tailwind CSS support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="mohitdevelopment2001@gmail.com",
    url="https://github.com/mohitprajapat2001/django-ui-forms",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=5.1",
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

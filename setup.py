import setuptools

setuptools.setup(
    name="fairmarket-rl",
    version="1.0.0",
    author="FairMarket-RL Authors",
    author_email="",
    description="Public interface and demo for FairMarket-RL research project",
    license="MIT",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "PyYAML>=5.4"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research"
    ],
    project_urls={
        "Source": "https://github.com/{{YOUR_GITHUB_HANDLE_OR_ORG}}/fairmarket-rl-public",
    }
)

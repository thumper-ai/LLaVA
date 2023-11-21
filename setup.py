from setuptools import setup, find_packages

setup(
    name="llava",
    version="1.1.3",
    description="Towards GPT-4 like large language and visual assistant.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://llava-vl.github.io",
    author="Your Name",  # Add your name
    author_email="your.email@example.com",  # Add your email
    license="Apache Software License",  # Update if your license differs
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=find_packages(exclude=["assets*", "benchmark*", "docs", "dist*", "playground*", "scripts*", "tests*"]),
    install_requires=[
        "torch>=2.0.1", "torchvision>=0.15.2",
        "transformers>=4.31.0", "tokenizers>=0.12.1,<0.14", "sentencepiece>=0.1.99", "shortuuid",
        "accelerate>=0.21.0", "peft>=0.4.0", "bitsandbytes>=0.41.0",
        "pydantic<2,>=1", "markdown2[all]", "numpy", "scikit-learn==1.2.2",
        # "gradio==3.35.2", "gradio_client==0.2.9",
        "requests", "httpx==0.24.0", "uvicorn", "fastapi",
        "einops>=0.6.1", "einops-exts==0.0.4", "timm==0.6.13", "more_itertools",
    ],
    extras_require={
        "train": ["deepspeed==0.9.5", "ninja", "wandb"],
    },
    project_urls={
        "Bug Tracker": "https://github.com/haotian-liu/LLaVA/issues",
    },
)
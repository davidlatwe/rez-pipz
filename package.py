name = "pipz"
version = "1.2.1"
requires = [
    "rez-2.29+",
    "python>=2,<4"
]

tools = [
    "install",
    "search",
]

# Upon a new release of pip, wheel or setuptools, this is what you edit
build_command = " ".join([
    "python {root}/install.py ",
    "--pip=20.2b1",
    "--wheel=0.33.4",
    "--setuptools=41.0.1",
    "--packaging=19.0",
])


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")

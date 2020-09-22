
early = globals()["early"]


name = "pipz"

version = "1.2.2.dev.1"

requires = [
    "python-2.7+,<4",
    "rez-2.29+",
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


@early()
def authors():
    import subprocess
    name_list = subprocess.check_output(
        ["git", "shortlog", "-sn"]
    ).decode()
    return [
        n.strip().split("\t", 1)[-1]
        for n in name_list.strip().split("\n")
    ]


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")

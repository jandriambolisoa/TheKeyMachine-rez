name = "TheKeyMachine"

version = "0.1.41-r.1"

authors = [
    "Rodrigo Torres",
    "Jeremy Andriambolisoa"
]

description = \
    """
    TheKeyMachine (TKM) is an open source set of tools designed for Maya animators.
    These tools are crafted to accelerate and facilitate many of the tasks animators undertake on a daily basis.
    """

requires = [
    "python-3+",
    "maya-2022+",
]

uuid = "TheKeyMachine.TheKeyMachine"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
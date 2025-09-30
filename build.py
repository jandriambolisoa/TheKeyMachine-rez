import os
import os.path
import json
import shutil
import sys

CONFIG_FILENAME = "config.json"

def build(source_path, build_path, install_path, targets):

    def write_config_file():
        datas = {
            "STUDIO_INSTALL": True,
            "INSTALL_PATH": os.path.join(build_path, "python"),
            "USER_FOLDER_PATH": "",
            "LICENSE_FOLDER": "",
            "LICENSE_FILE_NAME": "",
            "UPDATER": False,
            "BUG_REPORT": True,
            "CUSTOM_TOOLS_MENU": True,
            "CUSTOM_SCRIPTS_MENU": True,
            "CUSTOM_TOOLS_EDITABLE_BY_USER": True,
            "CUSTOM_SCRIPTS_EDITABLE_BY_USER": True
        }

        directory = os.path.join(
            build_path,
            "python",
            "TheKeyMachine",
            "data",
            "config"
        )

        with open(os.path.join(directory, CONFIG_FILENAME), "w") as file:
            file.write(json.dumps(datas, indent=4))

    def _build():
        # python source
        src_py = os.path.join(source_path, "python")
        dest_py = os.path.join(build_path, "python")

        if not os.path.exists(dest_py):
            shutil.copytree(src_py, dest_py)

        write_config_file()

    def _install():
        src = os.path.join(build_path, "python")
        dest = os.path.join(install_path, "python")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )

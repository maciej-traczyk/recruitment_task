import os
import subprocess
import sys
from pathlib import Path

from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = str(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def build_extension(self, ext: CMakeExtension) -> None:
        ext_fullpath = Path(self.get_ext_fullpath(ext.name))
        extdir = ext_fullpath.parent.resolve()

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DPYTHON_VERSION_STRING={sys.version_info.major}.{sys.version_info.minor}",
            "-DCMAKE_BUILD_TYPE=Release",
        ]

        if "CMAKE_ARGS" in os.environ:
            cmake_args += os.environ["CMAKE_ARGS"].split()

        pybind11_dir = os.path.join(
            os.environ.get("PREFIX", sys.prefix),
            "share", "cmake", "pybind11",
        )
        if Path(pybind11_dir).exists():
            cmake_args.append(f"-Dpybind11_DIR={pybind11_dir}")

        build_args = ["--build", ".", "--config", "Release"]

        if sys.platform == "win32":
            cmake_args += ["-GNinja"]
        else:
            build_args += [f"-j{os.cpu_count() or 2}"]

        build_temp = Path(self.build_temp) / ext.name
        build_temp.mkdir(parents=True, exist_ok=True)

        subprocess.check_call(
            ["cmake", ext.sourcedir, *cmake_args], cwd=build_temp
        )
        subprocess.check_call(
            ["cmake", *build_args], cwd=build_temp
        )


setup(
    name="recruitment_task",
    version="1.0.0",
    packages=find_packages(),
    ext_modules=[CMakeExtension("dicelib")],
    cmdclass={"build_ext": CMakeBuild},
    package_data={
        "game": [
            "assets/fonts/*.ttf",
            "assets/img/*.png",
        ]
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "task = game.main:main",
        ]
    },
    python_requires=">=3.11,<3.12",
)
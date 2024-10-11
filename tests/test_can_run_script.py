import subprocess


def test_can_run_script():
    assert subprocess.run(["floridayvine", "about"]).returncode == 0


def test_can_print_version():
    assert subprocess.run(["floridayvine", "about", "version"]).returncode == 0

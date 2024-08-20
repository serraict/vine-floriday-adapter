import subprocess


def test_can_run_script():
    subprocess.run(["floridayvine", "about"])


def test_can_print_version():
    subprocess.run(["floridayvine", "print-version"])

import subprocess


def test_can_run_about():
    assert subprocess.run(["floridayvine", "about"]).returncode == 0


def test_can_print_version():
    assert subprocess.run(["floridayvine", "about", "version"]).returncode == 0


def test_can_show_info():
    assert subprocess.run(["floridayvine", "about", "show-info"]).returncode == 0


def test_can_run_sync():
    assert subprocess.run(["floridayvine", "sync", "--help"]).returncode == 0


def test_can_run_db():
    assert subprocess.run(["floridayvine", "db", "--help"]).returncode == 0

import project


def test_get_work_rest():
    assert project.get_work_rest("n") == (25, 5)

def test_repeat(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert project.repeat() == True
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert project.repeat() == False

def test_get(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert project.get() == "y"
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert project.get() == "n"
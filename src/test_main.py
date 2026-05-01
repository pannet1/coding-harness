import os
import tempfile
import shutil
from pathlib import Path
from main import sanitize_lang, is_version_controlled, get_repo_path

def test_sanitize_lang():
    assert sanitize_lang(None) == 'unknown'
    assert sanitize_lang('unknown') == 'unknown'
    assert sanitize_lang('Python') == 'python'
    assert sanitize_lang('Jupyter Notebook') == 'jupyter-notebook'
    assert sanitize_lang('C++') == 'c-'
    print("PASS: test_sanitize_lang")

def test_is_version_controlled():
    tmp = tempfile.mkdtemp()
    try:
        real = os.path.join(tmp, "real-repo")
        os.makedirs(os.path.join(real, ".git"))
        assert is_version_controlled(real) == True

        mock = os.path.join(tmp, "mock-repo")
        os.makedirs(mock)
        assert is_version_controlled(mock) == False
    finally:
        shutil.rmtree(tmp)
    print("PASS: test_is_version_controlled")

def test_get_repo_path():
    repo = {'name': 'test-repo', 'primaryLanguage': {'name': 'Python'}}
    owner = 'user1'
    path = get_repo_path(repo, owner)
    expected = Path.home() / "programs" / "python" / "github.com" / "user1" / "test-repo"
    assert path == expected

    repo_no_lang = {'name': 'test-repo', 'primaryLanguage': None}
    path = get_repo_path(repo_no_lang, owner)
    expected = Path.home() / "programs" / "unknown" / "github.com" / "user1" / "test-repo"
    assert path == expected
    
    print("PASS: test_get_repo_path")

if __name__ == "__main__":
    test_sanitize_lang()
    test_is_version_controlled()
    test_get_repo_path()
    print("\nAll tests passed!")

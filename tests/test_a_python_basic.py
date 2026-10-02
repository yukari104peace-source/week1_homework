import sys
from pathlib import Path

# tests/ フォルダーから python_basic/ フォルダーのファイルを読み込むための準備
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def test_a_1():
    from python_basic.a_1 import users

    assert users == ["Bob", "Tom", "Ken"]
    print("A-1 OK")


def test_a_2():
    from python_basic.a_2 import int_numbers

    assert int_numbers == [1, 2, 3, 4, 5]
    print("A-2 OK")


def test_a_3():
    from python_basic.a_3 import bob_info

    assert bob_info == ["Bob", "Dylan", 79]
    print("A-3 OK")


def run_script(file_path):
    import subprocess
    import sys
    from pathlib import Path

    root_dir = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(root_dir / file_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def test_a_4():
    assert run_script("python_basic/a_4.py") == ["Bob", "Tom"]
    print("A-4 OK")


def test_a_5():
    assert run_script("python_basic/a_5.py") == ["Name: Bob Dylan, Age: 79"]
    print("A-5 OK")


def test_a_6():
    assert run_script("python_basic/a_6.py") == ["1", "3", "5", "7", "9"]
    print("A-6 OK")


def test_a_7():
    assert run_script("python_basic/a_7.py") == ["4", "8", "12", "16"]
    print("A-7 OK")


def test_a_8():
    assert run_script("python_basic/a_8.py") == [
        "Name: Bob, Age: 79",
        "Name: Tom, Age: 59",
        "Name: Ken, Age: 61",
    ]
    print("A-8 OK")


def test_a_9():
    from python_basic.a_9 import bob_info

    assert bob_info["first_name"] == "Bob"
    assert bob_info["family_name"] == "Dylan"
    assert bob_info["age"] == 79
    print("A-9 OK")


def test_a_10():
    from python_basic.a_10 import dice

    for _ in range(100):
        result = dice()
        assert isinstance(result, int)
        assert 1 <= result <= 6
    print("A-10 OK")


def main():
    test_a_1()
    test_a_2()
    test_a_3()
    test_a_4()
    test_a_5()
    test_a_6()
    test_a_7()
    test_a_8()
    test_a_9()
    test_a_10()


main()

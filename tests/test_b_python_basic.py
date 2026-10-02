import sys
from pathlib import Path

# tests/ フォルダーから python_basic2/ フォルダーのファイルを読み込むための準備
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def test_b_1():
    from python_basic2.kuku_1 import create_kuku_table

    table = create_kuku_table()

    assert table[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert table[8] == [9, 18, 27, 36, 45, 54, 63, 72, 81]
    print("B-1 OK")


def test_b_2():
    from python_basic2.kuku_2 import create_kuku_table

    assert create_kuku_table(4, 6) == [
        [1, 2, 3, 4, 5, 6],
        [2, 4, 6, 8, 10, 12],
        [3, 6, 9, 12, 15, 18],
        [4, 8, 12, 16, 20, 24],
    ]
    print("B-2 OK")


def test_b_3():
    from python_basic2.beautiful_kuku import format_kuku

    assert format_kuku(2, 2) == [
        "1 x 1 =  1 | 2 x 1 =  2 | ",
        "1 x 2 =  2 | 2 x 2 =  4 | ",
    ]
    print("B-3 OK")


def test_b_4():
    from python_basic2.weather_info_analysis import (
        average_temperature,
        average_temperature_by_prefecture,
        station_names_by_prefecture,
    )

    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    assert average_temperature(weather_information) == 9.5
    assert station_names_by_prefecture(weather_information, "大阪府") == "梅田,大阪,堺"
    assert average_temperature_by_prefecture(weather_information, "福岡県") == 14.0
    print("B-4 OK")


def test_b_5():
    from python_basic2.my_statistic_functions import my_average, my_max, my_min, my_sum

    numbers = [1, 1, 2, 3, 5, 8, 13, 21]

    assert my_sum(numbers) == 54
    assert my_max(numbers) == 21
    assert my_min(numbers) == 1
    assert my_average(numbers) == 6
    print("B-5 OK")


def test_b_6():
    from python_basic2.dice import roll_dice

    results = roll_dice(sides=8, times=20)

    assert len(results) == 20
    for result in results:
        assert isinstance(result, int)
        assert 1 <= result <= 8
    print("B-6 OK")


def main():
    test_b_1()
    test_b_2()
    test_b_3()
    test_b_4()
    test_b_5()
    test_b_6()


if __name__ == "__main__":

    main()

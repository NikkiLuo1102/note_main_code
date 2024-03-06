from app import process_query


def test_knows_about_dinosaurs():
    st1 = "Dinosaurs ruled the Earth 200 million years ago"
    assert process_query("dinosaurs") == st1


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def tests_name():
    assert process_query("What is your name?") == "KFC V50"


def tests_multi():
    assert process_query("What is 2 multiplied by 22?") == "44"


def tests_largest():
    str1 = "Which of the following numbers is the largest: 32, 15, 44?"
    assert process_query(str1) == "44"


def tests_plus():
    assert process_query("What is 34 plus 12?") == "46"


def tests_square_cube():
    str1 = "Which of the following numbers is both a square and a cube: "
    str2 = "78, 64, 16, 27, 729?"
    assert process_query(str1+str2) == "64, 729"


def tests_prime():
    str1 = "Which of the following numbers are primes: 7, 16, 23, 46, 41, 128?"
    assert process_query(str1) == "7, 23, 41"


def tests_minus():
    assert process_query("What is 25 minus 12?") == "13"

import bd
import pytest
from decimal import Decimal
import datetime


expected_output = [
    [
        (1, 'shivdutt', Decimal('500000.20'), datetime.date(2001, 3, 6)),
        (2, 'mikku', Decimal('400000.20'), datetime.date(2001, 5, 27)),
        (3, 'dewansh sharma ', Decimal('2500000.20'), datetime.date(2001, 9, 4)),
        (4, 'sahil matta  ', Decimal('410000.20'), datetime.date(2001, 5, 29))
    ]
]

def test_data():
    actual_output = bd.db_fetching()
    emp = []
    emp.append(actual_output)
    print(expected_output)
    if expected_output != actual_output:
        print("Expected Output:")
        for row in expected_output:
            print(row)
        print("Actual Output:")
        for row in actual_output:
            print(row)
    assert expected_output == emp

def main():
    test_data()
    print ("your test have bin run successfully")

if __name__ == "__main__":
    main()


## this is a new feature created by harshit paliwal

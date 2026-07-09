#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "plant" + 42  # type: ignore[operator]
    else:
        print("Operation completed successfully")


def test_one_operation(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    try:
        garden_operations(operation_number)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    test_one_operation(0)
    test_one_operation(1)
    test_one_operation(2)
    test_one_operation(3)
    test_one_operation(4)

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

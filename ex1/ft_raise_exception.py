#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_one_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_one_temperature("25")
    test_one_temperature("abc")
    test_one_temperature("100")
    test_one_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

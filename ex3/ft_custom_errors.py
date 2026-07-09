#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_specific_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_all_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    test_specific_errors()
    print()
    test_all_garden_errors()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

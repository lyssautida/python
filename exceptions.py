while True:
    try:
        number = int(input("Number: "))
        result = 10/number
    except ValueError as e:
        print(f"Error of value: {e}")
        raise ValueError("Incompatible variable types")
    except Exception as e:
        print(f"General Error: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("The End")
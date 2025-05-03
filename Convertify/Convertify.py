def convert_length(value, from_unit, to_unit):
    length_units = {
        'm': 1,
        'cm': 100,
        'km': 0.001,
        'mm': 1000,
        'mile': 0.000621371,
        'yard': 1.09361,
        'foot': 3.28084
    }
    value_in_meters = value * length_units[from_unit]
    result = value_in_meters / length_units[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kg': 1,
        'g': 1000,
        'mg': 1000000,
        'lb': 2.20462,
        'oz': 35.274
    }
    value_in_kg = value * weight_units[from_unit]
    result = value_in_kg / weight_units[to_unit]
    return result

def main():
    print("Welcome to the unit converter!")
    
    while True:
        print("\nChoose the type of conversion:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("Type 'q' to quit the program.")
        
        choice = input("Enter the number for your choice or 'q' to quit: ")
        
        if choice == 'q':  # If user types 'q', quit the program
            print("Exiting the program. Goodbye!")
            break
        
        if choice == '1':  # Length Conversion
            value = float(input("Enter the value: "))
            from_unit = input("Enter the unit to convert from (m, cm, km, mm, mile, yard, foot): ")
            to_unit = input("Enter the unit to convert to (m, cm, km, mm, mile, yard, foot): ")
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result} {to_unit}")
        
        elif choice == '2':  # Temperature Conversion
            value = float(input("Enter the value: "))
            from_unit = input("Enter the unit to convert from (C, F, K): ")
            to_unit = input("Enter the unit to convert to (C, F, K): ")
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result} {to_unit}")
        
        elif choice == '3':  # Weight Conversion
            value = float(input("Enter the value: "))
            from_unit = input("Enter the unit to convert from (kg, g, mg, lb, oz): ")
            to_unit = input("Enter the unit to convert to (kg, g, mg, lb, oz): ")
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result} {to_unit}")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

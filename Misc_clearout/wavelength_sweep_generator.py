"""
Function to generate list of linear shifts, in mm, given a frequency in GHz. 

The function produces 9 shifts from 0 to one wavelength.
"""

def generate_wavelength_shifts(frequency: float) -> list:
    """
    Generate a list of linear shifts in mm given a frequency in GHz.
    
    Args:
        frequency (float): Frequency in GHz.
        
    Returns:
        list: List of linear shifts in mm.
    """
    wavelength = 300 / frequency
    shifts = [i * wavelength / 9 for i in range(10)]
    return shifts

if __name__ == "__main__":
    frequency = 5.6  # Example frequency in GHz
    shifts = generate_wavelength_shifts(frequency)
    print(f"Shifts for {frequency} GHz: {shifts}")


def convert_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes_full = (decimal_degrees - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60

    return degrees, minutes, seconds


# Test the function
test_degrees = 262.81
converted_dms = convert_to_dms(test_degrees)
print(f"Converted DMS: {converted_dms[0]}° {
      converted_dms[1]}' {converted_dms[2]:.2f}\"")

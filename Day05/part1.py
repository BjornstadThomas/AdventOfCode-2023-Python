def read_almanac(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    # Extract initial seeds
    seeds = list(map(int, lines[0].split(': ')[1].split()))

    # Function to find the index of a given header
    def find_header_index(header):
        for i, line in enumerate(lines):
            if line.startswith(header):
                return i
        return None

    # Function to create a mapping function
    def create_mapping_func(start_idx):
        mapping_ranges = []
        i = start_idx + 1
        while i < len(lines) and lines[i][0].isdigit():
            dest_start, source_start, length = map(int, lines[i].split())
            mapping_ranges.append((source_start, dest_start, length))
            i += 1

        def mapping_func(number):
            for source_start, dest_start, length in mapping_ranges:
                if source_start <= number < source_start + length:
                    return dest_start + (number - source_start)
            return number  # Default to same number if not in any range

        return mapping_func

    # Extract mapping functions
    seed_to_soil_func = create_mapping_func(find_header_index('seed-to-soil map'))
    soil_to_fertilizer_func = create_mapping_func(find_header_index('soil-to-fertilizer map'))
    fertilizer_to_water_func = create_mapping_func(find_header_index('fertilizer-to-water map'))
    water_to_light_func = create_mapping_func(find_header_index('water-to-light map'))
    light_to_temperature_func = create_mapping_func(find_header_index('light-to-temperature map'))
    temperature_to_humidity_func = create_mapping_func(find_header_index('temperature-to-humidity map'))
    humidity_to_location_func = create_mapping_func(find_header_index('humidity-to-location map'))

    return seeds, seed_to_soil_func, soil_to_fertilizer_func, fertilizer_to_water_func, \
           water_to_light_func, light_to_temperature_func, temperature_to_humidity_func, humidity_to_location_func

def convert_number(mapping_func, number):
    return mapping_func(number)

def find_lowest_location(seeds, mapping_funcs):
    lowest_location = float('inf')
    for seed in seeds:
        soil = convert_number(mapping_funcs[0], seed)
        fertilizer = convert_number(mapping_funcs[1], soil)
        water = convert_number(mapping_funcs[2], fertilizer)
        light = convert_number(mapping_funcs[3], water)
        temperature = convert_number(mapping_funcs[4], light)
        humidity = convert_number(mapping_funcs[5], temperature)
        location = convert_number(mapping_funcs[6], humidity)
        lowest_location = min(lowest_location, location)

    return lowest_location

# Read the almanac and calculate the lowest location number
file_path = 'input.txt'
seeds, *mapping_funcs = read_almanac(file_path)
lowest_location = find_lowest_location(seeds, mapping_funcs)
print("Lowest location number part 1:", lowest_location)

input_file = 'input/rettangolo_input_1.txt'  # Adjusted for consistency
output_file = 'output/rettangolo_output_1.txt'

# Open the input file for reading
with open(input_file, 'r') as file:
    # First line: Number of cases
    T = int(file.readline().strip())

    # Initialize a counter for the number of cases processed
    cases_processed = 0

    while cases_processed < T:
        lines = []
        while len(lines) < 3:
            line = file.readline().strip()
            # Skip any blank lines
            if line:
                lines.append(line)
        
        # Unpack the collected lines into coordinates
        x1, y1 = map(int, lines[0].split())
        x2, y2 = map(int, lines[1].split())
        x3, y3 = map(int, lines[2].split())

        # Logic to calculate the fourth point remains the same
        if x1 == x2:
            x4 = x3
        elif x1 == x3:
            x4 = x2
        else:
            x4 = x1

        if y1 == y2:
            y4 = y3
        elif y1 == y3:
            y4 = y2
        else:
            y4 = y1

        # Writing the output for each case to the output file
        with open(output_file, 'a') as out:
            out.write(f'Case #{cases_processed + 1}: {x4} {y4}\n')
        
        # Increment the case processed count
        cases_processed += 1


#!/usr/bin/python3

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
count_by_code = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            # Extract file size and status code from line
            fields = line.split()
            size = int(fields[-1])
            code = int(fields[-2])
            if code in count_by_code:
                count_by_code[code] += 1
            total_size += size
            line_count += 1
        except (IndexError, ValueError):
            # Ignore lines that don't match the input format
            pass

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(count_by_code):
                print(f"{code}: {count_by_code[code]}")

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) by printing final metrics
    print(f"Total file size: {total_size}")
    for code in sorted(count_by_code):
        print(f"{code}: {count_by_code[code]}")

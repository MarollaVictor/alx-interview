#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 
                     403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                # Check if line has correct format
                if len(parts) >= 7:
                    ip = parts[0]
                    date = parts[3] + " " + parts[4]
                    method = parts[5]
                    path = parts[6]
                    status_code = parts[-2]
                    file_size = parts[-1]

                    # Validate and process
                    if (method == '"GET' and path.startswith('/projects/260') and 
                        status_code.isdigit() and file_size.isdigit()):
                        status_code = int(status_code)
                        file_size = int(file_size)
                        
                        if status_code in status_counts:
                            total_size += file_size
                            status_counts[status_code] += 1
                            line_count += 1

                            # Print every 10 lines
                            if line_count % 10 == 0:
                                print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        # Print stats on CTRL+C
        print_stats(total_size, status_counts)
        raise

    # Print final stats if we reach EOF
    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

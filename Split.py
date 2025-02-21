#!/usr/bin/env python3
import json
import os
import sys

def split_json_file(input_file, rows_per_file=1000):
    output_file_index = 1
    current_rows = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON: {line}")
                continue

            current_rows.append(obj)

            if len(current_rows) == rows_per_file:
                output_filename = f"{os.path.splitext(input_file)[0]}_{output_file_index}.json"
                with open(output_filename, 'w', encoding='utf-8') as outfile:
                    for item in current_rows:
                        json.dump(item, outfile)
                        outfile.write('\n')
                print(f"Wrote {output_filename} with {rows_per_file} rows.")
                output_file_index += 1
                current_rows = []

        if current_rows:
            output_filename = f"{os.path.splitext(input_file)[0]}_{output_file_index}.json"
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                for item in current_rows:
                    json.dump(item, outfile)
                    outfile.write('\n')
            print(f"Wrote {output_filename} with {len(current_rows)} rows.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 split_json.py <input_file> [rows_per_file]")
        sys.exit(1)

    input_path = sys.argv[1]
    rows = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

    split_json_file(input_path, rows)
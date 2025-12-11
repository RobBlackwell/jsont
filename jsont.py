#!/usr/bin/env python3

import argparse
import json
import datetime
import json
from pathlib import Path


def escape(s):
    return s.encode("unicode_escape").decode("ascii")


def main():

    parser = argparse.ArgumentParser(
        description="Process a template file and a JSONL file to produce formatted strings."
    )
    parser.add_argument("template_file", type=str, help="Path to the template file.")
    parser.add_argument("jsonl_file", type=str, help="Path to the JSONL file.")
    parser.add_argument(
        "--remove-line-endings",
        action="store_true",
        help="Remove line endings from the template (useful for JSONL).",
    )
    parser.add_argument(
        "--escape-strings",
        action="store_true",
        help="Escape strings from the JSONL (useful for JSONL).",
    )

    args = parser.parse_args()

    # Read the template string from the template file
    with open(args.template_file, "r") as file:
        template_string = file.read()

        if args.remove_line_endings:
            template_string = template_string.replace("\n", "")

    line_number = 0
    # Process each line in the JSONL file
    with open(args.jsonl_file, "r") as file:
        for line in file:
            # Convert JSON line to dictionary
            data = json.loads(line.strip())

            line_number += 1

            # Create a safe environment containing the data
            safe_env = {
                "line": data,
                "line_number": line_number,
                "json": json,
                "Path": Path,
                "str": str,
                "escape": escape,
            }

            # Use eval to interpret the string as an f-string dynamically
            formatted_string = eval(
                f"f'''{template_string}'''", {"__builtins__": {}}, safe_env
            )

            # Print the result
            print(formatted_string)


if __name__ == "__main__":
    main()

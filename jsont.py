#!/usr/bin/env python3

from pathlib import Path
import argparse
import datetime
import socket
import getpass
import os
import json
import sys


def escape(s):
    return s.encode("unicode_escape").decode("ascii")


def load_template_file(filename, remove_line_endings=False):
    with open(filename, "r") as file:
        content = file.read()
        if remove_line_endings:
            content = content.replace("\n", "")
        return content


def template(
    template_string,
    data,
    line_number,
):

    # Create a safe environment containing the data
    safe_env = {"line": data, "data": data, "line_number": line_number}

    # Use eval to interpret the template as an f-string dynamically
    return eval(f"f'''{template_string}'''", globals(), safe_env)


def main():

    parser = argparse.ArgumentParser(
        description="Process a template file and a JSONL file to produce formatted strings."
    )
    parser.add_argument("template_file", type=str, help="Path to the template file.")
    parser.add_argument("jsonl_file", type=str, help="Path to the JSONL file.")
    parser.add_argument(
        "--header",
        type=str,
        help="Path to a template file to render once before processing the JSONL lines.",
    )
    parser.add_argument(
        "--trailer",
        type=str,
        help="Path to a template file to render once after processing the JSONL lines.",
    )
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
    parser.add_argument(
        "--ignore-errors",
        action="store_true",
        help="Ignore lines with errors and continue processing.",
    )

    # args = parser.parse_args()
    args, unknown = parser.parse_known_args()

    # Convert unknown args into dictionary
    arg_dict = {}
    i = 0
    while i < len(unknown):
        key = unknown[i].lstrip("-")
        if i + 1 < len(unknown) and not unknown[i + 1].startswith("--"):
            value = unknown[i + 1]
            i += 2
        else:
            value = True
            i += 1
        arg_dict[key] = value

    # Read main template
    template_string = load_template_file(
        args.template_file,
        remove_line_endings=args.remove_line_endings,
    )

    # Read optional header template
    header_template = (
        load_template_file(args.header, remove_line_endings=args.remove_line_endings)
        if args.header
        else None
    )

    # Read optional trailer template
    trailer_template = (
        load_template_file(args.trailer, remove_line_endings=args.remove_line_endings)
        if args.trailer
        else None
    )

    # Render header once before the loop
    if header_template is not None:
        print(template(header_template, arg_dict, 0))

    # Read the template string from the template file
    with open(args.template_file, "r") as file:
        template_string = file.read()

        if args.remove_line_endings:
            template_string = template_string.replace("\n", "")

    line_number = 0
    # Process each line in the JSONL file
    with open(args.jsonl_file, "r") as file:
        for line in file:

            line_number += 1

            try:
                # Convert JSON line to dictionary
                data = json.loads(line.strip())

                print(template(template_string, data, line_number))

            except Exception as e:
                if args.ignore_errors:
                    print(f"Error on line {line_number}: {e}", file=sys.stderr)
                    continue
                else:
                    raise

    # Render trailer once after the loop
    if trailer_template is not None:
        print(template(trailer_template, arg_dict, line_number + 1))


if __name__ == "__main__":
    # print(
    #     template(
    #         "Date: {datetime.datetime.now()} and {data['a']}", json.loads('{"a":1}'), 1
    #     )
    # )
    main()

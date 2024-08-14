#!/usr/bin/env python3

import csv
import json
import sys


def read_json_object_list_write_csv(
    input_filename: str,
    output_filename: str,
) -> None:
    with open(input_filename, 'rt') as f:
        output_json_str = f.read()

    output_json = json.loads(output_json_str)
    header = output_json[0].keys()

    with open(output_filename, 'wt') as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(output_json)

if __name__ == "__main__":
    read_json_object_list_write_csv(
        input_filename=sys.argv[1],
        output_filename=sys.argv[2])
  

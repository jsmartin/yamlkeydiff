#! /usr/bin/env python

import yaml
import argparse
from difflib import unified_diff

# new_vars_file is considered the authoritative source.
# if new_vars_file has keys that are not present in old_vars_file, 
# they will be printed as "New Keys".
# if old_vars_file has keys that are not present in new_vars_file, 
# they will be printed as "Depricated Keys".

parser = argparse.ArgumentParser()
parser.add_argument("new_vars_file")
parser.add_argument("old_vars_file")
args = parser.parse_args()


file1_data = yaml.load(open(args.new_vars_file).read())
file2_data = yaml.load(open(args.old_vars_file).read())
s1 = file1_data.keys()
s2 = file2_data.keys()
s1.sort()
s2.sort()

for key in unified_diff(s1, s2, fromfile=args.old_vars_file, tofile=args.new_vars_file):
    print key

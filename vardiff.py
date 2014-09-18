#! /usr/bin/env python

import yaml
import argparse

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

new_keys = list(set(file1_data.keys()).difference(file2_data.keys()))

print "\nNew Keys:"
print '\n'.join(new_keys)

print "\nDepricated Keys:"
depricated_keys = []

for key in file2_data.keys():
	if not key in file1_data.keys():
		print key
		depricated_keys.append(key)


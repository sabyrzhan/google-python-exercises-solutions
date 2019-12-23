#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def move_to_dir(files, todir):
  if not os.path.exists(todir):
    os.makedirs(todir)
  for file in files:
    shutil.copy(file, os.path.join(todir, file))

def zip_files(files, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(files)
  (status, output) = commands.getstatusoutput(cmd)
  if status != 0:
    print output

def gather_files(dirs, todir, tozip):
  r = r'__\w+__'
  result = []
  for dir in dirs:
    files = os.listdir(dir)
    for file in files:
      match = re.search(r, file)
      if match:
        result.append(file)

  if len(files) > 0 and todir:
    move_to_dir(result, todir)

  if len(files) > 0 and tozip:
    zip_files(result, tozip)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  gather_files(args, todir, tozip)
  
if __name__ == "__main__":
  main()

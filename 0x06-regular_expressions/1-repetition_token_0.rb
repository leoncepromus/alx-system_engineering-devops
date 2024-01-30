#!/usr/bin/env ruby

# Get the argument passed to the script
input = ARGV[0]

# Define the regular expression pattern using repetition token
pattern = /hbt{2,5}n/

# Check if the input matches the pattern
if input =~ pattern
  puts input
else
  puts '$'
end

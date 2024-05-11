#!/usr/bin/env ruby

# Check if the argument contains the word "School"
def match_school(str)
  # Regular expression to match "School"
  regex = /School/

  # Check if the string matches the regular expression
  if str.match?(regex)
    puts "School"
  else
    # Output nothing if "School" is not found
    puts ""
  end
end

# Accept the argument from the command line
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Call the method with the provided argument
match_school(ARGV[0])

#!/usr/bin/env ruby

# Define a method to extract sender, receiver, and flags from a log entry
def extract_info(log_entry)
    sender = log_entry.match(/\[from:(?<sender>[^\]]+)\]/)[:sender]
    receiver = log_entry.match(/\[to:(?<receiver>[^\]]+)\]/)[:receiver]
    flags = log_entry.match(/\[flags:(?<flags>[^\]]+)\]/)[:flags]
    
    [sender, receiver, flags]
  end
  
  # Read each line of the log file and process it
  File.open(ARGV[0], "r") do |file|
    file.each_line do |line|
      if line.include?("Sent SMS") || line.include?("Receive SMS")
        sender, receiver, flags = extract_info(line)
        puts "#{sender},#{receiver},#{flags}"
      end
    end
  end
  
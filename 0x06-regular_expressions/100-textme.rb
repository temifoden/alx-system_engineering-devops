#!/usr/bin/env ruby

def extract_info(log_entry)
    sender = log_entry.match(/\[from:(?<sender>[^\]]+)\]/)[:sender]
    receiver = log_entry.match(/\[to:(?<receiver>[^\]]+)\]/)[:receiver]
    flags = log_entry.match(/\[flags:(?<flags>[^\]]+)\]/)[:flags]
    "#{sender},#{receiver},#{flags}"
  end
  
  ARGF.each_line do |line|
    next unless line.include?("mdr: ")
    log_entry = line.match(/mdr:.*?\[(.*?)\]/)[1]
    puts extract_info(log_entry)
  end
  
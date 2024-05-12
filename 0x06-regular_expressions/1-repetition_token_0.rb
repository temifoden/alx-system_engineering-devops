#!/usr/bin/env ruby

regex = /hb{0,1}tn/
puts ARGV[0].scan(regex).join

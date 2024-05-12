#!/usr/bin/env ruby

regex = /^\d{10}$/
puts ARGV[0].match?(regex) ? ARGV[0] : ''

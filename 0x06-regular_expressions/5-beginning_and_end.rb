#!/usr/bin/env ruby

regex = /^h.n$/
puts ARGV[0].match?(regex) ? ARGV[0] : ''

#!/usr/bin/env ruby
# Repetitive token

puts ARGV[0].scan(/\bh{1}b{1}t{1,4}n{1}\b/)

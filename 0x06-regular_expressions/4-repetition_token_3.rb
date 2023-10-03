#!/usr/bin/env ruby
# Repetitive token

input_text = ARGV[0]
puts input_text.scan(/\bhbt*n\b/).join

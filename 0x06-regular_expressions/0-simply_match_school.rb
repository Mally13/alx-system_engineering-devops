#!/usr/bin/env ruby
# A regular expression to match arg with School

input_texts = ARGV[0].split(' ')
regex = /School/
input_texts.each do |word|
 if word =~ regex
   print "School"
 end
end
print "\n"

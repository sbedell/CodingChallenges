# Temperature Comparison​
# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).

File.open( 'ckChallenge.txt' ) do |line|
    puts line
end

# Your program must read input data and write the result on the standard output.
f = File.open("ckChallenge.txt", "r")
# Display 0 (zero) if no temperatures are provided.
# Otherwise, display the temperature closest to 0.
# Input Line 1: N, the number of temperatures to analyze, 0 ≤ N < 1,000,000
#n = f.readLines[0]
if n < 0 || n > 1000000
    puts "error shit idk"
end

# Input Line 2: The N space delimited temperatures expressed as integers ranging from -273 to 5526
#line2 = f.readLines[1]
puts line2

# File.open( 'file.txt' ) do |f|
#   loop do
#     break if not line = f.gets
#     puts "#{f.lineno}: #{line}"
#   end
# end

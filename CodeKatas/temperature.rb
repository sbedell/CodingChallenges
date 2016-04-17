# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).
# Your program must read input data and write the result on the standard output.

def getTempClosestToZero(filename)
    f = File.open(filename, "r")

    # OR

    File.open(filename) do |line|
        puts line
    end
end

# Your program must read input data and write the result on the standard output.
# f = File.open("ckChallenge.txt", "r")
# Display 0 (zero) if no temperatures are provided.
# Otherwise, display the temperature closest to 0.
# Input Line 1: N, the number of temperatures to analyze, 0 ≤ N < 1,000,000
# n = f.readLines[0]
# if n < 0 || n > 1000000
#     puts "error shit idk"
# end

# Input Line 2: The N space delimited temperatures expressed as integers ranging from -273 to 5526
# line2 = f.readLines[1]
# puts line2

# File.open( 'file.txt' ) do |f|
#   loop do
#     break if not line = f.gets
#     puts "#{f.lineno}: #{line}"
#   end
# end

#-----------------------------------------

# def getTempClosestToZero(filename):
#     with open(filename, "r") as f:
#         #Input Line 1: N, the number of temperatures to analyze, 0 ≤ N < 1,000,000
#         n = int(f.readline())
#         assert n >= 0 and n < 1000000
#
#         #Input Line 2: The N space delimited temperatures
#         # expressed as integers ranging from -273 to 5526
#         numbers = f.readline().strip().split(" ")
#
#         # Display 0 (zero) if no temperatures are provided.
#         if n == 0:
#             return 0
#         else:
#             # Otherwise, display the temperature closest to 0.
#             assert len(numbers) == n, "number of elements must be equal to the N on line 1"
#             lowestTemp = 5526
#             for i in numbers:
#                 x = int(i)
#
#                 # Check if number is outside of acceptable range
#                 # and skip it if it is.
#                 if x < -273 or x > 5526:
#                     continue
#
#                 if abs(x) < abs(lowestTemp):
#                     lowestTemp = x
#                 elif (abs(x) == abs(lowestTemp)) and x > 0:
#                     lowestTemp = x
#
#             return lowestTemp

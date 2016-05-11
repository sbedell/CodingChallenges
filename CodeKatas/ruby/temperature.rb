# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).
# Your program must read input data and write the result on the standard output.

class TemperatureChecker
    # empty constructor, for now
    def initialize
    end
    
    def getTempClosestToZero(filename)
        f = File.open(filename, "r")
        #Input Line 1: N, the number of temperatures to analyze, 0 ≤ N < 1,000,000
        n = f.readline.to_i
        #puts n
        
        if n < 0 || n > 1000000
            puts "error, n outside of valid range"
            return nil
        end
        
        #Input Line 2: The N space delimited temperatures
        # expressed as integers ranging from -273 to 5526
        numbers = f.readline.strip.split
        #puts numbers
        f.close
        
        # assert len(numbers) == n, "number of elements must be equal to the N on line 1"
        if numbers.length != n
            puts "error, number of elements must be equal to the N on line 1 of the input file"
            return nil
        end
        
        # Display 0 (zero) if no temperatures are provided.
        if n == 0
            return 0
        else        # Otherwise, display the temperature closest to 0.
            lowestTemp = 5526
            for i in numbers
                x = i.to_i
                
                # Check if number is outside of acceptable range
                # and skip it if it is.
                if x < -273 or x > 5526
                    next
                end
                
                if (x.abs < lowestTemp.abs) || ((x.abs == lowestTemp.abs) && x > 0) 
                    lowestTemp = x
                end
            end
            
            return lowestTemp
        end
    end
end

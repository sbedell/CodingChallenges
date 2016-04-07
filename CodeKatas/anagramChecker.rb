require "benchmark"

def checkAnagram(string1, string2)
    # Strip spaces and change to lowercase
    str1 = string1.delete(' ').downcase
    str2 = string2.delete(' ').downcase

    if str1.length != str2.length
        return false
    end

    # Get characters arrays and sort them
    str1chars = str1.chars.sort
    str2chars = str2.chars.sort

    # Loop thru the sorted character arrays and if any chars don't match up, return false
    x = 0
    while x < str1chars.length
        if (str1chars[x] != str2chars[x])
            return false
        end
        x += 1
    end

    # Return true if it makes it thru all the checks
    return true
end

def checkAnagram2(string1, string2)
    str1 = string1.delete(' ').downcase
    str2 = string2.delete(' ').downcase

    # For "perfect" anagrams
    if str1.length != str2.length
        return false
    end

    charMap1 = Hash.new
    charMap2 = Hash.new

    for x in str1.chars
        if !charMap1.has_key?(x)
            charMap1[x] = 1
        else
            charMap1[x] += 1
        end
    end
    #puts charMap1

    for y in str2.chars
        if !charMap2.has_key?(y)
            charMap2[y] = 1
        else
            charMap2[y] += 1
        end
    end

    # Loop thru the sorted character arrays
    # and if any chars don't match up, return false
    i = 0
    while i < charMap1.size
        if (charMap1[i] != charMap2[i])
            return false
        end
        i += 1
    end

    # Return true if it makes it thru all the checks
    return true
end

# Testing
puts "\nTesting notAnagram and test => " + checkAnagram("notAnagram", "test").to_s
puts "test and seTT => \t\t" + checkAnagram("test", "seTT").to_s
puts "William Shakespeare and I am a weakish speller => " +
    checkAnagram("William Shakespeare", "I am a weakish speller").to_s
puts "Anagram and a nag ram => " + checkAnagram("anagram", "a nag ram").to_s
puts "Time and tide wait for no man. and Notified madman into water. => \t" +
    checkAnagram("Time and tide wait for no man.", "Notified madman into water.").to_s
puts "Tom Marvolo Riddle and I am Lord Voldemort => \t" + checkAnagram("Tom Marvolo Riddle", "I am Lord Voldemort").to_s

puts checkAnagram2("Tom Marvolo Riddle", "I am Lord Voldemort")
puts Benchmark.measure { checkAnagram("Tom Marvolo Riddle", "I am Lord Voldemort") }
puts Benchmark.measure { checkAnagram2("Tom Marvolo Riddle", "I am Lord Voldemort") }

time1 = Time.now
puts checkAnagram('Anagram', 'A nag ram')
puts "Time elapsed = " + (Time.now - time1).to_s

time2 = Time.now
puts checkAnagram2('Anagram', 'A nag ram')
puts "Time elapsed = " + (Time.now - time2).to_s
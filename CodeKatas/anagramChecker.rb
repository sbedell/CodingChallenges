class AnagramChecker
    # Empty constructor, for now:
    def initialize
    end
    
    def checkAnagram(string1, string2)
        # regex is finding anything that's not a-z 0-9 and stripping it
        str1 = string1.downcase.gsub(/[^a-z0-9]/i, '')
        str2 = string2.downcase.gsub(/[^a-z0-9]/i, '')

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
        # regex is finding anything that's not a-z 0-9 and stripping it
        str1 = string1.downcase.gsub(/[^a-z0-9]/i, '')
        str2 = string2.downcase.gsub(/[^a-z0-9]/i, '')

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
end

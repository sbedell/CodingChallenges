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

# Testing
puts 'Testing notAnagram and test'
puts checkAnagram('notAnagram', 'test')
puts checkAnagram('test', 'seTT')
puts checkAnagram('William Shakespeare', 'I am a weakish speller')
puts checkAnagram('anagram', 'a nag ram')
puts checkAnagram('Time and tide wait for no man.', 'Notified madman into water.')
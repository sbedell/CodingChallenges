require 'test/unit'
require_relative "anagramChecker"

class AnagramCheckerTest < Test::Unit::TestCase
    def setup
        @ac = AnagramChecker.new()
    end

    # def teardown
    # end

    def testAnagram1
        assert(@ac.checkAnagram('Anagram', 'A nag ram'))
    end
    
    def testAnagram1otherAlgo
        assert(@ac.checkAnagram2('Anagram', 'A nag ram'))
    end
    
    def testAnagram2
        assert(@ac.checkAnagram("Tom Marvolo Riddle", "I am Lord Voldemort"))
    end
    
    def testOtherAlgorithm
        assert(@ac.checkAnagram2("Tom Marvolo Riddle", "I am Lord Voldemort"))
    end
    
    def testWeirdCases
        assert(@ac.checkAnagram("test", "seTT"))
    end
    
    def testSentence
        assert(@ac.checkAnagram("William Shakespeare", "I am a weakish speller"))
    end
    
    def testSentence2
        assert(@ac.checkAnagram2("Time and tide wait for no man.", "Notified madman into water."))
    end
    
    def testAnagramAlgos
        assert_equal(@ac.checkAnagram("Tom Marvolo Riddle", "I am Lord Voldemort"), @ac.checkAnagram2("Tom Marvolo Riddle", "I am Lord Voldemort"))
    end
    
    def testLong
        assert(@ac.checkAnagram('It was a dark and stormy night; the rain fell in torrents, except at
            occasional intervals, when it was checked by a violent gust of wind
            which swept up the streets (for it is in London that our scene lies),
            rattling along the housetops, and fiercely agitating the scanty flame
            of the lamps that struggled against the darkness.', 'Tut-tut! Bulwer-Lyttons known penchant for inelegant, stagnant,
            over-affected, cost-inflated prose evokes mirth a hundred years hence.
            Ah-ha! A well-known comic strip talent hatches it - a textual gag for a dog:
            (Snoopy wags his tail, sits at his typewriter, fidgets, and then
            distills a classic theme: "Its raining, theres no light")'))
    end
    
    def testLongSecondAlgo
        assert(@ac.checkAnagram2('It was a dark and stormy night; the rain fell in torrents, except at
        occasional intervals, when it was checked by a violent gust of wind
        which swept up the streets (for it is in London that our scene lies),
        rattling along the housetops, and fiercely agitating the scanty flame
        of the lamps that struggled against the darkness.', 'Tut-tut! Bulwer-Lyttons known penchant for inelegant, stagnant,
        over-affected, cost-inflated prose evokes mirth a hundred years hence.
        Ah-ha! A well-known comic strip talent hatches it - a textual gag for a dog:
        (Snoopy wags his tail, sits at his typewriter, fidgets, and then
        distills a classic theme: "Its raining, theres no light")'))
    end
    
    def testFalseCase
        assert_equal(false, @ac.checkAnagram("notAnagram", "test"))
    end
end


# puts Benchmark.measure { checkAnagram('It was a dark and stormy night; the rain fell in torrents, except at
# occasional intervals, when it was checked by a violent gust of wind
# which swept up the streets (for it is in London that our scene lies),
# rattling along the housetops, and fiercely agitating the scanty flame
# of the lamps that struggled against the darkness.', 'Tut-tut! Bulwer-Lyttons known penchant for inelegant, stagnant,
# over-affected, cost-inflated prose evokes mirth a hundred years hence.
# Ah-ha! A well-known comic strip talent hatches it - a textual gag for a dog:
# (Snoopy wags his tail, sits at his typewriter, fidgets, and then
# distills a classic theme: "Its raining, theres no light")') }
# time2 = Time.now
puts 

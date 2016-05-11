require 'test/unit'
require_relative "temperature"

class TemperatureCheckerTest < Test::Unit::TestCase
    def setup
        @tc = TemperatureChecker.new()
        #puts @tc.getTempClosestToZero("testData/kataTemp1.txt")
    end
    
    def testAbsoluteValue
        assert_equal(1, -1.abs)
    end

    def testInputFile1
        assert_equal(1, @tc.getTempClosestToZero("testData/kataTemp1.txt"))
    end
    
    def testInputFile2
        assert_equal(-5, @tc.getTempClosestToZero("testData/kataTemp2.txt"))
    end
    
    def testInputFile3
        assert_equal(5, @tc.getTempClosestToZero("testData/kataTemp3.txt"))
    end
    
    def testInputFile4
        assert_equal(5, @tc.getTempClosestToZero("testData/kataTemp4.txt"))
    end
    
    def testInputFile5
        assert_equal(2, @tc.getTempClosestToZero("testData/kataTemp5.txt"))
    end
    
    def testInputFile6
        assert_equal(0, @tc.getTempClosestToZero("testData/kataTemp6.txt"))
    end
end
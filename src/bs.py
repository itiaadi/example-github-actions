import unittest
def binary(arr,n):
    low = 0
    high = len(arr)-1

    while low <= high:
        #print(arr)
        #print(low,high)
        mid = low + (high - low) // 2
        mid_num = arr[mid]
        if mid_num > n:
            high = mid - 1
            #print(arr[mid])
        elif mid_num < n:
            low = mid + 1
        else:
            return mid
    return -1

n = 91
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary(arr,n))



class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        r1 = binary([1, 2, 3, 4, 5], 3)
        self.assertEqual(r1, 2)


    def test_empty_array(self):
        r2 = binary([], 3)
        self.assertEqual(r2, -1)


if __name__ == '__main__':
    unittest.main()
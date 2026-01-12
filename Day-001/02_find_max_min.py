"""
Problem: Find Maximum and Minimum Element in Array
Platform: GeeksforGeeks / LeetCode
Difficulty: Easy
Day: 1

Approach: Single traversal comparing with min and max
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def find_min_max(self, arr):
        """
        Find minimum and maximum elements in array
        
        Args:
            arr: List of integers
            
        Returns:
            Tuple (min_element, max_element)
        """
        if not arr:
            return None, None
        
        # Initialize with first element
        min_element = arr[0]
        max_element = arr[0]
        
        # Traverse array once
        for num in arr:
            if num < min_element:
                min_element = num
            if num > max_element:
                max_element = num
        
        return min_element, max_element
    
    def find_min_max_optimized(self, arr):
        """
        Optimized approach: Compare elements in pairs
        Reduces number of comparisons from 2n to 3n/2
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return None, None
        
        n = len(arr)
        
        # If only one element
        if n == 1:
            return arr[0], arr[0]
        
        # Initialize min and max based on first two elements
        if arr[0] < arr[1]:
            min_element = arr[0]
            max_element = arr[1]
        else:
            min_element = arr[1]
            max_element = arr[0]
        
        # Process remaining elements in pairs
        i = 2
        while i < n - 1:
            # Compare pair elements first
            if arr[i] < arr[i + 1]:
                smaller = arr[i]
                larger = arr[i + 1]
            else:
                smaller = arr[i + 1]
                larger = arr[i]
            
            # Update min and max
            if smaller < min_element:
                min_element = smaller
            if larger > max_element:
                max_element = larger
            
            i += 2
        
        # Handle last element if array size is odd
        if n % 2 != 0:
            if arr[n - 1] < min_element:
                min_element = arr[n - 1]
            if arr[n - 1] > max_element:
                max_element = arr[n - 1]
        
        return min_element, max_element
    
    def find_min_max_builtin(self, arr):
        """
        Using Python built-in functions
        Simple but less interview-friendly
        """
        if not arr:
            return None, None
        return min(arr), max(arr)


def test_solution():
    """Test cases for the solution"""
    sol = Solution()
    
    # Test Case 1: Normal array
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    min_val, max_val = sol.find_min_max(arr1)
    print(f"Array: {arr1}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val == 1 and max_val == 9, "Test Case 1 Failed"
    
    # Test Case 2: Array with negative numbers
    arr2 = [-5, 10, -3, 8, -20, 15]
    min_val, max_val = sol.find_min_max(arr2)
    print(f"\nArray: {arr2}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val == -20 and max_val == 15, "Test Case 2 Failed"
    
    # Test Case 3: Single element
    arr3 = [42]
    min_val, max_val = sol.find_min_max(arr3)
    print(f"\nArray: {arr3}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val == 42 and max_val == 42, "Test Case 3 Failed"
    
    # Test Case 4: All same elements
    arr4 = [7, 7, 7, 7]
    min_val, max_val = sol.find_min_max(arr4)
    print(f"\nArray: {arr4}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val == 7 and max_val == 7, "Test Case 4 Failed"
    
    # Test Case 5: Empty array
    arr5 = []
    min_val, max_val = sol.find_min_max(arr5)
    print(f"\nArray: {arr5}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val is None and max_val is None, "Test Case 5 Failed"
    
    # Test optimized approach
    print("\n--- Testing Optimized Approach ---")
    arr6 = [3, 5, 1, 8, 2, 9, 4, 7]
    min_val, max_val = sol.find_min_max_optimized(arr6)
    print(f"Array: {arr6}")
    print(f"Min: {min_val}, Max: {max_val}")
    assert min_val == 1 and max_val == 9, "Optimized Test Failed"
    
    print("\nAll test cases passed! ✅")


if __name__ == "__main__":
    test_solution()

"""
Key Learnings:
1. Single pass solution is sufficient for finding min and max
2. Initialize with first element, not with extreme values
3. Can optimize by comparing in pairs (3n/2 comparisons vs 2n)
4. Always handle edge cases: empty array, single element, all same

Comparison Analysis:
- Simple approach: 2n comparisons
- Optimized approach: 3n/2 comparisons (25% improvement)
- Both have O(n) time, O(1) space

Interview Tips:
- Start with simple solution, then mention optimization
- Discuss trade-offs between simplicity and optimization
- Consider using built-in functions but know the implementation
- Handle edge cases explicitly
"""
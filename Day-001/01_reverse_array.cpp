// Problem: Reverse an Array
// Platform: GeeksforGeeks / LeetCode
// Difficulty: Easy
// Day: 1

// Approach: Two-pointer technique
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Method 1: Using two pointers (In-place)
    void reverseArray(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;
        
        while (left < right) {
            // Swap elements at left and right positions
            swap(arr[left], arr[right]);
            left++;
            right--;
        }
    }
    
    // Method 2: Using recursion
    void reverseArrayRecursive(vector<int>& arr, int left, int right) {
        if (left >= right) {
            return;
        }
        
        swap(arr[left], arr[right]);
        reverseArrayRecursive(arr, left + 1, right - 1);
    }
    
    // Helper function to print array
    void printArray(const vector<int>& arr) {
        for (int num : arr) {
            cout << num << " ";
        }
        cout << endl;
    }
};

int main() {
    Solution sol;
    
    // Test Case 1
    vector<int> arr1 = {1, 2, 3, 4, 5};
    cout << "Original Array: ";
    sol.printArray(arr1);
    sol.reverseArray(arr1);
    cout << "Reversed Array: ";
    sol.printArray(arr1);
    
    // Test Case 2
    vector<int> arr2 = {10, 20, 30};
    cout << "\nOriginal Array: ";
    sol.printArray(arr2);
    sol.reverseArrayRecursive(arr2, 0, arr2.size() - 1);
    cout << "Reversed Array: ";
    sol.printArray(arr2);
    
    // Test Case 3: Single element
    vector<int> arr3 = {42};
    cout << "\nOriginal Array: ";
    sol.printArray(arr3);
    sol.reverseArray(arr3);
    cout << "Reversed Array: ";
    sol.printArray(arr3);
    
    // Test Case 4: Empty array
    vector<int> arr4 = {};
    cout << "\nOriginal Array: ";
    sol.printArray(arr4);
    sol.reverseArray(arr4);
    cout << "Reversed Array: ";
    sol.printArray(arr4);
    
    return 0;
}

/* 
Key Learnings:
1. Two-pointer technique is very efficient for array manipulation
2. In-place reversal saves space complexity
3. Always consider edge cases: empty array, single element
4. Recursion can be used but may cause stack overflow for large arrays

Alternative Approaches:
1. Using STL reverse() function: reverse(arr.begin(), arr.end())
2. Using extra space: Create new array and fill in reverse order

Interview Tips:
- Discuss time and space complexity
- Ask about constraints (array size, memory limitations)
- Consider edge cases
- Mention different approaches and trade-offs
*/
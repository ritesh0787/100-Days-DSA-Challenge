# 🤝 Contributing to 100 Days DSA Challenge

Thank you for your interest in contributing to this challenge! This guide will help you get started.

## 🚀 Getting Started

### Fork and Clone
```bash
# Fork this repository on GitHub
# Clone your forked repository
git clone https://github.com/YOUR-USERNAME/100-Days-DSA-Challenge.git
cd 100-Days-DSA-Challenge

# Add upstream remote
git remote add upstream https://github.com/ritesh0787/100-Days-DSA-Challenge.git
```

## 📝 How to Use This Repository

### 1. Daily Workflow

#### Start Your Day
1. Go to the respective day's folder (e.g., `Day-001`)
2. Copy the template from `Resources/DAY_TEMPLATE.md` if README doesn't exist
3. Read the problems from `TOPICS.md` for that day

#### During Problem Solving
1. Create solution files in the day's folder:
   - `problem1_reverse_array.cpp` (or .java, .py, etc.)
   - `problem2_find_max_min.cpp`
2. Write clean, well-commented code
3. Test your solution thoroughly

#### End Your Day
1. Update the day's README with:
   - Problem details
   - Your approach
   - Time and space complexity
   - Key learnings
2. Update `PROGRESS.md`:
   - Mark completed problems with ✅
   - Update statistics
3. Commit and push your changes:
```bash
git add .
git commit -m "Day X: Completed [problem names]"
git push origin main
```

### 2. File Naming Conventions

#### Solution Files
- Use lowercase with underscores
- Include problem number or name
- Examples:
  - `01_reverse_array.cpp`
  - `reverse_array.py`
  - `MaxMin.java`

#### Documentation
- Each day folder should have a `README.md`
- Use the template from `Resources/DAY_TEMPLATE.md`

### 3. Code Guidelines

#### General Principles
- Write clean, readable code
- Add comments for complex logic
- Follow language-specific conventions
- Include test cases in comments

#### Code Structure
```cpp
// Problem: [Problem Name]
// Platform: [LeetCode/GFG/etc.]
// Difficulty: Easy/Medium/Hard

// Approach: [Brief description]
// Time Complexity: O(?)
// Space Complexity: O(?)

#include <bits/stdc++.h>
using namespace std;

// Your solution here
class Solution {
public:
    void solve() {
        // Implementation
    }
};

// Test cases
int main() {
    Solution sol;
    // Test case 1
    // Test case 2
    return 0;
}
```

## 🎯 Types of Contributions

### 1. Adding Your Solutions
- Solve problems and add your solutions
- Document your approach and learnings
- Share alternative solutions

### 2. Improving Documentation
- Fix typos or unclear explanations
- Add more detailed explanations
- Improve formatting

### 3. Adding Resources
- Share helpful articles in `Resources/Articles/`
- Add video tutorial links in `Resources/Videos/`
- Create cheatsheets in `Resources/Cheatsheets/`

### 4. Adding New Problems
- Suggest additional problems in discussions
- Ensure problems are relevant and well-categorized
- Include problem links and difficulty levels

### 5. Creating Utilities
- Add helper scripts (e.g., progress tracker)
- Create visualization tools
- Build automation scripts

## 📊 Progress Tracking

### Update PROGRESS.md
After completing problems, update the progress tracker:

```markdown
- [x] Day 1: Reverse an array
- [x] Day 1: Find maximum and minimum element
```

### Update Statistics
Keep track of your progress in the statistics section:
- Total problems solved
- Difficulty breakdown
- Time spent

## 💡 Best Practices

### Commit Messages
Use clear and descriptive commit messages:
- ✅ Good: "Day 5: Completed Kadane's Algorithm and Subarray Sum"
- ❌ Bad: "Updated files"

### Format:
```
Day X: [Brief description]

- Problem 1: [Name]
- Problem 2: [Name]
- Additional notes if any
```

### Code Quality
- Test your code with multiple test cases
- Handle edge cases
- Optimize when possible
- Add complexity analysis

### Documentation
- Keep README files updated
- Document your thought process
- Share insights and patterns
- Note down mistakes and learnings

## 🌟 Community Guidelines

### Be Respectful
- Respect others' solutions and approaches
- Give constructive feedback
- Help fellow participants

### Share Knowledge
- Discuss different approaches
- Explain your solutions
- Ask questions when stuck

### Stay Consistent
- Try to code daily
- Update progress regularly
- Review and revise old problems

## 🔧 Tools and Setup

### Recommended IDEs
- VS Code
- IntelliJ IDEA
- PyCharm
- CLion

### Useful Extensions (VS Code)
- C/C++ Extension Pack
- Python Extension
- Java Extension Pack
- Code Runner
- GitLens

### Online Compilers
- [Replit](https://replit.com/)
- [OnlineGDB](https://www.onlinegdb.com/)
- [Compiler Explorer](https://godbolt.org/)

## 📞 Getting Help

### Stuck on a Problem?
1. Re-read the problem carefully
2. Check hints in the problem statement
3. Look at similar problems
4. Search for the pattern
5. Discuss in community forums

### Technical Issues?
- Open an issue on GitHub
- Check existing issues first
- Provide clear description and steps to reproduce

## 🎓 Learning Tips

### Before Starting
- Understand the problem completely
- Think about edge cases
- Consider multiple approaches

### While Coding
- Start with brute force
- Optimize step by step
- Test frequently

### After Solving
- Analyze time and space complexity
- Compare with other solutions
- Note down patterns
- Revisit after a few days

## 📜 Code of Conduct

### Our Pledge
We are committed to making participation in this challenge a harassment-free experience for everyone.

### Our Standards
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community

## 📞 Contact

- Create an issue for bugs or suggestions
- Start a discussion for questions
- Share your progress on social media with #100DaysDSA

## 🙏 Acknowledgments

Thank you to all contributors who help make this challenge better!

---

**Happy Coding!** 🚀💻

*Remember: Consistency is more important than perfection. Keep going!*
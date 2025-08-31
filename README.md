# 📘 DSA Practice (Python)

A collection of **Data Structures & Algorithms** problems solved in **Python**, organized by topic.  
This repo is meant for **learning, practicing**.

---

## 🚀 Covered Problems

### 🔹 Arrays
#### 1. Two Sum ([arrays/two_sum.py](arrays/two_sum.py))
**Problem:**  
Given an array of integers, return the indices of the two numbers such that they add up to a specific target.  

**Example:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1] # because nums[0] + nums[1] = 9



**Complexity:**  
- Time: `O(n)`  
- Space: `O(n)`  

---

#### 2. Kadane’s Algorithm ([arrays/kadane_algorithm.py](arrays/kadane_algorithm.py))
**Problem:**  
Find the contiguous subarray with the largest sum within a given array.  

**Example:**
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 # subarray [4,-1,2,1] has the largest sum



**Complexity:**  
- Time: `O(n)`  
- Space: `O(1)`  

---

### 🔹 Linked List
#### 1. Reverse a Linked List ([linked_list/reverse_linked_list.py](linked_list/reverse_linked_list.py))
**Problem:**  
Reverse a singly linked list and return the new head.  

**Example:**
Input: 1 -> 2 -> 3
Output: 3 -> 2 -> 1


**Complexity:**  
- Time: `O(n)`  
- Space: `O(1)`  

---

## 📂 Folder Structure
📦 dsa-practice
┣ 📂 arrays
┃ ┣ two_sum.py
┃ ┗ kadane_algorithm.py
┣ 📂 linked_list
┃ ┗ reverse_linked_list.py
┣ LICENSE
┗ README.md



## 🛠 How to Run
Clone the repo and run any script:

---bash
git clone https://github.com/ab12a/DSA-practice.git
cd DSA-practice

# Example: run Kadane’s Algorithm
python arrays/kadane_algorithm.py
📜 License
This repository is licensed under the Apache 2.0 License.


⭐ Contribute
This repo is mainly for practice, but feel free to:

Open issues if you spot improvements.

Submit pull requests with new DSA problems.

If you find this helpful, ⭐ the repo!



⚡ Done — copy everything above into a file named `README.md` at your repo root.  

Do you also want me to prepare a **`.gitignore` file** (Python standard) so your repo stays clean from cache files, `.pyc`, etc.?

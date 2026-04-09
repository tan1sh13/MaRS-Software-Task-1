#  MaRS Software Task – 1

##  Overview

This repository contains solutions to various problem levels including Bash scripting, filtering algorithms, coordinate transformations, and pathfinding logic. The tasks were designed to test both practical coding and conceptual understanding.

---

#  Learning Experience

Working on this task helped me:

* Understand **Bash scripting fundamentals** (conditions, loops, system checks)
* Learn how to use **Git and GitHub** effectively (branching, pushing, resolving conflicts)
* Apply **mathematical concepts** like coordinate transformations and averaging filters
* Improve problem-solving skills by breaking down complex problems into smaller steps

---

# 📐 Equations, Theorems & Concepts Used

###  1. Moving Average (Muchiko Filter)

Average of a window:

$$
\text{Mean} = \frac{\sum x_i}{n}
$$

---

###  2. Median Filter (Sanchiko Filter)

* Sort values in a window
* Take the middle value
   Helps remove noise and outliers

---

###  3. Coordinate Transformation (3D Rotation)

Rotation formulas:

**X-axis:**

$$
y' = y\cos\theta - z\sin\theta
$$

$$
z' = y\sin\theta + z\cos\theta
$$

**Y-axis:**

$$
x' = x\cos\theta + z\sin\theta
$$

$$
z' = -x\sin\theta + z\cos\theta
$$

**Z-axis:**

$$
x' = x\cos\theta - y\sin\theta
$$

$$
y' = x\sin\theta + y\cos\theta
$$

---

###  4. BFS (Breadth First Search)

* Used for shortest path in grid
* Explores level-by-level using a queue
* Guarantees shortest path in unweighted graphs

---

#  Approach

###  Bash Script (Rover System Check)

* Generated random battery value
* Checked threshold condition
* Verified network using `ping`
* Used exit conditions for failure cases

---

###  Filtering Problems

* Implemented sliding window technique
* Applied mean and median filters
* Combined both in hybrid filter for better smoothing

---

###  Coordinate Transformation

* Took user input dynamically
* Applied sequential rotation (X → Y → Z)
* Added translation to convert to world coordinates

---

### Pathfinding (BFS)

* Represented environment as grid
* Marked obstacles
* Used queue-based traversal to find shortest path

---

#  Challenges Faced

* Understanding **Git errors** like:

  * non-fast-forward push rejection
  * merge conflicts
  * authentication issues
* Converting **mathematical formulas into code**
* Debugging Bash syntax issues (spacing, conditions)
* Understanding **coordinate rotations in 3D space**

---

#  Resources Used

* Official documentation of Git
* GitHub guides
* Online tutorials for Bash scripting
* Mathematical references for coordinate transformations
* Problem-solving platforms and notes

---

#  Conclusion

This task helped me bridge the gap between:

* Theory and implementation
* Mathematics and programming
* Basic scripting and real-world problem solving

It significantly improved my confidence in handling both coding and debugging challenges.

---

#  Future Improvements

* Optimize BFS using A* algorithm
* Add logging system in Bash scripts
* Improve modularity of code
* Add visualizations for pathfinding

---


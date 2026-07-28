# Maximum Frequency Stack

**Difficulty:** Hard
**Topic:** Stack, Hash Map, Design

## Problem

Design a stack-like data structure that pushes elements normally, but
whose `pop()` removes and returns the **most frequent** element pushed
so far. If multiple elements are tied for the highest frequency, the
one **closest to the top of the stack** is removed and returned.

Implement the `FreqStack` class:
- `FreqStack()` — constructs an empty frequency stack.
- `void push(int val)` — pushes an integer `val` onto the top of the stack.
- `int pop()` — removes and returns the most frequent element in the stack (ties broken by proximity to the top).

## Approach

The solution tracks three pieces of state alongside the raw stack:

- **`stack`** — the elements in push order (last index = top of stack).
- **`freq`** — a hash map from value → current count of that value in the stack.
- **`maxi`** — the value currently holding the highest frequency (with ties resolved in favor of the value closer to the top).

**On `push`**, the value is appended to `stack` and its count in `freq`
is incremented. `maxi` is then updated to the new value whenever its
frequency is greater than *or equal to* the current `maxi`'s frequency
— using `>=` for the tie-break naturally favors the most recently
pushed value, satisfying the "closest to top" rule.

**On `pop`**, the frequency of `maxi` is decremented first (one
occurrence is about to leave the stack). A single pass is then made
over the stack to:
1. locate the index of the topmost occurrence of that value (to remove
   the correct instance rather than an earlier one), and
2. recompute what the new `maxi` should be once that occurrence is
   removed, again favoring the element closest to the top on ties.

The located index is then popped from `stack`, and the removed value
is returned.

## Complexity

- **Time complexity:** `O(n)` per `pop()` call, where `n` is the number of elements currently in the stack (the scan to find the removal index and recompute `maxi` is linear). `push()` is `O(1)`.
- **Space complexity:** `O(n)` — the stack itself plus the frequency map.

## Submission Performance (LeetCode)

- **Result:** Accepted — 23 / 23 test cases
- **Runtime:** 44 ms (faster than 22.28% of submissions)
- **Memory:** 8.0 MB (less than 81.52% of submissions)

class FreqStack:
    """
    A stack-like structure where pop() removes and returns the most
    frequent element pushed so far. If several elements share the
    highest frequency, the one closest to the top of the stack wins.
    """

    def __init__(self):
        self.stack = []   # stores values in push order (index 0 = bottom, last index = top)
        self.length = 0   # current number of elements in the stack
        self.freq = {}    # maps value -> how many times it currently appears in the stack
        self.maxi = 0      # value that currently has the highest frequency (tie -> closest to top)

    def push(self, val: int) -> None:
        self.stack.append(val)          # place val on top of the stack
        self.length = self.length + 1   # one more element in the stack

        # Update the frequency count for val
        if self.freq.get(val, -1) > 0:
            self.freq[val] = self.freq[val] + 1   # val already seen before -> increment
        else:
            self.freq[val] = 1                     # first time seeing val -> start at 1

        # Update maxi: if val's new frequency is at least as high as the
        # current maxi's frequency, val becomes the new maxi. Using "<="
        # (rather than "<") means that on a tie, the most recently pushed
        # value (val, which is now the top of the stack) wins -- this is
        # exactly the "closest to the top" tie-break rule required by the problem.
        if self.freq.get(self.maxi, -1) <= self.freq[val]:
            self.maxi = val

    def pop(self) -> int:
        # The element we are about to remove is the current maxi.
        # Decrement its frequency first, since one occurrence of it is
        # about to leave the stack.
        self.freq[self.maxi] = self.freq[self.maxi] - 1
        a = self.maxi   # value that will be returned

        # Single pass over the stack (front to back) that does two things at once:
        #   1) finds b, the index of the topmost occurrence of "a" in the
        #      stack (since we iterate in order, the last match overwrites
        #      earlier ones, so b ends up being the highest/most-recent index)
        #   2) recomputes what the new maxi should be, for after "a" is removed
        for i in range(self.length):
            if self.stack[i] == a:
                b = i   # remember index of the (so far) topmost occurrence of a

            # Candidate for new maxi: any element whose frequency is now >=
            # the current maxi's frequency. Using ">=" while scanning left to
            # right means later (higher/closer-to-top) elements overwrite
            # earlier ones on a tie, preserving the "closest to top" rule.
            # The last index is excluded here and handled separately below,
            # because it needs an extra check (stack[i] != a) to avoid
            # re-selecting the very occurrence that is being popped.
            if self.freq[self.stack[i]] >= self.freq[self.maxi] and i != self.length - 1:
                self.maxi = self.stack[i]
            elif i == self.length - 1 and self.stack[i] != a and self.freq[self.stack[i]] >= self.freq[self.maxi]:
                self.maxi = self.stack[i]

        # Remove the topmost occurrence of "a" (found at index b) from the stack
        self.stack.pop(b)
        self.length = self.length - 1
        return a

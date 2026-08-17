class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        # We do binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        m = len(A)
        n = len(B)

        # Number of elements that should be on the left side
        #
        # +1 makes the left side contain the extra element
        # when the total number of elements is odd.
        total_left = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:

            # Partition A
            partitionA = (left + right) // 2

            # Whatever elements we don't take from A,
            # we take from B.
            partitionB = total_left - partitionA

            # Elements immediately to the left/right
            # of partition A
            leftA = (
                A[partitionA - 1]
                if partitionA > 0
                else float("-inf")
            )

            rightA = (
                A[partitionA]
                if partitionA < m
                else float("inf")
            )

            # Elements immediately to the left/right
            # of partition B
            leftB = (
                B[partitionB - 1]
                if partitionB > 0
                else float("-inf")
            )

            rightB = (
                B[partitionB]
                if partitionB < n
                else float("inf")
            )

            # Check if the partition is correct
            if leftA <= rightB and leftB <= rightA:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return float(max(leftA, leftB))

                # Even number of elements
                return (
                    max(leftA, leftB) +
                    min(rightA, rightB)
                ) / 2

            # A's partition is too far RIGHT
            elif leftA > rightB:
                right = partitionA - 1

            # A's partition is too far LEFT
            else:
                left = partitionA + 1
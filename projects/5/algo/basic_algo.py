from collections import deque
from typing import Optional


def example():
    print("example")


def divmod_palindrome_number():
    def solution(x: int) -> bool:
        if x < 0:
            return False

        new = 0
        orig = x
        while x:
            x, d = divmod(x, 10)
            new = new * 10 + d
        return new == orig

    print(solution(123))
    print(solution(121))
    print(solution(-121))
    pass


def hash_contains_duplicate():
    def solution(nums: list[int]) -> bool:
        # new = []
        # for i in nums:
        #     if i in new:  # JS: Array.contains()
        #         return False
        #     else:
        #         new.append(i)
        # return True

        return len(nums) != len(set(nums))

    print(solution([1, 2, 3, 1]))
    print(solution([1, 2, 3, 4]))
    pass


def linked_list_remove_linked_list_elements():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def solution(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, next=head)
        cur = head
        prev = dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur.next = cur.next

        return dummy.next

    print(solution([1, 2, 6, 3, 4, 5, 6], 6))
    print(solution([7, 7, 7, 7], 7))
    pass


def bitwise_counting_bits():
    def solution(n: int) -> list[int]:
        ans = [0]
        for i in range(1, n):
            cur = 0
            while i:
                cur += i & 1
                i >>= 1
            ans.append(cur)
        return ans

    print(solution(2))
    print(solution(5))
    pass


def hash_unique_email_addresses():
    def solution(emails: list[str]) -> int:
        unique = set()
        for e in emails:
            name, dom = e.split('@')
            name = name.split("+")[0]
            name = name.replace('.', '')
            unique.add(f"{name}@{dom}")
        return len(unique)

    print(solution(["bogdan.1@mail.com", "bogdan1@mail.com", "bogdan1@mail.ru"]))
    pass


def sliding_window_maximum_awerage_subarray():
    def solution(nums: list[int], k: int) -> float:
        cur = sum(nums[:k])
        cur_max = cur
        for i in range(k, len(nums)):
            cur -= nums[i - k]
            cur += nums[i]
            cur_max = max(cur, cur_max)
        return cur_max / k

    print(solution([1, 12, -5, -6, 50, 3], 4))
    pass


def two_pointers_move_zeroes():
    def solution(nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)

    print(solution([0, 1, 0, 3, 12]))
    pass


def binary_search_valid_perfect_square():
    def solution(num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

    print(solution(16))
    print(solution(50))
    print(solution(1))
    pass


def divmod_add_digits():
    def solution(num: int) -> int:
        while num >= 10:
            cur = num
            new_num = 0
            while cur:
                cur, d = divmod(cur, 10)
                new_num += d
            num = new_num
        return num

    print(solution(38))
    print(solution(0))
    pass


def string_student_attendance_record():
    def solution(s: str) -> bool:
        l_cnt = 0
        a_cnt = 0
        for c in s:
            if c == "A":
                a_cnt += 1
                if a_cnt == 2:
                    return False
            if c == "L":
                l_cnt += 1
                if l_cnt > 2:
                    return False
            else:
                l_cnt = 0
        return True

    print(solution("PPALLP"))
    print(solution("PPALLL"))
    pass


def tree_binary_tree_postorder_traversal():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def solution(root: Optional[TreeNode]) -> list[int]:
        ans = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)

                ans.append(node.val)

        helper(root)
        return ans

    print([1, None, 2, 3])
    print([])
    pass


def stack_is_subsequence():
    def solution(s: str, t: str) -> bool:
        stack = list(s)[::-1]

        for c in t:
            if stack and stack[-1] == c:
                stack.pop()
        return len(stack) == 0

    print(solution('abc', "ahbgdc"))
    print(solution('axc', "ahbgdc"))
    pass


def tree_symmetric_tree():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def solution(root: Optional[TreeNode]) -> bool:
        q = deque([root])
        levels = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val if cur else None)
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

            if len(level) < 1:
                n = len(level)
                if level[:n // 2] != level[n // 2:][::-1]:
                    return False
        return True

    print(solution([1, 2, 2, 3, 4, 4, 3]))
    print(solution([]))
    pass


def divmod_plus_one():
    def solution(digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        return digits if not carry else [carry] + digits

    print(solution([1, 2, 3]))
    print(solution([4, 3, 2, 1]))
    pass


def sorting_meeting_rooms():
    def solution(intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

    print(solution([[0, 30], [45, 50]]))
    print(solution([[0, 30], [5, 10], [15, 20]]))
    print(solution([[0, 30], [5, 10], [15, 20]]))
    pass


def linked_list_middle_of_the_linked_list():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def solution(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    print(solution([1, 2, 3, 4, 5]))
    print(solution([3, 4, 5]))
    pass


def hash_check_if_n_and_its_double_exists():
    def solution(arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False

    print(solution([10, 2, 5, 3]))
    print(solution([7, 1, 14, 11]))
    pass


def dp_n_th_tribonacci_number():
    def solution(n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
        return dp[-1]

    print(solution(4))
    print(solution(25))
    pass


def binary_search_binary_search():
    def solution(nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    print(solution([-1, 0, 3, 5, 9, 12], 9))
    print(solution([-1, 0, 3, 5, 9, 12], 2))
    pass


def dp_pascale_triangle():
    def solution(num_rows: int) -> list[list[int]]:
        dp = [[1], [1, 1]]
        if num_rows < 3:
            return dp[:num_rows]
        for _ in range(num_rows - 2):
            next_row = [1]
            for i in range(1, len(dp[-1])):
                next_row.append(dp[-1][i] + dp[-1][i - 1])

            next_row += [1]
            dp.append(next_row)

        return dp

    print(solution(5))
    print(solution(1))
    pass


def bitwise_single_number():
    def solution(nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans

    print(solution([2, 2, 1]))
    print(solution([4, 1, 2, 1, 2]))
    pass


def binary_search_peak_index_in_a_mountain_array():
    def solution(arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                l = mid
            else:
                r = mid
        pass

    print(solution([0, 1, 0]))
    print(solution([0, 2, 1, 0]))
    pass


def two_pointers_valid_palindrome():
    def solution(arr: list[int]) -> int:
        pass

    print(solution([0, 1, 0]))
    print(solution([0, 2, 1, 0]))
    pass


if __name__ == "__main__":
    # асимптоматика
    # эвристика

    # divmod_palindrome_number()
    # hash_contains_duplicate()
    # linked_list_remove_linked_list_elements()
    # bitwise_counting_bits()
    # hash_unique_email_addresses()
    # sliding_window_maximum_awerage_subarray()
    # two_pointers_move_zeroes()
    # binary_search_valid_perfect_square()
    # divmod_add_digits()
    # string_student_attendance_record()
    # tree_binary_tree_postorder_traversal()
    # stack_is_subsequence()
    # tree_symmetric_tree()
    # divmod_plus_one()
    # sorting_meeting_rooms()
    # linked_list_middle_of_the_linked_list()
    # hash_check_if_n_and_its_double_exists()
    # dp_n_th_tribonacci_number()
    # binary_search_binary_search()
    # dp_pascale_triangle()
    # bitwise_single_number()
    # binary_search_peak_index_in_a_mountain_array()
    # two_pointers_valid_palindrome()
    pass

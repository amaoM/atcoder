# coding: utf-8

import array

def compute(nums, N, K):
    left = 0
    p = 1
    ans = 0
    l = 0

    for right in range(N):
        p *= nums[right]
        l += 1

        if p > K:
            p //= nums[left]
            left += 1
            l -= 1

        if l > ans:
            ans = l

    return ans

if __name__ == '__main__':
    N, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    if 0 in nums:
        print(N)
    else:
        print(compute(nums, N, K))

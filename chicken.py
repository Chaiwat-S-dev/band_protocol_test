"""
Problem 2: Superman's Chicken Rescue
    Description:
    In a one-dimensional world, Superman needs to protect chickens from a heavy rainstorm using a roof of limited
    length. Given the positions of chickens and the length of the roof Superman can carry, determine the maximum
    number of chickens Superman can protect.
Input:
    The input consists of two integers n and k (1 <= n,k <= 1,000,000), where n represents the number of chickens
    and k denotes the length of the roof Superman can carry. The next line contains n integers (1 <= x <=
    1,000,000,000) representing the positions of the chickens on the one-dimensional axis.
Output:
    Output a single integer, denoting the maximum number of chickens Superman can protect with the given roof
    length.
Note:
    - Superman can position the roof starting at any point on the axis.
    - The roof can cover chickens whose positions are within k units from its starting point. [p, p+k)
    - It's not required to cover all chickens, but to maximize the number of chickens protected.
    - It's guaranteed that the given positions of the chickens will be sorted from lowest to highest.
"""


def main(num_chicken: int=0, roof_length: int=0, chickens: list=[int]) -> int:
    # keep position chick that roof have cover for re-check.
    safe_chicken = {
        "position": 0,
        "cover_chicken": 0
    }
    if num_chicken == 0:
        return 0
    for p in range(len(chickens)):
        length_safe = chickens[p] + roof_length - 1
        for idx in range(p, len(chickens)):
            if chickens[idx] <= length_safe:
                if (idx - p >= safe_chicken["cover_chicken"]):
                    safe_chicken.update({
                        "position": p,
                        "cover_chicken": idx - p + 1
                    })
            else:
                break
    return safe_chicken["cover_chicken"]

if __name__ == '__main__':
    '''
    * Fragment for input and random test.
    print("enter: num chicken (int): ")
    num_chicken = int(input())
    print(f"enter: range of the roof (int): ")
    roof_length = int(input())
    from random import randrange
    chickens = [randrange(0, num_chicken) for _ in range(num_chicken)]
    chickens.sort()
    print(f'{chickens=}')
    print(main(num_chicken, roof_length, chickens))
    '''
    print(main(3, 1, [4, 6, 18]))
    print(main(10, 20, [4, 6, 18, 31, 35, 43, 47, 51, 54, 81]))
    print(main(6, 10, [1, 11, 30, 34, 35, 37]))
    print(main(5, 5, [2, 5, 10, 12, 15]))
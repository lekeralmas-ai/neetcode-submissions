class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible_flowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left  = flowerbed[i-1] if i > 0 else 0
                right = flowerbed[i+1] if i < len(flowerbed)-1 else 0
                if left == 0 and right == 0:
                    possible_flowers += 1
                    flowerbed[i] = 1
        return possible_flowers >= n
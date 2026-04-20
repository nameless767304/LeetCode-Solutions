class Solution(object):
    def maxDistance(self, colors):
        colors_set = list()
        colors_length_set = list()

        ans_1, ans_2 = 0, 0

        for color in colors:
            if not colors_set:
                colors_set.append(color)
                colors_length_set.append(1)
            else:
                if color == colors_set[-1]:
                    colors_length_set.append(colors_length_set.pop(-1) + 1)
                else:
                    colors_set.append(color)
                    colors_length_set.append(1)

        # case1
        for color in range(len(colors_set)):
            if colors_set[color] != colors_set[-1]:
                ans_1 = sum(colors_length_set[color:]) - 1
                break

        # case2
        for color in range(len(colors_set) - 1, 0, -1):
            if colors_set[color] != colors_set[0]:
                ans_2 = sum(colors_length_set[:color + 1]) - 1
                break

        return max(ans_1, ans_2)

        

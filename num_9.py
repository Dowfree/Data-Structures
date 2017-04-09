from BinaryTree import LinkedBinaryTree
from BinaryTree import LinkedBinaryTreeNode


class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, data=[]):
        self.root = None
        self.length = 0
        for item in data:
            self.insert(item)

    def insert(self, item):
        if self.root is None:
            self.root = LinkedBinaryTreeNode(item)
            self.length += 1
            return

        found, node = self.find(item)

        if item <= node.item:
            node.left_child = LinkedBinaryTreeNode(item)
        else:
            node.right_child = LinkedBinaryTreeNode(item)

        self.length += 1

    def find(self, item):
        if self.root is None:
            return False, None

        node = self.root

        while True:
            finished = True
            while item > node.item and node.right_child:
                node = node.right_child
                finished = False
            while item <= node.item and node.left_child:
                node = node.left_child
                finished = False
            if finished:
                break

        if node == item:
            return True, node
        else:
            return False, node

    def find_item(self, item, parent=None):
        if parent==None:
            if self.root:
                parent=self.root
                if parent.item == item:
                    return True, None, -1, parent

                return self.find_item(item,parent)

        if item <= parent.item and parent.left_child:
            if parent.left_child.item == item:
                return True, 0, parent.item, parent.left_child.item
            else:
                res = self.find_item(item, parent.left_child)
                if res[0]:
                    return res

        elif item > parent.item and parent.right_child:
            if parent.right_child.item == item:
                return True, 1, parent.item, parent.right_child.item
            else:
                res = self.find_item(item, parent.right_child)
                if res[0]:
                    return res
        return False, None, -1, None

    def find_parent(self, item):
        result = [item]
        while item != self.root.item:
            result.append(self.find_item(item)[2])
            item = self.find_item(item)[2]
        return result

    def find_address(self, item):
        return self._find(self.root, item)

    def _find(self, node, item):

        if node:
            if node.item == item:
                return True, '', node

            res = self._find(node.left_child, item)
            if res[0]:
                return True, '0' + res[1], res[2]

            res = self._find(node.right_child, item)
            if res[0]:
                return True, '1' + res[1], res[2]

        return False, '', None

a = [320, 342, 595, 605, 676, 349, 467, 654, 579, 347, 309, 77, 601, 560, 607, 437, 505, 332, 43, 394, 552, 156, 594, 523, 682, 535, 173, 635, 421, 490, 108, 112, 208, 758, 178, 203, 312, 740, 166, 720, 383, 117, 432, 79, 367, 624, 599, 431, 606, 29, 90, 262, 128, 439, 702, 637, 189, 541, 671, 198, 148, 534, 99, 209, 393, 591, 14, 502, 675, 645, 777, 642, 42, 25, 659, 271, 158, 764, 506, 757, 2, 452, 456, 72, 655, 322, 27, 263, 187, 242, 182, 296, 705, 498, 658, 338, 408, 486, 440, 400, 172, 327, 102, 334, 667, 268, 600, 118, 636, 562, 169, 19, 750, 58, 360, 215, 98, 572, 743, 258, 62, 612, 38, 282, 325, 194, 132, 729, 358, 3, 438, 458, 351, 573, 551, 107, 171, 278, 581, 397, 769, 162, 634, 139, 240, 210, 425, 522, 492, 292, 580, 362, 227, 472, 35, 288, 12, 272, 377, 661, 370, 31, 517, 91, 126, 138, 609, 167, 365, 32, 232, 379, 761, 176, 531, 380, 65, 134, 623, 751, 120, 197, 235, 10, 779, 4, 330, 679, 719, 741, 135, 378, 716, 604, 15, 228, 436, 497, 276, 357, 460, 587, 625, 571, 709, 445, 588, 476, 55, 630, 686, 473, 696, 160, 343, 414, 147, 747, 728, 539, 760, 371, 60, 387, 753, 496, 76, 319, 603, 401, 69, 742, 290, 611, 202, 701, 152, 181, 355, 516, 712, 735, 413, 602, 457, 514, 455, 216, 144, 451, 481, 318, 110, 617, 718, 409, 404, 24, 583, 736, 221, 346, 372, 503, 406, 26, 771, 150, 137, 547, 649, 706, 214, 364, 616, 175, 234, 106, 684, 598, 470, 629, 301, 710, 521, 399, 734, 403, 584, 291, 195, 446, 524, 765, 664, 608, 550, 18, 463, 161, 13, 407, 224, 644, 582, 543, 668, 294, 567, 184, 226, 70, 767, 57, 239, 261, 75, 665, 435, 650, 448, 746, 94, 313, 651, 127, 714, 39, 331, 180, 269, 518, 402, 255, 511, 192, 532, 424, 694, 739, 619, 529, 698, 615, 569, 314, 538, 653, 183, 639, 647, 775, 243, 483, 678, 47, 140, 485, 557, 685, 16, 568, 419, 159, 626, 133, 596, 281, 699, 422, 103, 86, 307, 559, 265, 199, 738, 260, 477, 691, 643, 71, 640, 238, 442, 762, 63, 315, 703, 341, 542, 298, 700, 87, 119, 478, 564, 222, 384, 731, 392, 253, 247, 763, 179, 96, 450, 80, 666, 755, 489, 536, 722, 415, 51, 566, 669, 545, 631, 381, 73, 683, 501, 177, 471, 674, 475, 125, 113, 8, 366, 354, 217, 628, 283, 78, 509, 443, 548, 465, 657, 205, 348, 673, 82, 513, 423, 656, 30, 500, 279, 749, 484, 744, 704, 275, 433, 83, 92, 143, 146, 527, 153, 105, 201, 768, 6, 681, 537, 130, 211, 622, 732, 389, 585, 317, 780, 21, 575, 335, 293, 546, 44, 149, 577, 297, 648, 45, 116, 267, 352, 597, 461, 337, 303, 670, 373, 430, 33, 328]
b = BinarySearchTree(a)
c = [(222, 681), (25, 91), (551, 484), (473, 199), (159, 247), (743, 180), (415, 354), (503, 211), (379, 87), (2, 4), (671, 471), (106, 484), (604, 579), (431, 372), (582, 704), (130, 700), (87, 445), (226, 486), (765, 424), (503, 535), (357, 496), (314, 327), (591, 6), (675, 775), (656, 699), (691, 683), (80, 442), (750, 617), (118, 734), (209, 57), (629, 239), (73, 358), (58, 372), (746, 279), (575, 765), (599, 351), (314, 415), (636, 227), (130, 505), (545, 291), (38, 744), (743, 666), (600, 341), (291, 671), (265, 349), (560, 296), (465, 51), (682, 235), (536, 224), (543, 317), (450, 643), (371, 103), (536, 355), (383, 647), (615, 348), (751, 4), (440, 271), (404, 192), (75, 234), (639, 602), (167, 523), (365, 557), (673, 628), (91, 182), (694, 276), (179, 403), (176, 636), (402, 738), (435, 298), (91, 38), (201, 278), (539, 8), (303, 559), (438, 751), (682, 666), (96, 198), (227, 702), (779, 679), (149, 42), (35, 779), (125, 127), (542, 243), (478, 414), (521, 661), (451, 603), (665, 657), (146, 644), (183, 709), (32, 118), (490, 150), (331, 179), (232, 584), (676, 535), (661, 771), (127, 535), (596, 686), (63, 98), (203, 442), (80, 767), (117, 566)]
ancestor, address_len = [], []

for i in a:    # 找所有地址的长度
    address_len.append(len(b.find_address(i)[1]))

for i in range(16):  # 找长度中的众数，即为最宽层数
    print((i, address_len.count(i)))

for i in c:  # 遍历第一个元素的祖先，对第二个元素往上开始找祖先，当出现在第一个元素的祖先列中，即为二者的第一个共同祖先。
    a1 = b.find_parent(i[0])
    a2 = i[1]
    while a2 not in a1:
        a2 = b.find_item(a2)[2]
    ancestor.append(a2)
answer = ((11, 77), ancestor)
print(answer)

from BinaryTree import LinkedBinaryTree

a = [(507, 1, 168), (357, 0, 718), (650, 1, 281), (517, 1, 704), (402, 1, 700), (683, 0, 707), (711, 1, 708), (770, 1, 227), (165, 1, 601), (24, 0, 224), (630, 1, 120), (426, 1, 369), (696, 0, 668), (429, 0, 121), (628, 0, 2), (235, 0, 450), (307, 1, 606), (775, 1, 442), (478, 0, 715), (408, 0, 447), (641, 0, 445), (574, 1, 338), (134, 0, 486), (708, 1, 597), (249, 1, 470), (555, 0, 522), (16, 1, 495), (103, 0, 259), (750, 1, 682), (140, 1, 92), (140, 0, 182), (503, 0, 219), (649, 1, 719), (522, 0, 615), (84, 1, 781), (322, 1, 40), (233, 0, 175), (750, 0, 327), (82, 1, 732), (578, 0, 278), (81, 0, 624), (288, 0, 694), (296, 0, 402), (80, 0, 545), (114, 1, 595), (35, 0, 725), (317, 1, 111), (514, 1, 151), (425, 1, 550), (255, 1, 564), (665, 1, 333), (157, 0, 75), (284, 1, 750), (553, 0, 765), (683, 1, 431), (605, 0, 412), (430, 0, 419), (145, 1, 544), (175, 1, 190), (714, 1, 734), (495, 0, 604), (775, 0, 557), (725, 0, 546), (511, 1, 506), (349, 1, 509), (570, 1, 500), (222, 0, 638), (653, 0, 405), (766, 0, 128), (239, 0, 305), (261, 0, 196), (71, 1, 724), (391, 0, 223), (37, 1, 574), (560, 1, 511), (411, 0, 727), (500, 0, 261), (480, 0, 373), (725, 1, 488), (536, 1, 530), (529, 1, 671), (279, 0, 282), (458, 1, 582), (55, 0, 166), (24, 1, 134), (660, 1, 199), (509, 0, 792), (765, 1, 408), (721, 1, 296), (25, 0, 723), (499, 0, 203), (159, 0, 752), (218, 0, 759), (480, 1, 640), (694, 0, 64), (456, 0, 71), (306, 1, 747), (543, 0, 687), (343, 0, 148), (195, 0, 556), (310, 1, 456), (734, 0, 602), (433, 0, 632), (707, 0, 267), (251, 1, 316), (441, 1, 512), (64, 1, 542), (127, 1, 348), (681, 0, 760), (55, 1, 519), (2, 1, 527), (453, 1, 739), (204, 1, 754), (617, 0, 343), (625, 1, 137), (278, 1, 252), (340, 1, 324), (35, 1, 68), (656, 1, 3), (360, 1, 576), (660, 0, 517), (38, 1, 370), (545, 1, 55), (475, 1, 441), (701, 1, 63), (38, 0, 762), (152, 1, 706), (697, 0, 371), (130, 0, 686), (152, 0, 284), (233, 1, 406), (594, 0, 756), (560, 0, 665), (455, 0, 636), (70, 1, 532), (188, 1, 195), (706, 0, 444), (159, 1, 81), (519, 1, 66), (282, 1, 649), (281, 1, 193), (332, 0, 605), (737, 0, 685), (542, 0, 791), (559, 1, 189), (459, 0, 14), (608, 0, 540), (504, 1, 255), (241, 1, 37), (617, 1, 19), (271, 0, 535), (495, 1, 696), (386, 1, 22), (564, 1, 152), (130, 1, 1), (375, 1, 314), (752, 0, 266), (163, 0, 117), (211, 0, 210), (535, 1, 626), (756, 0, 587), (526, 1, 459), (762, 0, 183), (737, 1, 643), (353, 0, 711), (246, 0, 200), (670, 1, 323), (723, 1, 473), (405, 1, 672), (83, 1, 443), (504, 0, 407), (390, 1, 45), (615, 0, 186), (40, 0, 104), (327, 1, 688), (302, 0, 326), (290, 1, 287), (139, 1, 611), (668, 1, 571), (203, 1, 533), (199, 1, 100), (94, 1, 460), (526, 0, 729), (353, 1, 363), (731, 0, 285), (536, 0, 228), (765, 0, 202), (724, 1, 36), (407, 1, 463), (317, 0, 553), (302, 1, 778), (615, 1, 264), (439, 0, 61), (467, 0, 216), (71, 0, 234), (781, 1, 620), (276, 1, 735), (113, 1, 616), (203, 0, 472), (316, 1, 543), (687, 0, 637), (32, 1, 129), (335, 0, 409), (251, 0, 514), (28, 0, 242), (222, 1, 145), (670, 0, 294), (605, 1, 86), (444, 0, 639), (786, 0, 235), (686, 1, 491), (182, 1, 742), (399, 1, 133), (543, 1, 634), (279, 1, 623), (315, 1, 480), (149, 0, 768), (183, 0, 307), (52, 1, 158), (358, 0, 404), (326, 0, 135), (2, 0, 458), (639, 1, 243), (103, 1, 315), (14, 0, 478), (143, 1, 140), (688, 0, 693), (433, 1, 660), (196, 0, 690), (627, 0, 515), (290, 0, 82), (407, 0, 433), (532, 1, 714), (483, 1, 761), (218, 1, 485), (234, 1, 262), (578, 1, 301), (770, 0, 774), (622, 1, 332), (645, 1, 334), (762, 1, 652), (75, 0, 479), (505, 1, 411), (693, 1, 424), (763, 1, 709), (408, 1, 114), (431, 0, 513), (693, 0, 108), (685, 0, 385), (757, 0, 360), (757, 1, 164), (697, 1, 656), (786, 1, 502), (288, 1, 695), (607, 1, 187), (453, 0, 204), (753, 1, 498), (511, 0, 510), (215, 0, 677), (446, 0, 753), (570, 0, 302), (522, 1, 374), (687, 1, 763), (143, 0, 731), (270, 1, 664), (334, 1, 340), (316, 0, 214), (287, 0, 720), (792, 0, 341), (224, 1, 83), (229, 0, 784), (759, 1, 21), (707, 1, 239), (94, 0, 403), (262, 1, 366), (224, 0, 594), (62, 0, 537), (6, 1, 310), (281, 0, 746), (87, 0, 375), (259, 1, 139), (215, 1, 780), (69, 1, 653), (252, 1, 60), (430, 1, 529), (189, 0, 629), (527, 0, 290), (378, 0, 312), (14, 1, 125), (308, 1, 645), (766, 1, 62), (187, 1, 429), (80, 1, 570), (37, 0, 386), (473, 1, 361), (607, 0, 551), (204, 0, 449), (133, 1, 578), (715, 0, 681), (520, 1, 171), (729, 0, 38), (461, 1, 232), (486, 1, 469), (113, 0, 628), (99, 1, 90), (553, 1, 276), (283, 0, 701), (769, 1, 161), (286, 0, 99), (17, 1, 610), (88, 0, 32), (576, 0, 766), (68, 1, 269), (517, 0, 6), (286, 1, 683), (739, 0, 84), (174, 0, 46), (310, 0, 770), (307, 0, 487), (148, 0, 625), (609, 0, 641), (147, 1, 12), (695, 1, 430), (187, 0, 588), (100, 0, 378), (550, 1, 149), (153, 0, 28), (641, 1, 586), (711, 0, 384), (148, 1, 757), (618, 1, 437), (-1, None, 504), (387, 0, 217), (724, 0, 661), (704, 1, 16), (230, 1, 179), (527, 1, 560), (473, 0, 357), (90, 1, 237), (735, 1, 390), (165, 0, 591), (624, 0, 427), (108, 1, 5), (137, 0, 43), (652, 0, 159), (16, 0, 627), (650, 0, 251), (721, 0, 387), (285, 0, 249), (111, 0, 349), (120, 0, 181), (70, 0, 188), (128, 1, 15), (409, 1, 270), (181, 1, 607), (627, 1, 67), (438, 1, 105), (645, 0, 142), (241, 0, 215), (266, 1, 435), (546, 1, 453), (498, 1, 352), (781, 0, 524), (729, 1, 35), (500, 1, 362), (402, 0, 271), (181, 0, 392), (761, 1, 609), (682, 0, 250), (449, 1, 528), (234, 0, 206), (509, 1, 667), (447, 1, 717), (746, 1, 499), (643, 1, 17), (625, 0, 507), (104, 0, 218), (756, 1, 254), (214, 1, 95), (99, 0, 79), (784, 1, 87), (704, 0, 393), (246, 1, 156), (133, 0, 52), (392, 1, 157), (386, 0, 279), (301, 1, 769), (361, 0, 57), (166, 1, 775), (425, 0, 697), (723, 0, 247), (739, 1, 622), (77, 0, 263), (462, 1, 501), (734, 1, 88), (461, 0, 490), (77, 1, 764), (667, 0, 101), (636, 0, 225), (166, 0, 167), (714, 0, 633), (149, 1, 618), (227, 0, 106), (285, 1, 446), (561, 1, 621), (608, 1, 581), (195, 1, 306), (390, 0, 283), (446, 1, 308), (36, 0, 505), (301, 0, 536), (157, 1, 475), (760, 0, 80), (28, 1, 147), (460, 1, 30), (385, 0, 561), (326, 1, 77), (40, 1, 335), (19, 0, 391), (532, 0, 503), (25, 1, 786), (346, 0, 613), (250, 1, 425), (87, 1, 288), (380, 1, 554), (478, 1, 229), (582, 0, 772), (506, 1, 127), (604, 1, 230), (784, 0, 461), (81, 1, 399), (391, 1, 70), (374, 0, 291), (284, 0, 737), (708, 0, 670), (95, 0, 457), (512, 0, 18), (505, 0, 130), (163, 1, 69), (68, 0, 322), (120, 1, 113), (175, 0, 755), (760, 1, 222), (529, 0, 286), (352, 1, 358), (207, 0, 559), (287, 1, 165), (611, 1, 96), (412, 0, 169), (459, 1, 483), (588, 1, 534), (639, 0, 782), (463, 1, 650), (563, 0, 174), (488, 0, 58), (117, 0, 631), (499, 1, 233), (631, 0, 648), (393, 1, 555), (387, 1, 426), (681, 1, 241), (656, 0, 33), (677, 1, 178), (588, 0, 692), (393, 0, 721), (183, 1, 608), (557, 1, 65), (609, 1, 467), (630, 0, 143), (483, 0, 669), (628, 1, 617), (392, 0, 462), (694, 1, 455), (202, 0, 508), (652, 1, 211), (229, 1, 103), (763, 0, 94), (315, 0, 163), (92, 0, 448), (174, 1, 265), (715, 1, 630), (188, 0, 153), (127, 0, 563), (259, 0, 346), (182, 0, 439), (424, 1, 716), (435, 1, 438), (442, 0, 246), (199, 0, 24), (375, 0, 207), (441, 0, 520), (22, 1, 434), (456, 1, 599), (731, 1, 317), (334, 0, 367), (458, 0, 11), (633, 1, 380), (255, 0, 526), (682, 1, 353), (695, 0, 25)]
b = []
for i in a:
    if i[0] == -1:
        b.append((1, i[2]))
        a.remove(i)

# 把输入形式转化成二叉树的输入形式，即找到每个元素的位置
while a:
    for i in a:
        for j in b:
            if i[0] == j[1]:
                b.append((2*j[0]+i[1], i[2]))
                a.remove(i)
b.sort()
bt = LinkedBinaryTree(nodes=b)
res = []
d = [742, 71, 352, 524, 450, 217, 269, 597, 246, 380, 649, 784, 731, 70, 285, 503, 296, 704, 77, 515, 429, 174, 601, 520, 79, 534, 55, 597, 507, 483, 704, 781, 582, 532, 17, 65, 449, 667, 693, 333, 621, 503, 715, 727, 341, 316, 70, 425, 223, 392, 210, 735, 88, 335, 343, 467, 510, 166, 760, 288, 735, 70, 143, 737, 772, 393, 706, 380, 408, 362, 770, 243, 687, 21, 128, 335, 249, 100, 667, 316, 94, 145, 276, 435, 622, 444, 786, 405, 677, 64, 149, 62, 30, 426, 672, 766, 105, 517, 694, 369]
for i in d:
    res.append(bt.find(i)[1])
print(res)



import hashlib

L1 = [8184, 6142, 5299, 5084, 459, 7072, 9702, 7469, 2543, 3581, 3740, 7167, 6507, 1981, 2744, 5409, 1787, 4733, 9578,
      2733, 4165, 7558, 6436, 4160, 7676, 9229, 6920, 1234, 2885, 3663, 5195, 2559, 1751, 6325, 8220, 4555, 8155, 6889,
      6601, 4054, 8533, 2931, 5566, 7461, 3256, 2272, 4314, 2991, 8327, 4176, 7090, 3258, 2275, 8283, 4477, 579, 6428,
      8467, 5901, 4178, 4223, 1024, 4527, 652, 7401, 4154, 2446, 3694, 1065, 2054, 4274, 1776, 4479, 7731, 8267, 2055,
      7819, 6045, 514, 1195, 2329, 250, 6734, 9488, 5395, 8900, 4757, 6573, 1041, 2095, 6824, 7540, 9672, 6463, 2892,
      6835, 8108, 9264, 7746, 7420, 966, 5495, 5442, 6882, 633, 8802, 8959, 644, 9947, 8668, 8043, 5860, 6107, 7847,
      5584, 3435, 8524, 6481, 5736, 7345, 6572, 7147, 6847, 8434, 5944, 7195, 2808, 4813, 8843, 2488, 1321, 1546, 6330,
      1962, 5828, 7538, 8396, 1430, 7190, 7514, 2713, 6770, 6497, 502, 3988, 6985, 4633, 3111, 2056, 639, 8087, 1742,
      4618, 334, 6113, 3254, 3396, 8466, 7837, 4839, 3576, 3923, 8770, 9436, 3925, 9922, 462, 623, 314, 5409, 2372,
      2941, 6649, 1337, 1424, 7875, 3737, 9532, 3426, 986, 2458, 2876, 1644, 1338, 9847, 2256, 7818, 4630, 4168, 7528,
      6400, 5625, 4283, 1918, 2484, 2999, 7347, 2264, 7233, 4225]

L2 = [5172, 234, 7804, 5519, 2926, 1574, 106, 1290, 9451, 1954, 1457, 5578, 5218, 2820, 352, 3794, 9370, 379, 4257,
      3977, 24, 2265, 668, 3390, 6891, 9664, 6454, 7537, 9447, 5398, 2331, 4446, 8643, 5568, 2184, 4553, 5398, 2075,
      2531, 9207, 312, 1345, 4868, 3360, 5310, 3253, 7055, 4598, 1698, 4684, 2291, 6030, 2446, 4867, 852, 4485, 4617,
      4247, 5553, 9845, 464, 6880, 5583, 5699, 5248, 4849, 1128, 7347, 930, 1195, 3683, 7928, 2421, 5970, 6252, 4304, 4,
      7040, 2135, 5343, 5910, 1753, 4221, 9697, 8115, 1254, 9496, 8631, 5065, 8029, 4224, 5358, 1694, 9526, 8230, 652,
      9952, 760, 244, 8698, 3043, 4182, 4259, 2282, 8125, 4060, 350, 7802, 5096, 3159, 5981, 181, 4530, 6542, 1724,
      7482, 1305, 7212, 7634, 6052, 2057, 8628, 8473, 3588, 4607, 641, 1640, 5564, 7164, 3884, 1883, 1373, 6971, 6080,
      5051, 2579, 9067, 7563, 8557, 6612, 1901, 3873, 8467, 8018, 5685, 1410, 1727, 5685, 2631, 766, 9068, 7211, 6428,
      8917, 2878, 3203, 1720, 1415, 5700, 7097, 2724, 6265, 5288, 339, 6811, 3682, 530, 741, 5895, 3998, 8781, 51, 1592,
      9877, 8140, 4184, 4731, 7278, 5384, 6021, 6760, 5622, 4464, 4744, 8521, 8454, 5562, 2260, 5995, 6763, 7278, 6845,
      1984, 6678, 2506, 8815, 6222, 2748, 6401, 2171]


def L1_sort(L):
    """ 第一位任務：
        將 L1 進行升序排序，排序演算法不限，唯禁止使用內建或第三方函式庫的 sort
    """
    for i in range(len(L)-1):
        for k in range(len(L)-1-i):
            if L[k] > L[k+1]:
                temp = L[k]
                L[k] = L[k+1]
                L[k+1] = temp

    # for i in range(len(L)):
        # print(L[i])

    return L


def L2_sort(L):
    """ 第二位任務：
        將 L2 進行升序排序，排序演算法不限，唯禁止使用內建或第三方函式庫的 sort
    """

    return L


def list_processing(L1, L2):
    """ 第三位任務：
        0. 先設定一個長度為 512-bit 的字串 S，所有 bit 皆為 0
        1. 將 L1’ 與 L2’ 做完交集得到 L’
        2. 將 L’ 裡面的每個數字 x 丟到 sha256 得到 sha256(x) (這邊請直接將 int 轉為 str 去做 hash)
        3. 取每個 sha256(x) 的最後 9-bit 轉成數字 y (範圍是 0~511) (請將 hash 的結果轉為 binary 再取最後 9-bit)
        4. 將 S 內的第 y 個 bit 設為 1 (每個 y 都要做喔)
    """


def binary_tree(L):
    """ 第四位任務：
        將 L1’ 與 L2’ 交集後的結果建成 binary tree(盡可能平衡) 並輸出
    """
    pass


if __name__ == "__main__":
    """ main program here """
# L1_sort(L1)

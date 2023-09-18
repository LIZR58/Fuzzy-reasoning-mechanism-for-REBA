import numpy as np
from CM_REBA import fuzzy_operator

class CMTableScore:
    def __init__(self, neck_membership, trunk_membership, leg_membership, upper_arm_membership, lower_arm_membership):
        self.neck_membership = neck_membership
        self.trunk_membership = trunk_membership
        self.leg_membership = leg_membership
        self.upper_arm_membership = upper_arm_membership
        self.lower_arm_membership = lower_arm_membership



    def Table_A_membership(self):
        # 1,2,3
        neck = self.neck_membership
        # 1,2,3,4,5
        trunk = self.trunk_membership
        # 1,2,3,4
        leg = self.leg_membership

        table_A = np.array([
            [[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [3, 5, 6, 7], [4, 6, 7, 8]],
            [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
            [[3, 3, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 9]]
        ])

        # 定义空数组存储隶属度
        membership_1_set = []
        membership_2_set = []
        membership_3_set = []
        membership_4_set = []
        membership_5_set = []
        membership_6_set = []
        membership_7_set = []
        membership_8_set = []
        membership_9_set = []

        # 通过遍历和append函数存储隶属度，求Einstein积
        # neck
        for i in range(3):
            # trunk
            for j in range(5):
                # leg
                for k in range(4):
                    a = table_A[i,j,k]
                    # 对应的隶属度（交集，乘积t算子）
                    m = neck[i]*trunk[j]*leg[k]
                    if a == 1:
                        membership_1_set.append(m)
                    elif a == 2:
                        membership_2_set.append(m)
                    elif a == 3:
                        membership_3_set.append(m)
                    elif a == 4:
                        membership_4_set.append(m)
                    elif a == 5:
                        membership_5_set.append(m)
                    elif a == 6:
                        membership_6_set.append(m)
                    elif a == 7:
                        membership_7_set.append(m)
                    elif a == 8:
                        membership_8_set.append(m)
                    elif a == 9:
                        membership_9_set.append(m)

        membership_1_A = fuzzy_operator.einstein_sum_aggregation(membership_1_set)
        membership_2_A = fuzzy_operator.einstein_sum_aggregation(membership_2_set)
        membership_3_A = fuzzy_operator.einstein_sum_aggregation(membership_3_set)
        membership_4_A = fuzzy_operator.einstein_sum_aggregation(membership_4_set)
        membership_5_A = fuzzy_operator.einstein_sum_aggregation(membership_5_set)
        membership_6_A = fuzzy_operator.einstein_sum_aggregation(membership_6_set)
        membership_7_A = fuzzy_operator.einstein_sum_aggregation(membership_7_set)
        membership_8_A = fuzzy_operator.einstein_sum_aggregation(membership_8_set)
        membership_9_A = fuzzy_operator.einstein_sum_aggregation(membership_9_set)

        membership_A = [membership_1_A, membership_2_A, membership_3_A, membership_4_A, membership_5_A, membership_6_A, membership_7_A, membership_8_A, membership_9_A]
        normalized_membership_A = fuzzy_operator.normalize_membership(membership_A)


        return normalized_membership_A


    def Table_B_membership(self):
        # 1,2,3,4,5,6
        upper_arm = self.upper_arm_membership
        # 1,2
        lower_arm = self.lower_arm_membership
        # 假定wrist为1分
        wrist = 1

        # 定义空数组存储隶属度
        # Table B 评分是1-2
        membership_1_set = []
        membership_2_set = []
        membership_3_set = []
        membership_4_set = []
        membership_5_set = []
        membership_6_set = []
        membership_7_set = []
        membership_8_set = []
        #membership_9_set = []

        table_B = np.array([
            [[1, 2], [1, 2]],
            [[1, 2], [2, 3]],
            [[3, 4], [4, 5]],
            [[4, 5], [5, 6]],
            [[6, 7], [7, 8]],
            [[7, 8], [8, 9]],
        ])

        # upper_arm
        for i in range(6):
            # lower_arm
            for j in range(2):
                # wrist = 2(需要取第二个，即k=1)
                k = wrist-1
                a = table_B[i, j, k]
                # 对应的隶属度（交集，乘积t算子）
                # wrist已经确定为2，所以membership为1
                # m = upper_arm[i] * lower_arm[j] * wrist
                m = upper_arm[i] * lower_arm[j] * 1
                if a == 1:
                    membership_1_set.append(m)
                elif a == 2:
                    membership_2_set.append(m)
                elif a == 3:
                    membership_3_set.append(m)
                elif a == 4:
                    membership_4_set.append(m)
                elif a == 5:
                    membership_5_set.append(m)
                elif a == 6:
                    membership_6_set.append(m)
                elif a == 7:
                    membership_7_set.append(m)
                elif a == 8:
                    membership_8_set.append(m)
                #elif a == 9:
                    #membership_9_set.append(m)


        # Table B范围是1-8
        membership_1_B = fuzzy_operator.einstein_sum_aggregation(membership_1_set)
        membership_2_B = fuzzy_operator.einstein_sum_aggregation(membership_2_set)
        membership_3_B = fuzzy_operator.einstein_sum_aggregation(membership_3_set)
        membership_4_B = fuzzy_operator.einstein_sum_aggregation(membership_4_set)
        membership_5_B = fuzzy_operator.einstein_sum_aggregation(membership_5_set)
        membership_6_B = fuzzy_operator.einstein_sum_aggregation(membership_6_set)
        membership_7_B = fuzzy_operator.einstein_sum_aggregation(membership_7_set)
        membership_8_B = fuzzy_operator.einstein_sum_aggregation(membership_8_set)

        membership_B = [membership_1_B, membership_2_B, membership_3_B, membership_4_B, membership_5_B, membership_6_B, membership_7_B, membership_8_B]
        normalized_membership_B = fuzzy_operator.normalize_membership(membership_B)

        return normalized_membership_B


    def Table_C_membership(self):
        # 数组形式
        membership_A = np.array(self.Table_A_membership())
        membership_B = np.array(self.Table_B_membership())

        # 定义空数组存储隶属度（仅仅是顺序，实际上2-12）
        membership_1_set = []
        membership_2_set = []
        membership_3_set = []
        membership_4_set = []
        membership_5_set = []
        membership_6_set = []
        membership_7_set = []
        membership_8_set = []
        membership_9_set = []
        membership_10_set = []
        membership_11_set = []
        # Table_A和Table_B的范围都是9*8
        table_C = np.array([
            [2, 2, 3, 4, 4, 5, 6, 6],
            [3, 3, 3, 4, 5, 6, 7, 7],
            [4, 4, 4, 5, 6, 7, 8, 8],
            [4, 4, 5, 6, 7, 8, 8, 9],
            [6, 6, 7, 8, 8, 9, 9, 10],
            [7, 7, 8, 9, 9, 9, 10, 10],
            [8, 8, 9, 10, 10, 10, 10, 10],
            [9, 9, 10, 10, 10, 11, 11, 11],
            [10, 10, 11, 11, 11, 11, 12, 12]
        ])
        # Table A 2-10 9个
        for i in range(9):
            # Table B 2-9 8个
            for j in range(8):
                a = table_C[i, j]
                m = membership_A[i] * membership_B[j]
                if a == 2:
                    membership_1_set.append(m)
                elif a == 3:
                    membership_2_set.append(m)
                elif a == 4:
                    membership_3_set.append(m)
                elif a == 5:
                    membership_4_set.append(m)
                elif a == 6:
                    membership_5_set.append(m)
                elif a == 7:
                    membership_6_set.append(m)
                elif a == 8:
                    membership_7_set.append(m)
                elif a == 9:
                    membership_8_set.append(m)
                elif a == 10:
                    membership_9_set.append(m)
                elif a == 11:
                    membership_10_set.append(m)
                elif a == 12:
                    membership_11_set.append(m)
        # 分数2-12的对应隶属度（并非是分数值，仅仅是顺序）

        # 2-12
        membership_1_C = fuzzy_operator.einstein_sum_aggregation(membership_1_set)
        membership_2_C = fuzzy_operator.einstein_sum_aggregation(membership_2_set)
        membership_3_C = fuzzy_operator.einstein_sum_aggregation(membership_3_set)
        membership_4_C = fuzzy_operator.einstein_sum_aggregation(membership_4_set)
        membership_5_C = fuzzy_operator.einstein_sum_aggregation(membership_5_set)
        membership_6_C = fuzzy_operator.einstein_sum_aggregation(membership_6_set)
        membership_7_C = fuzzy_operator.einstein_sum_aggregation(membership_7_set)
        membership_8_C = fuzzy_operator.einstein_sum_aggregation(membership_8_set)
        membership_9_C = fuzzy_operator.einstein_sum_aggregation(membership_9_set)
        membership_10_C = fuzzy_operator.einstein_sum_aggregation(membership_10_set)
        membership_11_C = fuzzy_operator.einstein_sum_aggregation(membership_11_set)

        membership_C = [membership_1_C, membership_2_C, membership_3_C, membership_4_C, membership_5_C, membership_6_C, membership_7_C, membership_8_C, membership_9_C, membership_10_C, membership_11_C]
        normalized_membership_C = fuzzy_operator.normalize_membership(membership_C)

        return normalized_membership_C







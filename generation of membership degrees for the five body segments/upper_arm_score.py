from CM_REBA import fuzzy_operator

class CMUpperArmREBA:

    def __init__(self, left_upper_arm_flexion, right_upper_arm_flexion, upper_arm_shoulder_gap, left_upper_arm_abduction, right_upper_arm_abduction):
        self.left_upper_arm_flexion = left_upper_arm_flexion
        self.right_upper_arm_flexion = right_upper_arm_flexion
        self.upper_arm_shoulder_gap = upper_arm_shoulder_gap
        self.left_upper_arm_abduction = left_upper_arm_abduction
        self.right_upper_arm_abduction = right_upper_arm_abduction

    def upper_arm_reba_membership(self):
        # upper_arm_flexion 2，1，2，3，4
        left_upper_arm_flexion_1 = self.left_upper_arm_flexion[0]
        left_upper_arm_flexion_2 = self.left_upper_arm_flexion[1]
        left_upper_arm_flexion_3 = self.left_upper_arm_flexion[2]
        left_upper_arm_flexion_4 = self.left_upper_arm_flexion[3]
        left_upper_arm_flexion_5 = self.left_upper_arm_flexion[4]

        right_upper_arm_flexion_1 = self.right_upper_arm_flexion[0]
        right_upper_arm_flexion_2 = self.right_upper_arm_flexion[1]
        right_upper_arm_flexion_3 = self.right_upper_arm_flexion[2]
        right_upper_arm_flexion_4 = self.right_upper_arm_flexion[3]
        right_upper_arm_flexion_5 = self.right_upper_arm_flexion[4]

        # upper_arm_flexion 1，2，3，4
        upper_arm_flexion_1 = left_upper_arm_flexion_2 * right_upper_arm_flexion_2
        upper_arm_flexion_2 = fuzzy_operator.einstein_sum_aggregation(
            [left_upper_arm_flexion_1 * right_upper_arm_flexion_1, left_upper_arm_flexion_1 * right_upper_arm_flexion_2,
             left_upper_arm_flexion_1 * right_upper_arm_flexion_3, left_upper_arm_flexion_2 * right_upper_arm_flexion_1,
             left_upper_arm_flexion_2 * right_upper_arm_flexion_2, left_upper_arm_flexion_2 * right_upper_arm_flexion_3,
             left_upper_arm_flexion_3 * right_upper_arm_flexion_1, left_upper_arm_flexion_3 * right_upper_arm_flexion_2,
             left_upper_arm_flexion_3 * right_upper_arm_flexion_3])
        upper_arm_flexion_3 = fuzzy_operator.einstein_sum_aggregation(
            [left_upper_arm_flexion_1 * right_upper_arm_flexion_4, left_upper_arm_flexion_2 * right_upper_arm_flexion_4,
             left_upper_arm_flexion_3 * right_upper_arm_flexion_4, left_upper_arm_flexion_4 * right_upper_arm_flexion_1,
             left_upper_arm_flexion_4 * right_upper_arm_flexion_2, left_upper_arm_flexion_4 * right_upper_arm_flexion_3,
             left_upper_arm_flexion_4 * right_upper_arm_flexion_4])
        upper_arm_flexion_4 = fuzzy_operator.einstein_sum_aggregation(
            [left_upper_arm_flexion_1 * right_upper_arm_flexion_5, left_upper_arm_flexion_2 * right_upper_arm_flexion_5,
             left_upper_arm_flexion_3 * right_upper_arm_flexion_5, left_upper_arm_flexion_4 * right_upper_arm_flexion_5,
             left_upper_arm_flexion_5 * right_upper_arm_flexion_5, left_upper_arm_flexion_5 * right_upper_arm_flexion_4,
             left_upper_arm_flexion_5 * right_upper_arm_flexion_3, left_upper_arm_flexion_5 * right_upper_arm_flexion_2,
             left_upper_arm_flexion_5 * right_upper_arm_flexion_1])

        # upper_arm_shoulder_gap 1，0，1
        upper_arm_shoulder_gap_1 = self.upper_arm_shoulder_gap[0]
        upper_arm_shoulder_gap_2 = self.upper_arm_shoulder_gap[1]
        upper_arm_shoulder_gap_3 = self.upper_arm_shoulder_gap[2]


        # upper_arm_abduction 1，0，1
        left_upper_arm_abduction_1 = self.left_upper_arm_abduction[0]
        left_upper_arm_abduction_2 = self.left_upper_arm_abduction[1]
        left_upper_arm_abduction_3 = self.left_upper_arm_abduction[2]

        right_upper_arm_abduction_1 = self.right_upper_arm_abduction[0]
        right_upper_arm_abduction_2 = self.right_upper_arm_abduction[1]
        right_upper_arm_abduction_3 = self.right_upper_arm_abduction[2]

        #  0，1
        upper_arm_abduction_1 = left_upper_arm_abduction_2 * right_upper_arm_abduction_2
        upper_arm_abduction_2 = fuzzy_operator.einstein_sum_aggregation(
            [left_upper_arm_abduction_2 * (right_upper_arm_abduction_1 + right_upper_arm_abduction_3),
             (left_upper_arm_abduction_1 + left_upper_arm_abduction_3) * right_upper_arm_abduction_2,
             (left_upper_arm_abduction_1 + left_upper_arm_abduction_3) * (right_upper_arm_abduction_1 + right_upper_arm_abduction_3)])


        # flexion   1, 2, 3, 4
        # gap       1, 0, 1
        # abduction 0, 1

        membership_1 = upper_arm_flexion_1 * upper_arm_shoulder_gap_2 * upper_arm_abduction_2

        membership_2 = fuzzy_operator.einstein_sum_aggregation(
            [upper_arm_flexion_2 * upper_arm_shoulder_gap_2 * upper_arm_abduction_1,  # 2+0+0
             upper_arm_flexion_1 * upper_arm_shoulder_gap_1 * upper_arm_abduction_1,  # 1+1+0
             upper_arm_flexion_1 * upper_arm_shoulder_gap_3 * upper_arm_abduction_1,
             upper_arm_flexion_1 * upper_arm_shoulder_gap_2 * upper_arm_abduction_2  # 1+0+1
             ])

        membership_3 = fuzzy_operator.einstein_sum_aggregation(
            [upper_arm_flexion_3 * upper_arm_shoulder_gap_2 * upper_arm_abduction_1,  # 3+0+0
             upper_arm_flexion_2 * upper_arm_shoulder_gap_1 * upper_arm_abduction_1,  # 2+1+0
             upper_arm_flexion_2 * upper_arm_shoulder_gap_3 * upper_arm_abduction_1,

             upper_arm_flexion_2 * upper_arm_shoulder_gap_2 * upper_arm_abduction_2,  # 2+0+1

             upper_arm_flexion_1 * upper_arm_shoulder_gap_1 * upper_arm_abduction_2,  # 1+1+1
             upper_arm_flexion_1 * upper_arm_shoulder_gap_3 * upper_arm_abduction_2])

        membership_4 = fuzzy_operator.einstein_sum_aggregation(
            [upper_arm_flexion_3 * upper_arm_shoulder_gap_2 * upper_arm_abduction_1,  # 4+0+0
             upper_arm_flexion_3 * upper_arm_shoulder_gap_1 * upper_arm_abduction_1,  # 3+1+0
             upper_arm_flexion_3 * upper_arm_shoulder_gap_3 * upper_arm_abduction_1,
             upper_arm_flexion_3 * upper_arm_shoulder_gap_2 * upper_arm_abduction_2,  # 3+0+1

             upper_arm_flexion_2 * upper_arm_shoulder_gap_1 * upper_arm_abduction_2,  # 2+1+1
             upper_arm_flexion_2 * upper_arm_shoulder_gap_3 * upper_arm_abduction_2])

        membership_5 = fuzzy_operator.einstein_sum_aggregation(
            [upper_arm_flexion_3 * upper_arm_shoulder_gap_1 * upper_arm_abduction_2,  # 3+1+1
             upper_arm_flexion_3 * upper_arm_shoulder_gap_3 * upper_arm_abduction_2,

             upper_arm_flexion_4 * upper_arm_shoulder_gap_1 * upper_arm_abduction_1,  # 4+1+0
             upper_arm_flexion_4 * upper_arm_shoulder_gap_3 * upper_arm_abduction_1,
             upper_arm_flexion_4 * upper_arm_shoulder_gap_2 * upper_arm_abduction_2  # 4+0+1
             ])

        membership_6 = fuzzy_operator.einstein_sum_aggregation(
            [upper_arm_flexion_4 * upper_arm_shoulder_gap_1 * upper_arm_abduction_2,  # 4+1+1
             upper_arm_flexion_4 * upper_arm_shoulder_gap_3 * upper_arm_abduction_2])

        membership_upper_arm = [membership_1, membership_2, membership_3, membership_4, membership_5, membership_6]
        normalized_membership_upper_arm = fuzzy_operator.normalize_membership(membership_upper_arm)

        return normalized_membership_upper_arm







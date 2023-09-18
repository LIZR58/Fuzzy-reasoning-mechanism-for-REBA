from CM_REBA import fuzzy_operator

class CMLowerArmREBA:

    def __init__(self, left_lower_arm_flexion, right_lower_arm_flexion):
        self.left_lower_arm_flexion = left_lower_arm_flexion
        self.right_lower_arm_flexion = right_lower_arm_flexion

    def lower_arm_reba_membership(self):
        # upper_arm_flexion 2，1，2
        left_lower_arm_flexion_1 = self.left_lower_arm_flexion[0]
        left_lower_arm_flexion_2 = self.left_lower_arm_flexion[1]
        left_lower_arm_flexion_3 = self.left_lower_arm_flexion[2]
        
        right_lower_arm_flexion_1 = self.right_lower_arm_flexion[0]
        right_lower_arm_flexion_2 = self.right_lower_arm_flexion[1]
        right_lower_arm_flexion_3 = self.right_lower_arm_flexion[2]
        
        # lower_arm_flexion 1，2
        membership_1 = left_lower_arm_flexion_2 * right_lower_arm_flexion_2
        membership_2 = fuzzy_operator.einstein_sum_aggregation([left_lower_arm_flexion_2 * (right_lower_arm_flexion_1 + right_lower_arm_flexion_3),
             (left_lower_arm_flexion_1 + left_lower_arm_flexion_3) * right_lower_arm_flexion_2,
             (left_lower_arm_flexion_1 + left_lower_arm_flexion_3) * (right_lower_arm_flexion_1 + right_lower_arm_flexion_3)])

        membership_lower_arm = [membership_1, membership_2]
        normalized_membership_lower_arm = fuzzy_operator.normalize_membership(membership_lower_arm)

        return normalized_membership_lower_arm


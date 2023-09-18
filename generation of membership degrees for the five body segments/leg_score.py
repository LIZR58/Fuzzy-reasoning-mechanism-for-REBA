from CM_REBA import fuzzy_operator

class CMLegREBA:

    def __init__(self, leg_support, left_leg_angle, right_leg_angle):
        self.leg_support = leg_support
        self.left_leg_angle = left_leg_angle
        self.right_leg_angle = right_leg_angle
        

    def leg_reba_membership(self):
        # leg support 2，1，2
        leg_support_1 = self.leg_support[0]
        leg_support_2 = self.leg_support[1]
        leg_support_3 = self.leg_support[2]

        # leg angle 0，1，2
        left_leg_angle_1 = self.left_leg_angle[0]
        left_leg_angle_2 = self.left_leg_angle[1]
        left_leg_angle_3 = self.left_leg_angle[2]

        right_leg_angle_1 = self.right_leg_angle[0]
        right_leg_angle_2 = self.right_leg_angle[1]
        right_leg_angle_3 = self.right_leg_angle[2]

        leg_angle_1 = left_leg_angle_1 * right_leg_angle_1
        leg_angle_2 = fuzzy_operator.einstein_sum_aggregation(
            [left_leg_angle_1 * right_leg_angle_2, left_leg_angle_2 * right_leg_angle_1,
             left_leg_angle_2 * right_leg_angle_2])
        leg_angle_3 = fuzzy_operator.einstein_sum_aggregation(
            [left_leg_angle_1 * right_leg_angle_3, left_leg_angle_2 * right_leg_angle_3,
             left_leg_angle_3 * right_leg_angle_1, left_leg_angle_3 * right_leg_angle_2,
             left_leg_angle_3 * right_leg_angle_3])

        membership_1 = leg_support_2 * leg_angle_1

        membership_2 = fuzzy_operator.einstein_sum_aggregation([leg_support_1 * leg_angle_1, leg_support_2 * leg_angle_2,
                                                                leg_support_3 * leg_angle_1])

        membership_3 = fuzzy_operator.einstein_sum_aggregation([leg_support_1 * leg_angle_2, leg_support_2 * leg_angle_3,
                                                                leg_support_3 * leg_angle_2])

        membership_4 = fuzzy_operator.einstein_sum_aggregation([leg_support_1 * leg_angle_3, leg_support_3 * leg_angle_3])

        membership_leg = [membership_1, membership_2, membership_3, membership_4]
        normalized_membership_leg = fuzzy_operator.normalize_membership(membership_leg)

        return normalized_membership_leg







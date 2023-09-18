from CM_REBA import fuzzy_operator

class CMNeckREBA:

    def __init__(self, neck_flexion, neck_adjustment):
        self.neck_flexion = neck_flexion
        self.neck_adjustment = neck_adjustment

    def neck_reba_membership(self):
        # neck flexion 2，1，2
        neck_flexion_1 = self.neck_flexion[0]
        neck_flexion_2 = self.neck_flexion[1]
        neck_flexion_3 = self.neck_flexion[2]

        # neck adjustment 1，0，1
        neck_adjustment_1 = self.neck_adjustment[0]
        neck_adjustment_2 = self.neck_adjustment[1]
        neck_adjustment_3 = self.neck_adjustment[2]


        membership_1 = neck_flexion_2 * neck_adjustment_2

        membership_2 = fuzzy_operator.einstein_sum_aggregation([neck_flexion_1 * neck_adjustment_2, neck_flexion_2 * neck_adjustment_1,
                                                                neck_flexion_2 * neck_adjustment_3, neck_flexion_3 * neck_adjustment_2])

        membership_3 = fuzzy_operator.einstein_sum_aggregation([neck_flexion_1 * neck_adjustment_1, neck_flexion_1 * neck_adjustment_3,
                                                               neck_flexion_3 * neck_adjustment_1, neck_flexion_3 * neck_adjustment_3])

        membership_neck = [membership_1, membership_2, membership_3]
        normalized_membership_neck = fuzzy_operator.normalize_membership(membership_neck)

        return normalized_membership_neck







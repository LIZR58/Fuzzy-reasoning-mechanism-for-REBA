from CM_REBA import fuzzy_operator

class CMTrunkREBA:

    def __init__(self, trunk_flexion, trunk_bending, trunk_twisting):
        self.trunk_flexion = trunk_flexion
        self.trunk_bending = trunk_bending
        self.trunk_twisting = trunk_twisting


    def trunk_reba_membership(self):
        # trunk flexion 3, 2, 1, 2, 3, 4
        trunk_flexion_1 = self.trunk_flexion[0]
        trunk_flexion_2 = self.trunk_flexion[1]
        trunk_flexion_3 = self.trunk_flexion[2]
        trunk_flexion_4 = self.trunk_flexion[3]
        trunk_flexion_5 = self.trunk_flexion[4]
        trunk_flexion_6 = self.trunk_flexion[5]

        # trunk bending and twisting 1，0，1
        trunk_bending_1 = self.trunk_bending[0]
        trunk_bending_2 = self.trunk_bending[1]
        trunk_bending_3 = self.trunk_bending[2]

        trunk_twisting_1 = self.trunk_twisting[0]
        trunk_twisting_2 = self.trunk_twisting[1]
        trunk_twisting_3 = self.trunk_twisting[2]

        # adjustment 0、1
        trunk_adjustment_1 = trunk_bending_2 * trunk_twisting_2
        trunk_adjustment_2 = fuzzy_operator.einstein_sum_aggregation(
            [trunk_bending_2 * (trunk_twisting_1 + trunk_twisting_3),
             (trunk_bending_1 + trunk_bending_3) * trunk_twisting_2,
             (trunk_bending_1 + trunk_bending_3) * (trunk_twisting_1 + trunk_twisting_3)])
 

        # flexion: 3, 2, 1, 2, 3, 4
        # adjustment: 0, 1

        #  1, 2, 3, 4, 5
        membership_1 = trunk_flexion_3 * trunk_adjustment_1

        membership_2 = fuzzy_operator.einstein_sum_aggregation([trunk_flexion_2 * trunk_adjustment_1, trunk_flexion_4 * trunk_adjustment_1, trunk_flexion_3 * trunk_adjustment_2])

        membership_3 = fuzzy_operator.einstein_sum_aggregation([trunk_flexion_1 * trunk_adjustment_1, trunk_flexion_5 * trunk_adjustment_1, trunk_flexion_2 * trunk_adjustment_2, trunk_flexion_4 * trunk_adjustment_2])

        membership_4 = fuzzy_operator.einstein_sum_aggregation([trunk_flexion_1 * trunk_adjustment_2, trunk_flexion_5 * trunk_adjustment_2, trunk_flexion_6 * trunk_adjustment_1])

        membership_5 = fuzzy_operator.einstein_sum_aggregation([trunk_flexion_6 * trunk_adjustment_2])

        membership_trunk = [membership_1, membership_2, membership_3, membership_4, membership_5]
        normalized_membership_trunk = fuzzy_operator.normalize_membership(membership_trunk)

        return normalized_membership_trunk







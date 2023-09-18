import numpy as np

def einstein_sum_aggregation(memberships):
    complement = [1 - m for m in memberships]
    aggregated_membership = 1
    for value in complement:
        aggregated_membership *= value
    aggregated_membership = 1 - aggregated_membership
    return aggregated_membership


def product_t_norm(memberships):
    result = 1.0  # initialization
    for membership in memberships:
        result *= membership
    return result



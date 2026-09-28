"""
Reference:
Yau, S. S., & Yin, Y. (2011).
"QoS-based Service Ranking and Selection for Service-based Systems."

Stephen S. Yau and Yin Yin
Information Assurance Center
School of Computing, Informatics, and Decision Systems Engineering
Arizona State University
Tempe, AZ, USA

Source used for the satisfaction metric implementation.

Implementation date: 09/23/2026
"""
import math
REFERENCE_POINT = 0.5
#variable multiplication
def normalize_qos_value(value, lower, upper, kpi_type):
    if kpi_type == "utility":
        return (value - lower) / (upper - lower)

    if kpi_type == "cost":
        return (upper - value) / (upper - lower)

    raise ValueError("kpi_type must be 'utility' or 'cost'")

# system boundries functions 
################################################################################
def utility_boundary(value, lower, upper): # checking the utlity values boundries
    if value <= lower:
        return 0.0
    if value >= upper:
        return 1.0
    return None

def cost_boundary(value, lower, upper): # checking the cost values boundries
    if value <= lower:
        return 1.0
    if value >= upper:
        return 0.0
    return None
################################################################################
def normalize_utility(value, lower, upper, kpi_type): # normalize utility value to [0, 1] range
    if upper <= lower:
        raise ValueError("upper must be greater than lower")

    utility_check = utility_boundary(value, lower, upper)  
    if utility_check is not None:
        return utility_check
    normalized_value_utility= normalize_qos_value(
        value,
        lower,
        upper,
        kpi_type)    
    return normalized_value_utility

def normalize_cost(value, lower, upper, kpi_type):
    if upper <= lower:
        raise ValueError("upper must be greater than lower")

    cost_check = cost_boundary(value, lower, upper)

    if cost_check is not None:
        return cost_check

    normalized_value = normalize_qos_value(
        value,
        lower,
        upper,
        kpi_type
    )

    return normalized_value

###################################################################################
def satisfaction_above_reference(normalized_value, weight):
    exponent = 1 - weight
    distance_from_reference = 2 * normalized_value - 1
    powered_value = math.pow(distance_from_reference, exponent)
    satisfaction_score = REFERENCE_POINT * powered_value + REFERENCE_POINT 
    return satisfaction_score

def satisfaction_below_reference(normalized_value, weight):
    exponent = 1 - weight
    distance_from_reference = -2 * normalized_value + 1
    powered_value = math.pow(distance_from_reference, exponent)
    satisfaction_score = -REFERENCE_POINT * powered_value + REFERENCE_POINT 
    return satisfaction_score

#satisfaction functions
#satisfaction for one KPI based on normalized value and weight
def satisfaction_score(normalized_value, weight):
    if normalized_value > REFERENCE_POINT:
        return satisfaction_above_reference(normalized_value, weight)
    else:    
        return satisfaction_below_reference(normalized_value, weight)  
      
################################################################################

# combination of satisfaction functions for multiple KPIs based on their normalized values and weights
def combination_function(
    throughput_score, throughput_weight,
    latency_score, latency_weight,
    cost_score, cost_weight,
    energy_score, energy_weight
):
    weighted_sum = (
        throughput_score * throughput_weight
        + latency_score * latency_weight
        + cost_score * cost_weight
        + energy_score * energy_weight
    )

    total_weight = (
        throughput_weight
        + latency_weight
        + cost_weight
        + energy_weight
    )
    total_satisfaction = weighted_sum / total_weight
    return total_satisfaction

  ######################################################################################      
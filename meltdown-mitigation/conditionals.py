""" Meltdown Mitigation exercise """


from typing import Annotated
from unittest.loader import defaultTestLoader


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

""" 
print("below are some inputs and outputs from is_criticality_balanced")

test_1 = is_criticality_balanced(750, 650)
test_1_answer = True

test_2 = is_criticality_balanced(1000, 800)
test_2_answer = False

print(f'Result of test 1 with data: (750, 650) was {test_1} but the correct answer is {test_1_answer}')
print(f'Result of test 2 with data: (1000, 800) was {test_2} but the correct answer is {test_2_answer}')

 """

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,                     80..100
    2. orange -> efficiency of less than 80% but at least 60%, 60..79 %
    3. red -> efficiency below 60%, but still 30% or more,     30..59 %
    4. black ->  less than 30% efficient. 0 < black < 29% |     0..29 %

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    # 1. räkna ut generated power ( effekten vi genererar just i detta nu. I * U // voltage * current)
    generated_power = voltage * current
    # 2. räkna ut effektiviteten, dvs genererad effekt delat med teoretiskt möjlig maxeffekt
    efficiency_percentage = (generated_power/ theoretical_max_power)*100
    # 3. returnerna en av fyra strängar, beroende på intervallet hos efficiency_percentage
    if efficiency_percentage < 30:
        return 'black'
    elif efficiency_percentage < 60:
        return 'red'
    elif efficiency_percentage < 80:
        return 'orange'
    else:
        return 'green'

#print(reactor_efficiency(10, 10, 400))

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """

    pass

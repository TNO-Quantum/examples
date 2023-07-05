"""Winnow example"""

import numpy as np

from tno.quantum.communication.qkd_key_rate.base import Message, Permutations, Schedule
from tno.quantum.communication.qkd_key_rate.protocols.classical.winnow import (
    WinnowCorrector,
    WinnowReceiver,
    WinnowSender,
)

error_rate = 0.05
message_length = 10000
input_message = Message.random_message(message_length=message_length)
error_message = Message(
    [x if np.random.rand() > error_rate else 1 - x for x in input_message]
)
schedule = Schedule.schedule_from_error_rate(error_rate=error_rate)
number_of_passes = np.sum(schedule.schedule)
permutations = Permutations.random_permutation(
    number_of_passes=number_of_passes, message_size=message_length
)

alice = WinnowSender(
    message=input_message, permutations=permutations, schedule=schedule
)
bob = WinnowReceiver(
    message=error_message, permutations=permutations, schedule=schedule
)
corrector = WinnowCorrector(alice=alice, bob=bob)
summary = corrector.correct_errors()

print(summary)

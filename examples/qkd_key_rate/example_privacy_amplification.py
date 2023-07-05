"""Privacy-amplification example"""

from tno.quantum.communication.qkd_key_rate.base import Message
from tno.quantum.communication.qkd_key_rate.protocols.classical.privacy_amplification import (
    PrivacyAmplification,
)

message = Message.random_message(message_length=100)
privacy = PrivacyAmplification(message.length, error_rate_basis_x=0)
entropy = privacy.get_entropy_estimate(error_correction_loss=10)
privacy.do_hash(message, entropy)

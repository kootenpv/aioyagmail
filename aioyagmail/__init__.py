__project__ = "aioyagmail"
__version__ = "0.0.3"

from yagmail.error import YagConnectionClosed
from yagmail.error import YagAddressError
from yagmail.sender import SMTP
from yagmail.utils import raw
from yagmail.utils import inline
from aioyagmail.aio import AIOSMTP

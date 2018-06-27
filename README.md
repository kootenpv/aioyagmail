
<p align="center">
  <img src="./resources/icon.png" width="48px"/>
</p>

# aioyagmail -- Yet Another GMAIL/SMTP client, using AsyncIO

[![Join the chat at https://gitter.im/kootenpv/aioyagmail](https://badges.gitter.im/kootenpv/aioyagmail.svg)](https://gitter.im/kootenpv/aioyagmail?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI](https://img.shields.io/pypi/v/aioyagmail.svg?style=flat-square)](https://pypi.python.org/pypi/aioyagmail/)
[![PyPI](https://img.shields.io/pypi/pyversions/aioyagmail.svg?style=flat-square)](https://pypi.python.org/pypi/aioyagmail/)

The goal here is to make it as simple and painless as possible to send emails using asyncio.

In the end, your code will look something like this:

```python
import asyncio
from aioyagmail import AIOSMTP

loop = asyncio.get_event_loop()

async def send_single():
    # walks you through oauth2 process if no file at this location
    async with AIOSMTP(oauth2_file="~/oauth2_gmail.json") as yag:
        await yag.send(to="someone@gmail.com", subject="hi")

async def send_multi():
    async with AIOSMTP(oauth2_file="~/oauth2_gmail.json") as yag:
        # Runs asynchronously!
        await asyncio.gather(yag.send(subject="1"),
                             yag.send(subject="2"),
                             yag.send(subject="3"))

loop.run_until_complete(send_single())
loop.run_until_complete(send_multi())
```

### Username and password

It is possible like in `yagmail` to use username and password, but this is not actively encouraged anymore.
See https://github.com/kootenpv/yagmail#username-and-password how to do it.

### For more information

Have a look at `yagmail`. Any issue NOT related to async should be posted there (or found out about).

### Word of caution

Watch out that gmail does not block you for spamming. Using async you could potentially be sending emails too rapidly.

### Donate

If you like `aioyagmail`, feel free (no pun intended) to donate any amount you'd like :-)

[![PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Y7QCCEPGC6R5E)

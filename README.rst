aioyagmail - Yet Another GMAIL/SMTP client, using AsyncIO
=========================================
`aioyagmail` is a GMAIL/SMTP client that aims to
make it as simple as possible to send emails.

Sending an Email is as simple:

.. code-block:: python

    import asyncio
    from aioyagmail import AIOSMTP

    loop = asyncio.get_event_loop()

    async def send_single():
        # walks you through oauth2 process if no file at this location
        async with AIOSMTP(oauth2_file="~/oauth2_gmail.json") as yag:
            await yag.send(to="someone@gmail.com", subject="hi")

    loop.run_until_complete(send_single())

For further documentation please go to https://github.com/kootenpv/aioyagmail or https://github.com/kootenpv/yagmail

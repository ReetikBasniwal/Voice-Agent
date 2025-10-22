import asyncio
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

async def main():

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        from_="+16892639732",
        to="+918930228152",
        url="http://demo.twilio.com/docs/voice.xml",
    )
    print("Started server.")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
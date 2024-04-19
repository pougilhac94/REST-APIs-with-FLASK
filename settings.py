import os
from dotenv import load_dotenv
"""When deploying to Render.com, it's much easier if we don't have to pass the REDIS_URL and the queue name directly to the command.
So instead, let's create a settings.py file and put our rq worker configuration there.

To run the rq worker using this settings file use rq worker -c settings.
"""

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
QUEUES = ["emails", "default"]
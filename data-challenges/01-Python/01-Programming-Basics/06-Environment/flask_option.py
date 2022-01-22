# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    if os.environ.get("FLASK_ENV") == "development":
        out = "Starting in development mode..."
    else:
        out = "Starting in production mode..."
    return out

if __name__ == "__main__":
    print(start())

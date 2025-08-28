#! /usr/bin/env python

import argparse
import datetime

from dateutil.tz import tzlocal


def main(args):
    """
    Convert AD timestamp to datetime.
    """
    dt = convert_ad_filetime_to_datetime(int(args.timestamp))
    if args.local:
        tz_local = tzlocal()
        dt = dt.astimezone(tz_local)
    print(dt.isoformat())


def convert_ad_filetime_to_datetime(ad_filetime):
    """
    Converts an Active Directory pwdLastSet (FileTime) value to a Python datetime object.
    """
    # The number of 100-nanosecond intervals between Jan 1, 1601 and Jan 1, 1970
    # (Unix epoch)
    EPOCH_DIFFERENCE = 116444736000000000

    # Convert 100-nanosecond intervals to seconds
    seconds_since_1601 = ad_filetime / 10000000

    # Subtract the epoch difference to get seconds since Jan 1, 1970
    unix_timestamp = seconds_since_1601 - (EPOCH_DIFFERENCE / 10000000)

    # Create a datetime object from the Unix timestamp
    return datetime.datetime.fromtimestamp(unix_timestamp, tz=datetime.timezone.utc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Convert AD timestamp to datetime.")
    parser.add_argument("timestamp", action="store", help="The timestamp to covert.")
    parser.add_argument(
        "-l", "--local", action="store_true", help="Convert to local time zone."
    )
    args = parser.parse_args()
    main(args)

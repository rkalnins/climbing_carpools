"""Backend for reading data from JSON.

Primarily for debugging and testing

"""

import json
import logging

from scheduler.util import *

logger = logging.getLogger(__name__)


def members_from_json(filename: str) -> (list, list):
    """
    Gets members from a JSON file.
    """

    with open(filename) as f:
        members = json.load(f)

    riders = filter_dues_payers(get_riders(members))
    drivers = get_drivers(members)

    return riders, drivers

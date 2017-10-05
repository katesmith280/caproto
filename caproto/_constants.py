import datetime

DEFAULT_PROTOCOL_VERSION = 13
MAX_ID = 2**16  # max value of various integer IDs

# official IANA ports
EPICS_CA1_PORT, EPICS_CA2_PORT = 5064, 5065

EPICS2UNIX_EPOCH = 631152000.0
EPICS_EPOCH = datetime.datetime.utcfromtimestamp(EPICS2UNIX_EPOCH)

MAX_STRING_SIZE = 40
MAX_UNITS_SIZE = 8
MAX_ENUM_STRING_SIZE = 26
MAX_ENUM_STATES = 16

DO_REPLY = 10
NO_REPLY = 5

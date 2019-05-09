import hashlib
import sys

def sha1_digest(s):
    m = hashlib.sha1()
    m.update(str.encode(s))
    return m.hexdigest()

def next_alphabet(c):
    assert c.isalpha() and c.islower()
    return 'a' if c == 'z' else chr(ord(c) + 1)

def input_multiple_choice(question, choices):
    q = '{0} ({1}): '.format(question, '/'.join(choices))
    response = vc_input(q)
    while response not in choices:
        response = vc_input(q)
    return response

def vc_input(params):
  return raw_input(params) if (sys.version_info.major <= 2) else input(params)

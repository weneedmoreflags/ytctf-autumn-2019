# Base taken from https://github.com/Dvd848/CTFs/blob/master/2018_picoCTF/Super%20Safe%20RSA.md

from factordb.factordb import FactorDB
import time, requests, gmpy2
from pwn import *

modules = []

for i in range(1000):
    r = remote("vega.evgfilim1.me", 27003)
    output = r.recvall()
    params = {}
    for line in output.rstrip().split("\n"):
        if ':' in line:
            param, value = line.split(": ")
            log.info("{}: {}".format(param, value))
            params[param] = int(value.rstrip())

    log.info("Connecting to FactorDB")

    for old in modules:
        if int(gmpy2.gcd(old, params["n"])) != 1:
            print str(old) + ' ' + str(params["n"])
            exit(0)

    print '  [~] All modules are co-prime'
    modules.append(params["n"])

    # It looks like in some cases, the FactorDB won't factorize a number unless
    # we first access the web API.
    requests.get("http://factordb.com/index.php?query={}".format(params["n"]))

    status = ''
    if True:
        f = FactorDB(params["n"])
        f.connect()
        factor_list = f.get_factor_list()
        status = f.get_status()
        log.info("Received from FactorDB: {} (status: {})".format(factor_list, status))

    if len(factor_list) == 1:
        continue

    p, q = factor_list
    log.info("p: {}".format(p))
    log.info("q: {}".format(q))
    assert(p * q == params["n"])

    ph = (p-1)*(q-1)
    log.info("Phi: {}".format(ph))
    d = gmpy2.invert(params["e"], ph)
    log.info("d: {}".format(d))

    plaintext = pow(params["c"], d, params["n"])
    log.success("Flag: {}".format(format(plaintext, 'x').decode("hex")))

    exit(0)

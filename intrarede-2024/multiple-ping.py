from pythonping import ping

TARGETS = [
    "yahoo.com",
    "google.com",
    "cisco.com",
    "cern.ch",
    "juniper.com",
    "nic.br",
    "arin.org",
    "lacnic.org",
]


def myping(host):
    response = ping(host)
    if response.success:
        print("%s OK, latency is %.3fms" % (host, response.rtt_avg_ms))
    else:
        print(host, "FAILED")


def main():
    for target in TARGETS:
        myping(target)


if __name__ == "__main__":
    main()

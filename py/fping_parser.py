import re


r = re.compile


def to_string(output):
    '''
    most of the time output given is list
    This class assumes output as string
    This helper converts the input to string if required
    '''
    if isinstance(output, list):
        if len(output) == 1:
            output = output[0]
        else:
            output = "\n".join(output)
    # remove tabs if any
    output = "\n".join(output.split("\t"))
    return output


def parse_str(string):
    string = string.strip()
    try:
        return int(string)
    except (TypeError, ValueError):
        pass
    if string.startswith('0x'):
        try:
            return int(string, 16)
        except Exception:
            return string
    return string


def parse_line(line, patterns, strict=True, typecast=True):
    line = line.strip()
    for regexp in patterns:
        m = regexp.match(line)
        if m is None:
            continue
        d = m.groupdict()
        for key, value in d.iteritems():
            if typecast and value:
                d[key] = parse_str(value)
        return d
    if strict is True:
        raise LookupError('Failed to parse line "{}"'.format(line))


def fping_summary_parser():
    data = '''
           1 targets
           0 alive
           1 unreachable
           0 unknown addresses

           1 timeouts (waiting for response)
           1 ICMP Echos sent
           0 ICMP Echo Replies received
           0 other ICMP received

     0.00 ms (min round trip time)
     0.00 ms (avg round trip time)
     0.00 ms (max round trip time)
            0.526 sec (elapsed real time)
    '''

    data = to_string(data).strip()
    patterns = [
                r(r'(?P<targets>\d+) targets'),
                r(r'(?P<alive>\d+) alive'),
                r(r'(?P<unreachable>\d+) unreachable'),
                r(r'(?P<unknown>\d+) unknown addresses'),
                r(r'(?P<timeouts>\d+) timeouts \(waiting for response\)'),
                r(r'(?P<echos_sent>\d+) ICMP Echos sent'),
                r(r'(?P<echos_rcvd>\d+) ICMP Echo Replies received'),
                r(r'(?P<other_icmp>\d+) other ICMP received'),
                r(r'(?P<min_rtt>\d+\.\d+ \w+) \(min round trip time\)'),
                r(r'(?P<avg_rtt>\d+\.\d+ \w+) \(avg round trip time\)'),
                r(r'(?P<max_rtt>\d+\.\d+ \w+) \(max round trip time\)'),
                r(r'(?P<time_taken>\d+\.\d+ \w+) \(elapsed real time\)'),
               ]

    for line in data.splitlines():
        line = line.strip()
        if line:
            parsed_line = parse_line(line, patterns)
            print parsed_line


def fping_parser():
    data = '''
    127.0.0.1 : [0], 84 bytes, 0.03 ms (0.03 avg, 0% loss)
    127.0.0.1 : [1], 84 bytes, 0.04 ms (0.03 avg, 0% loss)

    128.0.0.1 : xmt/rcv/%loss = 2/2/0%
    127.0.0.1 : xmt/rcv/%loss = 3/3/0%, min/avg/max = 0.03/0.04/0.06<Paste>
    '''

    datarx = '''
    123.0.0.1 is unreachable
    127.0.0.1 is alive
    127.0.0.2 is alive
    127.0.0.1x address not found
    '''

    return_dict = dict()
    pattern_dict = {
            'addr_not_found': r(r'(?P<ip>\S+) address not found'),
            'unreachable': r(r'(?P<ip>\S+) is unreachable'),
            'reachable': r(r'(?P<ip>\S+) is alive'),
            'summary': r(r'(?P<ip>\S+)\s+:\s+xmt/rcv/%loss = (?P<sent>\d+)/(?P<recvd>\d+)/(?P<loss>\d+)%(, min/avg/max = (?P<min>\d+\.\d+)/(?P<avg>\d+\.\d+)/(?P<max>\d+\.d+))?')
            }

    data = to_string(data).strip()
    for line in data.splitlines():
        if line:
            for key, pattern in pattern_dict.iteritems():
                match = pattern.search(line)
                if match:
                    match_dict = match.groupdict()
                    ip = match_dict.pop('ip')
                    if match_dict:
                        return_dict.setdefault(key, dict()).setdefault(ip, match_dict)
                    else:
                        return_dict.setdefault(key, []).append(ip)
                    break

    print return_dict


fping_parser()

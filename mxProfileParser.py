import json
import argparse


def add_args(parser):
    parser.add_argument("--file",
                        help="profile json file", default="profile.json")
    parser.add_argument("--op", help="operator need to anlyze", default="all")
    parser.add_argument("--iterations",
                        help="number of iteration, including warm up",
                        default=0, type=int)


def parse_all(events, ops, cnt, dur):
    assert isinstance(events, list)
    for i in range(len(events)):
        if events[i]['name'] in ops:
            name = events[i]['name']
            if events[i]['ph'] == 'B' and \
               events[i+1]['name'] == name and \
               events[i+1]['ph'] == 'E':
                cnt[str(name)] += 1
                dur[str(name)] += events[i+1]['ts'] - events[i]['ts']

    return ops, cnt, dur


def print_all(cnt, dur, iters=0):
    print('Time of each OP:')
    oplen = [len(v) for v in cnt.keys()]
    maxname = max(oplen)
    maxtotal = max([len(str(v / 1000.0)) for v in dur.values()])
    maxpercall = max([len(str(dur[v] / 1000.0 / cnt[v])) for v in dur.keys()])
    maxcall = max([len(str(v)) for v in cnt.values()])

    for i in range(len(cnt)):
        name = list(cnt.keys())[i]
        if iters != 0:
            assert cnt[name] % iters == 0
            str1 = ('%%-%ds' % maxname) % name
            str2 = ('%%-%ds ms' % maxtotal) % (dur[name] / 1000.0)
            str3 = ('%%-%ds ms/call' % maxpercall) % \
                (dur[name] / 1000.0 / cnt[name])
            str4 = ('%%-%ds calls' % maxcall) % cnt[name]
            str5 = '%-4s calls/iter' % (cnt[name] / iters)
            print('%s  %s \t%s \t%s \t%s' % (str1, str2, str3, str4, str5))
        else:
            str1 = ('%%-%ds' % maxname) % name
            str2 = ('%%-%ds ms' % maxtotal) % (dur[name] / 1000.0)
            str3 = ('%%-%ds ms/call' % maxpercall) % \
                (dur[name] / 1000.0 / cnt[name])
            str4 = ('%%-%ds calls' % maxcall) % cnt[name]
            print('%s  %s \t%s \t%s' % (str1, str2, str3, str4))

    print('\nTotal OP Time: %.8f ms' % (sum(dur.values()) / 1000.0))
    if iters != 0:
        print('Iteration Time: %.8f ms\n' %
              (sum(dur.values()) / 1000.0 / iters))


def print_op(op, cnt, dur, iters=0):
    print('Time of %s:' % op)
    oplen = [len(v) for v in cnt.keys()]
    maxname = max(oplen)
    maxtotal = max([len(str(v / 1000.0)) for v in dur.values()])
    maxpercall = max([len(str(dur[v] / 1000.0 / cnt[v])) for v in dur.keys()])
    maxcall = max([len(str(v)) for v in cnt.values()])

    for i in range(len(cnt)):
        name = list(cnt.keys())[i]
        if op in name:
            if iters != 0:
                assert cnt[name] % iters == 0
                str1 = ('%%-%ds' % maxname) % name
                str2 = ('%%-%ds ms' % maxtotal) % (dur[name] / 1000.0)
                str3 = ('%%-%ds ms/call' % maxpercall) % \
                    (dur[name] / 1000.0 / cnt[name])
                str4 = ('%%-%ds calls' % maxcall) % cnt[name]
                str5 = '%-4s calls/iter' % (cnt[name] / iters)
                print('%s  %s \t%s \t%s \t%s' % (str1, str2, str3, str4, str5))
            else:
                str1 = ('%%-%ds' % maxname) % name
                str2 = ('%%-%ds ms' % maxtotal) % (dur[name] / 1000.0)
                str3 = ('%%-%ds ms/call' % maxpercall) % \
                    (dur[name] / 1000.0 / cnt[name])
                str4 = ('%%-%ds calls' % maxcall) % cnt[name]
                print('%s  %s \t%s \t%s' % (str1, str2, str3, str4))


def init_table(events):
    ops = []
    cnt = {}
    dur = {}
    for i in range(len(events)):
        if events[i]['name'] != 'process_name' and \
           events[i]['name'] not in ops:
            ops.append(str(events[i]['name']))
            if events[i]['name'] not in cnt.keys():
                cnt.update({events[i]['name']: 0})
            if e[i]['name'] not in dur.keys():
                dur.update({events[i]['name']: 0})

    return ops, cnt, dur


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mxnet profile file analysis",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter) # noqa
    add_args(parser)
    args = parser.parse_args()
    f = open(args.file, 'r')
    j = json.load(f)
    e = j['traceEvents']

    ops, cnt, dur = init_table(e)
    parse_all(e, ops, cnt, dur)
    if args.op == 'all':
        print_all(cnt, dur, args.iterations)
    else:
        print_op(args.op, cnt, dur, args.iterations)

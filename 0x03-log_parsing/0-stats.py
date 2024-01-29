#!/usr/bin/python3
"""
script that reads stdin line by line & computes metrics:
"""
import re


def extrct_inpt(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    fp_ = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*', r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    data = {
        'status_code': 0,
        'file_size': 0,
    }
    fm_log = '{}\\-{}{}{}{}\\s*'.format(fp_[0], fp_[1], fp_[2], fp_[3], fp_[4])
    match_resp = re.fullmatch(fm_log, input_line)
    if match_resp is not None:
        state_code = match_resp.group('status_code')
        file_size = int(match_resp.group('file_size'))
        data['status_code'] = state_code
        data['file_size'] = file_size
    return data


def msg_printer(file_size_total, sc_stats):
    """
        Prints accumulated statistics of HTTP request log.
    """
    print('File size: {:d}'.format(file_size_total), flush=True)
    for sc_stats in sorted(sc_stats.keys()):
        num = sc_stats.get(sc_stats, 0)
        if num > 0:
            print('{:s}: {:d}'.format(sc_stats, num), flush=True)


def updt_metrics(line, file_size_total, sc_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    data_lne = extrct_inpt(line)
    sc_stats = data_lne.get('status_code', '0')
    if sc_stats in sc_stats.keys():
        sc_stats[sc_stats] += 1
    return file_size_total + data_lne['file_size']


def run():
    '''Starts the log parser.
    '''
    num_lne = 0
    file_size_total = 0
    sc_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_size_total = updt_metrics(
                line,
                file_size_total,
                sc_stats,
            )
            num_lne += 1
            if num_lne % 10 == 0:
                msg_printer(file_size_total, sc_stats)
    except (KeyboardInterrupt, EOFError):
        msg_printer(file_size_total, sc_stats)


if __name__ == '__main__':
    run()

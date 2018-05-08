# shellback [![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/chrispetrou/shellback/blob/master/LICENSE) [![](https://img.shields.io/badge/Made%20with-python-yellow.svg)](https://www.python.org/)

This is a simple script to automate the process of generating a reverse-shell command like those described in [pentestmonkey](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) blog:

```
$ ./shellback.py -h
usage: shellback.py [-h] [-l] [-p] [-v] [-f] [-c]

shellback.py: generates a reverse shell

arguments:
  -h, --help       show this help message and exit
  -l , --lhost     Specify local host ip
  -p , --lport     Specify a local port [default 8080]
  -v , --version   Specify the language to generate the reverse shell [default bash]
  -f, --tofile     reverse-shell command to be written in a file
  -c, --copy       Copy reverse-shell command to clipboard
```
Example:

<img src="images/shellback.png" width="80%">

>This script was originally part of the script in my [pypentesting-repository](https://github.com/chrispetrou/pypentesting), but since I tend to use a lot on CTF-like challenges and pentesting labs I decided to create a separate repository for it.

**Requirements:**

*   [pyperclip](https://pypi.python.org/pypi/pyperclip)
*   [colorama](https://pypi.python.org/pypi/colorama)

**Note:** To install the requirements:

`pip install -r requirements.txt --upgrade --user`

### Disclaimer
>This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
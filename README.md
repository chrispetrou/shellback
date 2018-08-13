# shellback [![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/chrispetrou/shellback/blob/master/LICENSE) [![](https://img.shields.io/badge/python-2.7%20%7C%203.5-orange.svg)](https://www.python.org/)

This is a standalone python script to automate the process of generating a reverse-shell command like those described in [pentestmonkey](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) blog:

<img src="images/shellback.png" width="80%">

__Compatibility:__ The `shellback.py` script is compatible with **python 2.7** and the `/py3_version/shellback.py` is compatible with **python3.5**.

> __Examples:__

<img src="images/example1.png" width="80%">
<img src="images/example2.png" width="80%">

### Supported reverse shells (-v option)
__default__: bash

Reverse shells |
|-|
| bash |
| perl |
| python |
| php |
| ruby |
| nc1 (nc version 1)|
| nc2 (nc version 2)|
| java |

### Supported shell types (-s option) 
__default__: /bin/sh

In some cases it is possible to specify the shell type. The supported shell-types are the following:

Shell types |
|-|
| sh |
| zsh |
| ksh |
| tcsh |
| bash |
| dash |

> This script was originally part of the scripts in my [pypentesting-repository](https://github.com/chrispetrou/pypentesting#revshell), but since I tend to use a lot on CTF-like challenges and pentesting labs I decided to create a separate repository for it.

**Requirements:**

*   [pyperclip](https://pypi.python.org/pypi/pyperclip)
*   [colorama](https://pypi.python.org/pypi/colorama)

#### **Note:** To install the requirements:
---
>__python2.7:__ `pip install -r requirements.txt --upgrade --user`

>__python3.5:__ `pip3 install -r requirements.txt --upgrade --user`

### Disclaimer
> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
# Scraping-for-OpenEmbedded

![webscrapping](https://github.com/user-attachments/assets/7b3199a9-3921-48dd-85f0-4d6bdc326525)

## Installation

```bash
# inside a virtual environment

$ pip install git+ssh://github.com/Moatasem-Elsayed/Scraping-for-OpenEmbedded.git@main
```

## Usage

```bash
$ scrapeOpenEmbedded --help

usage: Scraping-for-OpenEmbedded [-h] -s TERM [-p | --pretty | --no-pretty]

Scrape Recipe Information from (https://layers.openembedded.org/)

options:
  -h, --help            show this help message and exit
  -s TERM, --term TERM  name of recipe search term
  -p, --pretty, --no-pretty
                        print results as table (tabulate)

All rights reserved
```

## Example

```bash
$ scrapeOpenEmbedded -p -s ssh

+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
| Name                 | Version   | Description                                                                                                                  | Layer             |
+======================+===========+==============================================================================================================================+===================+
| autossh              | 1.4g      | autossh is a program to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic | meta-networking   |
+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
| ksshaskpass          | 5.26.2    | ssh-add helper that uses kwallet and kpassworddialog                                                                         | meta-qt5-extra    |
+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
| libssh               | 0.11.1    | Multiplatform C library implementing the SSHv2 and SSHv1 protocol                                                            | meta-oe           |
+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
| libssh2              | 1.11.1    | A client-side C library implementing the SSH2 protocol                                                                       | openembedded-core |
+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
| lxqt-openssh-askpass | 1.2.0     | This is a very small helper app for ssh-agent                                                                                | meta-qt5-extra    |
+----------------------+-----------+------------------------------------------------------------------------------------------------------------------------------+-------------------+
```

## Test

```bash
$ python -m unittest tests/testparse.py

..s
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK (skipped=1)
```

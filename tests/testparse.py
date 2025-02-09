import unittest
from itertools import islice
from openEmbedded.parse import (
    raw_html,
    parse_html,
    parse_recipe_table,
    parse_search_table,
)


class TestHTTPGet(unittest.TestCase):

    @unittest.skip("skip network request")
    def test_search_recipe_term(self):
        status, is_redirected, content = raw_html(
            "https://layers.openembedded.org/layerindex/branch/master/recipes/?q=ssh"
        )
        # print(a.decode("utf-8"))
        with open("ssh.html", "w", encoding="UTF-8") as f:
            f.write(content.decode("utf-8"))

    # def test_echo_recipe_autossh(self):
    #     with open("tests/autossh.html", "r", encoding="UTF-8") as f:
    #         print(f.read())

    def test_parse_recipe_autossh(self):
        with open("tests/autossh.html", "r", encoding="UTF-8") as f:
            tree = parse_html(f.read())
            self.assertTupleEqual(
                parse_recipe_table(tree),
                (
                    "autossh",
                    "1.4g",
                    "autossh is a program to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic",
                    "meta-networking (master branch)",
                ),
            )

    def test_parse_search_ssh(self):
        with open("tests/ssh.html", "r", encoding="UTF-8") as f:
            tree = parse_html(f.read())

            self.assertListEqual(
                list(islice(parse_search_table(tree), 3)),
                [
                    (
                        "autossh",
                        "1.4g",
                        "autossh is a program to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic",
                        "meta-networking",
                    ),
                    (
                        "ksshaskpass",
                        "5.26.2",
                        "ssh-add helper that uses kwallet and kpassworddialog",
                        "meta-qt5-extra",
                    ),
                    (
                        "libssh",
                        "0.11.1",
                        "Multiplatform C library implementing the SSHv2 and SSHv1 protocol",
                        "meta-oe",
                    ),
                ],
            )

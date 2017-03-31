# -*- coding: utf-8 -*-

from ...installer import Installer

from .command import Command


class InstallCommand(Command):
    """
    Install and lock dependencies specified in the <comment>poetry.toml</comment> file.

    install
        {--no-dev : Do not install dev dependencies}
    """

    def handle(self):
        dev = not self.option('no-dev')

        installer = Installer(self, self._repository)

        if self.has_lock():
            poet = self.poet.lock
        else:
            poet = self.poet

        installer.install(poet, dev=dev)
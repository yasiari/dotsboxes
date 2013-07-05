# -*- coding: utf-8 -*- 

import os
import sys

from dotsboxes.utils.commands import DotsBoxesCommand

if __name__ == "__main__":

    # arguments ["dostboxes.py", , , ]
    DotsBoxesCommand().get_command(sys.argv)

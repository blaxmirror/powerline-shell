import re
import os
from ..utils import BasicSegment

def get_gsnws_name():
    new_gsnws_pat_match = re.match('^(?:prototype|dev|ref|master|maint)/(\w+)$', os.getenv('GSN_WS_NAME'))
    pat_match = re.match('^\w{7}__ndpgsn_5_0_(?:wb__ndpgsn_5_0_(\w+)|(\w+))$', os.getenv('GSN_WS_NAME'))
    if new_gsnws_pat_match:
        return new_gsnws_pat_match.group(1)
    if not pat_match:
        return ''
    if pat_match.group(1):
        return pat_match.group(1)
    if pat_match.group(2):
        return pat_match.group(2)

class Segment(BasicSegment):
    def add_to_powerline(self):
        if not os.getenv('GSN_WS_NAME'):
            pass
        else: 
            gsnws = get_gsnws_name()
            bg = self.powerline.theme.GSNWS_BG
            fg = self.powerline.theme.GSNWS_FG

            self.powerline.append(" " + gsnws + " ", fg, bg)


# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

define_multipurpose_modmap({
    # Ctrl単押しでEsc
    Key.LEFT_CTRL: [Key.ESC, Key.LEFT_CTRL],

    # Enter同時押しでCtrl
    Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL],

    # SandS
    Key.SPACE: [Key.SPACE, Key.LEFT_SHIFT],
})

# Fn + hjkl
define_keymap(None, {
    K('KPASTERISK'): Key.LEFT,
    K('KPSLASH'): Key.DOWN,
    K('HOME'): Key.UP,
    K('PAGE_UP'): Key.RIGHT,
    K('UP'): Key.PAGE_UP,
    K('DOWN'): Key.PAGE_DOWN,
    K('LEFT'): Key.HOME,
    K('RIGHT'): Key.END,
}, "Vim-like cursor")

# [vscode|terminal]Escしたときに自動でIMEオフ
define_keymap(re.compile('(Code|Gnome-terminal)'), {
    K('esc'): [K('muhenkan'), K('esc')]
}, "Esc and IME off")

# [terminal]C-s後C-q押しても表示再開できないのでpass_through
define_keymap(re.compile('(Gnome-terminal)'), {
    K('C-s'): pass_through_key,
}, "'C-s' pass throush")

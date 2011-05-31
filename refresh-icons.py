#!/usr/bin/env python

# Released to the public domain.
# http://creativecommons.org/publicdomain/zero/1.0/

import ctypes
from ctypes import wintypes

# http://msdn.microsoft.com/en-us/library/ms644950
SendMessageTimeout = ctypes.windll.user32.SendMessageTimeout
SendMessageTimeout.restype = wintypes.LPARAM  # aka LRESULT
SendMessageTimeout.argtypes = [wintypes.HWND, wintypes.UINT, ctypes.WPARAM, ctypes.LPARAM,
                               wintypes.UINT, wintypes.UINT, ctypes.c_void_p]

# http://msdn.microsoft.com/en-us/library/bb762118
SHChangeNotify = ctypes.windll.shell32.SHChangeNotify
SHChangeNotify.restype = None
SHChangeNotify.argtypes = [wintypes.LONG, wintypes.UINT, wintypes.LPCVOID, wintypes.LPCVOID]

HWND_BROADCAST     = 0xffff
WM_SETTINGCHANGE   = 0x001A
SMTO_ABORTIFHUNG   = 0x0002
SHCNE_ASSOCCHANGED = 0x08000000

def main():
    SendMessageTimeout(HWND_BROADCAST, WM_SETTINGCHANGE, 0, 0, SMTO_ABORTIFHUNG, 5000, None)
    SHChangeNotify(SHCNE_ASSOCCHANGED, 0, None, None)

if __name__ == "__main__":
    main()

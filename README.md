With the advent of GNOME 3 I have switched to XFCE. I decided to take 
xmonad-log-applet with me.

This is a fork of [Adam Wick's original GNOME 2 panel 
applet](http://uhsure.com/xmonad-log-applet.html).

This applet (well, it is really a "panel plugin" now..) listens for DBus 
signals at /org/xmonad/Log with the method org.xmonad.Log.Update. This method 
has a single string argument, which is the current XMonad log message. To use 
the applet, you must configure XMonad to send these DBus signals. Look in 
xmonad.hs.example (included in this distribution) for a working example.

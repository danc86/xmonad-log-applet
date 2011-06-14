AC_INIT([XMonad Log Applet], [1.1.0], [djc@djc.id.au], [xmonad-log-applet],
    [https://github.com/danc86/xmonad-log-applet])

AC_PREFIX_DEFAULT([/usr])
AC_PROG_CC
AC_PROG_SED
AC_PROG_INSTALL
AC_HEADER_STDC

PKG_CHECK_MODULES([GLIB], [glib-2.0 >= 2.20.0])
PKG_CHECK_MODULES([DBUS_GLIB], [dbus-glib-1 >= 0.80])
PKG_CHECK_MODULES([LIBXFCE4PANEL], [libxfce4panel-1.0 >= 4.6.0])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

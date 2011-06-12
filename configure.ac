AC_INIT([XMonad Log Applet], [1.0.0], [awick@uhsure.com], [xmonad-log-applet])

AC_PREFIX_DEFAULT([/usr])
AC_PROG_CC
AC_PROG_SED
AC_PROG_INSTALL
AC_HEADER_STDC

PKG_CHECK_MODULES([GLIB], [glib-2.0 >= 2.20.0])
PKG_CHECK_MODULES([DBUS_GLIB], [dbus-glib-1 >= 0.80])
PKG_CHECK_MODULES([LIBPANEL], [libpanelapplet-2.0 >= 2.26.0])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

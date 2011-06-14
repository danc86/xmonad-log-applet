Name:		xmonad-log-applet
Version:	1.0.0
Release:	1%{?dist}
Summary:	A little applet that grabs logging output from Xmonad

Group:		User Interface/X
License:	BSD
URL:		http://uhsure.com/xmonad-log-applet.html
Source0:	xmonad-log-applet.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  xfce4-panel-devel

%description
XFCE panel plugin to display XMonad log messages, received over DBus.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root,-)
%{_libexecdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/xmonad48.png
%doc LICENSE README.md



%changelog
* Mon Aug 15 2010 Adam Wick <awick@uhsure.com> - 1.0.0-1
- Initial spec file

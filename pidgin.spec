# OPTION: perl split into subpackages (FC1+)
%define perl_integration	1
# OPTION: krb5 for Zephyr protocol (FC1+)
%define krb_integration		1
# OPTION: gtkspell integration (FC1+)
%define gtkspell_integration	1
# OPTION: Preferred Applications with gnome-open (FC1+)
%define gnome_open_integration	1
# OPTION: Evolution 1.5+ integration (FC3+)
%define evolution_integration	1
# OPTION: SILC integration (FC3+)
%define silc_integration	1
# OPTION: dbus integration (FC5+)
%define dbus_integration	1
# OPTION: gstreamer integration (FC5+)
%define gstreamer_integration	1
# OPTION: NetworkManager integration (FC5+)
%define nm_integration	        1
# OPTION: Modular X (FC5+)
%define modular_x               1
# OPTION: dbus-glib split (FC6+)
%define dbus_glib_splt		1
# OPTION: Bonjour support (FC6+)
%define bonjour_support		1
# OPTION: Meanwhile integration (F6+)
%define meanwhile_integration	1
# OPTION: Perl devel separated out (F7+)
%define perl_devel_separated    1

Name:		pidgin
Version:	2.2.0
Release:	3%{?dist}
License:        GPLv2+ and GPLv2 and MIT
# GPLv2+ - libpurple, gnt, finch, pidgin, most prpls
# GPLv2 - silc & novell prpls
# MIT - Zephyr prpl
Group:		Applications/Internet
URL:		http://pidgin.im/
Source0:	http://download.sourceforge.net/pidgin/pidgin-%{version}.tar.bz2
Obsoletes:      gaim < 999:1
Provides:       gaim = 999:1
ExcludeArch:    s390 s390x

## Fedora pidgin defaults - Please Regenerate for Each Major Release
# 1) run pidgin as new user 2) edit preferences 3) close 4) copy .purple/prefs.xml
# - enable ExtPlacement plugin
# - enable History plugin
# - enable Message Notification plugin
#   Insert count of new messages into window title
#   Set window manager "URGENT" hint
# - disable buddy icon in buddy list
# - enable Logging (in HTML)
# - Browser "GNOME Default"
# - Smiley Theme "Default"
Source1:	purple-fedora-prefs.xml


## Patches 0-99: Fedora specific or upstream wont accept

## Patches 100+: To be Included in Future Upstream
Patch100:         pidgin-2.2.0-plug_memleaks.patch 
Patch101:         pidgin-2.2.0-fix-proxy-settings.patch
Patch102:         pidgin-2.2.0-fix-status-scores.patch
Patch103:         pidgin-2.2.0-plug-more-memleaks.patch
Patch113: pidgin-2.0.0-beta7-reread-resolvconf.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Summary:	A Gtk+ based multiprotocol instant messaging client

# Require Binary Compatible glib
# returns bogus value if glib2-devel is not installed in order for parsing to succeed
# bogus value wont make it into a real package
%define glib_ver %([ -a %{_libdir}/pkgconfig/glib-2.0.pc ] && pkg-config --modversion glib-2.0 | cut -d. -f 1,2 || echo -n "999")
BuildRequires:	glib2-devel
Requires:       glib2 >= %{glib_ver}
# Require exact libpurple
Requires:       libpurple = %{version}-%{release}

Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2

# Basic Library Requirements
BuildRequires:  autoconf
BuildRequires:	startup-notification-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:	mozilla-nss-devel
BuildRequires:	gtk2-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  libxml2-devel

# krb5 needed for Zephyr (FC1+)
%if %{krb_integration}
BuildRequires:	krb5-devel
%endif
# gtkspell integration (FC1+)
%if %{gtkspell_integration}
BuildRequires:	gtkspell-devel, aspell-devel
%endif
# Preferred Applications (FC1+)
%if %{gnome_open_integration}
Requires:	libgnome
%else
Requires:	htmlview
%endif
# Evolution integration (FC3+)
%if %{evolution_integration}
BuildRequires:	evolution-data-server-devel
%endif
# SILC integration (FC3+)
%if %{silc_integration}
BuildRequires:	libsilc-devel
%endif
# DBus integration (FC5+)
%if %{dbus_integration}
BuildRequires:  dbus-devel >= 0.60
BuildRequires:  python     >= 2.4
%endif
# GStreamer integration (FC5+)
%if %{gstreamer_integration}
BuildRequires:	gstreamer-devel >= 0.10
%endif
# NetworkManager integration (FC5+)
%if %{nm_integration}
%ifnarch s390 s390x
# No NetworkManager on s390/s390x
BuildRequires:	NetworkManager-glib-devel
%endif
%endif
# Modular X (FC5+)
%if %{modular_x}
BuildRequires:  libSM-devel
BuildRequires:  libXScrnSaver-devel
%endif
# DBus GLIB Split (FC6+)
%if %{dbus_glib_splt}
BuildRequires:  dbus-glib-devel >= 0.70
%endif
%if %{bonjour_support}
BuildRequires:	avahi-devel
%endif
# Meanwhile integration (F7+)
%if %{meanwhile_integration}
BuildRequires:	meanwhile-devel
%endif
# Perl devel separated out (F7+)
%if %{perl_devel_separated}
BuildRequires:  perl-devel
%endif


%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple and
Zephyr.  These protocols are implemented using a modular, easy to
use design.  To use a protocol, just add an account using the
account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.


%package devel
Summary: Development headers and libraries for pidgin
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libpurple-devel = %{version}-%{release}
Requires: pkgconfig
Requires: gtk2-devel
Obsoletes: gaim-devel
Provides:  gaim-devel


%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%if %{perl_integration}
%package perl
Summary:    Perl scripting support for Pidgin
Group:      Applications/Internet
Requires:   libpurple = %{version}-%{release}
Requires:   libpurple-perl = %{version}-%{release}

%description perl
Perl plugin loader for Pidgin. This package will allow you to write or
use Pidgin plugins written in the Perl programming language.
%endif


%package -n libpurple
Summary:    libpurple library for IM clients like Pidgin and Finch
Group:      Applications/Internet
# Ensure elimination of gaim.i386 on x86_64
Obsoletes: gaim < 999:1
%if %{meanwhile_integration}
Obsoletes:  gaim-meanwhile
%endif
Requires:   glib2 >= %{glib_ver}
# Bug #212817 Jabber needs cyrus-sasl plugins for authentication
Requires: cyrus-sasl-plain, cyrus-sasl-md5

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.


%package -n libpurple-devel
Summary:    Development headers, documentation, and libraries for libpurple
Group:      Applications/Internet
Requires:   libpurple = %{version}-%{release}
Requires:   pkgconfig
%if %{dbus_integration}
Requires:   dbus-devel >= 0.60
%endif
%if %{dbus_glib_splt}
Requires:   dbus-glib-devel >= 0.70
%endif

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%if %{perl_integration}
%package -n libpurple-perl
Summary:    Perl scripting support for libpurple
Group:      Applications/Internet
Requires:   libpurple = %{version}-%{release}

%description -n libpurple-perl
Perl plugin loader for libpurple. This package will allow you to write or
use libpurple plugins written in the Perl programming language.
%endif


%package -n libpurple-tcl
Summary:    Tcl scripting support for libpurple
Group:      Applications/Internet
Requires:   libpurple = %{version}-%{release}

%description -n libpurple-tcl
Tcl plugin loader for libpurple. This package will allow you to write or
use libpurple plugins written in the Tcl programming language.


%package -n finch
Summary:    A text-based user interface for Pidgin
Group:      Applications/Internet
Requires:   glib2 >= %{glib_ver}

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.


%package -n finch-devel
Summary:    Headers etc. for finch stuffs
Group:      Applications/Internet
Requires:   finch = %{version}-%{release}
Requires:   libpurple-devel = %{version}-%{release}
Requires:   pkgconfig
Requires:   ncurses-devel

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.



%prep
%setup -q
## Patches 0-99: Fedora specific or upstream wont accept

## Patches 100+: To be Included in Future Upstream
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch113 -p1

# Relabel internal version for support purposes
sed -i "s/%{version}/%{version}-%{release}/g" configure
chmod 755 configure

# If not using gnome-open, then default to htmlview 
cp %{SOURCE1} prefs.xml
if [ "%{gnome_open_integration}" == "0" ]; then
	sed -i "s/gnome-open/custom/g" prefs.xml
	sed -i "s/pref name='command' type='string' value=''/pref name='command' type='string' value='htmlview'/" prefs.xml
fi


%build
SWITCHES=""
%if %{krb_integration}
	SWITCHES="$SWITCHES --with-krb4"
%endif
%if %{silc_integration}
	SWITCHES="$SWITCHES --with-silc-includes=%{_includedir}/silc --with-silc-libs=%{_libdir}"
%endif
%if %{perl_integration}
	SWITCHES="$SWITCHES --enable-perl"
%else
	SWITCHES="$SWITCHES --disable-perl"
%endif
%if %{dbus_integration}
	SWITCHES="$SWITCHES --enable-dbus"
%else
	SWITCHES="$SWITCHES --disable-dbus"
%endif
%if %{nm_integration}
	SWITCHES="$SWITCHES --enable-nm"
%endif
%if %{gstreamer_integration}
	SWITCHES="$SWITCHES --enable-gstreamer"
%else
	SWITCHES="$SWITCHES --disable-gstreamer"
%endif

# FC5+ automatic -fstack-protector-all switch
export RPM_OPT_FLAGS=${RPM_OPT_FLAGS//-fstack-protector/-fstack-protector-all}
export CFLAGS="$RPM_OPT_FLAGS"

# gnutls is buggy so use mozilla-nss on all distributions
%configure --enable-gnutls=no --enable-nss=yes --enable-cyrus-sasl \
           --enable-tcl --enable-tk \
           --disable-schemas-install $SWITCHES

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

desktop-file-install --vendor pidgin --delete-original       \
  --add-category X-Red-Hat-Base                            \
  --copy-generic-name-to-name                              \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications            \
  $RPM_BUILD_ROOT%{_datadir}/applications/pidgin.desktop

# remove libtool libraries and static libraries
rm -f `find $RPM_BUILD_ROOT -name "*.la" -o -name "*.a"`
# remove the old perllocal.pod file
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
# remove relnot.so plugin since it is unusable for our package
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/relnot.so
# remove dummy nullclient
rm -f $RPM_BUILD_ROOT%{_bindir}/nullclient
# install Fedora pidgin default prefs.xml
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/purple/
install -m 644 prefs.xml $RPM_BUILD_ROOT%{_sysconfdir}/purple/prefs.xml

%if %{perl_integration}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif

# make sure that we can write to all the files we've installed
# so that they are properly stripped
chmod -R u+w $RPM_BUILD_ROOT/*

%find_lang pidgin

# symlink /usr/bin/gaim to new pidgin name
ln -sf %{_bindir}/pidgin $RPM_BUILD_ROOT%{_bindir}/gaim

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
                %{_sysconfdir}/gconf/schemas/purple.schemas >/dev/null || :
    killall -HUP gconfd-2 &> /dev/null || :
fi

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
            %{_sysconfdir}/gconf/schemas/purple.schemas > /dev/null || :
killall -HUP gconfd-2 &> /dev/null || :

%post -n libpurple -p /sbin/ldconfig

%post -n finch -p /sbin/ldconfig

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
                %{_sysconfdir}/gconf/schemas/purple.schemas > /dev/null || :
    killall -HUP gconfd-2 &> /dev/null || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun -n libpurple -p /sbin/ldconfig

%postun -n finch -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc NEWS COPYING AUTHORS README ChangeLog doc/PERL-HOWTO.dox
%{_bindir}/pidgin
%{_bindir}/gaim
%{_libdir}/pidgin/
%{_mandir}/man1/pidgin.*
%{_datadir}/applications/pidgin.desktop
%{_datadir}/pixmaps/pidgin/
%{_datadir}/icons/hicolor/*/apps/pidgin.*
%{_sysconfdir}/gconf/schemas/purple.schemas

%if %{perl_integration}
%files perl
%defattr(-,root,root,-)
%{_mandir}/man3/Pidgin*
%{perl_vendorarch}/Pidgin.pm
%dir %{perl_vendorarch}/auto/Pidgin/
%{perl_vendorarch}/auto/Pidgin/Pidgin.so
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/pidgin/
%{_libdir}/pkgconfig/pidgin.pc

%files -f pidgin.lang -n libpurple
%{_libdir}/purple-2/
%{_libdir}/libpurple.so.*
%{_datadir}/pixmaps/purple/
%{_datadir}/sounds/purple/
%{_datadir}/purple/ca-certs/
%{_sysconfdir}/purple/
%if %{dbus_integration}
%{_bindir}/purple-client-example
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-url-handler
%{_libdir}/libpurple-client.so.*
#%{_datadir}/dbus-1/services/pidgin.service
%doc libpurple/purple-notifications-example
%endif
%exclude %{_libdir}/purple-2/tcl.so
%if %{perl_integration}
%exclude %{_libdir}/purple-2/perl.so
%endif

%files -n libpurple-devel
%{_datadir}/aclocal/purple.m4
%{_libdir}/libpurple.so
%{_includedir}/libpurple/
%{_libdir}/pkgconfig/purple.pc
%if %{dbus_integration}
%{_libdir}/libpurple-client.so
%endif

%if %{perl_integration}
%files -n libpurple-perl
%{_mandir}/man3/Purple*
%{_libdir}/purple-2/perl.so
%{perl_vendorarch}/Purple.pm
%dir %{perl_vendorarch}/auto/Purple/
%{perl_vendorarch}/auto/Purple/Purple.so
%{perl_vendorarch}/auto/Purple/autosplit.ix
%endif

%files -n libpurple-tcl
%{_libdir}/purple-2/tcl.so

%files -n finch
%{_bindir}/finch
%{_libdir}/finch/
%{_libdir}/gnt/
%{_libdir}/libgnt.so.*
%{_mandir}/man1/finch.*

%files -n finch-devel
%{_includedir}/finch/
%{_includedir}/gnt/
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/gnt.pc


%changelog
* Sat Sep 29 2007 Michel Salim <michel.sylvan@gmail.com> - 2.2.0-3
- Build against avahi proper instead of its HOWL compatibility layer

* Tue Sep 18 2007 Warren Togami <wtogami@redhat.com> - 2.2.0-2
- License clarification
- Backport patches to fix memory leaks
- Backport patches to fix proxy settings & status scores

* Tue Sep 18 2007 Warren Togami <wtogami@redhat.com> - 2.2.0-1
- 2.2.0

* Mon Aug 20 2007 Warren Togami <wtogami@redhat.com> - 2.1.1-1
- 2.1.1

* Wed Aug 15 2007 Warren Togami <wtogami@redhat.com> - 2.1.0-2
- Upstream fix backports
  115: gmail-notification-crash #2323
  117: drag-and-drop-mouse-click-group-header #2333
  118: jabber-confirm-authentication-unencrypted-crash #2493

* Mon Aug 6 2007 Warren Togami <wtogami@redhat.com>
- require exact version of libpurple (#250720)

* Mon Jul 30 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.1.0-1
- 2.1.0
- Only include translations in libpurple instead of duplicating them in
  packages that depend on libpurple anyway

* Tue Jun 19 2007 Warren Togami <wtogami@redhat.com> - 2.0.2-3
- libpurple obsoletes and provides gaim
  This smoothens multilib the upgrade path.

* Fri Jun 15 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.2-1
- 2.0.2

* Wed Jun 6 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-5
- Enable Bonjour support (#242949)
- Fix building against latest evolution-data-server

* Tue Jun 5 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-4
- Fix purple-remote for AIM & ICQ accounts (#240589)
- Add missing Requires to -devel packages
- Add missing BuildRequires for libxml2-devel

* Fri May 31 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-2
- Call g_thread_init early (#241883)
- Fix purple-remote syntax error (#241905)

* Mon May 28 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-1
- 2.0.1

* Wed May 9 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-3
- Split out Perl plugin support into subpackages
- Add Tcl plugin support in a subpackage

* Sun May 6 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-2
- Silence errors when gconfd-2 is not running

* Sat May 5 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-1.1
- Add perl-devel to BuildRequires

* Fri May 4 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-1
- 2.0.0
- Add scriptlets to install & uninstall GConf schemas
- Move schema file from libpurple to Pidgin to avoid GConf
  dependencies in libpurple
- rename gaim-fedora-prefs.xml to purple-fedora-prefs.xml

* Tue May 1 2007 Stu Tomlinson <stu@nosnilmot.com>
- Update Gtk icon cache when installing or uninstalling (#238621)
- Don't own all directories we put icons in

* Mon Apr 30 2007 Warren Togami <wtogami@redhat.com> - 2.0.0-0.36.beta7
- pidgin-2.0.0beta7, bug fixes and pref migration handling

* Sat Apr 21 2007 Warren Togami <wtogami@redhat.com> - 2.0.0-0.35.beta7devel
- upstream insists that we remove the Epoch
  rawhide users might need to use --oldpackage once to upgrade
- remove mono and howl cruft

* Wed Apr 18 2007 Stu Tomlinson <stu@nosnilmot.com> - 2:2.0.0-0.34.beta7devel
- Split into pidgin, finch & libpurple, along with corresponding -devel RPMs
- Remove ldconfig for plugin directories
- Fix non-UTF8 %%changelog

* Tue Apr 17 2007 Warren Togami <wtogami@redhat.com> 
- -devel req pkgconfig (#222488)

* Mon Apr 16 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.33.beta7devel
- pidgin-2.0.0 snapshot prior to beta7
- rename gaim to pidgin/purple/finch in various places of spec (not complete)
- ExcludeArch s390, s390x.  It never did work there.
- Include meanwhile plugin by moving to Extras

* Fri Mar 23 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.31.beta6
- Removed debian-02_gnthistory-in-gtk
  Removed debian-03_gconf-gstreamer.patch
  Upstream recommended removing these patches.
- Add fix-buggy-fetch-url
- Enable type_chat and type_chat_nick in default prefs.xml

* Sat Jan 20 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.30.beta6
- 2.0.0 beta6

* Thu Jan 18 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.29.beta5
- Debian patch 17_upnp_crash
- Debian patch 18_jabber-roster-crash

* Mon Dec 11 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.28.beta5
- Debian patch 13_yahoo_webauth_disable
  temporarily disable the broken yahoo web auth fallback

* Wed Dec 06 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.27.beta5
- Debian patch 12_gstreamer-cleanup, hopefully fixes #218070

* Tue Dec 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.26.beta5
- Jabber SASL Authentication Crash (#217335)

* Wed Nov 29 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.25.beta5
- GTK File dialog blanked fix (#217768)

* Tue Nov 28 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.24.beta5
- Debian patch 10_text-arrow-keys
- Debian patch 11_reread-resolvconf

* Sun Nov 26 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.23.beta5
- Debian patch 08_jabber-info-crash

* Tue Nov 21 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.22.beta5
- 2.0.0 beta5
- Debian patches
    02_gnthistory-in-gtk
    03_gconf-gstreamer
    04_blist-memleak
    05_url-handler-xmpp
    06_jabber-registration-srv
    07_msn-custom-smiley-crash
- SILC Account Edit Crash

* Tue Nov 21 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.21.beta4
- #212817 Jabber needs cyrus-sasl plugins for authentication

* Wed Nov 15 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.20.beta4
- #215704 Revert Yahoo protocol version identifier

* Wed Nov 8 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.19.beta4
- buildreq NetworkManager-glib-devel FC5+ (katzj)
- #213800 debug window freeze fix
- #212818 IRC SIGPIPE crash fix

* Wed Oct 25 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.17.beta4
- temporary workaround for gstreamer build bug in beta4
  --enable-gstreamer prevented it from working =)
  NOTE: beta4 removed libao support entirely.  Distros that lack gstreamer-0.10+
  will need to use command line sound output from now on.
- Gadu Gadu is re-included in beta4 without requirement of external library

* Mon Oct 23 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.16.beta4
- 2.0.0 beta4
- gaim-text ncurses interface!
- gstreamer integration with FC5+

* Thu Oct 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.15.beta3
- delete config.h correctly (rvokal)

* Thu Oct 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.14.beta3
- Fix multilib conflict in -devel (#205206)

* Sat Sep 30 2006 Matthias Clasen <mclasen@redhat.com> - 2:2.0.0-0.13.beta3
- Make the tray icon work with transparent panels (#208706)

* Mon Jul 31 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.11.beta3
- rebuild for new libebook

* Tue Jul 25 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.9.beta3
- fix crash with certain UTF-8 names in buddy list (#199590)

* Sat Jul 22 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.8.beta3
- move gaim.pc to -devel (#199761)

* Wed Jul 19 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.7.beta3
- cleanup spec and update default pref

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2:2.0.0-0.6.beta3.2
- Add BR for dbus-glib-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:2.0.0-0.6.beta3.1
- rebuild

* Wed Jul 05 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.6.beta3
- SILC blank realname failure fix (#173076)

* Thu Jun 29 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.5.beta3
- buildreq libSM-devel (#197241)

* Wed Jun 28 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.4.beta3
- rebuild against libsilc-1.0.2

* Tue Jun 27 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.3.beta3
- more spec cleanups
- buildreq libXScrnSaver-devel, gettext, intltool, desktop-file-utils
- disable mono for now due to #196877

* Mon Jun 26 2006 Tom "spot" Callaway <tcallawa@redhat.com>
- split out -devel package to meet guidelines

* Mon Jan 23 2006 Tom "spot" Callaway <tcallawa@redhat.com>
- gaim2 version of the spec

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-9
- Ensure that security opt flags are used (#165795)
- Many bug fixes from Peter Lawler (#171350)
  156: Fix Yahoo chatroom ignore on join
  157: Fix Italian yahoo profiles
  158: Strip HTML from status
  159: xmlnode cleanup
  160: Fix crash on non-terminated strings
  161: silc-close-gaim_request-window-prpl-disconnect-p1
  162: silc-close-gaim_request-window-prpl-disconnect-p2
  163: silc-close-gaim_request-window-prpl-disconnect-p3
  164: silc-close-gaim_request-window-prpl-disconnect-p4
  165: silc-close-gaim_request-window-prpl-disconnect-p5
  166: silc-close-gaim_request-window-prpl-disconnect-p6
  167: MSN data corruption fix
  168: msn-kill-convo-close-timeout-notices-p1
  169: msn-kill-convo-close-timeout-notices-p2
  170: msn-kill-convo-close-timeout-notices-p3
  171: forceful-connection_disconnect-not-wipe-password
  172: Clipboard leak and history scrolling fix
  173: smileys-logtype-p1
  174: smileys-logtype-p2
  175: Allow Italics in IRC
  176: Add more authors
  177: Update copyright
  178: Update HACKING doc
  179: Fix doc creation
  180: Fix AIM/ICQ Rate Limiting issue

* Thu Oct 13 2005 Ray Strode <rstrode@redhat.com> - 1:1.5.0-7
- use upstream desktop file (except use generic name, because 
  this is our default instant messaging client)

* Tue Sep 27 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-6
- remove -Wno-pointer-sign, not sure why it was needed earlier
- fix FORTIFY_SOURCE on FC3

* Thu Sep 15 2005 Jeremy Katz <katzj@redhat.com> - 1:1.5.0-5
- rebuild for new e-d-s

* Sun Aug 21 2005 Peter Jones <pjones@redhat.cm> - 1:1.5.0-4
- rebuild for new cairo, add -Wno-pointer-sign
- add -Wno-pointer-sign until somebody maintaining this package makes it build
  without it.

* Sun Aug 14 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-2
- always use -z relro and FORTIFY_SOURCE opt flags for FC3+ and RHEL4+ 
  (compiler simply ignores these flags if they are unsupported)

* Thu Aug 11 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-1
- 1.5.0 security and bug fixes
  CAN-2005-2370 Gadu-Gadu memory alignment bug
  CAN-2005-2102 AIM/ICQ non-UTF-8 Filename Crash
  CAN-2005-2103 AIM/ICQ away message buffer overflow

* Tue Aug  9 2005 Jeremy Katz <katzj@redhat.com> - 1:1.4.0-7
- rebuild for new evolution-data-server

* Mon Aug  1 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-6
- FC5+ bash regex replace for -fstack-protector-all (mharris)

* Sun Jul 31 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-5
- FC5+ automatic -fstack-protector-all switch
- 150: MSN buddy names with space disconnect and profile corruption
       (supercedes patch 149)
- 151: Gadu Gadu memory alignment crash
- 152: Rename Group Merge crash
- 153: mailto: parse crash (util.c)
- 154: mailto: parse crash (MSN)
- 155: mailto: parse crash (Zephyr)

* Mon Jul 11 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-4
- 149: MSN username with space disconnect fix
- Do not own perl dir, remove empty files (#162994 jpo)

* Sun Jul 10 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-2
- 148: AIM login crash fix

* Thu Jul 07 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-1
- 1.4.0

* Thu Jun 09 2005 Warren Togami <wtogami@redhat.com> 1:1.3.1-0
- 1.3.1 more bug fixes
  CAN-2005-1269 CAN-2005-1934
- enable Message Notification plugin by default

* Tue May 10 2005 Warren Togami <wtogami@redhat.com> 1:1.3.0-1
- 1.3.0 many bug fixes and two security fixes
  long URL crash fix (#157017) CAN-2005-1261
  MSN bad messages crash fix (#157202) CAN-2005-1262

* Thu Apr 07 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-4
- use mozilla-nss everywhere because gnutls is buggy (#135778)

* Wed Apr 06 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-2
- 147: drag-n-drop URL crash fix

* Sun Apr 03 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-1
- update to 1.2.1 CAN-2005-0965 CAN-2005-0966 CAN-2005-0967

* Fri Mar 18 2005 Warren Togami <wtogami@redhat.com> 1:1.2.0-1
- update to 1.2.0 (minor bug fixes)

* Mon Mar 07 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-5
- Copy before modifying prefs.xml

* Sun Mar 06 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-4
- 144: POSIX functions became macros, build fix (#150429)
- 145: Fix non-proxy yahoo file transfer
- 146: Fix non-proxy yahoo buddy icons

* Fri Mar 04 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-3
- 143: Gadu Gadu protocol crash fix (#149984)

* Mon Feb 28 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-2
- remove gcc4 conditional since FC4 is gcc4 default

* Thu Feb 24 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-1
- 1.1.4 with MSN crash fix, g_stat() crash workaround
  CAN-2005-0208 Gaim HTML parsing DoS (another one)

* Tue Feb 22 2005 Warren Togami <wtogami@redhat.com> 1:1.1.3-4
- Test fixes for #149190 and #149304

* Mon Feb 21 2005 Dan Williams <dcbw@redhat.com> 1:1.1.3-3
- Work around #149190 gaim-1.1.3-2 segfaults when calling g_stat()

* Fri Feb 18 2005 Warren Togami <wtogami@redhat.com> 1:1.1.3-2
- 1.1.3 including two security fixes
  CAN-2005-0472 Client freezes when receiving certain invalid messages
  CAN-2005-0473 Client crashes when receiving specific malformed HTML

* Fri Jan 28 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Thu Jan 20 2005 Warren Togami <wtogami@redhat.com> 1:1.1.2-1
- 1.1.2 with more bugfixes

* Tue Jan 18 2005 Chip Turner <cturner@redhat.com> 1:1.1.1-3
- rebuild for new perl

* Mon Jan 03 2005 Warren Togami <wtogami@redhat.com> 1.1.1-2
- force required glib2 version

* Tue Dec 28 2004 Warren Togami <wtogami@redhat.com> 1.1.1-1
- 1.1.1 (minor bugfixes)

* Thu Dec 2 2004 Warren Togami <wtogami@redhat.com> 1.1.0-1
- upgrade 1.1.0 (mostly bugfixes)
- fix PIE patch

* Sat Nov 20 2004 Warren Togami <wtogami@redhat.com> 1.0.3-3
- make gcc4 conditional

* Sat Nov 20 2004 Daniel Reed <djr@redhat.com> 1.0.3-2
- Rebuild using gcc4
  - To revert, remove "BuildRequires: gcc4" and "CC=gcc4"

* Fri Nov 12 2004 Warren Togami <wtogami@redhat.com> 1.0.3-1
- 1.0.3 another bugfix release

* Tue Oct 19 2004 Warren Togami <wtogami@redhat.com> 1.0.2-1
- 1.0.2 fixes many crashes, endian and other issues

* Tue Oct 19 2004 Warren Togami <wtogami@redhat.com> 1.0.1-3
- nosnilmot: zephyr krb build was broken by thinko

* Wed Oct 13 2004 Warren Togami <wtogami@redhat.com> 1.0.1-2
- CAN-2004-0891

* Thu Oct 07 2004 Warren Togami <wtogami@redhat.com> 1.0.1-1
- update to 1.0.1
- disable naive GNOME session check
- switch to gnutls default (FC3+)

* Mon Sep 27 2004 Warren Togami <wtogami@redhat.com> 1.0.0-5
- djr fixed PIE
- added gnutls option, disabled and favoring mozilla-nss

* Sat Sep 25 2004 Warren Togami <wtogami@redhat.com> 1.0.0-4
- PIE

* Mon Sep 20 2004 Warren Togami <wtogami@redhat.com> 1.0.0-3
- 141: Jabber chat room list fix

* Mon Sep 20 2004 Daniel Reed <djr@redhat.com> 1.0.0-2
- #132967 Remove GenericName

* Sat Sep 18 2004 Warren Togami <wtogami@redhat.com> 1.0.0-1
- 1.0.0

* Wed Sep 01 2004 Warren Togami <wtogami@redhat.com> 0.82.1-2
- enable SILC protocol

* Thu Aug 26 2004 Warren Togami <wtogami@redhat.com> 0.82.1-1
- new upstream point release with crash fix and added translation

* Wed Aug 25 2004 Warren Togami <wtogami@redhat.com> 0.82-2
- 140: Buddy icon pref changing crash fix

* Wed Aug 25 2004 Warren Togami <wtogami@redhat.com> 0.82-1
- Update to 0.82 resolves several security issues and bugs
  CAN-2004-0500, CAN-2004-0754, CAN-2004-0784, CAN-2004-0785
  More details at http://gaim.sourceforge.net/security/

* Mon Aug 16 2004 Warren Togami <wtogami@redhat.com> 0.81-7
- CVS backport 138: GTK Prefs bug fix

* Sun Aug 15 2004 Warren Togami <wtogami@redhat.com> 0.81-6
- CVS backport 137: System Log viewer fd leak

* Sun Aug 15 2004 Warren Togami <wtogami@redhat.com> 0.81-5
- fix substitution for browser back compat
- req fix for htmlview back compat
- update prefs.xml

* Fri Aug 13 2004 Warren Togami <wtogami@redhat.com> 0.81-4
- conditionalize features for alternate target distributions
- remove unnecessary ExclusiveArch
- other cleanups

* Wed Aug 11 2004 Warren Togami <wtogami@redhat.com> 0.81-3
- CVS backport 133: CAN-2004-0500 MSNLP buffer overflow
               134: Select buddy icon in new account crash
               135: Jabber join crash
               136: Jabber tooltip fake self crash

* Mon Aug  9 2004 Daniel Reed <djr@redhat.com> 0.81-2
- #125847 Change gaim.desktop names to "IM"

* Thu Aug 05 2004 Warren Togami <wtogami@redhat.com> 0.81-1
- 0.81
- krb5-devel for Zephyr
- evolution-data-server-devel integration
  plugin disabled by default because it seems very unstable

* Sun Jul 18 2004 Warren Togami <wtogami@redhat.com> 0.80-3
- CVS backport 130, 131: MSN buddy scaling issue fix
               132: Drag and Drop crash fix

* Sat Jul 17 2004 Warren Togami <wtogami@redhat.com> 0.80-2
- CVS backport 129: IRC buddy list flood disconnect fix

* Fri Jul 16 2004 Warren Togami <wtogami@redhat.com> 0.80-1
- update to 0.80
- enable ExtPlacement plugin by default
- Smiley Theme "Default" by default (bug fix)
- Insertions -> Control-{B/I/U} by default

* Mon Jun 28 2004 Warren Togami <wtogami@redhat.com> 0.79-2
- remove tray icon patch temporarily because it seems to cause more
  problems than it solves.
- provide gaim-devel
- CVS backport 128: Cached buddy icons fix

* Fri Jun 25 2004 Warren Togami <wtogami@redhat.com> 0.79-1
- update to 0.79
- update desktop patch
- update header and pkgconfig locations
- update default prefs
- FC3 sed behavior workaround
- temporarily disable evolution integration

* Tue Jun 22 2004 Warren Togami <wtogami@redhat.com> 0.78-8
- rebuilt

* Mon Jun 08 2004 Warren Togami <wtogami@redhat.com> 0.78-7
- CVS backport 125: MSN disconnect on non-fatal error fix
               126: Paste html with img crash fix
               127: Misplaced free fix

* Sat Jun 05 2004 Warren Togami <wtogami@redhat.com> 0.78-4
- CVS backport 123: jabber disconnect fix
               124: log find click fix

* Sun May 30 2004 Warren Togami <wtogami@redhat.com> 0.78-2
- update to 0.78 (without SILC support for now)

* Sun May 09 2004 Warren Togami <wtogami@redhat.com> 0.77-7
- CVS backport 121: byte order badness and crashing copy & paste fix
               122: history.so scroll to bottom in new tabs fix

* Tue May 04 2004 Warren Togami <wtogami@redhat.com> 0.77-6
- CVS backport 118: x86-64 yahoo auth fix
               119: Copy/paste fixes for UCS-2 encoded selection
               120: IRC reconnect segfault fix
- remove relnot.so plugin because it is unusable in FC
- Default enable logging and history.so plugin
          enable autoreconnect plugin
- Fix Gnome Default url handler

* Thu Apr 29 2004 Warren Togami <wtogami@redhat.com> 0.77-3
- remove gnome-open manual, since 0.77 has "GNOME Default" as default.
- update default prefs.xml, disable buddy icons in buddy list
- CVS backport 114: plugin prefs saving fix
               115: autoreconn-suppress-dialogs
               116: fix smileys in dialogs
               117: gtk+ 2.0 compat

* Sun Apr 25 2004 Warren Togami <wtogami@redhat.com> 0.77-1
- 0.77, remove cvs backports

* Fri Apr 15 2004 Warren Togami <wtogami@redhat.com> 0.76-6
- CVS backports:
  111 Prevent Crash during password change if blank fields
  112 Prevent Crash if remote sends invalid characters
  113 Enable /etc/gaim/prefs.xml defaults for new profiles
- Tray Icon enabled by default
- Relabel internal version with V-R

* Fri Apr 14 2004 Warren Togami <wtogami@redhat.com> 0.76-5
- CVS backports: 
  102 Fix ^F keybinding when gtkrc is set to emacs mode
  103 Add Missing File: evolution-1.5.x buildability
  104 When MSN server intermittently has problems accessing buddy list, MSN will crash with 0.76
  105, 106, 107 MSN Error reporting fixes
  108 History plugin causes unnecessary horizontal scrollbars
  109 Fix the text replace plugin 
  110 Prevent message sending while offline

* Fri Apr 09 2004 Warren Togami <wtogami@redhat.com> 0.76-3
- CVS backport: Fix oscar tooltip misbehavior
                Fix yahoo more

* Thu Apr 01 2004 Warren Togami <wtogami@redhat.com> 0.76-2
- 0.76

* Sun Mar 28 2004 Warren Togami <wtogami@redhat.com>
- CVS snapshot
- more spec cleanups

* Tue Mar 16 2004 Warren Togami <wtogami@redhat.com>
- CVS snapshot, generated with automake-1.7.9
- update #4
- update #2 but disable
- #5 no longer needed
- default to gnome-open #6
- some spec cleanup

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 23 2004 Christopher Blizzard <blizzard@redhat.com> 1:0.75-1.1.0
- Include patch that fixes a bunch of buffer-related problems, mostly
  from nectar@freebsd.org and some of my own changes.

* Wed Jan 14 2004 Christopher Blizzard <blizzard@redhat.com> 1:0.75-0
- Update to 0.75.
- Remove mem leak patch that is already included in 0.75.
- Clean up a lot of old unused patches and old source tarballs.

* Fri Dec 12 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-10
- Add patch that fixes a large memory leak.

* Thu Dec 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-9
- Bump release to rebuild for fc2.

* Wed Nov 25 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-0
- Upgrade to 0.74
- Include libao-devel and startup-notification-devel to the
  buildreq list

* Mon Nov 03 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-2
- Add gtk2-devel to the buildreq list.

* Fri Oct 24 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-2
- Include patch that should fix some input problems for ja_JP users

* Fri Oct 17 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-1
- Include patch that updates the tray icon to a more recent version

* Mon Sep 29 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.70-0
- Update to 0.70

* Thu Sep 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.68-0
- Update to 0.68

* Tue Aug 26 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.66-2
- Change Instant Messenger to Messaging Client

* Wed Jul 23 2003 Jeremy Katz <katzj@redhat.com> 1:0.66-1
- 0.66

* Thu Jul 17 2003 Matt Wilson <msw@redhat.com> 1:0.65-1
- 0.65
- don't include .a or .la files

* Tue Jul 15 2003 Matt Wilson <msw@redhat.com> 1:0.64-2
- rebuild against gtkspell

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.64-0
- 0.64

* Mon Apr 14 2003 Matt Wilson <msw@redhat.com> 1:0.61-1
- 0.61
- remove prefs patch, no longer needed

* Wed Apr  9 2003 Matt Wilson <msw@redhat.com> 1:0.59.8-1
- use system libtool (#88340)

* Wed Jan 29 2003 Christopher Blizzard <blizzard@redhat.com> 0.59.8-0
- Update to 0.59.8

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 18 2002 Elliot Lee <sopwith@redhat.com> 0.59-11
- Add libtoolize etc. steps

* Tue Dec 17 2002 Elliot Lee <sopwith@redhat.com> 0.59-10
- Rebuild

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- build on all arches

* Fri Aug 09 2002 Christopher Blizzard <blizzard@redhat.com> 0.59-7
- Include patch that uses htmlview instead of calling Netscape
  directly
- Include patch that turns off the buddy ticker and changes the button
  look to the (sane) default.

* Thu Aug 01 2002 Christopher Blizzard <blizzard@redhat.com>
- Fix .desktop file, and put it in the right place.
- More .desktop file fixes

* Tue Jun 25 2002 Christopher Blizzard <blizzard@redhat.com>
- Update to 0.59.
- Disable perl for now.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 24 2002 Matt Wilson <msw@redhat.com> 0.58-1
- 0.58
- remove applet

* Fri Mar 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.53-1
- Langify

* Wed Mar 13 2002 Christopher Blizzard <blizzard@redhat.com>
- update 0.53

* Thu Feb 21 2002 Christopher Blizzard <blizzard@redhat.com>
- update to 0.52

* Tue Jan 29 2002 Christopher Blizzard <blizzard@redhat.com>
- update to 0.51

* Fri Sep 14 2001 Matt Wilson <msw@redhat.com>
- update to 0.43

* Fri Aug 03 2001 Christopher Blizzard <blizzard@redhat.com>
- Add BuildRequires for gnome-libs-devel (bug #44739)

* Mon Jul 02 2001 Christopher Blizzard <blizzard@redhat.com>
- Add BuildRequires for gnome-core-devel (bug #44739)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Feb 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- make it compile

* Sun Feb 11 2001 Tim Powers <timp@redhat.com>
- updated to 0.11.0pre4 (bug fixes)
- applied Bero's konqueror patch to fix kfm->konq

* Tue Dec  5 2000 Tim Powers <timp@redhat.com>
- updated to 0.11.0pre2
- enable gnome support
- updated ispell to aspell patch
- cleaned up file list

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- updated to 0.10.3

* Fri Nov 10 2000 Tim Powers <timp@redhat.com> 
- update to 0.10.2

* Mon Sep 11 2000 Tim Powers <timp@redhat.com>
- some ideas taken from the package available at the gaim website, mainly to install the applet stuff too.

* Wed Aug 9 2000 Tim Powers <timp@redhat.com>
- added Serial so that we can upgrade from Helix packages from 6.2

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Tue Jul 18 2000 Tim Powers <timp@redhat.com>
- changed default spell checker to aspell from ispell, patched.
- requires aspell

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jun 22 2000 Tim Powers <timp@redhat.com>
- fixed problems with ldconfig PreReq, shouls have been /sbin/ldconfig

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- 0.9.19
- fix ldconfig stuff

* Thu Jun 1 2000 Tim Powers <timp@redhat.com>
- cleaned up spec for use with RPM 4.0 (al la _sysconfdir _datadir etc)
- update to 0.9.17
- yay! a man page!

* Thu May 25 2000 Tim Powers <timp@redhat.com>
- we left a bunch of stuff out, pixmaps, plugins. Fixed
- added applnk entry

* Wed May 10 2000 Tim Powers <timp@redhat.com>
- updated to 0.9.15

* Mon Apr 24 2000 Matt Wilson <msw@redhat.com>
- updated to 0.9.14

* Mon Apr 24 2000 Matt Wilson <msw@redhat.com>
- updated to 0.9.13

* Thu Feb 10 2000 Matt Wilson <msw@redhat.com>
- added patch to prevent floating point errors in lag-o-meter update
  code

* Wed Nov 10 1999 Tim Powers <timp@redhat.com>
- updated to 0.9.10

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- rebuilt and put into Powertools 6.1

* Mon Jul 12 1999 Dale Lovelace <dale@redhat.com>
- First RPM Build

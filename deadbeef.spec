Summary:	A music player with *.cue support
Name:		deadbeef
Version:	0.4.4
Release:	1%{?dist}

Group:		Applications/Multimedia
License:	GPLv2
URL:		http://deadbeef.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/deadbeef/deadbeef-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	faad2-devel
BuildRequires:	libmms-devel
BuildRequires:	gtk2-devel
BuildRequires:	intltool gettext-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcurl-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	wavpack-devel

Requires:	%{name}-plugins = %{version}


%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux systems with X11 
(though now it also runs in plain console without X, in FreeBSD, and in
OpenSolaris).

It is mainly written by Alexey Yakovenko, with contributions from a lot of
different people (see about box in the player for more details).

It is distributed under the terms of General Public License version 2.


%package devel
Summary:	Static library and header files for the %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}


%description devel
The %{name}-devel package contains API documentation for
developing %{name}.

%package plugins
Summary:	Plugins for %{name}
Group:          Applications/Multimedia
Requires:       %{name} = %{version}

%description plugins
This package contains plugins for %{name}


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

install -dD $RPM_BUILD_ROOT%{_datadir}/pixmaps

cp $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/deadbeef.png \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README INSTALL ChangeLog COPYING AUTHORS
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/deadbeef.desktop
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*


%files devel
%defattr(-,root,root,-)
%doc README INSTALL ChangeLog COPYING AUTHORS
%{_includedir}/deadbeef/*

%files plugins
%doc README INSTALL ChangeLog COPYING AUTHORS
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.so.*


%changelog 
* Tue Nov 16 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.4-1
- update to 0.4.4

* Tue Nov  2 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.3-1
- update to 0.4.3

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.2-2
- install deadbeef.png to /usr/share/pixmaps

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.2-1
- initial build for Fedora

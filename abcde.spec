%define name abcde
%define version 2.3.3
%define release %mkrel 2

Summary:	Command-line utility to rip and encode audio cds
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://www.hispalinux.es/~data/files/
Group:		Sound
Source0:	%{URL}/%{name}_%{version}.orig.tar.bz2
Source1:	%{URL}/cd-discid/cd-discid_0.9.orig.tar.bz2
Patch0:		%{URL}/cd-discid_0.9-1.diff
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	cdparanoia wget

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -b0
%setup -q -b1
%patch0 -p0
%build
cd ../cd-discid-0.9
%{__cc} cd-discid.c -o cd-discid
%install
install -D -m755 %{name}	$RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m644 %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -D -m755 cddb-tool	$RPM_BUILD_ROOT%{_bindir}/cddb-tool
install -D -m644 cddb-tool.1	$RPM_BUILD_ROOT%{_mandir}/man1/cddb-tool.1

install -D -m644 %{name}.conf	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

cd ../cd-discid-0.9
install -D -m755 cd-discid	$RPM_BUILD_ROOT%{_bindir}/cd-discid
install -D -m644 cd-discid.1	$RPM_BUILD_ROOT%{_mandir}/man1/cd-discid.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc changelog README COPYING  TODO FAQ  examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/*
%{_mandir}/man1/abcde.1.bz2
%{_mandir}/man1/cd-discid.1.bz2
%{_mandir}/man1/cddb-tool.1.bz2
%config(noreplace) %{_sysconfdir}/%{name}.conf


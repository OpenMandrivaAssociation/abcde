%define name abcde
%define version 2.4.0
%define release %mkrel 1

Summary:	Command-line utility to rip and encode audio cds
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		http://www.hispalinux.es/~data/files/
Group:		Sound
Source0:	http://ftp.de.debian.org/debian/pool/main/a/abcde/%{name}_%{version}.orig.tar.gz
Source1:	http://linukz.org/download/cd-discid-1.1.tar.gz
Patch1:		abcde-2.3.99.6-install.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	cdparanoia wget vorbis-tools

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.


%prep

%setup -q -b0
%setup -q -b1
%patch1 -p0

%build
cd ../cd-discid-1.1
%make

%install
rm -rf %buildroot
%makeinstall_std

cd ../cd-discid-1.1
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr (-,root,root)
%doc changelog README COPYING TODO FAQ examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/*
%{_mandir}/man1/abcde.*
%{_mandir}/man1/cd-discid.*
%{_mandir}/man1/cddb-tool.*
%config(noreplace) %{_sysconfdir}/%{name}.conf


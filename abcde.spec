%define name abcde
%define version 2.3.99.6
%define release %mkrel 1

Summary:	Command-line utility to rip and encode audio cds
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://www.hispalinux.es/~data/files/
Group:		Sound
Source0:	http://ftp.de.debian.org/debian/pool/main/a/abcde/%{name}_%{version}.orig.tar.gz
Source1:	%{URL}/cd-discid/cd-discid_0.9.orig.tar.bz2
Patch1:		abcde-2.3.99.6-install.patch
Patch2:		cd-discid-0.9-install.patch
Requires:	cdparanoia wget vorbis-tools

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -b0
%setup -q -b1
%patch1 -p0
cd ../cd-discid-0.9
%patch2 -p0

%build
cd ../cd-discid-0.9
%make

%install
%makeinstall_std

cd ../cd-discid-0.9
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc changelog README COPYING  TODO FAQ  examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/*
%{_mandir}/man1/abcde.*
%{_mandir}/man1/cd-discid.*
%{_mandir}/man1/cddb-tool.*
%config(noreplace) %{_sysconfdir}/%{name}.conf


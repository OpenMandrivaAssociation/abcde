%define name abcde
%define version 2.9.3
%define release 1

Summary:	Command-line utility to rip and encode audio cds
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		 http://abcde.einval.com
Group:		Sound
Source0:	http://ftp.de.debian.org/debian/pool/main/a/abcde/%{name}_%{version}.orig.tar.gz
Source1:	http://linukz.org/download/cd-discid-1.3.1.tar.gz
Patch1:		abcde-2.3.99.6-install.patch
Requires:	cdparanoia 
Requires: wget 
Requires: vorbis-tools

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.


%prep
%setup -q -b0 -a 1

%patch0 -p1 -b .FIX_MAK
pushd cd-discid-1.3.1
%patch1 -p0
popd

%build
pushd cd-discid-1.3.1
    %make_build
popd

%install
%make_install

pushd cd-discid-1.3.1
    make install PREFIX=%{buildroot}%{_prefix}
popd

%files
%doc changelog COPYING README FAQ
%doc examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/abcde
%{_bindir}/abcde-musicbrainz-tool
%{_bindir}/cd-discid
%{_bindir}/cddb-tool
%{_mandir}/man1/abcde.*
%{_mandir}/man1/cd-discid.*
%{_mandir}/man1/cddb-tool.*
%config(noreplace) %{_sysconfdir}/%{name}.conf

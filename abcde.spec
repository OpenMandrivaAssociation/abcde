%global __requires_exclude perl\\((WebService::MusicBrainz)\\)
%global debug_package %{nil}

Summary:	Command-line utility to rip and encode audio cds
Name:		abcde
Version:	2.9.3
Release:	3
License:	GPLv2
URL:		https://abcde.einval.com
Group:		Sound
#Source0:	http://ftp.de.debian.org/debian/pool/main/a/abcde/%{name}_%{version}.orig.tar.gz
Source0:	https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Source1:	http://linukz.org/download/cd-discid-1.3.1.tar.gz
Patch0:		abcde-2.3.99.6-install.patch
Requires: cdparanoia 
Requires: wget 
Requires: vorbis-tools
Requires: perl(MusicBrainz::DiscID)
Requires: perl(WebService::MusicBrainz)

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.

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

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -b0 -a1

#%%patch0 -p1 -b .FIX_MAK
#pushd cd-discid-1.3.1
#patch1 -p0
#popd

%build
%make_build -C cd-discid-1.3.1

%install
%make_install
%make_install PREFIX=%{buildroot}%{_prefix} -C cd-discid-1.3.1


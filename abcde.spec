%global __requires_exclude perl\\((WebService::MusicBrainz)\\)
%global debug_package %{nil}

Summary:	Command-line utility to rip and encode audio cds
Name:		abcde
Version:	2.9.3
Release:	4
License:	GPLv2
URL:		https://abcde.einval.com
Group:		Sound
#Source0:	https://ftp.de.debian.org/debian/pool/main/a/abcde/%%{name}_%%{version}.orig.tar.gz
Source0:	https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Patch0:		abcde-2.3.99.6-install.patch
Requires:	cd-discid
Requires:	cdparanoia
Requires:	wget
Requires:	vorbis-tools
Requires:	perl(MusicBrainz::DiscID)
Requires:	perl(WebService::MusicBrainz)
Recommends:	glyr
Recommends:	flac
Recommends:	lame
Recommends:	mkcue
Suggests:	cdrdao
Suggests:	imagemagick
Suggests:	normalize
Suggests:	opus-tools
Suggests:	twolame
Suggests:	vorbisgain
Suggests:	wavpack

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.

%prep
%autosetup -p1 -b0

%install
%make_install

%files
%doc changelog COPYING README FAQ
%doc examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/abcde
%{_bindir}/abcde-musicbrainz-tool
%{_bindir}/cddb-tool
%{_mandir}/man1/abcde.*
%{_mandir}/man1/cddb-tool.*
%config(noreplace) %{_sysconfdir}/%{name}.conf

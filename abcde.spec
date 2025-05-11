Summary:	Command-line utility to rip and encode audio cds
Name:		abcde
Version:	2.9.3
Release:	6
License:	GPLv2
URL:		https://abcde.einval.com
Group:		Sound
#Source0:	https://ftp.de.debian.org/debian/pool/main/a/abcde/%%{name}_%%{version}.orig.tar.gz
Source0:	https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Requires:	cd-discid
Requires:	cdparanoia
Requires:	wget
Requires:	which
Requires:	vorbis-tools
Requires:	perl(MusicBrainz::DiscID)
Requires:	perl(WebService::MusicBrainz)
Recommends:	diffutils
Recommends:	glyr
Recommends:	flac
Recommends:	lame
Recommends:	mkcue
Suggests:	cdrdao
Suggests:	imagemagick
Suggests:	mac
Suggests:	normalize
Suggests:	opus-tools
Suggests:	ttaenc
Suggests:	twolame
Suggests:	vorbisgain
Suggests:	wavpack

BuildArch:	noarch

#BuildSystem:	autotools

%patchlist
abcde-2.3.99.6-install.patch
# https://src.fedoraproject.org/rpms/abcde/raw/rawhide/f/abcde-gnudb.patch
abcde-gnudb.patch

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.

%files
%doc changelog COPYING README FAQ
%doc examples/abcded examples/abcde.init examples/autorip.sh
%{_bindir}/abcde
%{_bindir}/abcde-musicbrainz-tool
%{_bindir}/cddb-tool
%{_mandir}/man1/abcde.*
%{_mandir}/man1/cddb-tool.*
%config(noreplace) %{_sysconfdir}/%{name}.conf

#----------------------------------------------------------------------

%prep
%autosetup -p1 -b0

%conf

%build

%install
%make_install



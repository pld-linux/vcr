Name: vcr
Summary: VCR is a program which enables you to record a program using a video grabber card
Version: 1.07
Release: 1
Group: X11/Applications/Multimedia
Copyright: GPL
Url: http://www.stack.nl/~brama/vcr/
Packager: Dag Wieers <dag@wieers.com>
Distribution: N/A 
Source: http://www.stack.nl/~brama/vcr/src/%{name}-%{version}.tar.gz
Requires: avifile
BuildRequires: avifile-devel
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%description
VCR is a program which enables you to record a program using a video 
grabber card that's supported by the video4linux drivers. It doesn't 
require a graphical environment, and you can use all popupular windows 
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the 
avifile library. Now, you can finally record your favourite program from a 
remote place, because Murphy's law dictates that you remember to record it 
when you're as far away from your home as possible...

%prep
%setup

%build
%configure
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/vcr
%{_datadir}/vcr/*
%{_mandir}/man1/vcr.1

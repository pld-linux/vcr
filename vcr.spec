Name:		vcr
Summary:	VCR is a program which enables you to record a program using a video grabber card
Version:	1.07
Release:	1
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Url:		http://www.stack.nl/~brama/vcr/
Source0:	http://www.stack.nl/~brama/vcr/src/%{name}-%{version}.tar.gz
Patch0:		vcr-printf.patch
BuildRequires:	avifile-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
VCR is a program which enables you to record a program using a video
grabber card that's supported by the video4linux drivers. It doesn't
require a graphical environment, and you can use all popupular windows
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the
avifile library. Now, you can finally record your favourite program
from a remote place, because Murphy's law dictates that you remember
to record it when you're as far away from your home as possible...

%prep
%setup -q
%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install 

gzip -9fn AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/vcr
%{_datadir}/vcr
%{_mandir}/man1/*

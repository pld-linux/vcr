Summary:	VCR is a program which enables you to record a program using a video grabber card
Summary(pl):	VCR - program pozwalaj±cy nagrywaæ programy przez video grabber
Name:		vcr
Version:	1.07
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.stack.nl/~brama/vcr/src/%{name}-%{version}.tar.gz
Patch0:		vcr-printf.patch
URL:		http://www.stack.nl/~brama/vcr/
BuildRequires:	avifile-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
VCR is a program which enables you to record a program using a video
grabber card that's supported by the video4linux drivers. It doesn't
require a graphical environment, and you can use all popular windows
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the
avifile library. Now, you can finally record your favourite program
from a remote place, because Murphy's law dictates that you remember
to record it when you're as far away from your home as possible...

%description -l pl
VCR jest programem pozwalaj±cym nagrywaæ programy przy u¿yciu karty
typu video grabber obs³ugiwanej przez sterowniki video4linux. Nie
wymaga graficznego ¶rodowiska, mo¿e byæ u¿ywany z popularnymi
windowsowymi codekami (jak DivX, Indeo Video 5 itp.) poniewa¿ VCR jest
budowany z u¿yciem biblioteki avifile. Teraz mo¿esz wreszcie nagraæ
swój ulubiony program zdalnie, bo zgodnie z prawami Murphy'ego
przypomnisz sobie o nagraniu wtedy, kiedy bêdziesz najdalej od domu...

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

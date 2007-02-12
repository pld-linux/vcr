Summary:	VCR is a program which enables you to record a program using a video grabber card
Summary(pl.UTF-8):   VCR - program pozwalający nagrywać programy przez video grabber
Name:		vcr
Version:	1.09
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.stack.nl/~brama/vcr/src/%{name}-%{version}.tar.gz
# Source0-md5:	18a41f998647b8e32f07de3c9f899009
Patch0:		%{name}-DEBIAN.patch
Patch1:		%{name}-ac_fixes.patch
URL:		http://www.stack.nl/~brama/vcr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCR is a program which enables you to record a program using a video
grabber card that's supported by the video4linux drivers. It doesn't
require a graphical environment, and you can use all popular windows
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the
avifile library. Now, you can finally record your favourite program
from a remote place, because Murphy's law dictates that you remember
to record it when you're as far away from your home as possible...

%description -l pl.UTF-8
VCR jest programem pozwalającym nagrywać programy przy użyciu karty
typu video grabber obsługiwanej przez sterowniki video4linux. Nie
wymaga graficznego środowiska, może być używany z popularnymi
windowsowymi kodekami (jak DivX, Indeo Video 5 itp.) ponieważ VCR jest
budowany z użyciem biblioteki avifile. Teraz możesz wreszcie nagrać
swój ulubiony program zdalnie, bo zgodnie z prawami Murphy'ego
przypomnisz sobie o nagraniu wtedy, kiedy będziesz najdalej od domu...

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-avifile-0_6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/vcr
%{_datadir}/vcr
%{_mandir}/man1/*

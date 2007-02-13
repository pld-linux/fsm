%define		fversion	%(echo %{version} |tr . _)
Summary:	Finite-State Machine Library
Summary(pl.UTF-8):	Biblioteka automatów skończonych
Name:		fsm
Version:	4.0
Release:	1
License:	Free for educational use, non-distributable
Group:		Applications/Text
# from http://akpublic.research.att.com/cgi-bin/access.cgi/as/vt/ext-software/www-ne-license.cgi?form.fsm.binary
Source0:	%{name}-%{fversion}.linux.i386.tar.gz
URL:		http://www.research.att.com/sw/tools/fsm/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FSM library is a set of general-purpose software tools available
for Unix, for building, combining, optimizing, and searching weighted
finite-state acceptors and transducers. Finite-state transducers are
automata for which each transition has an output label in addition to
the more familiar input label. Weighted acceptors or transducers are
acceptors or transducers in which each transition has a weight as well
as the input or input and output labels.

%description -l pl.UTF-8
Biblioteka FSM to zbiór narzędzi ogólnego przeznaczenia dostępnych dla
Uniksa służących do budowania, łączenia, optymalizacji i
przeszukiwania akceptorów i transduktorów ważonych o skończonej
liczbie stanów. Transduktory skończone to automaty, dla których każde
przejście ma etykietę wyjściową oprócz bardziej znanej etykiety
wejściowej. Akceptory i transduktory ważone to akceptory i
transduktory, w których każde przejście ma wagę oprócz etykiety
wejściowej lub wejściowej i wyjściowej.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3}}
install bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%define		fversion	%(echo %{version} |tr . _)
Summary:	Finite-State Machine Library
Summary(pl):	Biblioteka automatów skoñczonych
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

%description -l pl
Biblioteka FSM to zbiór narzêdzi ogólnego przeznaczenia dostêpnych dla
Uniksa s³u¿±cych do budowania, ³±czenia, optymalizacji i
przeszukiwania akceptorów i transduktorów wa¿onych o skoñczonej
liczbie stanów. Transduktory skoñczone to automaty, dla których ka¿de
przej¶cie ma etykietê wyj¶ciow± oprócz bardziej znanej etykiety
wej¶ciowej. Akceptory i transduktory wa¿one to akceptory i
transduktory, w których ka¿de przej¶cie ma wagê oprócz etykiety
wej¶ciowej lub wej¶ciowej i wyj¶ciowej.

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

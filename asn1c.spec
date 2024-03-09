Summary:	The ASN.1 to C compiler
Summary(pl.UTF-8):	Kompilator ASN.1 do C
Name:		asn1c
Version:	0.9.28
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://lionet.info/soft/%{name}-%{version}.tar.gz
# Source0-md5:	e78906866d7ea784a58b3d340bdec8ea
URL:		http://github.com/vlm/asn1c
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The asn1c compiler turns ASN.1 specifications into C language source
files containing the BER/CER/DER/XER encoders and decoders for the
given abstract notation.

%description -l pl.UTF-8
Kompilator asn1c zamienia specyfikacje ASN.1 na pliki źródłowe w
języku C zawierające funkcje kodujące i dekodujące BER/CER/DER/XER dla
podanej notacji abstrakcyjnej.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' examples/crfc2asn1.pl

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/asn1c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FAQ LICENSE README.md TODO doc/asn1c-{quick,usage}.pdf
%attr(755,root,root) %{_bindir}/asn1c
%attr(755,root,root) %{_bindir}/crfc2asn1.pl
%attr(755,root,root) %{_bindir}/enber
%attr(755,root,root) %{_bindir}/unber
%{_datadir}/asn1c
%{_mandir}/man1/asn1c.1*
%{_mandir}/man1/enber.1*
%{_mandir}/man1/unber.1*

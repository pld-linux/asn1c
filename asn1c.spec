Summary:	The ASN.1 to C compiler
Summary(pl.UTF-8):   Kompilator ASN.1 do C
Name:		asn1c
Version:	0.9.19
Release:	0.1
License:	BSD
Group:		Development/Languages
Source0:	http://lionet.info/soft/%{name}-%{version}.tar.gz
# Source0-md5:	6c555d806fa0fa465d1838076f27c385
URL:		http://asn1c.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-exec \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C skeletons install-data \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C asn1c install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ COPYING ChangeLog BUGS TODO doc/asn1c-usage.pdf doc/asn1c-usage.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/asn1c
%{_mandir}/man1/*

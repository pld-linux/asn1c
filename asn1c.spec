#
# $Id: asn1c.spec,v 1.1 2005-12-04 16:46:31 ggodlewski Exp $
#

Name:		asn1c
Version:	0.9.19
Release:	0.1
Source0:	http://lionet.info/soft/%{name}-%{version}.tar.gz
# Source0-md5:	6c555d806fa0fa465d1838076f27c385
URL:		http://asn1c.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Group:		Development/Languages
Summary:	The ASN.1 to C compiler
License:	BSD

%description
The asn1c compiler turns ASN.1 specifications into C language source
files containing the BER/CER/DER/XER encoders and decoders for the
given abstract notation.

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
%{__make} install-exec DESTDIR=$RPM_BUILD_ROOT
(cd skeletons && %{__make} install-data DESTDIR=$RPM_BUILD_ROOT)
(cd asn1c && %{__make} install-man DESTDIR=$RPM_BUILD_ROOT)


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ COPYING ChangeLog BUGS TODO
%doc doc/asn1c-usage.pdf doc/asn1c-usage.html
%attr(755,root,root) %{_bindir}
%attr(644,root,root) %{_datadir}/asn1c
%{_mandir}/man1

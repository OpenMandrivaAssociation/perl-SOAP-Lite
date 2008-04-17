%define module  SOAP-Lite
%define name    perl-%{module}
%define version 0.71.02
%define release %mkrel 1
%define _requires_exceptions perl(MQSeries.*)\\|perl(MQClient.*)

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL or Artistic
Summary:        Client and server side SOAP implementation
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/SOAP/%{module}-%{version}.tar.bz2
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(XML::Parser) >= 2.23
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(Net::Jabber)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
SOAP::Lite for Perl is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

To learn about SOAP, go to http://www.soaplite.com/#LINKS for more
information.

This version of SOAP::Lite supports a subset of the SOAP 1.1
specification and has initial support for SOAP 1.2 specification.  See
http://www.w3.org/TR/SOAP for details.

%prep
%setup -q -n %{module}-%{version}

find examples -type f | xargs perl -pi \
    -e 's|^#!perl -w|#!%{__perl} -w|;' \
    -e 's|^#!d:\\perl\\bin\\perl.exe ||;'
find examples -type f -name *.bat | xargs rm -f 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --noprompt
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{_mandir}/*/*
%{_bindir}/*.pl
%{perl_vendorlib}/Apache
%{perl_vendorlib}/IO
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/UDDI
%{perl_vendorlib}/XML
%{perl_vendorlib}/XMLRPC
%{perl_vendorlib}/OldDocs



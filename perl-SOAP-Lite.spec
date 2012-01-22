%define upstream_name    SOAP-Lite
%define upstream_version 0.712

%define _requires_exceptions perl(MQSeries.*)\\|perl(MQClient.*)
%define _provides_exceptions perl(LWP::Protocol)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Client and server side SOAP implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SOAP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Net::Jabber)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(XML::Parser) >= 2.230.0

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

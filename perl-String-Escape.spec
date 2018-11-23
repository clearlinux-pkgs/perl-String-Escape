#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Escape
Version  : 2010.002
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/E/EV/EVO/String-Escape-2010.002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EV/EVO/String-Escape-2010.002.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-escape-perl/libstring-escape-perl_2010.002-2.debian.tar.xz
Summary  : Backslash escapes, quoted phrase, word elision, etc.
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-String-Escape-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
String::Escape
This module provides a flexible calling interface to some
frequently-performed string conversion functions, including applying
and expanding standard C/Unix-style backslash escapes like \n and \t, wrapping
and removing double-quotes, and truncating to fit within a desired length.

%package dev
Summary: dev components for the perl-String-Escape package.
Group: Development
Provides: perl-String-Escape-devel = %{version}-%{release}

%description dev
dev components for the perl-String-Escape package.


%package license
Summary: license components for the perl-String-Escape package.
Group: Default

%description license
license components for the perl-String-Escape package.


%prep
%setup -q -n String-Escape-2010.002
cd ..
%setup -q -T -D -n String-Escape-2010.002 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/String-Escape-2010.002/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Escape
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-String-Escape/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/String/Escape.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Escape.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Escape/deblicense_copyright

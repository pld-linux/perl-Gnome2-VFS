# Conditional build:
%bcond_with     tests   # perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-VFS
Summary:	Perl bindings for the Gnome Virtual File System
Summary(pl):	Dowi±zania perla dla biblioteki Gnome Virtual File System
Name:		perl-%{pnam}
Version:	0.90
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	dbdb40cc02c63e9fda48c87d1cd1aa19
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.00
BuildRequires:	perl-Glib >= 1.021
BuildRequires:	perl-Gtk2 >= 1.023
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VFS module allows a perl developer to use the Gnome Virtual File
System.

%description -l pl
Modu³ VFS pozwala programistom perlowym na u¿ywanie biblioteki Gnome
Virtual File System.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/VFS/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorarch}/auto/Gnome2/VFS
%dir %{perl_vendorarch}/Gnome2/VFS
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/VFS/*.so
%{perl_vendorarch}/auto/Gnome2/VFS/*.bs
%{perl_vendorarch}/Gnome2/VFS/Install
%{perl_vendorarch}/Gnome2/*.pm
%{_mandir}/man3/*

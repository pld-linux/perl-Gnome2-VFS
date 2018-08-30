#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gnome2
%define		pnam	VFS
Summary:	Perl bindings for the GNOME Virtual File System
Summary(pl.UTF-8):	Dowiązania Perla dla biblioteki GNOME Virtual File System
Name:		perl-Gnome2-VFS
Version:	1.082
Release:	5
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	374e7d611d080d893bb3da9d40c64733
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gnome-vfs2-devel >= 2.14.1
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.120
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gnome-vfs2-libs >= 2.14.1
Requires:	perl-Glib >= 1.120
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VFS module allows a perl developer to use the GNOME Virtual File
System.

%description -l pl.UTF-8
Moduł VFS pozwala programistom perlowym na używanie biblioteki GNOME
Virtual File System.

%package devel
Summary:	Development files for Perl Gnome2-VFS bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-VFS dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.14.1
Requires:	perl-Cairo-devel
Requires:	perl-Glib >= 1.120

%description devel
Development files for Perl Gnome2-VFS bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-VFS dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/VFS/{*,*/*,*/*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/Gnome2/VFS.pm
%dir %{perl_vendorarch}/Gnome2/VFS
%dir %{perl_vendorarch}/auto/Gnome2/VFS
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/VFS/VFS.so
%{_mandir}/man3/Gnome2::VFS*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/VFS/Install

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
Version:	1.081
Release:	2
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Gnome2/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d220cbbe9f1ebc78d7047593f9cd633
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gnome-vfs2-devel >= 2.14.1
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.120
BuildRequires:	perl-Gtk2 >= 1.121
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gnome-vfs2-libs >= 2.14.1
Requires:	perl-Glib >= 1.120
Requires:	perl-Gtk2 >= 1.121
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VFS module allows a perl developer to use the GNOME Virtual File
System.

%description -l pl.UTF-8
Moduł VFS pozwala programistom perlowym na używanie biblioteki GNOME
Virtual File System.

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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/VFS/{*,*/*,*/*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{perl_vendorarch}/Gnome2/VFS
%{perl_vendorarch}/Gnome2/VFS/Install
%{perl_vendorarch}/Gnome2/*.pm
%dir %{perl_vendorarch}/auto/Gnome2/VFS
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/VFS/*.so
%{perl_vendorarch}/auto/Gnome2/VFS/*.bs
%{_mandir}/man3/Gnome2::VFS*.3pm*

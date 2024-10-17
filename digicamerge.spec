%define name digicamerge
%define version 2.00
%define release  6

Summary: 	Digital camera filename manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.librelogiciel.com/software/DigicaMerge/tarballs/%name-%{version}.tar.bz2
URL: 		https://www.librelogiciel.com/software/DigicaMerge/action_Presentation
License: 	GPL
Group: 		Graphics
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	python-devel 
Requires: 	python
Buildarch:	noarch

%description
DigicaMerge is a commandline tool to merge directories of pictures taken
with digital cameras. If you've got a digital camera, your hard disk
probably contains many directories full of pictures all named with the
same names. This utility allows you to merge such directories' contents
into a new directory, and renames all the pictures on the fly, ensuring
no filename clash will occur. You can define your own naming scheme,
using either a set of predefined variables or any recognized Exif tag
which may be present in your pictures, and also specify a pattern to
select only certain files.

%prep
%setup -q

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING CREDITS NEWS PKG-INFO README TODO
%_bindir/%name
%_mandir/man1/*
%py_sitedir/*



%changelog
* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 2.00-5mdv2011.0
+ Revision: 594774
- rebuild for python 2.7

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 2.00-4mdv2009.1
+ Revision: 324196
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.00-3mdv2009.0
+ Revision: 244308
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.00-1mdv2008.1
+ Revision: 132788
- adjust file list
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import digicamerge


* Mon Feb 20 2006 Austin Acton <austin@mandriva.org> 2.00-1mdk
- 2.00
- source URL
- man page

* Sun Feb 6 2005 Austin Acton <austin@mandrake.org> 1.80-1mdk
- 1.80

* Mon Jan 5 2004 Austin Acton <austin@linux.ca> 1.70-1mdk
- 1.70

* Sat Dec 27 2003 Austin Acton <austin@linux.ca> 1.60-1mdk
- 1.60

* Thu Jan 16 2003 Austin Acton <aacton@yorku.ca> 1.50-1mdk
- initial package

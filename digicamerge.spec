%define name digicamerge
%define version 2.00
%define release  %mkrel 4

Summary: 	Digital camera filename manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.librelogiciel.com/software/DigicaMerge/tarballs/%name-%{version}.tar.bz2
URL: 		http://www.librelogiciel.com/software/DigicaMerge/action_Presentation
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


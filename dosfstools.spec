Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:	3.0.16
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0:	http://www.daniel-baumann.ch/software/dosfstools/%{name}-%{version}.tar.bz2
Source0:	http://ftp.debian.org/debian/pool/main/d/dosfstools/%{name}_%{version}.orig.tar.xz
# Source0-md5:	27aca18aeb8bb0851ccaeb47e7416a6e
URL:		http://www.daniel-baumann.ch/software/dosfstools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE"	\
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*.{msdos,vfat}.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.msdos.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.vfat.8
echo ".so mkdosfs.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8
echo ".so mkdosfs.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.vfat.8
rm -f $RPM_BUILD_ROOT%{_mandir}/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*


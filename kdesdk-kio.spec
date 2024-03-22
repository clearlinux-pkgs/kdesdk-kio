#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdesdk-kio
Version  : 24.02.1
Release  : 46
URL      : https://download.kde.org/stable/release-service/24.02.1/src/kdesdk-kio-24.02.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.1/src/kdesdk-kio-24.02.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.1/src/kdesdk-kio-24.02.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdesdk-kio-data = %{version}-%{release}
Requires: kdesdk-kio-lib = %{version}-%{release}
Requires: kdesdk-kio-license = %{version}-%{release}
Requires: kdesdk-kio-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : perl
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
kio_perldoc - A KIO worker interface to the embedded Perl documentation.
It requires Perl 5.10 and the perl standard perldoc program to be installed.

%package data
Summary: data components for the kdesdk-kio package.
Group: Data

%description data
data components for the kdesdk-kio package.


%package lib
Summary: lib components for the kdesdk-kio package.
Group: Libraries
Requires: kdesdk-kio-data = %{version}-%{release}
Requires: kdesdk-kio-license = %{version}-%{release}

%description lib
lib components for the kdesdk-kio package.


%package license
Summary: license components for the kdesdk-kio package.
Group: Default

%description license
license components for the kdesdk-kio package.


%package locales
Summary: locales components for the kdesdk-kio package.
Group: Default

%description locales
locales components for the kdesdk-kio package.


%prep
%setup -q -n kdesdk-kio-24.02.1
cd %{_builddir}/kdesdk-kio-24.02.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711136182
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711136182
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesdk-kio
cp %{_builddir}/kdesdk-kio-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kdesdk-kio/a21ac62aee75f8fcb26b1de6fc90e5eea271854c || :
cp %{_builddir}/kdesdk-kio-%{version}/perldoc/COPYING %{buildroot}/usr/share/package-licenses/kdesdk-kio/d6458d52bfead6f1399b865f1aeea0caa639ef6c || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kio5_perldoc

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kio_perldoc/pod2html.pl

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/kf6/kio/perldoc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesdk-kio/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
/usr/share/package-licenses/kdesdk-kio/d6458d52bfead6f1399b865f1aeea0caa639ef6c

%files locales -f kio5_perldoc.lang
%defattr(-,root,root,-)


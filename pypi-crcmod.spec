#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-crcmod
Version  : 1.7
Release  : 61
URL      : https://files.pythonhosted.org/packages/6b/b0/e595ce2a2527e169c3bcd6c33d2473c1918e0b7f6826a043ca1245dd4e5b/crcmod-1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/b0/e595ce2a2527e169c3bcd6c33d2473c1918e0b7f6826a043ca1245dd4e5b/crcmod-1.7.tar.gz
Summary  : CRC Generator
Group    : Development/Tools
License  : MIT
Requires: pypi-crcmod-license = %{version}-%{release}
Requires: pypi-crcmod-python = %{version}-%{release}
Requires: pypi-crcmod-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
crcmod for Calculating CRCs
        ===========================
        
        The software in this package is a Python module for generating objects that
        compute the Cyclic Redundancy Check (CRC).  There is no attempt in this package
        to explain how the CRC works.  There are a number of resources on the web that
        give a good explanation of the algorithms.  Just do a Google search for "crc
        calculation" and browse till you find what you need.  Another resource can be
        found in chapter 20 of the book "Numerical Recipes in C" by Press et. al.
        
        This package allows the use of any 8, 16, 24, 32, or 64 bit CRC.  You can
        generate a Python function for the selected polynomial or an instance of the
        Crc class which provides the same interface as the ``md5`` and ``sha`` modules
        from the Python standard library.  A ``Crc`` class instance can also generate
        C/C++ source code that can be used in another application.
        
        ----------
        Guidelines
        ----------
        
        Documentation is available from the doc strings.  It is up to you to decide
        what polynomials to use in your application.  If someone has not specified the
        polynomials to use, you will need to do some research to find one suitable for
        your application.  Examples are available in the unit test script ``test.py``.
        You may also use the ``predefined`` module to select one of the standard
        polynomials.
        
        If you need to generate code for another language, I suggest you subclass the
        ``Crc`` class and replace the method ``generateCode``.  Use ``generateCode`` as
        a model for the new version.
        
        ------------
        Dependencies
        ------------
        
        Python Version
        ^^^^^^^^^^^^^^
        
        The package has separate code to support the 2.x and 3.x Python series.

%package license
Summary: license components for the pypi-crcmod package.
Group: Default

%description license
license components for the pypi-crcmod package.


%package python
Summary: python components for the pypi-crcmod package.
Group: Default
Requires: pypi-crcmod-python3 = %{version}-%{release}

%description python
python components for the pypi-crcmod package.


%package python3
Summary: python3 components for the pypi-crcmod package.
Group: Default
Requires: python3-core
Provides: pypi(crcmod)

%description python3
python3 components for the pypi-crcmod package.


%prep
%setup -q -n crcmod-1.7
cd %{_builddir}/crcmod-1.7
pushd ..
cp -a crcmod-1.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685560831
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-crcmod
cp %{_builddir}/crcmod-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-crcmod/3eb0123465010ad9f22c49106e26776969c7bcb2 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-crcmod/3eb0123465010ad9f22c49106e26776969c7bcb2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*

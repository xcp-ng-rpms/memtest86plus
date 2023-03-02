# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for x86 architecture systems
Name:		memtest86+
Version:	6.01
Release:	2%{?dist}
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.memtest.org
Source0:	https://github.com/memtest86plus/memtest86plus/archive/v%{version}/memtest86plus-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	binutils
ExclusiveArch:	x86_64

%description
MemTest86+ is a thorough, stand alone memory test for x86 architecture
systems. BIOS based memory tests are only a quick check and often
miss failures that are detected by MemTest86+.

%prep
%autosetup -p1 -n memtest86plus-%{version}

%build
cd build64
%make_build LD=/usr/bin/ld.bfd

%install
cd build64
mkdir -p %{buildroot}/boot
install -m644 memtest.{bin,efi} -D %{buildroot}/boot/

%files
/boot/memtest.efi
/boot/memtest.bin

%changelog
* next
- Fix upstream source URL

* Tue Jan 24 2023 Yann Dirson <yann.dirson@vates.fr> - 6.01-2
- Rename rpm back to upstream "memtest86+" name

* Fri Jan 06 2023 Yann Dirson <yann.dirson@vates.fr> - 6.01-1
- Initial packaging based on 6.00-1 from OpenMandriva

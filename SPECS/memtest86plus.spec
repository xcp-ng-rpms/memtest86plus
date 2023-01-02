# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for x86 architecture systems
Name:		memtest86plus
Version:	6.01
Release:	1%{?dist}
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.memtest.org
Source0:	https://github.com/memtest86plus/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	binutils
ExclusiveArch:	x86_64

%description
MemTest86+ is a thorough, stand alone memory test for x86 architecture
systems. BIOS based memory tests are only a quick check and often
miss failures that are detected by MemTest86+.

%prep
%autosetup -p1

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
* Fri Jan 6 2023 Yann Dirson <yann.dirson@vates.fr> - 6.01-1
- Initial packaging based on 6.00-1 from OpenMandriva

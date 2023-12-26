%global _target riscv64-linux-gnu

Name:		%{_target}-gdb
Version:	14.1
Release:	1%{?dist}
Summary:	The GNU Debugger for the 32bit and 64bit RISC-V target
License:	GPL3
URL:		https://www.gnu.org/software/gdb/

%global tarname gdb-%{version}
%global gdb_src %{tarname}

Source0:	https://ftp.gnu.org/gnu/gdb/%{tarname}.tar.xz

# BuildRequires:	boost
BuildRequires:	texinfo
BuildRequires:	readline-devel
BuildRequires:	expat-devel
BuildRequires:	gcc-c++
BuildRequires:	python3-devel
BuildRequires:	source-highlight-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glibc-devel
BuildRequires:	glibc-static
BuildRequires:	libgcc
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	libgnat
BuildRequires:	gcc-gnat
BuildRequires:	make

Requires:	xz
Requires:	ncurses
Requires:	expat
Requires:	python
Requires:	guile
Requires:	gdb-headless
Requires:	mpfr
Requires:	elfutils-libelf
Requires:	source-highlight

%description
The GNU Debugger for the 32bit and 64bit RISC-V target

%prep
%setup -q -n %{gdb_src}

%build
mkdir -p build && cd build

../configure \
  --target=%{_target} \
  --prefix=/usr \
  --enable-languages=c,c++ \
  --disable-multilib \
  --enable-interwork \
  --with-system-readline \
  --disable-nls \
  --enable-source-highlight \
  --with-python=/usr/bin/python3 \
  --with-system-gdbinit=/etc/gdbinit

make

%install
make -C gdb install %{?_smp_mflags}


%files
# TODO: Add files
/usr/bin/riscv64-linux-gnu-gdb
/usr/bin/riscv64-linux-gnu-gdb-add-index

%changelog
* Tue Dec 26 2023 <WangTsing.Yan@gmail.com> - 14.1
- Initial version

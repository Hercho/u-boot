Summary: Universal Boot Loader for embedded devices
Name: u-boot-imx
Version: 2015.04
Release: r0
License: GPLv2+
Group: bootloaders
Packager: Freescale Semiconductors <lauren.post@nxp.com>
URL: http://www.denx.de/wiki/U-Boot/WebHome
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: openssl-native
BuildRequires: virtual/libc
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc

%description
U-Boot provided by Freescale with focus on  i.MX reference boards.

%package -n u-boot-imx-dbg
Summary: Universal Boot Loader for embedded devices - Debugging files
Group: devel

%description -n u-boot-imx-dbg
U-Boot provided by Freescale with focus on  i.MX reference boards.  This
package contains ELF symbols and related sources for debugging purposes.

%package -n u-boot-imx-staticdev
Summary: Universal Boot Loader for embedded devices - Development files (Static Libraries)
Group: devel
Requires: u-boot-imx-dev = 2015.04-r0

%description -n u-boot-imx-staticdev
U-Boot provided by Freescale with focus on  i.MX reference boards.  This
package contains static libraries for software development.

%package -n u-boot-imx-dev
Summary: Universal Boot Loader for embedded devices - Development files
Group: devel
Requires: u-boot-imx = 2015.04-r0

%description -n u-boot-imx-dev
U-Boot provided by Freescale with focus on  i.MX reference boards.  This
package contains symbolic links, header files, and related items necessary
for software development.

%package -n u-boot-imx-doc
Summary: Universal Boot Loader for embedded devices - Documentation files
Group: doc

%description -n u-boot-imx-doc
U-Boot provided by Freescale with focus on  i.MX reference boards.  This
package contains documentation.

%package -n u-boot-imx-locale
Summary: Universal Boot Loader for embedded devices
Group: bootloaders

%description -n u-boot-imx-locale
U-Boot provided by Freescale with focus on  i.MX reference boards.

%files
%defattr(-,-,-,-)
%dir "/boot"
"/boot/u-boot-sd-2015.04-r0.imx"
"/boot/u-boot.imx-sd"
"/boot/u-boot.imx"

%files -n u-boot-imx-dbg
%defattr(-,-,-,-)

%files -n u-boot-imx-dev
%defattr(-,-,-,-)


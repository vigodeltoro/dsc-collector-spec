Name: dsc-collector		
Version: 2.2.1	
Release: 1%{?dist}
Summary: Domain Statistics Collector 
Group: Monitoring software		
License: GPL
URL: https://github.com/DNS-OARC/dsc	
%define NVdir   %{name}-%{version}

BuildRequires: autoconf automake gcc 	
Requires: libpcap-devel perl-Proc-PID-File 	

%description
Domain Statistics Collector - collects pcaps of nameserver, transcode to xml for presenting in Grafana graphs. 

%prep
rm -rf %{NVdir}
git clone %{url}.git %{NVdir}
cd %{NVdir}
git submodule update --init
./autogen.sh

%build
cd %{NVdir}
./configure
make %{?_smp_mflags}

%install
cd %{NVdir}
make install DESTDIR=%{buildroot}


%files
/usr/local/bin/dsc
/usr/local/etc/dsc
/usr/local/etc/dsc/dsc.conf.sample
/usr/local/libexec/dsc
/usr/local/libexec/dsc/upload-prep.pl
/usr/local/libexec/dsc/upload-rsync.sh
/usr/local/libexec/dsc/upload-ssh.sh
/usr/local/libexec/dsc/upload-x509.sh
/usr/local/share/doc/dsc
/usr/local/share/doc/dsc/CHANGES
/usr/local/share/doc/dsc/LICENSE
/usr/local/share/doc/dsc/README.md
/usr/local/share/doc/dsc/UPGRADE.md
/usr/local/share/man/man1/dsc.1
/usr/local/share/man/man5/dsc.conf.5

%changelog

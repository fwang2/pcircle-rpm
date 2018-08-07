%define name pcircle
%define unmangled_version 0.17.1
%define version 0.17.1
%define release 1%{?dist}

# turn off auto dependency check
Autoreq: 0

Summary: A parallel file system tool suite
Name: %{name}
Version: %{version}
Release: %{release}
Source0: tarballs/%{name}-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

#BuildRequires: python >= 2.7
#BuildRequires: openmpi-devel
#BuildRequires: libffi-devel
Requires: python >= 2.7
Requires: openmpi
Requires: python-cffi
Requires: numpy
Requires: python-scandir
Requires: pyxattr
Requires: mpi4py-openmpi
Requires: python2-future
Requires: python2-bitarray

#BuildRequires: lru-dict

#Prefix: %{_prefix}
BuildArch: noarch
Vendor: Feiyi Wang <fwang2@ornl.gov>
Url: http://github.com/ORNL-TechInt/pcircle

%description
ubiquitous MPI environment in HPC cluster + Work Stealing Pattern +
Distributed Termination Detection = Efficient and Scalable Parallel Solution.
pcircle contains a suite of file system tools that we are developing at OLCF to
take advantage of highly scalable parallel file system such as Lustre and GPFS.
Early tests show very promising scaling properties. However, it is still in
active development, please use it at your own risk. For bug report and
feedbacks, please post it here at https://github.com/olcf/pcircle/issues.


# explictly give it a name
# %package -n python2-%{name}


%prep
%setup -n %{name}-%{unmangled_version}

%build
%py2_build

%install
%py2_install

%files
%{python2_sitelib}/pcircle/
%{python2_sitelib}/pcircle-*.egg-info
%exclude /usr/bin/fcorruptor
%exclude /usr/bin/fdiff
%exclude /usr/bin/fgen
%exclude /usr/bin/fpipe
%exclude /usr/bin/fwalk
/usr/bin/fcp
/usr/bin/fprof
/usr/bin/fsum

%changelog

* Tue Aug 7 2018 Feiyi Wang <fwang2@gmail.com> 0.17.1
- Initial RPM release, openmpi flavor

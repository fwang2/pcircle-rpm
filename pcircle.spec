%define name pcircle
%define unmangled_version 0.17.1
%define version 0.17.1
%define release 1%{?dist}
%define debug_package %{nil}

Autoreq: 0
# turn off auto dependency check
#%define __find_requires %{nil}
#%define __find_provides %{nill}

Summary: A parallel file system tool suite
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python >= 2.7
BuildRequires: openmpi-devel
BuildRequires: libffi-devel
Requires: python >= 2.7
Requires: openmpi
Requires: python-cffi
Requires: numpy
Requires: python-scandir
Requires: libattr-devel
Requires: mpi4py-openmpi
#BuildRequires: lru-dict

#Prefix: %{_prefix}
BuildArch: x86_64
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



%prep
%setup -n %{name}-%{unmangled_version}

%build
%files
%post

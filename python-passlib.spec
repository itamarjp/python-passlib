%if 0%{?fedora}
%global with_python3 1
%endif

Name:		python-passlib
Version:	1.6.5
Release:	1%{?dist}
Summary:	Comprehensive password hashing framework supporting over 20 schemes

License:	BSD and Beerware and Copyright only
URL:		https://bitbucket.org/ecollins/passlib
Source0:	https://pypi.python.org/packages/source/p/passlib/passlib-%{version}.tar.gz
BuildArch:	noarch

# docs generation requires python-cloud-sptheme, which isn't packaged yet.
# so we won't generate the docs yet.
#BuildRequires:	python-sphinx >= 1.0
#BuildRequires:	python-cloud-sptheme

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package -n python2-passlib
Summary:	Comprehensive password hashing framework supporting over 20 schemes
%{?python_provide:%python_provide python2-passlib}
# python_provide does not exist in CBS Cloud buildroot
Provides:    python-passlib = %{version}-%{release}
Obsoletes:    python-passlib < 1.6.5-1

BuildRequires:	python2-devel
BuildRequires:	python-setuptools

%description -n python2-passlib
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%if 0%{?with_python3}
%package -n python3-passlib
Summary:	Comprehensive password hashing framework supporting over 20 schemes
%{?python_provide:%python_provide python3-passlib}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description -n python3-passlib
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.
%endif

%prep
%setup -q -n passlib-%{version}

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%endif

%files -n python2-passlib
%doc README
%license LICENSE
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-passlib
%doc README
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> - 1.6.5-1
- Added python2 and python3 subpackage
- updated to 1.6.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Alan Pevec <apevec@redhat.com> - 1.6.2-1
- update to 1.6.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Alan Pevec <apevec@redhat.com> - 1.6.1-1
- update to 1.6.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Matt Domsch <Matt_Domsch@dell.com> - 1.5.3-1
- initial release for Fedora

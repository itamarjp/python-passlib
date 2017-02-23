%if 0%{?fedora}
%global with_python3 1
%endif

Name:		python-passlib
Version:	1.7.0
Release:	4%{?dist}
Summary:	Comprehensive password hashing framework supporting over 20 schemes

License:	BSD and Beerware and Copyright only
URL:		https://bitbucket.org/ecollins/passlib
Source0:	https://pypi.io/packages/source/p/passlib/passlib-%{version}.tar.gz
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
# passlib setup.py append HG revision to the end of version by default
# which makes StrictVersion checks complaining
export PASSLIB_SETUP_TAG_RELEASE="no"
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
* Thu Feb 23 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.7.0-4
- Fix eggs-info generation

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Alan Pevec <alan.pevec@redhat.com> 1.7.0-1
- Update to 1.7.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

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

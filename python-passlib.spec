Name:		python-passlib
Version:	1.6.2
Release:	1%{?dist}
Summary:	Comprehensive password hashing framework supporting over 20 schemes

License:	BSD and Beerware and Copyright only
URL:		http://passlib.googlecode.com
Source0:	https://pypi.python.org/packages/source/p/passlib/passlib-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
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


%prep
%setup -q -n passlib-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc LICENSE README
%{python_sitelib}/*


%changelog
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

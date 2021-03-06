#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	tests	# test target (broken)

Summary:	OpenStack Hacking Guideline enforcement plugins
Summary(pl.UTF-8):	Wtyczki wymuszające OpenStack Hacking Guideline
Name:		python-hacking
Version:	0.10.3
Release:	5
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	https://github.com/openstack-dev/hacking/archive/%{version}/hacking-%{version}.tar.gz
# Source0-md5:	1a3881ee56e7fa20b2ed019a84738168
Patch0:		%{name}-requirements.patch
URL:		https://github.com/openstack-dev/hacking
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-pbr >= 0.11
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.1.2
BuildRequires:	python-coverage >= 3.6
BuildRequires:	python-discover
BuildRequires:	python-eventlet >= 0.16.1
BuildRequires:	python-fixtures >= 0.3.14
BuildRequires:	python-flake8 >= 2.2.4
BuildRequires:	python-mccabe >= 0.2.1
BuildRequires:	python-mock >= 1.0
BuildRequires:	python-oslosphinx >= 2.2.0
BuildRequires:	python-pep8 >= 1.5.7
BuildRequires:	python-pyflakes >= 0.8.1
BuildRequires:	python-six >= 1.7.0
BuildRequires:	python-subunit >= 0.0.18
BuildRequires:	python-testrepository >= 0.0.18
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 0.9.36
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pbr >= 0.11
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.1.2
BuildRequires:	python3-eventlet >= 0.16.1
BuildRequires:	python3-fixtures >= 0.3.14
BuildRequires:	python3-flake8 >= 2.2.4
BuildRequires:	python3-mccabe >= 0.2.1
BuildRequires:	python3-pep8 >= 1.5.7
BuildRequires:	python3-pyflakes >= 0.8.1
BuildRequires:	python3-six >= 1.7.0
BuildRequires:	python3-subunit >= 0.0.18
BuildRequires:	python3-testrepository >= 0.0.18
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 0.9.36
%endif
%endif
Requires:	python-flake8 >= 2.2.4
Requires:	python-mccabe >= 0.2.1
Requires:	python-modules >= 1:2.6
Requires:	python-pep8 >= 1.5.7
Requires:	python-six >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines <http://docs.openstack.org/developer/hacking>.

%description -l pl.UTF-8
Moduł hacking to zbiór wtyczek dla narzędzia flake8, testujących i
wymuszających przestrzeganie wskazówek OpenStack Style Guidlines
<http://docs.openstack.org/developer/hacking>.

%package -n python3-hacking
Summary:	OpenStack Hacking Guideline enforcement plugins
Summary(pl.UTF-8):	Wtyczki wymuszające OpenStack Hacking Guideline
Group:		Development/Languages/Python
Requires:	python3-flake8 >= 2.2.4
Requires:	python3-mccabe >= 0.2.1
Requires:	python3-modules >= 1:3.2
Requires:	python3-pep8 >= 1.5.7
Requires:	python3-six >= 1.7.0

%description -n python3-hacking
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines <http://docs.openstack.org/developer/hacking>.

%description -n python3-hacking -l pl.UTF-8
Moduł hacking to zbiór wtyczek dla narzędzia flake8, testujących i
wymuszających przestrzeganie wskazówek OpenStack Style Guidlines
<http://docs.openstack.org/developer/hacking>.

%prep
%setup -q -n hacking-%{version}
%patch0 -p1

%build
export PBR_VERSION="%{version}"
%if %{with python2}
%py_build %{?with_tests:test}

%{?with_tests:%{__rm} -r .testrepository}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}

%{?with_tests:%{__rm} -r .testrepository}
%endif

%install
rm -rf $RPM_BUILD_ROOT

export PBR_VERSION="%{version}"

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/hacking
%{py_sitescriptdir}/hacking-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hacking
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/hacking
%{py3_sitescriptdir}/hacking-%{version}-py*.egg-info
%endif

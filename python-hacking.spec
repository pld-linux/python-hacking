#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (failing; require already installed package?)

Summary:	OpenStack Hacking Guideline enforcement plugins
Summary(pl.UTF-8):	Wtyczki wymuszające OpenStack Hacking Guideline
Name:		python-hacking
# keep 2.x here for python2 support
Version:	2.0.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/h/hacking/hacking-%{version}.tar.gz
# Source0-md5:	232e583c3d72805122a91b6788524256
URL:		https://github.com/openstack-dev/hacking
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage >= 4.0
BuildRequires:	python-eventlet >= 0.21.0
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-flake8 >= 3.6.0
BuildRequires:	python-flake8 < 4
BuildRequires:	python-mock >= 2.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 4.0
BuildRequires:	python3-eventlet >= 0.21.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-flake8 >= 3.6.0
BuildRequires:	python3-flake8 < 4
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.8.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
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
Requires:	python3-modules >= 1:3.6

%description -n python3-hacking
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines <http://docs.openstack.org/developer/hacking>.

%description -n python3-hacking -l pl.UTF-8
Moduł hacking to zbiór wtyczek dla narzędzia flake8, testujących i
wymuszających przestrzeganie wskazówek OpenStack Style Guidlines
<http://docs.openstack.org/developer/hacking>.

%package apidocs
Summary:	API documentation for Python hacking module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona hacking
Group:		Documentation

%description apidocs
API documentation for Python hacking module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona hacking.

%prep
%setup -q -n hacking-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
stestr-2 run
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
stestr-3 run
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/hacking
%{py_sitescriptdir}/hacking-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hacking
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/hacking
%{py3_sitescriptdir}/hacking-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,user,*.html,*.js}
%endif

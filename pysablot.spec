Summary:	pysablot - Python bindings for Sablotron
Summary(pl.UTF-8):	pysablot - dowiązania Pythona dla Sablotrona
Name:		pysablot
Version:	0.1
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pysablot/PySablot-%{version}.tar.gz
# Source0-md5:	7c9b859f963c2c67e8276a348ecac51b
Patch0:		%{name}-libs.patch
URL:		http://pysablot.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	sablotron-devel
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Sablotron (a XSLT library). PySablot provides
a simple API for in-memory XSLT transformations or file-2-file
transformation.

%description -l pl.UTF-8
Dowiązania Pythona dla Sablotrona (biblioteki XSLT). PySablot
dostarcza proste API do przekształceń XSLT w pamięci i przekształceń
z pliku do pliku.

%prep
%setup -q -n PySablot-%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PySablot.so
%{py_sitedir}/Sablot.py[co]

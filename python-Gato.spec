%define name	python-Gato
%define version	0.20090311

%define	pkgdir	%{_datadir}/%{name}

Name:		%{name}
Group:		Development/Python
License:	LGPL
Summary:	Python Gato module
Version:	%{version}
Release:	%mkrel 1
# svn co https://gato.svn.sourceforge.net/svnroot/gato/trunk/Gato Gato
# tar jcvf Gato-0.`date +%\Y%\m%\d`.tar.bz
Source:		Gato-%{version}.tar.bz2
URL:		http://gato.sourceforge.net/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel
Requires:	tcl >= 8.6
Requires:	tk >= 8.6
Requires:	tkinter
Requires:	python-imaging

%description
Gato - the Graph Animation Toolbox - is a software which visualizes
algorithms on graphs. Graphs are mathematical objects consisting of
vertices and edges connecting pairs of vertices: think of cities as
vertices and interstates as edges connecting two cities. Algorithms
might find a shortest path - the fastest route - or a minimal spanning
tree or solve one of other interesting problems on graphs: maximal-flow,
weighted and non-weighted matching and min-cost flow. Visualisation
means linking cause - the statements of an algorithm - immediately to
an effect - changes to the graph the algorithm has as its input - by
terms of blinking, changing colors and other visual effects.

%prep
%setup -q -n Gato

%build
for f in `find . -name \*.py`; do
    sed -i -e 's|#!/usr/bin/env python2.3|#!/usr/bin/env python|' $f
done

%install
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
mkdir -p %{buildroot}/%{pkgdir}
cp -far Icons %{buildroot}/%{pkgdir}

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%dir %{pkgdir}
%{pkgdir}/*
%doc WWW

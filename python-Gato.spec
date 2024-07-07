Name:		python-Gato
Group:		Development/Python
License:	LGPLv2
Summary:	Python Gato module
Version:	1.2.7
Release:	1
Source:		https://files.pythonhosted.org/packages/source/G/Gato/Gato-%{version}.tar.gz
URL:		http://gato.sourceforge.net/index.html
Requires:	tcl >= 8.6
Requires:	tk >= 8.6
Requires:	tkinter
BuildRequires:	python
BuildArch:	noarch

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
%autosetup -p1 -n Gato-%{version}
sed -i -e 's:self.overrideredirect(1):self.overrideredirect(0):' GatoDialogs.py

%install
rm -fr %buildroot
mkdir -p %buildroot%{py_platsitedir}/Gato
cp *.py %buildroot%{py_platsitedir}/Gato

mkdir -p %buildroot%{_bindir}
pushd %buildroot%{_bindir}
ln -s %{py_platsitedir}/Gato/Gato.py gato
ln -s %{py_platsitedir}/Gato/Gred.py gred
popd

mkdir -p %buildroot%{_datadir}/Gato
cp BFS.* DFS.* sample.cat %buildroot%{_datadir}/Gato

%files
%defattr(-,root,root)
%{_bindir}/*
%{py_platsitedir}/*
%{_datadir}/Gato

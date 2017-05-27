%define		packname	affy

Summary:	Methods for Affymetrix Oligonucleotide Arrays
Name:		R-%{packname}
Version:	1.40.0
Release:	3
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	b58ebcb0117b685130425e8840088845
Patch0:		bogus-deps.patch
URL:		http://bioconductor.org/packages/release/bioc/html/affy.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-BiocGenerics
BuildRequires:	R-affyio
BuildRequires:	R-preprocessCore-devel
BuildRequires:	R-tkWidgets
BuildRequires:	texlive-latex
BuildRequires:	zlib-devel
Requires:	R
Requires:	R-Biobase
Requires:	R-BiocGenerics
Requires:	R-affyio
Requires:	R-preprocessCore
Suggests:	R-tkWidgets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package contains functions for exploratory oligonucleotide array
analysis.

The dependancy to tkWidgets only concerns few convenience functions.
'affy' is fully functional without it.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/demo
%{_libdir}/R/library/%{packname}/tests

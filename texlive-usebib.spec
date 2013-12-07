# revision 25969
# category Package
# catalog-ctan /macros/latex/contrib/usebib
# catalog-date 2012-04-13 23:54:56 +0200
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-usebib
Version:	1.0a
Release:	5
Summary:	A simple bibloography processor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/usebib
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is described by its author as "a poor person's
replacement for the more powerful methods provided by biblatex
to access data from a .bib file". Its principle commands are
\bibinput (which specifies a database to use) and \usebibdata
(which typesets a single field from a specified entry in that
database.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/usebib/usebib.sty
%doc %{_texmfdistdir}/doc/latex/usebib/README
%doc %{_texmfdistdir}/doc/latex/usebib/usebib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/usebib/usebib.dtx
%doc %{_texmfdistdir}/source/latex/usebib/usebib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 813170
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 787814
- Import texlive-usebib
- Import texlive-usebib


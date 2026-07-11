%global tl_name usebib
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	A simple bibliography processor
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/usebib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/usebib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is described by its author as "a poor person's replacement
for the more powerful methods provided by BibLaTeX to access data from a
.bib file". Its principle commands are \bibinput (which specifies a
database to use) and \usebibdata (which typesets a single field from a
specified entry in that database.


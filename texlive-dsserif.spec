%global tl_name dsserif
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.031
Release:	%{tl_revision}.1
Summary:	A double-struck serifed font for mathematical use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dsserif
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
DSSerif is a mathematical font package with double struck serifed
digits, upper and lower case letters, in regular and bold weights. The
design was inspired by the STIX double struck fonts, which are sans
serif, but starting from a Courier-like base.


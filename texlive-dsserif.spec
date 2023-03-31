Name:		texlive-dsserif
Version:	60898
Release:	2
Summary:	A double-struck serifed font for mathematical use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dsserif
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dsserif.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
DSSerif is a mathematical font package with double struck
serifed digits, upper and lower case letters, in regular and
bold weights. The design was inspired by the STIX double struck
fonts, which are sans serif, but starting from a Courier-like
base.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/dsserif
%{_texmfdistdir}/tex/latex/dsserif
%{_texmfdistdir}/fonts/type1/public/dsserif
%{_texmfdistdir}/fonts/tfm/public/dsserif
%{_texmfdistdir}/fonts/map/dvips/dsserif
%{_texmfdistdir}/fonts/afm/public/dsserif
%doc %{_texmfdistdir}/doc/fonts/dsserif

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

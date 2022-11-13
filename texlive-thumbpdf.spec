Name:		texlive-thumbpdf
Version:	62518
Release:	1
Summary:	Thumbnails for pdfTeX and dvips/ps2pdf
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/thumbpdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-thumbpdf.bin = %{EVRD}

%description
A Perl script that provides support for thumbnails in pdfTeX
and dvips/ps2pdf. The script uses ghostscript to generate the
thumbnails which get represented in a TeX readable file that is
read by the package thumbpdf.sty to automatically include the
thumbnails. This arrangement works with both plain TeX and
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/thumbpdf
%{_texmfdistdir}/scripts/thumbpdf/thumbpdf.pl
%{_texmfdistdir}/tex/generic/thumbpdf/thumbpdf.sty
%{_texmfdistdir}/tex/generic/thumbpdf/thumbpdf.tex
%doc %{_texmfdistdir}/doc/generic/thumbpdf/README
%doc %{_mandir}/man1/thumbpdf.1*
%doc %{_texmfdistdir}/doc/man/man1/thumbpdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/thumbpdf/thumbpdf.pl thumbpdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

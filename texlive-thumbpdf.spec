# revision 26689
# category Package
# catalog-ctan /support/thumbpdf
# catalog-date 2012-04-18 12:26:55 +0200
# catalog-license lppl
# catalog-version 3.15
Name:		texlive-thumbpdf
Version:	3.15
Release:	3
Summary:	Thumbnails for pdfTeX and dvips/ps2pdf
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/thumbpdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.doc.tar.xz
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
%doc %{_texmfdir}/doc/man/man1/thumbpdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/thumbpdf/thumbpdf.pl thumbpdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.15-2
+ Revision: 812924
- Update to latest release.
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.15-1
+ Revision: 805111
- Update to latest release.

* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.14-1
+ Revision: 790836
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.11-2
+ Revision: 756839
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.11-1
+ Revision: 719736
- texlive-thumbpdf
- texlive-thumbpdf
- texlive-thumbpdf

